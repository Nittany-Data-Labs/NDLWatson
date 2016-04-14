from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth import logout, login
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.management import call_command
from .forms import EntryForm, RegistrationForm, LoginForm
from .models import JournalEntry, ProcessedEntry

# Create your views here.
def index(request):
    current_user = request.user
    journal_entry_list = ''
    if current_user.is_authenticated():
        print 'authenticated'
        # journal_entry_list = JournalEntry.objects.all()
        journal_entry_list = JournalEntry.objects.filter(author=current_user)
    context = {'journal_entry_list': journal_entry_list, 'current_user': current_user}
    return render(request, 'journal_app/index.html', context)

@login_required
def detail(request, journal_entry_id):
    entry = get_object_or_404(JournalEntry, pk=journal_entry_id)
    if entry.processed == False:
        call_command('paired', entry_id=journal_entry_id)
        entry.processed = True
        entry.save()
    p = ProcessedEntry.objects.filter(entry=entry)
    return render(request, 'journal_app/detail.html', {'entry': entry, 'processed': p})

@login_required
def record_entry(request):
    template = loader.get_template('journal_app/record_entry.html')
    # Display form
    form = EntryForm()
    return render(request, 'journal_app/record_entry.html', {'form': form})

@login_required
def submit_entry(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EntryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            current_user = request.user
            title = form.cleaned_data['title']
            author = current_user
            body = form.cleaned_data['body']
            pub_date = timezone.now()

            j = JournalEntry(title = title, author = author, body = body, pub_date = pub_date, processed = False)
            j.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('journal_app:detail', args=[j.id]))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EntryForm()

    return render(request, 'journal_app/record_entry.html', {'form': form})

@login_required
def user_access(request):
    return render(request, 'journal_app/user_access.html')

def view_registration(request):
    template = loader.get_template('journal_app/view_registration.html')
    # Display formform = LoginForm()
    form = RegistrationForm()
    return render(request, 'journal_app/view_registration.html', {'form': form})

def submit_registration(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegistrationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            u = User.objects.create_user(username = username, password = password, email = email, first_name=first_name, last_name=last_name)
            u.save()
            # redirect to a new URL:
            journal_entry_list = JournalEntry.objects.all()
            return HttpResponseRedirect(reverse('journal_app:index'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegistrationForm()

    return render(request, 'journal_app/view_registration.html', {'form': form})

def view_login(request):
    template = loader.get_template('journal_app/view_login.html')
    form = LoginForm()
    return render(request, 'journal_app/view_login.html', {'form': form})

def submit_login(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # Redirect to a success page.
                    # redirect to a new URL:
                    return HttpResponseRedirect(reverse('journal_app:index'))
                else:
                    # Return a 'disabled account' error message
                    # redirect to a new URL:
                    return HttpResponseRedirect(reverse('journal_app:index'))
            else:
                # Return an 'invalid login' error message.
                # redirect to a new URL:
                error_message = 'Login Failed'
                context = {'form':form, 'error_message':error_message}
                return render(request, 'journal_app/view_login.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegistrationForm()

    return render(request, 'journal_app/view_login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('journal_app:index'))

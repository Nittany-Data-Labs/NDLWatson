from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import EntryForm, RegistrationForm
from .models import JournalEntry

# Create your views here.
def index(request):
    journal_entry_list = JournalEntry.objects.all()
    context = {'journal_entry_list': journal_entry_list}
    return render(request, 'journal_app/index.html', context)

def detail(request, journal_entry_id):
    entry = get_object_or_404(JournalEntry, pk=journal_entry_id)
    return render(request, 'journal_app/detail.html', {'entry': entry})

def record_entry(request):
    template = loader.get_template('journal_app/record_entry.html')
    # Display form
    form = EntryForm()
    return render(request, 'journal_app/record_entry.html', {'form': form})

def submit_entry(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EntryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            body = form.cleaned_data['body']
            pub_date = timezone.now()

            j = JournalEntry(title = title, author = author, body = body, pub_date = pub_date)
            j.save()
            # redirect to a new URL:
            journal_entry_list = JournalEntry.objects.all()
            return HttpResponseRedirect(reverse('journal_app:index'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EntryForm()

    return render(request, 'journal_app/record_entry.html', {'form': form})

@login_required(login_url='failed_login')
def user_access(request):
    return render(request, '/journal_app/user_access.html')

def failed_login(request):
    return render(request, '/journal_app/failed_login.html')

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

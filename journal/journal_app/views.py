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
from .models import JournalEntry, ProcessedEntry, UserProfile

from django.template import Context, RequestContext
from django.shortcuts import render_to_response, get_object_or_404


import json, pprint, requests, base64

# Create your views here.
def index(request, token=''):
    current_user = request.user
    journal_entry_list = ''
    if current_user.is_authenticated():
        print 'authenticated'
        # journal_entry_list = JournalEntry.objects.all()
        journal_entry_list = JournalEntry.objects.filter(author=current_user)
    context = {'journal_entry_list': journal_entry_list, 'current_user': current_user, 's_auth':token}
    return render(request, 'journal_app/index.html', context)

@login_required
def detail(request, journal_entry_id):
    entry = get_object_or_404(JournalEntry, pk=journal_entry_id)
    def getCurrentToken():
        u = request.user
        current_user = UserProfile.objects.get(user=u)
        client_id='13fe94eb9b5549d7a68fb33912b9e16a'
        client_secret='c9fb5919124243048393541378663c2e'

        body = {
            'grant_type': 'authorization_code',
            'refresh_token': current_user.rf,
            'client_id': client_id,
            'client_secret': client_secret,
        }

        r = request.post('https://accounts.spotify.com/api/token', data=body)
        json_token = json.loads(r.content)
        return json_token['access_token']

    def getUser():
        header = {
            'Authorization':'Bearer',
            getCurrentToken()
        }
        ru = requests.get('https://api.spotify.com/v1/me', headers=body)
        json_response = ru.json()
        user_id = json_response['id']
        return user_id


    def createPlaylistAndAddSong(list):
        user_id = getUser()
        header = {
            'Authorization':'Bearer',
            'Content-Type':'application/json',
            getCurrentToken()
        }
        response = requests.post('https://api.spotify.com/v1/users/{user_id}/playlists', data = {'name':'MyLifeMyPlaylist', 'public': False}, headers=header)
        if response:
            playlist_id = response['id']
            playlist_link = response['external_urls']['spotify']
            spotify_uris = []
            for i in list:
                i = i.replace(' ', "+")
                payload = {'q': i, 'type': 'track'}
                _request = requests.get('https://api.spotify.com/v1/search', params=payload, headers=header)
                if _request:
                    tracks = _request['tracks']
                    for j in tracks:
                        if j['type'] == track && j['name'] == i:
                            spotify_uris.append(j['uri'])
            last_request = requests.post('https://api.spotify.com/v1/users/{user_id}/playlists/{playlist_id}/tracks', data = {'uris': spotify_uris}, headers=header)
            if last_request:
                return playlist_link

    if entry.processed == False:
        call_command('paired', entry_id=journal_entry_id)
        entry.processed = True
        entry.save()

        playlist_link = createPlaylistAndAddSong()

    p = ProcessedEntry.objects.filter(entry=entry)
    return render(request, 'journal_app/detail.html', {'entry': entry, 'processed': p, 'playlist_link': playlist_link})

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
            p = UserProfile(user = u)
            p.save()
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

@login_required
def callback(request):

    verification_code = request.GET.get('code')

    client_id='13fe94eb9b5549d7a68fb33912b9e16a'
    client_secret='c9fb5919124243048393541378663c2e'
    redirect_uri='https://mylifemyplaylist.herokuapp.com/journal_app/callback'
    scope='user-library-read playlist-modify-public playlist-modify-private playlist-read-private'

    # def getAccessToken(code):
    payload = {
        'grant_type': 'authorization_code',
        'code': verification_code,
        'redirect_uri': redirect_uri,
        'client_id': client_id,
        'client_secret': client_secret,
    }

    rt = requests.post('https://accounts.spotify.com/api/token', data=payload)

    json_token = json.loads(rt.content)
    u = request.user
    current_user = UserProfile.objects.get(user=u)
    if rt.status_code == 200:
        current_user.sp_token = json_token['access_token']
        current_user.rf_token = json_token['refresh_token']
        current_user.save()

    context = {
        'status_code': rt.status_code,
        'json_token': json_token,
        'verification_code': verification_code,
        'current_user': current_user,
    }

    return render(request, 'journal_app/index.html', context)

def link_spotify(request):
    print 'linking to spotify...'
    client_id='13fe94eb9b5549d7a68fb33912b9e16a'
    client_secret='c9fb5919124243048393541378663c2e'
    redirect_uri='https://mylifemyplaylist.herokuapp.com/journal_app/callback'
    scope='user-library-read playlist-modify-public playlist-modify-private playlist-read-private'

    auth_data = {
        'client_id': client_id,
        'response_type': 'code',
        'redirect_uri': redirect_uri,
        'scope': scope,
        'show_dialog': True,
    }

    print 'sending requests...'
    ra=requests.get('https://accounts.spotify.com/authorize', params=auth_data)

    print 'finished request'
    print ra.status_code
    print ra.url

    return HttpResponseRedirect(ra.url)

import pprint
import sys
import os
import subprocess

import spotipy

import spotipy.util as util


if __name__ == '__main__':

    # scope = 'user-library-read playlist-modify-public playlist-modify-private playlist-read-private'
    scope = ''

    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print "Whoops, need your username!"
        print "usage: python user_playlists.py [username]"
        sys.exit()

    client_id='13fe94eb9b5549d7a68fb33912b9e16a'
    client_secret='c9fb5919124243048393541378663c2e'
    redirect_uri='https://mylifemyplaylist.herokuapp.com/journal_app/'

    token = util.prompt_for_user_token(username=username, scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)

    print token

    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace=True
        playlists = sp.user_playlists(username)
        for playlist in playlists['items']:
            print playlist['name'], str(playlist['id'])
    else:
        print("Can't get token for", username)

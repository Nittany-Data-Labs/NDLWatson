import sys
import spotipy
import spotipy.util as util

scope = 'user-library-read playlist-modify-public playlist-modify-private playlist-read-private'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print "Usage: %s username" % (sys.argv[0],)
    sys.exit()

client_id='13fe94eb9b5549d7a68fb33912b9e16a'
client_secret='c9fb5919124243048393541378663c2e'
redirect_uri='https://mylifemyplaylist.herokuapp.com/journal_app/'

token = util.prompt_for_user_token(username=username, scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)

if token:
    sp = spotipy.Spotify(auth=token)

    sp.user_playlist_create(username, 'MyLifeMyPlaylist')
    print 'MyLifeMyPlaylist created'

    # if not user_playlist(username, 'MyLifeMyPlaylist'):
    #     sp.user_playlist_create(username, 'MyLifeMyPlaylist', public=True)
    # else:



else:
    print "Can't get token for", username

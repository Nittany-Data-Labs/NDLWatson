import requests

verification_code= 'AQAtxseTryP03cHTAhs0hSBtJJtSYmqwDapmQyZeY4cUqkRUl90JE35CsZDdeCWWcjs1e24b3hYKiCVh6K2Ly7UrvN-9fHVpfB4X9mwCXoBAgiGNMxV-JDpSfAtfR-tVBMCxa7_YATpGkajh7D1zFxrH56e90KzAeucTCTiFsE1_vSfX2WEb73urhUCuaEZxj0kEOo3XP_3IKFqjrM6q2NDODCNdX7saiAs7AcGijYO_lWirRUyc60xJ6b0Gi-aXYoJRhBkMG9Az9u-1m3tXOudEbfTwjXPegQ80n0ZEkV9MpiiX0bMmWAZZiNIyz2Vb8hwZkFt612FIBoGymFUsQ854DCBCKqMAP5-NDA'
client_id='13fe94eb9b5549d7a68fb33912b9e16a'
client_secret='c9fb5919124243048393541378663c2e'
redirect_uri='https://mylifemyplaylist.herokuapp.com/journal_app/callback'
scope='user-library-read playlist-modify-public playlist-modify-private playlist-read-private'


payload = {
        'grant_type': 'authorization_code',
        'code': verification_code,
        'redirect_uri': redirect_uri,
        'client_id': client_id,
        'client_secret': client_secret,
    }

rt = requests.post('https://accounts.spotify.com/api/token', params=payload)

print rt.status_code
print rt.content

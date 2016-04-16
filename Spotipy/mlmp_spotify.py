import requests
import json
import pprint
import webbrowser

class SP:
    def __init__(self, client_id='13fe94eb9b5549d7a68fb33912b9e16a', client_secret='c9fb5919124243048393541378663c2e', redirect_uri='https://mylifemyplaylist.herokuapp.com/journal_app/callback', scope='user-library-read playlist-modify-public playlist-modify-private playlist-read-private'):
            self.client_id=client_id
            self.client_secret=client_secret
            self.redirect_uri=redirect_uri
            self.scope = scope

    def getAuthorization(self):
        auth_data = {
            'client_id': self.client_id,
            'response_type': 'code',
            'redirect_uri': self.redirect_uri,
            'scope': self.scope,
            'show_dialog': True,
        }

        r=requests.get('https://accounts.spotify.com/authorize', params=auth_data)
        print r.status_code
        return r.url

    def getAccessToken(self, code):
        payload = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': self.redirect_uri,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
        }

        r=requests.post('https://accounts.spotify.com/api/token', params=payload)
        print r.status_code
        print r.content

if __name__ == '__main__':
    sp = SP()
    code = 'AQD9JHff_1Ni7oACP8ZszwTJnPqgCB73UWj3cySFWjxQdKmUgWAnYwamBPMVuc6wRQlD2ASfCkg-zHViEj3NM2dMRZbJZSKoogdmKS9uquAM_J8CmXMJsNyuiwL38leY4494Nq6JmN_hPgjV95sEQYXWMA0YaZOvw9ZJ9GZpd9ZnP-u651KoLojHOokaG6nlEFxMSXuXjE9ROA8W08XRjajolY75dxaSodZS7_3t-t_3kLR9yYTcA4A_Ec_BpaT6fUrYieauaJj_ud_qIcVmZj2EBu1zi5qtqxfSHGXY_ncNJkIqKF38DaYn8uHFXXGjhsZhOnh4E3oVKPy5sH0_8nZOpdE'
    result = sp.getAuthorization()
    webbrowser.open_new_tab(result)
    sp.getAccessToken(code)

# https://mylifemyplaylist.herokuapp.com/journal_app/?code=AQD9JHff_1Ni7oACP8ZszwTJnPqgCB73UWj3cySFWjxQdKmUgWAnYwamBPMVuc6wRQlD2ASfCkg-zHViEj3NM2dMRZbJZSKoogdmKS9uquAM_J8CmXMJsNyuiwL38leY4494Nq6JmN_hPgjV95sEQYXWMA0YaZOvw9ZJ9GZpd9ZnP-u651KoLojHOokaG6nlEFxMSXuXjE9ROA8W08XRjajolY75dxaSodZS7_3t-t_3kLR9yYTcA4A_Ec_BpaT6fUrYieauaJj_ud_qIcVmZj2EBu1zi5qtqxfSHGXY_ncNJkIqKF38DaYn8uHFXXGjhsZhOnh4E3oVKPy5sH0_8nZOpdE

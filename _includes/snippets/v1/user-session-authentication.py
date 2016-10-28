import requests


def get_session(force=False):
    token_file = '.oncrawl-token.txt'
    session = requests.session()
    token = None
    if not force:
        try:
            with open(token_file) as istr:
                token = istr.read().rstrip()
        except IOError:
            pass
    if token is None:
        # Authenticate
        resp = session.post('https://app.oncrawl.com/api/session',
                            json=dict(identification='USERNAME',
                                      password='PASSWORD'))
        token = resp.json()['session']['token']
        with open(token_file, 'w') as ostr:
            ostr.write(token)
    session.headers['x-oncrawl-token'] = token
    return session


def list_projects(session):
    resp = session.get('https://app.oncrawl.com/api/projects')
    for project in resp.json()['projects']:
        print '{name}: {start_url}'.format(**project)


if __name__ == '__main__':
    session = get_session()
    list_projects(session)

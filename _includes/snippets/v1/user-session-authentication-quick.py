import requests
# Authenticate
resp = requests.post('https://app.oncrawl.com/api/session',
                     json=dict(identification='USERNAME',
                               password='PASSWORD'))
token = resp.json()['session']['token']
# List projects
resp = requests.get('https://app.oncrawl.com/api/projects',
                    headers={'x-oncrawl-token': token})
for project in resp.json()['projects']:
    print '{id}: {start_url}'.format(**project)

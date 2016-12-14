import json, requests

token = 'TOKEN'
crawl_id = 'CRAWL-ID'
url = 'https://app.oncrawl.com/api/crawls/{}/url-explorer'.format(crawl_id)
params = dict(
  limit=5,
  base_filters='nearduplicate_content:true',
  fields='url,inrank,status_code,meta_robots,clusters',
  sort='clusters:desc',
)
resp = requests.get(url, headers={'x-oncrawl-token': token}, params=params)
print json.dumps(resp.json(), indent=2, sort_keys=True)

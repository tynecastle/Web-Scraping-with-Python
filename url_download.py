# -*- coding: utf-8 -*-

from urllib import request
from urllib.error import URLError

def download(url, user_agent='wswp', num_retries=2):
  print('Downloading:', url)
  headers = {'User-agent': user_agent}
  req = request.Request(url, headers=headers)
  try:
    html = request.urlopen(req).read()
  except URLError as e:
    print('Download error:', e.reason)
    html = None
    if num_retries > 0:
      if hasattr(e,'code') and 500 <= e.code < 600:
        # recursively retry 5xx HTTP errors
        return download(url, num_retries-1)
  return html

if __name__ == '__main__':
  print(download('http://example.webscraping.com/sitemap.xml'))
  #print(download('http://www.google.com'))
  #print(download('http://www.isli.ac.uk'))
  #print(download('http://httpstat.us/500'))

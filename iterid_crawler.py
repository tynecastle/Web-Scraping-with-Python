import itertools
from url_download import download

# maximum number of consecutive download errors allowed
max_err = 5
# current number of consecutive download errors
curr_err = 0

for page in itertools.count(3):
  url = 'http://example.webscraping.com/index/%d' % page
  html = download(url)
  if html is None:
    # received an error trying to download this page
    curr_err += 1
    if curr_err == max_err:
      break
  else:
    print('Page %d is downloaded successfully!' % page)
    curr_err = 0

import flickr_api
import sys
import os
from dotenv import load_dotenv

load_dotenv()
FLICKR_API_KEY = os.getenv("FLICKR_API_KEY")
FLICKR_API_SECRET = os.getenv("FLICKR_API_SECRET")
if FLICKR_API_KEY is None or FLICKR_API_SECRET is None:
  print('The download script requires Flickr API keys.')
  print()
  print('Visit https://www.flickr.com/services/apps/create/ to request your keys.')
  print()
  print('Then, create a file called .env in this directory that contains your keys, like this:')
  print()
  print('  FLICKR_API_KEY = \'the_api_key_you_got_from_flickr\'')
  print('  FLICKR_API_SECRET = \'the_api_secret_you_got_from_flickr\'')
  print()
  sys.exit(0)

flickr_api.set_keys(api_key=FLICKR_API_KEY, api_secret=FLICKR_API_SECRET)

AUTH_FILENAME = 'flickr.key'
if not os.path.exists(AUTH_FILENAME):
  a = flickr_api.auth.AuthHandler()
  perms = "read"
  url = a.get_authorization_url(perms)
  print()
  print('To download your personal photos from Flickr you need to login first.')
  print('Visit the following URL, then paste in the oauth_verifier code and press enter:')
  print()
  print(url)
  print()
  oauth_verifier = input("oauth_verifier code: ")
  a.set_verifier(oauth_verifier)
  flickr_api.set_auth_handler(a)
  a.save('flickr.key')
  #sys.exit(0)

flickr_api.set_auth_handler(AUTH_FILENAME)

def ensure_dir(dirname):
  try:
    os.makedirs(dirname)
  except FileExistsError:
    pass
  except:
    raise

user = flickr_api.test.login()
photosets = user.getPhotosets()
for photoset in photosets:
  print('{} {}'.format(photoset.id, photoset.title))
  photoset_dir = 'photos/{}'.format(photoset.id)
  ensure_dir(photoset_dir)
  photos = photoset.getPhotos()
  for photo in photos:
    filename = '{}_o'.format(photo.id)
    abs_filename = os.path.join(photoset_dir, filename)
    if not os.path.exists(abs_filename + '.jpg'):
      print('  {} {}'.format(photo.id, photo.title))
      try:
        photo.save(abs_filename, size_label = 'Original')
      except KeyboardInterrupt:
        print('CTRL-C received, stopping...')
        try:
          os.remove(abs_filename + '.jpg')
        except FileNotFoundError:
          pass
        sys.exit(0)

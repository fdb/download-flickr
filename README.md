# Flickr Image downloader

This is a Python 3 script that downloads all your personal Flickr photos.

## Setup

### Getting the source code
Download the script using the normal method:

```
git clone https://github.com/fdb/download-flickr.git
cd download-flickr
```

Install dependencies using [pipenv](https://pipenv.readthedocs.io/en/latest/). On Mac, you can install Pipenv using Homebrew by typing `brew install pipenv`. On other systems, you can install it using `pip install --user pipenv`. Then run

```
pipenv install
```

### Flickr API Keys

To use this you need Flickr API keys. You can [request those here](https://www.flickr.com/services/apps/create/).
Create a file `.env` in the directory of the `download-flickr` folder that contains the following lines:

```
FLICKR_API_KEY = 'the_api_key_you_got_from_flickr'
FLICKR_API_SECRET = 'the_api_secret_you_got_from_flickr'
```

## Running
Run the following command to download all photos in your sets:

```
pipenv run python3 download.py
```

If this is the first time you run this script, it will ask to login:

```
To download your personal photos from Flickr you need to login first.
Visit the following URL, then paste in the oauth_verifier code and press enter:

https://www.flickr.com/services/oauth/authorize?oauth_token=16238489762138476-1287364128673123&perms=read

oauth_verifier code:
```
Open the URL in a browser, login and allow access. Then copy and paste the oauth_verifier code you get back from Flickr. It looks like `8737edb434cdd101`.

An authorization key is stored locally in the `download-flickr` folder in a file called `flickr.key`. This information stays and your machine and is never shared.

## Good to know
- Images you have already downloaded are skipped, so you can interrupt the process and continue later.
- Note that photos not in sets are not downloaded.

## Credits

This script is a simple wrapper around the [Python Flickr API](https://github.com/alexis-mignon/python-flickr-api) package by [Alexis Mignon](https://github.com/alexis-mignon).

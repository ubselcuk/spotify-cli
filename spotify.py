import os
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

with open("/home/anxiety/Documents/spotify-cli/user.json", "r") as f:
    data = json.load(f)

os.environ["SPOTIPY_CLIENT_ID"] = data['client_id']
os.environ["SPOTIPY_CLIENT_SECRET"] = data['client_secret']
os.environ["SPOTIPY_REDIRECT_URI"] = data['redirect_uri']


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=data['client_id'],
                                               client_secret=data['client_secret'],
                                               redirect_uri=data['redirect_uri'],
                                               scope=data['scope'],
                                               cache_path="/home/anxiety/Documents/spotify-cli/.cache-" + data['username']))



def next():
    sp.next_track()

def prev():
    sp.previous_track()

def start():
    if isplaying() == False:
        sp.start_playback()
    else:
        print('the music is already playing')

def pause():
    if isplaying() == True:
        sp.pause_playback()
    else:
        print('the music has already stopped')

def isplaying():
    pt = sp.current_user_playing_track()
    return pt['is_playing']

def now_playing():
    pt = sp.current_user_playing_track()
    artist = pt['item']['artists'][0]['name']
    track = pt['item']['name']
    print('{} ~ {}'.format(artist,track))
    
def device():
    dev = sp.devices()['devices'][0]['name']
    name = sp.current_user()['display_name']
    print('Device ~ {} | User ~ {}'.format(dev,name))

def volume(x):
    if x > 0 and x < 100:
        sp.volume(x)

def repeat(r):
    if r == 'track':
        sp.repeat('track')
    elif r == 'context':
        sp.repeat('context')
    elif r == 'off':
        sp.repeat('off')



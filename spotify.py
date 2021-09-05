import os
import json
import spotipy
from datetime import datetime
from spotipy.oauth2 import SpotifyOAuth

if __name__ == "__main__":
    print('Do not run this code directly, run cli.py to use the program.')
else:

    with open(os.path.dirname(__file__) + "/user.json", "r") as f:
        data = json.load(f)

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=data['client_id'],
                                                   client_secret=data['client_secret'],
                                                   redirect_uri=data['redirect_uri'],
                                                   scope=data['scope'],
                                                   cache_path=os.path.dirname(
                                                       __file__) + '/.cache-' + data['username']
                                                   ))

    def next():
        try:
            sp.next_track()
        except:
            print('help uwu')

    def prev():
        sp.previous_track()

    def start():
        if isplaying() == False:
            sp.start_playback()
        else:
            print("Looks like the song is already playing on spotify.")

    def pause():
        if isplaying() == True:
            sp.pause_playback()
        else:
            print("Looks like the song is already stopped on spotify.")

    def isplaying():
        pt = sp.current_user_playing_track()
        return pt['is_playing']

    def now_playing():
        if isplaying() == True:
            pt = sp.current_user_playing_track()
            artist = pt['item']['artists'][0]['name']
            track = pt['item']['name']
            print('{} ~ {}'.format(artist, track))
        else:
            print('The song is not playing right now.')

    def device():
        dev = sp.devices()['devices'][0]['name']
        name = sp.current_user()['display_name']
        print('Device ~ {} | User ~ {}'.format(dev, name))

    def volume(x):
        if x >= 0 and x <= 100:
            sp.volume(x)
        elif x > 100:
            print('I think you want to be deaf, please enter a value between 0 and 100.')
        else:
            print('Please enter a value between 0 and 100 when adjusting the volume.')

    def repeat(r):
        if r == 'track':
            sp.repeat('track')
        elif r == 'context':
            sp.repeat('context')
        elif r == 'off':
            sp.repeat('off')
        else:
            print('Try again by selecting one of the options.\nOptions: track, context, off')

    def test():
        pt = sp.current_user_playing_track()
        os.system('feh ' + pt['item']['album']['images'][0]['url'])

    def save():

        pt = sp.current_user_playing_track()

        
        y = {"date": str(datetime.now().strftime("%m %d %Y ~ %H:%M")),
             "track": pt['item']['name'],
             "artist": pt['item']['artists'][0]['name']}
     
        with open(os.path.dirname(__file__) + "/history.json",'r+') as file:
            file_data = json.load(file)

            file_data["saved"].append(y)

            file.seek(0)

            json.dump(file_data, file, indent = 4)

    def saved():
        with open(os.path.dirname(__file__) + "/history.json", "r") as f:
            data = json.load(f)
            for numb in data['saved']:
                print(numb['date'] + ' ~ ' + numb['track'] + ' ~ ' + numb['artist'])
            
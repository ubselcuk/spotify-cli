import json
import os
import urllib.parse
import urllib.request
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import spotipy
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

        with open(os.path.dirname(__file__) + "/history.json", 'r+') as file:
            file_data = json.load(file)

            file_data["saved"].append(y)

            file.seek(0)

            json.dump(file_data, file, indent=4)

    def saved():
        with open(os.path.dirname(__file__) + "/history.json", "r") as f:
            data = json.load(f)
            for numb in data['saved']:
                print(numb['date'] + ' ~ ' + numb['track'] + ' ~ ' + numb['artist'])

    def lyrics():
        # api_base
        client_access_token = "pySueg-HGk7MGO1b8SGob8GSRQw3tPW4QIyGdOHTCnYoO6tdaS63oAZQ_sXEaiFg"
        api_base = "https://api.genius.com"

        try:  # if artist returns none
            pt = sp.current_user_playing_track()
            artist = pt['item']['artists'][0]['name']
            track = pt['item']['name']
            artist_and_track = artist + track
        except TypeError:
            print("You need to open a song first (づ｡◕‿‿◕｡)づ ♬♪ ♪")
            return

        # search request
        search = "/search?q="
        query = api_base + search + urllib.parse.quote(artist_and_track)
        request = urllib.request.Request(query)
        request.add_header("Authorization", "Bearer {}".format(client_access_token))

        # get search response
        response = urllib.request.urlopen(request, timeout=3)
        raw = response.read().decode(response.headers.get_content_charset())
        data = json.loads(raw)["response"]["hits"]

        # --------- VERIFY RESPONSE ---------
        # print("SEARCHED: ", artist_and_track)
        # print("FOUND: ", data[0]["result"]["primary_artist"]["name"], data[0]["result"]["title"])

        # song request
        try:  # if no lyrics found
            song_api_path = data[0]["result"]["api_path"]
        except IndexError:
            print("No lyrics found for {} ~ {}".format(artist, track))
            return

        query = api_base + song_api_path
        request = urllib.request.Request(query)
        request.add_header("Authorization", "Bearer {}".format(client_access_token))

        # --------- VERIFY REQUEST ---------
        # print("API_PATH: ", song_api_path)
        # print("QUERY: ", query)

        # get song response
        response = urllib.request.urlopen(request, timeout=3)
        raw = response.read().decode(response.headers.get_content_charset())
        data_song = json.loads(raw)

        # song path url
        songpath = data_song["response"]["song"]["path"]

        # --------- VERIFY RESPONSE ---------
        # print("SONG PATH: ", song_api_path)
        # print("FOUND PATH: ", songpath)

        # HTML parsing
        base = "https://genius.com"
        url = base + song_api_path
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")

        [h.extract() for h in soup('script')]

        try:  # if failed to get text
            lyrics = soup.find("div", class_="lyrics").get_text()
            print("\n\n", artist, " ~ ", track, lyrics)
        except AttributeError:
            print("Couldn't get lyrics, please try again (╯°□°)╯︵ ┻━┻")



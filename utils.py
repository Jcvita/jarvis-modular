import pyttsx3
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from flask import make_response

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

PLAY_MUSIC_KEYWORDS = ['play', 'pay', 'listen']
PAUSE_MUSIC_KEYWORDS = ['pause', 'paws', 'paul\'s']

volume = 50


def process_input(query: str, wake_word=True, quiet_mode=False):
    cmd = query.split("_")
    if wake_word:
        cmd = cmd[cmd.index('jarvis') + 1:]
    if cmd[0] == 'set':
        if cmd[1] == 'volume':
            for word in cmd:
                if word.isnumeric():
                    if int(word) > 100:
                        return change_volume(100, quiet_mode)
                    elif int(word) < 0:
                        return change_volume(0, quiet_mode)
                    else:
                        return change_volume(int(word), quiet_mode)
                else:
                    continue
        if cmd[1] == 'alarm':
            if cmd[2] == 'for' or cmd[2] == 'at':
                pass  # TODO set an action to happen at a certain datetime object (maybe create a thread)
            if cmd[2] == 'sound':
                pass  # TODO store a variable somewhere of a sound
    if cmd[0] == 'remove' or cmd[0] == 'delete':

    if cmd[0] in PLAY_MUSIC_KEYWORDS:
        pass
    return make_response('Didn\'t understand arguments\n', 200)


def change_volume(vol: int, quiet_mode: bool):
    global volume
    volume = vol
    if not quiet_mode:
        speak(f'Set volume to {volume}')
    return make_response(f'Successfully changed volume to {volume}', 200)


def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('volume', volume / 100)
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def song_title_to_uri(title, artist):
    spotipy.Spotify.s


def play_song_with_spotify(uris: list):
    sp.volume(volume)
    sp.start_playback(sp.start_playback(uris=uris))

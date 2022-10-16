# This is a sample Python script.
from spotify_bot_player.spotify_runner import SpotifyRun


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    artist_uri = 'spotify:artist:3vEwg9EAiya6EsVv43AGT4'
    artist_track1 = 'spotify:track:7bvAJHOSrV8IRipnopqczx' #Lamelo
    artist_track2 = 'spotify:track:7bvAJHOSrV8IRipnopqczx' #Quarantine2
    sr = SpotifyRun(artist_uri=artist_uri, track_uri=artist_track2)
    sr.artist_info()
    sr.run_spotify()

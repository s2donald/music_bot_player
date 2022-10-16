from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as selEc
from selenium.webdriver.common.by import By as selBy
from selenium.webdriver.support.ui import WebDriverWait
import json, time, threading, random, sys
from common.definition import links, xpaths
from selenium import webdriver
import time

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials



class SpotifyRun():
    def __init__(self, artist_uri, track_uri):
        auth_manager = SpotifyClientCredentials(client_id='832dd1fa0c1f4a528ab44cb2a304f94c', client_secret='668da88de72042e5bf7b261b88aa2b24')
        self.sp = spotipy.Spotify(auth_manager=auth_manager)
        self.artist_uri = artist_uri
        self.track_uri = track_uri

    def run_spotify(self):
        driver = webdriver.Chrome()
        driver.get(self.sp.track(self.track_uri)['album']['external_urls']['spotify'])
        time.sleep(10)
        report1 = driver.find_element_by_xpath('//button[@class="Button-qlcn5g-0 kgFBvD"]')
        report1.click()
        print('clicked')
        time.sleep(60)
        driver.close()
        return print('lolz')

        # return self.sp.track(self.track_uri)['album']['external_urls']['spotify']


    def artist_info(self):
        return self.sp.artist(artist_id=self.artist_uri)
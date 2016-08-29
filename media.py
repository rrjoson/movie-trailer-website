import webbrowser
import urllib
import json
import requests
from bs4 import BeautifulSoup


class Movie():
    """This class provides a way to store movie related information

        Attributes:
            title (str): The title of the movie

    """

    # Creates an instance
    def __init__(self, title):
        url = "http://www.omdbapi.com/?t=" + title + "&y=&plot=short&r=json"
        connection = urllib.urlopen(url)  # Opens the url
        output = json.load(connection)  # Loads the json output

        self.title = output['Title']
        self.storyline = output['Plot']
        self.poster_image_url = output['Poster']
        self.trailer_youtube_url = self.get_trailer_url(title)

        connection.close()  

    # Gets the youtube link of the trailer of the movie
    def get_trailer_url(self, title):

        # Store the reponse of the get request
        response = requests.get(url = "https://youtube.com/results", params={
            'search_query': title + " trailer"
        })

        # Parse the DOM
        soup = BeautifulSoup(response.content, "html.parser")

        # Return the first video link in the search result
        for video in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
            return "https://youtube.com" + video["href"]

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
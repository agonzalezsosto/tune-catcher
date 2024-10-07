import os
import requests
from utils import convert_to_url_safe_text
from abc import ABC, abstractmethod

class AlbumDataSource(ABC):
    @abstractmethod
    def fetch_album_data(self, search_string: str) -> dict:
        pass

class LastFmDataSource(AlbumDataSource):
    def fetch_album_data(self, search_string: str) -> dict:
        search_string = convert_to_url_safe_text(search_string)
        key = os.getenv("LAST_FM_API_KEY")
        url = f"https://ws.audioscrobbler.com/2.0/?method=album.search&album={search_string}&api_key={key}&format=json"
        response = requests.get(url)
        json_result = response.json()
        album_matches = json_result.get("results", {}).get("albummatches", {})
        album_set = album_matches.get("album", [])

        try:
            album = album_set[0]
            return {
                "artist": album.get("artist"),
                "album": album.get("name"),
            }
        except Exception as e:
            raise Exception(f"Couldn't find {search_string} in LastFM")

class AlbumArtist:
    def __init__(self, search_string: str, data_source: AlbumDataSource):
        self.search_string = search_string
        self.data_source = data_source

    def get_album_data(self) -> dict:
        album = self.data_source.fetch_album_data(self.search_string)

        return {
            "artist": album.get("artist"),
            "album": album.get("album"),
        }
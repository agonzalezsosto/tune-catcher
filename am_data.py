import requests
from utils import convert_to_url_safe_text
from dataclasses import dataclass
from datetime import datetime

@dataclass
class AlbumData:
    artist: str
    album: str
    apple_music_link: str
    release_date: datetime
    source: str = ""


class AppleMusicData:
    def __init__(self, artist: str, album: str):
        self.artist = artist
        self.album = album

    def get_album_data(self) -> AlbumData:
        album_json = self.__get_album_json()
        apple_music_link = album_json.get("collectionViewUrl")
        release_date = album_json.get("releaseDate")

        return AlbumData(album=self.album, artist=self.artist, apple_music_link=apple_music_link, release_date=release_date)


    def __get_album_json(self):
        artist = convert_to_url_safe_text(self.artist)
        url = f"https://itunes.apple.com/search?term={artist}&media=music&entity=album&limit=200&country=gb"


        try:
            response = requests.get(url)
            json_result = response.json()
            album_results = json_result["results"]

            for album_result in album_results:
                if album_result.get("artistName") == self.artist and album_result.get("collectionName") == self.album:
                    return album_result
        except:
            raise Exception(f"Couldn't find data for {self.artist} - {self.album} on iTunes")
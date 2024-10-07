from album_artist import  AlbumArtist, LastFmDataSource
from rss_feed_extractor import PitchforkRssExtractor
from rss_feed_extractor import RssFeedExtractor
from am_data import AppleMusicData
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()

    album_search_terms = []
    album_search_terms += PitchforkRssExtractor().get_search_terms()
    for album_search_term in album_search_terms:
        try:
            album_artist = AlbumArtist(album_search_term, LastFmDataSource()).get_album_data()
            am_data = AppleMusicData(artist=album_artist.get("artist"), album=album_artist.get("album")).get_album_data()
            print(am_data)
        except Exception as e:
            print(f"Couldn't find {album_search_term}")


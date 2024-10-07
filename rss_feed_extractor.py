from abc import abstractmethod, ABC
from typing import List

import requests
import feedparser

class RssFeedExtractor(ABC):
    @abstractmethod
    def get_search_terms(self) -> List[str]:
        pass

class PitchforkRssExtractor(RssFeedExtractor):
    def get_search_terms(self) -> List[str]:
        pitchfork_rss_url = "https://pitchfork.com/feed/feed-album-reviews/rss"
        pitchfork_base_url = "https://pitchfork.com/reviews/albums/"

        response = requests.get(pitchfork_rss_url)
        feed = feedparser.parse(response.content)
        search_terms = []
        for entry in feed.entries:
            search_terms.append(entry.get("link").replace(pitchfork_base_url, ''))

        return search_terms
import os
import json
from langchain_tavily import TavilySearch
from langchain_google_community import GooglePlacesTool, GooglePlacesAPIWrapper 

class FoursquarePlaceSearchTool:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.foursquare.com/v3/places/search"
        self.headers = {
            "Accept": "application/json",
            "Authorization": self.api_key
        }

    def _search(self, query: str, location: str, limit: int = 5):
        params = {
            "query": query,
            "near": location,
            "limit": limit
        }
        response = requests.get(self.base_url, headers=self.headers, params=params)
        response.raise_for_status()
        results = response.json().get("results", [])
        return [place["name"] for place in results if place.get("name")]

    def foursquare_search_attractions(self, place: str) -> list:
        return self._search("attractions", place)

    def foursquare_search_restaurants(self, place: str) -> list:
        return self._search("restaurants", place)

    def foursquare_search_activity(self, place: str) -> list:
        return self._search("things to do", place)

    def foursquare_search_transportation(self, place: str) -> list:
        return self._search("transportation", place)


class TavilyPlaceSearchTool:
    def __init__(self):
        pass

    def tavily_search_attractions(self, place: str) -> dict:
        """
        Searches for attractions in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"top attractive places in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result
    
    def tavily_search_restaurants(self, place: str) -> dict:
        """
        Searches for available restaurants in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"what are the top 10 restaurants and eateries in and around {place}."})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result
    
    def tavily_search_activity(self, place: str) -> dict:
        """
        Searches for popular activities in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"activities in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result

    def tavily_search_transportation(self, place: str) -> dict:
        """
        Searches for available modes of transportation in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"What are the different modes of transportations available in {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result
    
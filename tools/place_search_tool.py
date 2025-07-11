from utils.place_info_search import FoursquarePlaceSearchTool, TavilyPlaceSearchTool
from typing import List
from langchain.tools import tool
from dotenv import load_dotenv
import os

class PlaceSearchTool:
    def __init__(self):
        load_dotenv()
        self.foursquare_api_key = os.environ.get("FOURSQUARE_API_KEY")
        self.foursquare_search = FoursquarePlaceSearchTool(self.foursquare_api_key)
        self.tavily_search = TavilyPlaceSearchTool()
        self.place_search_tool_list = self._setup_tools()

    def _setup_tools(self) -> List:
        """Setup all tools for the place search tool"""

        @tool
        def search_attractions(place: str) -> str:
            """Search attractions of a place"""
            try:
                result = self.foursquare_search.foursquare_search_attractions(place)
                return f"Attractions in {place} (via Foursquare): {', '.join(result)}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_attractions(place)
                return f"Foursquare failed: {e}\nFallback results: {tavily_result}"

        @tool
        def search_restaurants(place: str) -> str:
            """Search restaurants of a place"""
            try:
                result = self.foursquare_search.foursquare_search_restaurants(place)
                return f"Restaurants in {place} (via Foursquare): {', '.join(result)}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_restaurants(place)
                return f"Foursquare failed: {e}\nFallback results: {tavily_result}"

        @tool
        def search_activities(place: str) -> str:
            """Search activities of a place"""
            try:
                result = self.foursquare_search.foursquare_search_activity(place)
                return f"Activities in {place} (via Foursquare): {', '.join(result)}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_activity(place)
                return f"Foursquare failed: {e}\nFallback results: {tavily_result}"

        @tool
        def search_transportation(place: str) -> str:
            """Search transportation options of a place"""
            try:
                result = self.foursquare_search.foursquare_search_transportation(place)
                return f"Transport options in {place} (via Foursquare): {', '.join(result)}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_transportation(place)
                return f"Foursquare failed: {e}\nFallback results: {tavily_result}"

        return [
            search_attractions,
            search_restaurants,
            search_activities,
            search_transportation
        ]

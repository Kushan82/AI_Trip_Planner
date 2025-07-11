from utils.model_loader import ModelLoader
from prompt_library.prompt import SYSTEM_PROMPT
from langgraph.graph import StateGraph, END, START
from typing import TypedDict, List, Dict, Any
from langgraph.prebuilt import ToolNode, tools_condition

from tools.weather_info_tool import WeatherInfoTool
from tools.place_search_tool import PlaceSearchTool
from tools.expense_calculator_tool import CalculatorTool
from tools.currency_conversion_tool import CurrencyConverterTool


# 🧠 Define a TypedDict for the graph state (replaces MessageState)
class TripPlannerState(TypedDict):
    messages: List[Dict[str, Any]]


class GraphBuilder:
    def __init__(self, model_provider: str = "groq"):
        self.model_loader = ModelLoader(model_provider=model_provider)
        self.llm = self.model_loader.load_llm()

        # ✅ Tool initialization and aggregation
        self.weather_tools = WeatherInfoTool()
        self.place_search_tools = PlaceSearchTool()
        self.calculator_tools = CalculatorTool()
        self.currency_converter_tools = CurrencyConverterTool()

        # 👇 Fix: use correct attribute names
        self.tools = (
            self.weather_tools.weather_tool_list
            + self.place_search_tools.place_search_tool_list
            + self.calculator_tools.calculator_tool_list
            + self.currency_converter_tools.currency_converter_tool_list
        )

        # ✅ Bind LLM with tools
        self.llm_with_tools = self.llm.bind_tools(tools=self.tools)

        self.system_prompt = SYSTEM_PROMPT
        self.graph = None

    def agent_function(self, state: TripPlannerState) -> TripPlannerState:
        user_messages = state["messages"]
        input_messages = [self.system_prompt] + user_messages

        response = self.llm_with_tools.invoke(input_messages)
        return {"messages": user_messages + [response]}  # Append new message

    def build_graph(self):
        # ✅ Use TypedDict instead of MessageState
        graph_builder = StateGraph(TripPlannerState)

        graph_builder.add_node("agent", self.agent_function)
        graph_builder.add_node("tools", ToolNode(tools=self.tools))

        graph_builder.add_edge(START, "agent")
        graph_builder.add_conditional_edges("agent", tools_condition)
        graph_builder.add_edge("tools", "agent")
        graph_builder.add_edge("agent", END)

        self.graph = graph_builder.compile()
        return self.graph

    def __call__(self):
        return self.build_graph()

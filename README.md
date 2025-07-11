#  🤵‍♂️Travel Butler Ai Agent

An AI-powered travel planning assistant that helps users generate smart itineraries, explore places, calculate travel expenses, and get real-time weather updates. Built using LangChain, LangGraph, and Streamlit, this assistant is designed to streamline your travel planning with smart tools and contextual conversations.

---

## 🚀 Features

- 🔍 **Place Discovery:** Search and learn about tourist spots and attractions.
- 🌤 **Live Weather Updates:** Fetch real-time weather conditions for any location.
- 💱 **Currency Converter:** Convert currencies on the fly using the latest exchange rates.
- 🧮 **Expense Calculator:** Estimate your trip expenses based on various inputs.
- 🧠 **Agentic Workflow:** Powered by LangGraph and LangChain agents to route tasks intelligently.
- 🖼 **Visual Interface:** Clean and interactive UI via Streamlit.

---

## 📁 Project Structure
AI_Trip_Planner/
│
├── main.py # Entry point for core logic
├── streamit_app.py # Streamlit frontend
├── requirements.txt # Dependencies
├── setup.py # Package setup
├── pyproject.toml # Build configuration
│
├── agent/ # Agent logic using LangChain & LangGraph
│ └── agentic_workflow.py
│
├── tools/ # Toolset for the agent (search, weather, currency, etc.)
│ ├── place_search_tool.py
│ ├── weather_info_tool.py
│ ├── currency_conversion_tool.py
│ └── expense_calculator_tool.py
│
├── utils/ # Utility functions for support
│ ├── place_info_search.py
│ ├── config_loader.py
│ ├── currency_converter.py
│ └── save_to_document.py
│
├── config/ # Configuration files
│ └── config.yaml
│
├── logger/ # Custom logging logic
│ └── logging.py
│
├── exception/ # Error handling
│ └── exceptionhandling.py
│
├── prompt_library/ # Custom prompts for the agent
│ └── prompt.py
│
└── notebook/ # Experimental notebooks
└── exp.ipynb

## 🔧 Installation
git clone https://github.com/your-username/AI_Trip_Planner.git
pip install uvicorn
cd AI_Trip_Planner
uv venv venv
source venv/bin/activate   # or venv\Scripts\activate.bat on Windows
uv pip install -r requirements.txt

🧠 How It Works
This app uses a combination of:
  -LangChain Agents for tool routing and execution.
  -LangGraph for orchestrating multi-step workflows.
  -Google Places API and Tavily for place search and contextual content.
  -Streamlit for the user interface.

▶️ Run the App
streamlit run streamlit_app.py





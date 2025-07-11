import os
from typing import Any, Optional, Literal
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from utils.config_loader import load_config
from langchain_groq import ChatGroq

class ConfigLoader:
    def __init__(self):
        print(f"Loading configuration ...")
        self.config = load_config()

    def __getitem__(self,key):
        return self.config[key]

class ModelLoader(BaseModel):
    model_provider: Literal["groq"]="groq"
    config: Optional[ConfigLoader]= Field(default = None, exclude=True)

    def model_post_init(self, __context:Any) -> None:
        self.config = ConfigLoader()

    class Config:
        arbitrary_types_allowed = True
    
    def load_llm(self):
        print("Loading LLM ...")
        print(f" loading Model from provider: {self.model_provider}")
        if self.model_provider == "groq":
            print("Loading LLM from Groq model ...")
            groq_api_key = os.getenv("GROQ_API_KEY")
            model_name = self.config["llm"]["groq"]["model_name"]
            llm = ChatGroq(model_name=model_name, api_key=groq_api_key)
        return llm
from fastapi import FastAPI
from pydantic import BaseModel
import os

app=FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
async def query_travel_agent(query:QueryRequest):
    try:
        print(query)
        graph = Graphbuilder(modek_provider="groq")
        react_app=graph()

        png_graph =react_app.get_graph().draw_mermaid_png()
        with open("my_graph_png", "wb")as f:
            f.write(png_graph)
        print(f"Graph saved as 'my_graph_png' in {os.getcwd()}")
        messages = {"messages":[query.question]}
        output= react_app.invoke(messages)

        if ininstance(output,dict) and "messages" in output:
            final_output = output["messages"][-1].content
        else:
            final_output = str(output)
        return {"amswer": final_output}
    except Exception as e:
        return JSONResponse(status_code=500, content = {"error":str(e)})
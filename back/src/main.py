from fastapi import FastAPI
import sys
import uvicorn

#from all_classes_list import *



app = FastAPI()

@app.get("/")
async def get_main_page():
    try:
        return {"text" : "Main Page"}
    except:
        e = sys.exc_info()[1]
        print(e.args[0])

@app.get("/users")
async def get_main_page():
    try:
        return {"text" : "users"}
    except:
        e = sys.exc_info()[1]
        print(e.args[0])



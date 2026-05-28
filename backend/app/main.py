import threading
import time
import requests

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.hba1c import router as hba1c_router
from routes.proteinuria24h import router as proteinuria_router
from routes.relacao_prot_creatinina import router as rpc_router

app = FastAPI()

def keep_alive():

    while True:

        try:
            requests.get("https://labcalc-online.onrender.com/ping")
            print("Ping enviado")

        except Exception as e:
            print(e)

        time.sleep(45)

@app.on_event("startup")
def iniciar_keepalive():

    thread = threading.Thread(target=keep_alive)
    thread.daemon = True
    thread.start()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"LabCalc": "online"}

@app.get("/ping")
def ping():
    return {"status": "awake"}

app.include_router(hba1c_router)
app.include_router(proteinuria_router)
app.include_router(rpc_router)
import threading
import time

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.hba1c import router as hba1c_router
from routes.proteinuria24h import router as proteinuria_router
from routes.relacao_prot_creatinina import router as rpc_router
from routes.proteinas_tf import router as proteinas_router
from routes.calcio_ionico import router as calcio_ionico_router

app = FastAPI()



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
app.include_router(proteinas_router)
app.include_router(calcio_ionico_router)

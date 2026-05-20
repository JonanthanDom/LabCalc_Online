from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from Backend.app.routes.hba1c import router as hba1c_router
from Backend.app.routes.proteinuria24h import router as proteinuria_router
from Backend.app.routes.relacao_prot_creatinina import router as rpc_router

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


app.include_router(hba1c_router)
app.include_router(proteinuria_router)
app.include_router(rpc_router)
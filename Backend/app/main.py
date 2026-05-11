from fastapi import FastAPI

from routes.hba1c import router as hba1c_router
from routes.proteinuria24h import router as proteinuria_router
from routes.relacao_prot_creatinina import router as rpc_router
app = FastAPI()

app.include_router(hba1c_router)
app.include_router(proteinuria_router)
app.include_router(rpc_router)

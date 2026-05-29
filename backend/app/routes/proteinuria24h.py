from typing import Optional
from fastapi import APIRouter, HTTPException
from services.bioquimica import calcular_proteinuria_service

router = APIRouter()


@router.get("/proteinuria24h")
def calcular_proteinuria(
    volume_ml_24h: Optional[str] = None,
    proteina_mgdl: Optional[str] = None,
):

    # Verifica campos vazios
    if not volume_ml_24h or not proteina_mgdl:

        raise HTTPException(
            status_code=400,
            detail="Preencha volume e proteína."
        )

    try:

        # Aceita vírgula ou ponto
        volume_ml_24h = float(volume_ml_24h.replace(",", "."))

        proteina_mgdl = float(proteina_mgdl .replace(",", "."))

               # service
        resultado_proteinuria = calcular_proteinuria_service(
            volume_ml_24h,
            proteina_mgdl
        )
        return resultado_proteinuria
    

      
    except ValueError:

        raise HTTPException(
            status_code=400,
            detail="Valor numérico inválido."
        )
    
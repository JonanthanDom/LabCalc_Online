from fastapi import APIRouter, HTTPException
from typing import Optional

from services.bioquimica import calcular_proteinas_tf_service
                                

router = APIRouter()

@router.get("/proteinas_tf")
def calcular_proteinas_tf(
    albumina_gdl: Optional[str] = None,
    proteina_gdl: Optional[str] = None,
):

    # Verifica campos vazios
    if not albumina_gdl or not proteina_gdl:

        raise HTTPException(
            status_code=400,
            detail="Preencha albumina e proteína."
        )

    try:

        # Aceita vírgula ou ponto
        albumina = float(albumina_gdl.replace(",", "."))

        proteina = float(proteina_gdl.replace(",", "."))

        # service
        resultado_proteinas_tf = calcular_proteinas_tf_service(
            albumina,
            proteina,
        
        )
        return resultado_proteinas_tf
    
    except ValueError:

        raise HTTPException(
            status_code=400,
            detail="Valor numérico inválido."
        )
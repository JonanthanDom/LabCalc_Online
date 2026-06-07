from fastapi import APIRouter, HTTPException
from typing import Optional
from services.bioquimica import calcular_calcio_ionico_service
                                

router = APIRouter()

@router.get("/calcio_ionico")
def calcular_calcio_ionico(
    calcio_total: Optional[str] = None,     
    calcio_albumina_gdl: Optional[str] = None,
    calcio_proteina_gdl: Optional[str] = None,
):

    # Verifica campos vazios
    if not calcio_albumina_gdl or not calcio_proteina_gdl:

        raise HTTPException(
            status_code=400,
            detail="Preencha todos os campos."
        )

    try:

        # Aceita vírgula ou ponto
        calcio = float(calcio_total.replace(",", "."))

        albumina = float(calcio_albumina_gdl.replace(",", "."))

        proteina = float(calcio_proteina_gdl.replace(",", "."))

        # service
        resultado_calcio_ionico = calcular_calcio_ionico_service(
            calcio_total=calcio,
            calcio_albumina_gdl=albumina,
            calcio_proteina_gdl=proteina
        )
        return resultado_calcio_ionico
    
    except ValueError:

        raise HTTPException(
            status_code=400,
            detail="Valor numérico inválido."
        )
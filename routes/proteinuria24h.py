from typing import Optional

from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/proteinuria24h")
def calcular_proteinuria(
    volume_ml: Optional[str] = None,
    proteina_mgdl: Optional[str] = None,
):

    # Verifica campos vazios
    if volume_ml is None or proteina_mgdl is None:

        raise HTTPException(
            status_code=400,
            detail="Preencha volume e proteína."
        )

    try:

        # Aceita vírgula ou ponto
        volume = float(volume_ml.replace(",", "."))

        proteina = float(proteina_mgdl.replace(",", "."))

        # Cálculo
        resultado = (volume * proteina) / 100

        return {

            "volume_ml_24h": round(volume, 2),

            "proteina_mgdl": round(proteina, 2),

            "proteinuria_24h_mg": round(resultado, 2)
        }

    except ValueError:

        raise HTTPException(
            status_code=400,
            detail="Valor numérico inválido."
        )
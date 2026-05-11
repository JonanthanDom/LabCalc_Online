from typing import Optional

from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/rpc")
def calcular_rpc(
    proteina_mgdl: Optional[str] = None,
    creatinina_mgdl: Optional[str] = None,
):

    # Verifica campos vazios
    if proteina_mgdl is None or creatinina_mgdl is None:

        raise HTTPException(
            status_code=400,
            detail="Preencha proteína e creatinina."
        )

    try:

        # Aceita vírgula ou ponto
        proteina = float(
            proteina_mgdl.replace(",", ".")
        )

        creatinina = float(
            creatinina_mgdl.replace(",", ".")
        )

        # Evita divisão por zero
        if creatinina == 0:

            raise HTTPException(
                status_code=400,
                detail="Creatinina não pode ser zero."
            )

        # Cálculo
        rpc = proteina / creatinina

        return {

            "proteina_mgdl": round(proteina, 2),

            "creatinina_mgdl": round(creatinina, 2),

            "relacao_proteina_creatinina": round(rpc, 2)
        }

    except ValueError:

        raise HTTPException(
            status_code=400,
            detail="Valor numérico inválido."
        )
    
from typing import Optional
from fastapi import APIRouter, HTTPException
from services.bioquimica import calcular_relacao_prot_creatinina_service             

router = APIRouter()


@router.get("/rpc")
def calcular_rpc(
    proteina_mgdl: Optional[str] = None,
    creatinina_mgdl: Optional[str] = None,
):

    # Verifica campos vazios
    if not proteina_mgdl or not creatinina_mgdl:

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

        return calcular_relacao_prot_creatinina_service(proteina, creatinina)

    except ValueError:

        raise HTTPException(
            status_code=400,
            detail="Valor numérico inválido."
        )
    
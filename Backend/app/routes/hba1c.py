from fastapi import APIRouter, HTTPException
from typing import Optional

from Backend.app.services.bioquimica import calcular_hba1c_service

router = APIRouter()


@router.get("/hba1c")
def calcular_hba1c(
    hba1c_percent: Optional[str] = None,
    ifcc_mmol_mol: Optional[str] = None,
):

    # validação: apenas 1 campo
    campos = sum(v is not None for v in [hba1c_percent, ifcc_mmol_mol])

    if campos != 1:

        raise HTTPException(
            status_code=400,
            detail="Preencha apenas um parâmetro."
        )

    try:

        # parsing
        hba1c_float = None
        ifcc_float = None

        if hba1c_percent is not None:

            hba1c_float = float(
                hba1c_percent.replace(",", ".")
            )

        if ifcc_mmol_mol is not None:

            ifcc_float = float(
                ifcc_mmol_mol.replace(",", ".")
            )

        # service
        resultado = calcular_hba1c_service(
            hba1c_float,
            ifcc_float
        )

        return resultado

    except ValueError:

        raise HTTPException(
            status_code=400,
            detail="Valor numérico inválido."
        )
from typing import Optional

from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/hba1c")
def calcular_hba1c(
    hba1c_percent: Optional[str] = None,
    ifcc_mmol_mol: Optional[str] = None,
):

    # Conta quantos campos foram preenchidos
    campos_preenchidos = sum(
        valor is not None
        for valor in [hba1c_percent, ifcc_mmol_mol]
    )

    # Deve preencher apenas UM campo
    if campos_preenchidos != 1:

        raise HTTPException(
            status_code=400,
            detail="Preencha apenas um parâmetro."
        )

    try:

        # -----------------------------------
        # Se preencher HbA1c %
        # -----------------------------------
        if hba1c_percent is not None:

            hba1c = float(
                hba1c_percent.replace(",", ".")
            )

            ifcc = (10.93 * hba1c) - 23.5

        # -----------------------------------
        # Se preencher IFCC mmol/mol
        # -----------------------------------
        elif ifcc_mmol_mol is not None:

            ifcc = float(
                ifcc_mmol_mol.replace(",", ".")
            )

            hba1c = (ifcc + 23.5) / 10.93

        # -----------------------------------
        # Glicemia média estimada
        # -----------------------------------
        eag = (28.7 * hba1c) - 46.7

        return {

            "hba1c_percent": round(hba1c, 2),

            "ifcc_mmol_mol": round(ifcc, 2),

            "glicemia_media_estimada_mgdl": round(eag, 2)
        }

    except ValueError:

        raise HTTPException(
            status_code=400,
            detail="Valor numérico inválido."
        )
    
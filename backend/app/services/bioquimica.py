#--------------------------------
#calculo de hba1c
#--------------------------------
def calcular_hba1c_service(hba1c_percent: float = None, ifcc: float = None):

    # Caso venha HbA1c %
    if hba1c_percent is not None:

        ifcc_result = (10.93 * hba1c_percent) - 23.5
        eag = (28.7 * hba1c_percent) - 46.7

        return {
            "hba1c_percent": round(hba1c_percent, 2),
            "ifcc_mmol_mol": round(ifcc_result, 2),
            "glicemia_media_estimada_mgdl": round(eag, 2)
        }

    # Caso venha IFCC
    if ifcc is not None:

        hba1c_result = (ifcc + 23.5) / 10.93
        eag = (28.7 * hba1c_result) - 46.7

        return {
            "hba1c_percent": round(hba1c_result, 2),
            "ifcc_mmol_mol": round(ifcc, 2),
            "glicemia_media_estimada_mgdl": round(eag, 2)
        }

    return None
#--------------------------------
#calculo de proteinas totais.
#--------------------------------
def calcular_proteinas_tf_service(albumina_gdl: float, proteina_gdl: float):

    globulina = proteina_gdl - albumina_gdl

    return {
        "albumina_gdl": round(albumina_gdl, 2),
        "globulina_gdl": round(globulina, 2),
        "proteina_total_gdl": round(proteina_gdl, 2)
    }
    return None
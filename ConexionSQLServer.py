# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 17:26:46 2024

@author: jcgarciam
"""

import pyodbc
import pandas as pd
import numpy as np
from datetime import datetime
import glob

Tiempo_Total = datetime.now()

path_ent1 = r'\\dc1pvfnas1\Autos\Soat_Y_ARL\Pagos_Arl_Salud\Cierre\Años_anteriores\GM_Activa'
path_ent2 = r'\\DC1PVFNAS1\Autos\BusinessIntelligence\19-Soat-Salud-Arl\4-TRANSVERSAL\SISCO\SISCO\General\Salidas\SALUD\CONSOLIDADO_SISCO'
path_ent3 = r'\\dc1pvfnas1\Autos\Soat_Y_ARL\Pagos_Arl_Salud\Cierre\Años_anteriores\GM_Activa'
path_ent4 = r'D:\DATOS\Users\jcgarciam\OneDrive - AXA Colpatria Seguros\Documentos\Informes\12. Gasto Medico\Entradas\Consolidado'

conn = pyodbc.connect('Driver={SQL Server};'
                   'Server=DC2TVDSIT1,58354;'
                   'Database=SIT_MINERIA;'
                   'Trusted_Connection=yes;')

consulta = "select \
    FOLIO, NRO_CONTRATO, TIPO_IDEN_BENEF, NRO_IDENTIFICACION_BENEF, VALOR_BRUTO_FACTURA, VALOR_VALES, COD_PROCEDIMIENTO, NOMBRE_PROCEDIMIENTO, VALOR_DETALLE, FECHA_SERVICIO, NIT_PRESTADOR, FECHA_RAD_FACT, NUMERO_FACT, NUMERO_AUTORIZACION, FECHA_DETALLE\
    FROM [STAGE].[STG_MN_GENERAL_COMPARATIVO_GASTOMEDICO]\
    WHERE YEAR(FECHA_RAD_FACT) = 2023 AND UNIDAD_NEGOCIO NOT LIKE '%ARL%'"
    
df = pd.read_sql(consulta, conn)
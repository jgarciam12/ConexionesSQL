# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 16:35:55 2023

@author: jcgarciam
"""

import pandas as pd
import numpy as np

from sklearn import datasets
iris = datasets.load_iris()


iris_df = pd.DataFrame(data= np.c_[iris['data'], iris['target']], columns= iris['feature_names'] + ['target'])

iris_grouped_df = iris_df.groupby('target').mean().round(1)

condition_list = [iris_grouped_df.index == 0,iris_grouped_df.index == 1,iris_grouped_df.index == 2]
choice_list = ['setosa', 'versicolor', 'virginica']
iris_grouped_df['target_name'] = np.select(condition_list,choice_list,default='unknown')
iris_grouped_df.columns = ['N° Reclamación','Orden de Pago','Amparo/Cobertura','ID Lesionado','ID Apoderado']

#%%

from fpdf import FPDF

pdf = FPDF(orientation = 'L')
pdf.add_page()
pdf.set_font('arial', 'B', 11)
pdf.cell(60)
pdf.cell(10, 10, 'AXA COLPATRIA SEGUROS SA', 0, 2, 'L')
pdf.cell(10, 10, '860 002 184 - 9', 0, 2, 'L')
pdf.cell(10, 10, 'NOTIFICACIÓN DE PAGOS PERSONA NATURAL', 0, 2, 'L')
pdf.cell(10, 10, 'Soportes de pago por concepto de indemnizaciones correspondientes al día 03 al 06 de Marzo 2023 Ramo SOAT', 0, 2, 'L')


pdf.cell(90, 10, ' ', 0, 2, 'C')
pdf.cell(-55)
columnNameList = list(iris_grouped_df.columns)
for header in columnNameList[:-1]:
  pdf.cell(35, 10, columnNameList[-1], 1, 0, 'C')
pdf.cell(35, 10, columnNameList[-1], 1, 2, 'C')
pdf.cell(-140)
pdf.set_font('arial', '', 11)
for row in range(0, len(iris_grouped_df)):
  for col_num, col_name in enumerate(columnNameList):
    if col_num != len(columnNameList)-1:
      pdf.cell(35,10, str(iris_grouped_df['%s' % (col_name)].iloc[row]), 1, 0, 'C')
    else:
      pdf.cell(35,10, str(iris_grouped_df['%s' % (col_name)].iloc[row]), 1, 2, 'C')  
      pdf.cell(-140)
path = r'D:\DATOS\Users\jcgarciam\OneDrive - AXA Colpatria Seguros\Documentos\Informes'
pdf.output(path + '\iris_grouped_df_0.pdf', 'F')   

#%%

from pandas.plotting import table
import matplotlib.pyplot as plt

ax = plt.subplot(111, frame_on=False)
ax.xaxis.set_visible(0)
ax.yaxis.set_visible(0)
table(ax, iris_grouped_df, loc='upper center')
plt.savefig(path + '\iris_grouped_df_2.pdf')
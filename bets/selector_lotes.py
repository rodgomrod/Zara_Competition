#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 13:11:22 2019

@author: rde
"""

import pandas as pd

ruta = "/home/rde/stuff_workspace/2_Kaggle/Zara_Competition/bets/week2_bets_pw.csv"

df = pd.read_csv(ruta)

envio1 =  [315, 487, 560, 1058, 1121, 1580, 1850]
df.loc[df.block_id.isin(envio1),'n_products'].sum() # 45

df.loc[df.block_id.isin(envio1)]


l1_aux=  [315,       560,               1580,1850]

envio_rodri = [560,1058,1580,315,1850,1036,439,2359,96,2306,1412,2037,2493,1833,2169,1180] #47
df.loc[df.block_id.isin(envio_rodri),'n_products'].sum()

lista_mios_exc = list(set(envio1) - set(envio_rodri))
df.loc[df.block_id.isin(lista_mios_exc),'n_products'].sum()

lista_rodri_nuevos = list(set(envio_rodri) - set(envio1)) # [96, 439, 1036, 1180, 1412, 1833, 2037, 2169, 2306, 2359, 2493]
len(lista_rodri_nuevos) # 11
df.loc[df.block_id.isin(lista_rodri_nuevos),'n_products'].sum() # 20



df['valor_real'] = df.gain_per_block / df.n_products






lista_mios_nuevos = [487, 560, 1580, 1850,96, 439, 1036, 1180, 1412, 1833, 2037, 2169, 2306, 2359, 2493] 
df.loc[df.block_id.isin(lista_mios_nuevos),'n_products'].sum() # 20


df.sort_values('valor_real',ascending=False).loc[(df.n_products == 1) & ~(df.block_id.isin(lista_mios_nuevos))].head(20)
df.sort_values('valor_real',ascending=False).loc[(df.n_products == 1) & ~(df.block_id.isin(lista_mios_nuevos)),'block_id'].to_list()[:8]
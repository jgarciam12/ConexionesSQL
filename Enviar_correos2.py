# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 14:16:54 2023

@author: jcgarciam
"""

email = 'jovana.bautista@axacolpatria.co'

import win32com.client as win32

outlook_app = win32.Dispatch('Outlook.Application')
namespace = outlook_app.GetNamespace('MAPI')

mail_item = outlook_app.CreateItem(0)

mail_item.subject = 'Prueba2'
mail_item.Body = 'Prueba'

mail_item.To = email
#mail_item.SentOnBehalfOfName = 'BusinessIntelligence@seguros.axacolpatria.co' 

mail_item.Send()



# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 09:23:11 2021

@author: Josh
"""

import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'experience':2, 'test_score':9, 'interview_score':6})

print(r.json())
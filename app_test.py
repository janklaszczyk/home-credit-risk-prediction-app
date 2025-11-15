import requests

# Sample application data. Put your data here and check your stroke probability
application = [
    {   "ORGANIZATION_TYPE": "Self-employed",
        "EXT_SOURCE_1": 0.817352, 
        "EXT_SOURCE_2": 0.603948, 
        "EXT_SOURCE_3": 0.609276, 
        "AMT_CREDIT": 536917, 
        "SUM_CNT_PAYMENT_PREV_APP": 12, 
        "DAYS_BIRTH": -19746, 
        "OCCUPATION_TYPE": "None",
        "SUM_DAYS_LAST_DUE_1ST_VERSION_PREV_APP": -15, 
        "AMT_ANNUITY": 19413, 
        "SUM_AMT_DOWN_PAYMENT_PREV_APP": 6322, 
        "DAYS_EMPLOYED": -4093, 
        "SUM_AMT_CREDIT_SUM_DEBT_BUREAU": 0, 
        "AMT_GOODS_PRICE": 463500, 
        "SUM_LAST_AMT_BALANCE_CRED_CARD": 5000, 
        "DAYS_ID_PUBLISH": -3287, 
        "COUNT_LATE_PAYMENT": 0, 
        "OWN_CAR_AGE": 0, 
        "SUM_AMT_ANNUITY_PREV_APP": 6382, 
        "SUM_AMT_CREDIT_MAX_OVERDUE_BUREAU": 0, 
        "SUM_DAYS_FIRST_DRAWING_PREV_APP": 365243,
        "CODE_GENDER": "F",
        "SUM_DAYS_CREDIT_ENDDATE_BUREAU": 29399, 
        "SUM_NAME_CONTRACT_STATUS_Refused_PREV_APP": 0, 
        "SUM_AMT_CREDIT_SUM_BUREAU": 861120, 
        "COUNT_UNSUFFICIENT_PAYMENT": 0, 
    }
]

# Location of my server
# change 0.0.0.0 on your server location
url = "http://192.168.0.17:80/predict"

# Send request
resp = requests.post(url, json=application)

# Print result
print(resp.json())

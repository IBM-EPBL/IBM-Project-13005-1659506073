import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "h1hMyavnHReedEpmIHsp3xAuyEypRp-VnhyOAkHhN_pn"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"fields": [['f0','f1', 'f2', 'f3', 'f4', 'f5', 'f6']], "values": [[0.0, 0.0, 3.4, 3.0, 683.0, 56.0, 5.0]] }]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/31175a54-6ddd-42e7-b1d5-e071f3199d19/predictions?version=2022-11-17', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")

print(response_scoring.json())



pred = response_scoring.json()
output = pred['predictions'][0]['values'][0][0]
print(output)
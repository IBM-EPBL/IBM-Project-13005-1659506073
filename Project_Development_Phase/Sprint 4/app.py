
from flask import Flask, render_template, url_for, redirect,jsonify
from flask import request
import requests
from flask import g

import pickle


try:
    API_KEY = "h1hMyavnHReedEpmIHsp3xAuyEypRp-VnhyOAkHhN_pn"
    token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
    API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
    mltoken = token_response.json()["access_token"]
    
except:
  print("An exception occurred")

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}


model = pickle.load(open(r'demandest.pkl','rb'))

app = Flask(__name__)


@app.route('/', methods = ['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/predict', methods = ['POST', 'GET'])
def predict():
    try:
        homepageFeatured = request.form["homepageFeatured"]
        if(homepageFeatured == "Yes"):
            inp1 = 1
        else:
            inp1 = 0
        emailerForPromation = request.form["emailerForPromation"]
        if(emailerForPromation == "Yes"):
            inp2 = 1
        else:
            inp2 = 0
        op_area = request.form["op_area"]
        cuisine = request.form["cuisine"]
        if(cuisine == "Thai"):
            inp4 = 0
        elif (cuisine == "Indian"):
            inp4 = 1
        elif (cuisine == "Italian"):
            inp4 = 2
        elif (cuisine == "Continental"):
            inp4 = 3
        cityCode = request.form["cityCode"]
        regionCode = request.form["regionCode"]
        category = request.form["category"]
        if(category == "Beverages"):
            inp5 = 0
        elif (category == "Extras"):
            inp5 = 1
        elif (category == "Soup"):
            inp5 = 2
        elif (category == "Salad"):
            inp5 = 3
        elif (category == "Other Snacks"):
            inp5 = 4
        elif (category == "Salad"):
            inp5 = 5
        elif (category == "Rice Bowl"):
            inp5 = 6
        elif (category == "Starters"):
            inp5 = 7
        elif (category == "Sandwich"):
            inp5 = 8
        elif (category == "Pasta"):
            inp5 = 9
        elif (category == "Desert"):
            inp5 = 10
        elif (category == "Biryani"):
            inp5 = 11
        elif (category == "Pizza"):
            inp5 = 12
        elif (category == "Fish"):
            inp5 = 13
        elif (category == "Seafood"):
            inp5 = 14
        
        payload_scoring = {"input_data": [{"fields": [['f0','f1', 'f2', 'f3', 'f4', 'f5', 'f6']], "values": [[int(inp1),int(inp2),float(op_area),int(inp4),int(cityCode), int(regionCode), int(inp5)]] }]}
        
        #predict_input = [[int(inp1),int(inp2),float(op_area),int(inp4),int(cityCode), int(regionCode), int(inp5)]]

        #output = model.predict(predict_input)
        #print(output)
        try:
            response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/31175a54-6ddd-42e7-b1d5-e071f3199d19/predictions?version=2022-11-17', json=payload_scoring,
            headers={'Authorization': 'Bearer ' + mltoken})
            print("Scoring response")
        except:
            print("Exception Could not get the score")
        


        print(response_scoring.json())
        pred = response_scoring.json()
        output = pred['predictions'][0]['values'][0][0]

        print(output)
        
    except:
        print("Error in sumbiting form")

    return render_template('index.html',y = int(output))

if __name__ == "__main__":
    app.run(debug=True)
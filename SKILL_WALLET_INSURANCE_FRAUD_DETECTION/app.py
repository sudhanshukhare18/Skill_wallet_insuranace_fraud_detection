import numpy as np
import pickle
from flask import Flask, request, render_template

app = Flask(__name__)

model = pickle.load(open("fraud_model.pkl","rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():

    months_as_customer = int(request.form['months_as_customer'])
    policy_number = int(request.form['policy_number'])
    policy_bind_year = int(request.form['policy_bind_year'])
    policy_bind_month = int(request.form['policy_bind_month'])
    policy_state = int(request.form['policy_state'])
    policy_deductable = int(request.form['policy_deductable'])
    policy_annual_premium = float(request.form['policy_annual_premium'])
    umbrella_limit = int(request.form['umbrella_limit'])
    insured_sex = int(request.form['insured_sex'])
    insured_zip = int(request.form['insured_zip'])

    insured_education_level = int(request.form['insured_education_level'])
    insured_occupation = int(request.form['insured_occupation'])
    capital_gains = int(request.form['capital_gains'])
    capital_loss = int(request.form['capital_loss'])

    incident_day = int(request.form['incident_day'])
    incident_hour = int(request.form['incident_hour'])
    incident_city = int(request.form['incident_city'])
    incident_location = int(request.form['incident_location'])

    incident_type = int(request.form['incident_type'])
    collision_type = int(request.form['collision_type'])
    incident_severity = int(request.form['incident_severity'])
    authorities_contacted = int(request.form['authorities_contacted'])

    number_of_vehicles_involved = int(request.form['number_of_vehicles_involved'])
    property_damage = int(request.form['property_damage'])
    bodily_injuries = int(request.form['bodily_injuries'])
    witnesses = int(request.form['witnesses'])

    total_claim_amount = int(request.form['total_claim_amount'])
    auto_make = int(request.form['auto_make'])
    auto_model = int(request.form['auto_model'])
    auto_year = int(request.form['auto_year'])

    features = [[
        months_as_customer,policy_number,policy_bind_year,policy_bind_month,
        policy_state,policy_deductable,policy_annual_premium,umbrella_limit,
        insured_sex,insured_zip,insured_education_level,insured_occupation,
        capital_gains,capital_loss,incident_day,incident_hour,incident_city,
        incident_location,incident_type,collision_type,incident_severity,
        authorities_contacted,number_of_vehicles_involved,property_damage,
        bodily_injuries,witnesses,total_claim_amount,auto_make,auto_model,auto_year
    ]]

    prediction = model.predict(features)

    if prediction[0] == 1:
        result = "Fraud Detected"
    else:
        result = "Legitimate Claim"

    return render_template("result.html", prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)
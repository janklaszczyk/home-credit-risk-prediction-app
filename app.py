import streamlit as st
import joblib
import pandas as pd
from constans import org_type_list, occ_type_list

# Title and description
st.title("Home Credit Risk Predictor")
st.markdown(
    """
This application uses a Light Gradient Boosting Machine (LightGBM) model to predict the risk of a client encountering financial difficulties after receiving a home credit.

The model was trained on 307,511 samples, using 23 selected features out of a total of 331 available. These features were carefully chosen to best represent the factors influencing credit risk.

To get a prediction, fill in all required input fields and click the PREDICT button.
The app will inform you whether the application is likely to be approved or rejected, along with the model's confidence level in its prediction.
"""
)


# Load the model (assumes model_file.pkl is in the same directory)
@st.cache_resource
def load_model():
    return joblib.load("model_file.pkl")


model = load_model()


# Define input fields
def get_user_input():
    input_data = {
        "ORGANIZATION_TYPE": st.selectbox("Organization type", org_type_list),
        "EXT_SOURCE_1": st.number_input("External source 1"),
        "EXT_SOURCE_2": st.number_input("External source 2"),
        "EXT_SOURCE_3": st.number_input("External source 3"),
        "AMT_CREDIT": st.number_input("Credit Amount", value=536917),
        "DAYS_BIRTH": st.number_input(
        "Days since birth (negative)",
        help="Negative number of days since birth (eg. if born yesterday? >>> -1)",
        value=-19746,
        ),
        "SUM_DAYS_LAST_DUE_1ST_VERSION_PREV_APP": st.number_input(
            "Sum days last due (prev app)", value=-15
        ),
        "OCCUPATION_TYPE": st.selectbox("Occupation type", occ_type_list),
        "SUM_CNT_PAYMENT_PREV_APP": st.number_input(
            "Sum of payments on previous apps", value=12
        ),
        "AMT_ANNUITY": st.number_input("Annuity Amount", value=19413),
        "AMT_GOODS_PRICE": st.number_input("Goods Price", value=463500),
        "SUM_AMT_CREDIT_SUM_DEBT_BUREAU": st.number_input(
            "Sum credit debt (bureau)", value=0
        ),
        "SUM_LAST_AMT_BALANCE_CRED_CARD": st.number_input(
            "Sum of last balances from all credit cards", value=5000
        ),
        "COUNT_LATE_PAYMENT": st.number_input("Late payments", value=0),
        "SUM_AMT_DOWN_PAYMENT_PREV_APP": st.number_input(
            "Sum down payment (prev app)", value=6322
        ),
        "OWN_CAR_AGE": st.number_input("Own car age (years)", value=0),
        "DAYS_EMPLOYED": st.number_input(
            "Days employed (negative)", value=-4093
        ),
        "SUM_DAYS_CREDIT_ENDDATE_BUREAU": st.number_input(
            "Sum of remaining days at the time of application (bureau)", value=29399
        ),
        "SUM_AMT_CREDIT_MAX_OVERDUE_BUREAU": st.number_input(
            "Max overdue (bureau)", value=0
        ),
        "SUM_AMT_ANNUITY_PREV_APP": st.number_input(
            "Sum annuity (prev app)", value=6382
        ),
        "DAYS_ID_PUBLISH": st.number_input(
            "Days since ID publish (negative)", value=-3287
        ),
        "SUM_DAYS_FIRST_DRAWING_PREV_APP": st.number_input(
            "Days first drawing (prev app)", value=365243
        ),
        "SUM_SK_DPD_DEF_POS_CASH": st.number_input(
            "Sum of days past due in past applications (point of sales)", value=0
        ),
    }
    return input_data


# User input collection
input_features = get_user_input()

# Predict button
if st.button("Predict"):
    try:
        input_df = pd.DataFrame([input_features])
        categorical_cols = [
            "ORGANIZATION_TYPE",
            "OCCUPATION_TYPE",
        ]
        for col in categorical_cols:
            input_df[col] = pd.Categorical(input_df[col])

        proba = model.predict_proba(input_df)[0]
        predicted_class = model.predict(input_df)[0]
        confidence = proba[predicted_class]
        prediction_label = (
            "Approved" if predicted_class == 0 else "Not Approved"
        )

        st.success(f"Prediction: {prediction_label}")
        st.info(f"Confidence: {confidence:.2%}")
    except Exception as e:
        st.error(f"Exception during prediction: {e}")
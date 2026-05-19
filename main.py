import streamlit as st
from prediction_helper import predict

# Must be the first Streamlit command
st.set_page_config(
    page_title="Health Insurance Predictor",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E3A8A;
        font-weight: 700;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #4B5563;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 1.25rem;
        color: #2563EB;
        font-weight: 600;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
        border-bottom: 2px solid #E5E7EB;
        padding-bottom: 0.5rem;
    }
    div.stButton > button:first-child {
        background-color: #2563EB;
        color: white;
        font-size: 1.125rem;
        font-weight: 600;
        padding: 0.75rem 2rem;
        border-radius: 0.5rem;
        border: none;
        width: 100%;
        transition: all 0.3s ease;
    }
    div.stButton > button:first-child:hover {
        background-color: #1D4ED8;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    }
    .result-card {
        background-color: #F0FDF4;
        border-left: 5px solid #22C55E;
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-top: 1.5rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        text-align: center;
    }
    .result-text {
        font-size: 1.1rem;
        color: #166534;
        font-weight: 500;
    }
    .result-value {
        font-size: 2.5rem;
        color: #15803D;
        font-weight: 700;
        margin-top: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🏥 Health Insurance Premium Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Fill in the details below to get an estimated cost for your health insurance premium based on advanced predictive modeling.</div>', unsafe_allow_html=True)

categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer', ''],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
        'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

# --- Form starts ---
with st.container():
    st.markdown('<div class="section-header">👤 Personal Information</div>', unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        age = st.number_input('Age', min_value=18, step=1, max_value=100, help="Age of the primary policyholder")
    with col2:
        gender = st.selectbox('Gender', categorical_options['Gender'])
    with col3:
        marital_status = st.selectbox('Marital Status', categorical_options['Marital Status'])
    with col4:
        number_of_dependants = st.number_input('Dependants', min_value=0, step=1, max_value=20, help="Number of family members covered")

with st.container():
    st.markdown('<div class="section-header">⚕️ Health Profile</div>', unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        bmi_category = st.selectbox('BMI Category', categorical_options['BMI Category'], help="Body Mass Index category")
    with col2:
        smoking_status = st.selectbox('Smoking Status', categorical_options['Smoking Status'])
    with col3:
        medical_history = st.selectbox('Medical History', categorical_options['Medical History'], help="Pre-existing medical conditions")
    with col4:
        genetical_risk = st.number_input('Genetical Risk', step=1, min_value=0, max_value=5, help="Genetical risk score (0-5)")

with st.container():
    st.markdown('<div class="section-header">💼 Socio-Economic Details</div>', unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        income_lakhs = st.number_input('Income (in Lakhs)', step=1, min_value=0, max_value=200, help="Annual income in Lakhs (INR)")
    with col2:
        employment_status = st.selectbox('Employment Status', categorical_options['Employment Status'])
    with col3:
        region = st.selectbox('Region', categorical_options['Region'], help="Geographical region of residence")
    with col4:
        insurance_plan = st.selectbox('Insurance Plan', categorical_options['Insurance Plan'], help="Tier of the insurance plan")

# Create a dictionary for input values
input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

st.markdown("<br>", unsafe_allow_html=True)

# Button to make prediction
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button('Predict Insurance Premium', use_container_width=True):
        with st.spinner("Calculating premium..."):
            try:
                prediction = predict(input_dict)
                st.markdown(f"""
                <div class="result-card">
                    <div class="result-text">Predicted Health Insurance Premium</div>
                    <div class="result-value">₹ {prediction:,}</div>
                </div>
                """, unsafe_allow_html=True)
            except Exception as e:
                st.error(f"An error occurred during prediction: {e}")

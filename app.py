import numpy as np
import pickle
import pandas as pd
import streamlit as st
from PIL import Image
import base64

pickle_in = open("finalized_model.sav", "rb")
regressor = pickle.load(pickle_in)


# @app.route('/')
def welcome():
    return "Welcome All"

# @app.route('/predict',methods=["Get"])
def predict_strength(Cement, Blast_Furnace_Slag, Fly_Ash, Water, Superplasticizer, Coarse_Aggregate, Fine_Aggregate,Age):
    """Let's predict strength of cement.
    This is using docstrings for specifications.
    ---
    parameters:
      - name: Cement
        in: query
        type: number
        required: true
      - name: Blast_Furnance_Slag
        in: query
        type: number
        required: true
        name: Fly_Ash
        in: query
        type: number
        required: true
      - name: Water
        in: query
        type: number
        required: true
      - name: Superplasticizer
        in: query
        type: number
        required: true
        name: Coarse_Aggregate
        in: query
        type: number
        required: true
        name: Fine_Aggregate
        in: query
        type: number
        required: true
        name: Age
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values

    """

    prediction = regressor.predict(np.array([[Cement, Blast_Furnace_Slag, Fly_Ash, Water, Superplasticizer, Coarse_Aggregate, Fine_Aggregate, Age]]))

    return prediction[0]

@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_jpg_as_page_bg(jpg_file):
    bin_str = get_base64_of_bin_file(jpg_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/jpg;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_jpg_as_page_bg('image2.jpg')
def main():
    st.title("Strength Of Cement")
    #st.image("image1.jpg", width=700)
    image=Image.open("image2.jpg")
    st.image(image)
    html_temp = """
    
    <div style="background-image:"image2.jpg">
    <div style="background-color:pink;padding:10px">
    <h2 style="color:black;text-align:center;">Streamlit Cemenet Strength Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    Cement = st.text_input("Cement(In kg in a m^3)")
    Blast_Furnace_Slag = st.text_input("Blast_Furnace_Slag(In kg in a m^3)")
    Fly_Ash = st.text_input("Fly_Ash(In kg in a m^3)")
    Water = st.text_input("Water(In kg in a m^3)")
    Superplasticizer = st.text_input("Superplasticizer(In kg in a m^3)")
    Coarse_Aggregate = st.text_input("Coarse_Aggregate(In kg in a m^3)")
    Fine_Aggregate = st.text_input("Fine_Aggregate(In kg in a m^3)")
    Age = st.text_input("Age(In Day)")

    result = ""
    if st.button("Predict"):
        result = predict_strength(float(Cement), float(Blast_Furnace_Slag), float(Fly_Ash), float(Water),float(Superplasticizer), float(Coarse_Aggregate), float(Fine_Aggregate), float(Age))

    st.success('The output is {}'.format(result))

    if st.button("About ML App"):
        st.text(
            "Regression model to predict the concrete compressive strength based on the different features in the training data")
        st.text("Built with Streamlit")

    if st.button("Input Dictionary"):
        st.text("Cement : Quantity of Cement present in kg in a m3 mixture")
        st.text("Blast_Furnance_Slag :  Quantity of Blast_Furnance_Slag present in kg in a m3 mixture")
        st.text("Fly_Ash :  Quantity of Fly_Ash present in kg in a m3 mixture")
        st.text("Water : Quantity of Fly_Ash present in kg in a m3 mixture")
        st.text("Superplasticizer : Quantity of Superplasticizer in kg in a m3 mixture")
        st.text("Coarse_Aggregate : Quantity of Coarse_Aggregate in kg in a m3 mixture")
        st.text("Fine_Aggregate : Quantity of Fine_Aggregate in kg in a m3 mixture")
        st.text("Age : Age in days")
        st.text("Concrete compressive strength: Output Variable - Concrete compressive strength in (MPa, megapascals)")

    if st.button("About Author"):
        st.text("Name : Rohit Murkute")
        st.text("Name : Yash Bhambere")       
        st.text("Name : Akshay Deshmukh")
        
        st.text("Oragnization : Data Science Student at SPPU")


if __name__ == '__main__':
    main()

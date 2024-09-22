import streamlit as st
import pickle
import numpy as np

# Load the pre-trained model from the pickle file
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Prediction function
def predict_mushroom(cap_shape, bruises, gill_spacing, gill_size, gill_color,
                     stalk_surface_above_ring, stalk_color_above_ring,
                     stalk_color_below_ring, ring_type, spore_print_color, population):
    features = [cap_shape, bruises, gill_spacing, gill_size, gill_color, stalk_surface_above_ring,
                stalk_color_above_ring, stalk_color_below_ring, ring_type, spore_print_color, population]
    data = np.array([features])
    prediction = model.predict(data)[0]
    if prediction == 0:
        return "<div class='prediction success'>Enjoy Eating! This mushroom is edible.</div>"
    else:
        return "<div class='prediction danger'>Warning! This mushroom is poisonous.</div>"

# Add custom CSS for light and dark modes
st.markdown("""
<style>
    :root {
        --primary-text-color-light: black;
        --primary-text-color-dark: white;
        --success-color: green;
        --danger-color: red;
    }
    /* Adapt to light or dark mode */
    @media (prefers-color-scheme: light) {
        .prediction {
            text-align: center;
            font-size: 30px;
            font-weight: bold;
            color: var(--primary-text-color-light);
        }
        .success {
            color: var(--success-color);
        }
        .danger {
            color: var(--danger-color);
        }
    }
    @media (prefers-color-scheme: dark) {
        .prediction {
            text-align: center;
            font-size: 30px;
            font-weight: bold;
            color: var(--primary-text-color-dark);
        }
        .success {
            color: var(--success-color);
        }
        .danger {
            color: var(--danger-color);
        }
    }
    .reportview-container .main .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-right: 2rem;
        padding-left: 2rem;
        padding-bottom: 2rem;
    }
    h1 {
        text-align: center;
    }
    .stRadio > div {
        background-color: #f0f2f6;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    .stRadio > div > label {
        display: flex;
        align-items: center;
        cursor: pointer;
        margin: 0;
        padding: 5px;
        border-radius: 4px;
        transition: background-color 0.3s;
    }
    .stRadio > div > label:hover {
        background-color: #e0e2e6;
    }
    .stRadio > div > label > div:first-child {
        margin-right: 10px;
    }
    .row-widget.stRadio {
        padding: 10px;
    }
    .st-columns {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
    }
    .st-columns > div {
        flex: 1;
        padding: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.title("🍄 Mushroom Classification Project")
page = st.sidebar.radio("Go to Pages", ["Mushroom Edibility Prediction", "About Us"])

if page == "Mushroom Edibility Prediction":
    st.title("Mushroom Edibility Prediction")

    # Define the options for the inputs
    options = {
        "Cap Shape": {"Convex": 2, "Bell-shaped": 0, "Conical": 1, "Knobbed": 4, "Flat": 3, "Sunken": 5},
        "Gill Color": {"Black": 0, "Brown": 1, "Buff": 2, "Chocolate": 3, "Gray": 4, "Green": 5, "Orange": 6, "Pink": 7, "Purple": 8, "Red": 9, "White": 10, "Yellow": 11},
        "Gill Size": {"Broad": 0, "Narrow": 1},
        "Gill Spacing": {"Close": 0, "Crowded": 1},
        "Bruises": {"Bruises": 0, "No": 1},
        "Stalk Surface Above Ring": {"Fibrous": 0, "Scaly": 1, "Silky": 2, "Smooth": 3},
        "Stalk Color Above Ring": {"Brown": 0, "Buff": 1, "Cinnamon": 2, "Gray": 3, "Orange": 4, "Pink": 5, "Red": 6, "White": 7, "Yellow": 8},
        "Stalk Color Below Ring": {"Brown": 0, "Buff": 1, "Cinnamon": 2, "Gray": 3, "Orange": 4, "Pink": 5, "Red": 6, "White": 7, "Yellow": 8},
        "Ring Type": {"Evanescent": 0, "Flaring": 1, "Large": 2, "None": 3, "Pendant": 4},
        "Spore Print Color": {"Black": 0, "Brown": 1, "Buff": 2, "Chocolate": 3, "Green": 4, "Orange": 5, "Purple": 6, "White": 7, "Yellow": 8},
        "Population": {"Abundant": 0, "Clustered": 1, "Numerous": 2, "Scattered": 3, "Several": 4, "Solitary": 5}
    }

    # Organize the inputs in three columns
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Cap Shape")
        cap_shape = st.radio("", list(options["Cap Shape"].keys()), key="Cap Shape", label_visibility="collapsed")

        st.subheader("Gill Color")
        gill_color = st.radio("", list(options["Gill Color"].keys()), key="Gill Color", label_visibility="collapsed")

        st.subheader("Gill Size")
        gill_size = st.radio("", list(options["Gill Size"].keys()), key="Gill Size", label_visibility="collapsed")

        st.subheader("Gill Spacing")
        gill_spacing = st.radio("", list(options["Gill Spacing"].keys()), key="Gill Spacing", label_visibility="collapsed")

    with col2:
        st.subheader("Stalk Surface Above Ring")
        stalk_surface_above_ring = st.radio("", list(options["Stalk Surface Above Ring"].keys()), key="Stalk Surface Above Ring", label_visibility="collapsed")

        st.subheader("Stalk Color Above Ring")
        stalk_color_above_ring = st.radio("", list(options["Stalk Color Above Ring"].keys()), key="Stalk Color Above Ring", label_visibility="collapsed")

        st.subheader("Stalk Color Below Ring")
        stalk_color_below_ring = st.radio("", list(options["Stalk Color Below Ring"].keys()), key="Stalk Color Below Ring", label_visibility="collapsed")

    with col3:
        st.subheader("Bruises")
        bruises = st.radio("", list(options["Bruises"].keys()), key="Bruises", label_visibility="collapsed")

        st.subheader("Ring Type")
        ring_type = st.radio("", list(options["Ring Type"].keys()), key="Ring Type", label_visibility="collapsed")

        st.subheader("Spore Print Color")
        spore_print_color = st.radio("", list(options["Spore Print Color"].keys()), key="Spore Print Color", label_visibility="collapsed")

        st.subheader("Population")
        population = st.radio("", list(options["Population"].keys()), key="Population", label_visibility="collapsed")

    # Capture input values before prediction
    cap_shape_value = options["Cap Shape"][cap_shape]
    gill_color_value = options["Gill Color"][gill_color]
    gill_size_value = options["Gill Size"][gill_size]
    gill_spacing_value = options["Gill Spacing"][gill_spacing]
    bruises_value = options["Bruises"][bruises]
    stalk_surface_above_ring_value = options["Stalk Surface Above Ring"][stalk_surface_above_ring]
    stalk_color_above_ring_value = options["Stalk Color Above Ring"][stalk_color_above_ring]
    stalk_color_below_ring_value = options["Stalk Color Below Ring"][stalk_color_below_ring]
    ring_type_value = options["Ring Type"][ring_type]
    spore_print_color_value = options["Spore Print Color"][spore_print_color]
    population_value = options["Population"][population]

    # Display result above the button and gray line
    result = ""
    if st.button("Predict", use_container_width=True):
        result = predict_mushroom(cap_shape_value, bruises_value, gill_spacing_value, gill_size_value,
                                  gill_color_value, stalk_surface_above_ring_value, stalk_color_above_ring_value,
                                  stalk_color_below_ring_value, ring_type_value, spore_print_color_value, population_value)

    if result:
        st.markdown(result, unsafe_allow_html=True)

    # Add gray line after the output and before the button
    st.markdown("<hr>", unsafe_allow_html=True)


elif page == "About Us":
    st.title("🍄 Mushroom Classification Project")

    st.markdown("""
    ## 🎯 Project Overview
    Welcome to our Data Science mini-project focused on mushroom classification! This repository contains our work on developing a model to distinguish between edible and poisonous mushrooms.

    ## 🧠 Project Topic: Mushroom Classification
    Our goal is to create a reliable classification system for mushrooms using machine learning techniques. This project could have real-world applications in:

    - Foraging safety
    - Ecological research
    - Automated mushroom identification systems

    ## 📊 Data Source
    We're using the Mushroom Classification dataset from the UCI Machine Learning Repository, available on Kaggle:

    [Mushroom Classification Dataset](https://www.kaggle.com/datasets/uciml/mushroom-classification)

    ### Dataset Details:
    - This dataset includes descriptions of hypothetical samples corresponding to 23 species of gilled mushrooms in the Agaricus and Lepiota Family.
    - Each species is identified as definitely edible, definitely poisonous, or of unknown edibility and not recommended.
    - The dataset contains 8124 instances with 22 attributes (excluding the class attribute).

    ### Key Attributes(in source):
    1. Cap shape
    2. Cap surface
    3. Cap color
    4. Bruises
    5. Odor
    6. Gill attachment
    7. Gill spacing
    8. Gill size
    9. Gill color
    10. Stalk shape
    11. Stalk root
    12. Stalk surface above ring
    13. Stalk surface below ring
    14. Stalk color above ring
    15. Stalk color below ring
    16. Veil type
    17. Veil color
    18. Ring number
    19. Ring type
    20. Spore print color
    21. Population
    22. Habitat

    ## 🚀 Project Goals
    1. Explore and analyze the mushroom dataset to identify key features for classification.
    2. Develop and compare multiple machine learning models for mushroom classification.
    3. Evaluate model performance and select the best-performing model.
    4. Create visualizations to better understand the data and model results.

    ## 🤝 Contributing
    We welcome contributions and ideas! Feel free to fork this repository and submit pull requests with improvements or additional analyses.

    Happy Mushroom Classification! 🍄🔍
                
    [Github](https://github.com/SiriwatHuntra/MiniProjectDataSci)
    """)

import streamlit as st
import pickle
import numpy as np

# Load the pre-trained model from the pickle file
with open('model_LR.pkl', 'rb') as file:
    model = pickle.load(file)

# Prediction function
def predict_mushroom(cap_shape, cap_surface, cap_color, bruises, odor, gill_spacing,
                     gill_size, gill_color, stalk_shape, stalk_root, stalk_surface_above_ring, stalk_surface_below_ring,
                     stalk_color_above_ring, stalk_color_below_ring, veil_type, veil_color, ring_number, ring_type,
                     spore_print_color, population, habitat):
    # Use the selected numerical values directly
    features = [
        cap_shape, cap_surface, cap_color, bruises, odor,
        gill_spacing, gill_size, gill_color, stalk_shape, stalk_root,
        stalk_surface_above_ring, stalk_surface_below_ring, stalk_color_above_ring,
        stalk_color_below_ring, ring_type, spore_print_color, population, habitat
    ]
    
    # Reshape the data to match the model input
    data = np.array([features])
    
    # Predict using the model
    prediction = model.predict(data)[0]
    
    # Return the result based on prediction (0 for edible, 1 for poisonous)
    if prediction == 0:
        return ("Enjoy Eating! This mushroom is edible.", "green")
    else:
        return ("Warning! This mushroom is poisonous.", "red")

# Streamlit UI

st.title("Mushroom Classification")

# Input form
with st.form("mushroom_form"):
    st.write("### Cap Attributes")
    
    cap_shape = st.radio("Cap Shape", [2, 0, 1, 4, 3, 5], format_func=lambda x: ["convex", "bell-shaped", "conical", "knobbed", "flat", "sunken"][x])
    cap_surface = st.radio("Cap Surface", [0, 1, 2, 3], format_func=lambda x: ["fibrous", "grooves", "scaly", "smooth"][x])
    cap_color = st.radio("Cap Color", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], format_func=lambda x: ["brown", "buff", "cinnamon", "gray", "green", "pink", "purple", "red", "white", "yellow"][x])
    bruises = st.radio("Bruises", [0, 1], format_func=lambda x: ["bruises", "no"][x])
    odor = st.radio("Odor", [0, 1, 2, 3, 4, 5, 6, 7, 8], format_func=lambda x: ["almond", "anise", "creosote", "fishy", "foul", "musty", "none", "pungent", "spicy"][x])
    gill_spacing = st.radio("Gill Spacing", [0, 1], format_func=lambda x: ["close", "crowded"][x])
    gill_size = st.radio("Gill Size", [0, 1], format_func=lambda x: ["broad", "narrow"][x])
    gill_color = st.radio("Gill Color", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], format_func=lambda x: ["black", "brown", "buff", "chocolate", "gray", "green", "orange", "pink", "purple", "red", "white", "yellow"][x])

    st.write("### Stalk and Ring Attributes")
    stalk_shape = st.radio("Stalk Shape", [0, 1], format_func=lambda x: ["enlarging", "tapering"][x])
    stalk_root = st.radio("Stalk Root", [0, 1, 2, 3, 4], format_func=lambda x: ["bulbous", "club", "equal", "missing", "rooted"][x])
    stalk_surface_above_ring = st.radio("Stalk Surface Above Ring", [0, 1, 2, 3], format_func=lambda x: ["fibrous", "scaly", "silky", "smooth"][x])
    stalk_surface_below_ring = st.radio("Stalk Surface Below Ring", [0, 1, 2, 3], format_func=lambda x: ["fibrous", "scaly", "silky", "smooth"][x])
    stalk_color_above_ring = st.radio("Stalk Color Above Ring", [0, 1, 2, 3, 4, 5, 6, 7, 8], format_func=lambda x: ["brown", "buff", "cinnamon", "gray", "orange", "pink", "red", "white", "yellow"][x])
    stalk_color_below_ring = st.radio("Stalk Color Below Ring", [0, 1, 2, 3, 4, 5, 6, 7, 8], format_func=lambda x: ["brown", "buff", "cinnamon", "gray", "orange", "pink", "red", "white", "yellow"][x])
    
    st.write("### Additional Attributes")
    ring_number = st.radio("Ring Number", ['none', 'one', 'two'])
    ring_type = st.radio("Ring Type", [0, 1, 2, 3, 4], format_func=lambda x: ["evanescent", "flaring", "large", "none", "pendant"][x])
    spore_print_color = st.radio("Spore Print Color", [0, 1, 2, 3, 4, 5, 6, 7, 8], format_func=lambda x: ["black", "brown", "buff", "chocolate", "green", "orange", "purple", "white", "yellow"][x])
    population = st.radio("Population", [0, 1, 2, 3, 4, 5], format_func=lambda x: ["abundant", "clustered", "numerous", "scattered", "several", "solitary"][x])
    habitat = st.radio("Habitat", [0, 1, 2, 3, 4, 5, 6], format_func=lambda x: ["grasses", "leaves", "meadows", "paths", "urban", "waste", "woods"][x])

    # Submit button
    submitted = st.form_submit_button("Predict")

# Predict and display the result
if submitted:
    result, color = predict_mushroom(
        cap_shape, cap_surface, cap_color, bruises, odor, gill_spacing, gill_size, gill_color,
        stalk_shape, stalk_root, stalk_surface_above_ring, stalk_surface_below_ring,
        stalk_color_above_ring, stalk_color_below_ring, 'partial', 'white', ring_number,
        ring_type, spore_print_color, population, habitat
    )
    
    st.markdown(f"<div style='text-align: center; font-size: 30px; color: {color}; font-weight: bold;'>{result}</div>", unsafe_allow_html=True)

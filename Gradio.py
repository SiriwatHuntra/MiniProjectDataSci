import gradio as gr
import pickle
import numpy as np

# Load the pre-trained model from the pickle file
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Prediction function
def predict_mushroom(cap_shape, bruises, gill_spacing,
                     gill_size, gill_color, stalk_surface_above_ring,
                     stalk_color_above_ring, stalk_color_below_ring, ring_type,
                     spore_print_color, population):
    features = [
        cap_shape, bruises, gill_spacing,
        gill_size, gill_color, stalk_surface_above_ring,
        stalk_color_above_ring, stalk_color_below_ring, ring_type,
        spore_print_color, population
    ]
    data = np.array([features])
    prediction = model.predict(data)[0]
    
    if prediction == 0:
        return "<div style='text-align: center; font-size: 50px; color: green; font-weight: bold;'>Enjoy Eating! This mushroom is edible.</div>"
    else:
        return "<div style='text-align: center; font-size: 50px; color: red; font-weight: bold;'>Warning! This mushroom is poisonous.</div>"

# Custom CSS for selected radio button (orange background)
custom_css = """
    input[type="radio"]:checked + label {
        background-color: orange;
        color: white;
        border-radius: 8px;
        padding: 10px;
    }

    input[type="radio"] + label:hover {
        background-color: #ffd580; /* Lighter orange on hover */
    }

    .title {
    font-size: 4rem;
    color: #000000;
    text-align: center;
    margin-bottom: 1rem;
    font-weight: bold; 
    }

"""

# Create Gradio Interface with custom CSS for radio button styling
with gr.Blocks(css=custom_css) as demo:
    gr.Markdown("<div class='title'>Mushroom Edibility Prediction</div>", elem_classes="title")
    # Output section at the top using Markdown
    output = gr.Markdown(value="", elem_id="output_markdown", elem_classes="centered-output")

    # Input section in two columns
    with gr.Row(equal_height=True):
        with gr.Column():
            cap_shape = gr.Radio(choices=[('Convex', 2), ('Bell-shaped', 0), ('Conical', 1), ('Knobbed', 4), ('Flat', 3), ('Sunken', 5)], label="Cap Shape")
            bruises = gr.Radio(choices=[('Bruises', 0), ('No', 1)], label="Bruises")
            gill_spacing = gr.Radio(choices=[('Close', 0), ('Crowded', 1)], label="Gill Spacing")
            gill_size = gr.Radio(choices=[('Broad', 0), ('Narrow', 1)], label="Gill Size")
            gill_color = gr.Radio(choices=[('Black', 0), ('Brown', 1), ('Buff', 2), ('Chocolate', 3), ('Gray', 4), ('Green', 5), ('Orange', 6), ('Pink', 7), ('Purple', 8), ('Red', 9), ('White', 10), ('Yellow', 11)], label="Gill Color")
            spore_print_color = gr.Radio(choices=[('Black', 0), ('Brown', 1), ('Buff', 2), ('Chocolate', 3), ('Green', 4), ('Orange', 5), ('Purple', 6), ('White', 7), ('Yellow', 8)], label="Spore Print Color")
        with gr.Column():
            stalk_surface_above_ring = gr.Radio(choices=[('Fibrous', 0), ('Scaly', 1), ('Silky', 2), ('Smooth', 3)], label="Stalk Surface Above Ring")
            stalk_color_above_ring = gr.Radio(choices=[('Brown', 0), ('Buff', 1), ('Cinnamon', 2), ('Gray', 3), ('Orange', 4), ('Pink', 5), ('Red', 6), ('White', 7), ('Yellow', 8)], label="Stalk Color Above Ring")
            stalk_color_below_ring = gr.Radio(choices=[('Brown', 0), ('Buff', 1), ('Cinnamon', 2), ('Gray', 3), ('Orange', 4), ('Pink', 5), ('Red', 6), ('White', 7), ('Yellow', 8)], label="Stalk Color Below Ring")
            ring_type = gr.Radio(choices=[('Evanescent', 0), ('Flaring', 1), ('Large', 2), ('None', 3), ('Pendant', 4)], label="Ring Type")
            population = gr.Radio(choices=[('Abundant', 0), ('Clustered', 1), ('Numerous', 2), ('Scattered', 3), ('Several', 4), ('Solitary', 5)], label="Population")


    # Predict button
    predict_button = gr.Button("Predict")

    # Set the prediction function
    predict_button.click(fn=predict_mushroom, inputs=[
        cap_shape, bruises, gill_spacing, gill_size, gill_color,
        stalk_surface_above_ring, stalk_color_above_ring, stalk_color_below_ring,
        ring_type, spore_print_color, population
    ], outputs=output)

demo.launch(server_name="0.0.0.0", server_port=7860)

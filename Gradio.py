import gradio as gr
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
    # Use the selected numerical values directly, since they correspond to the mapping
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
        return "<div style='text-align: center; font-size: 50px; color: green; font-weight: bold;'>Enjoy Eating! This mushroom is edible.</div>"
    else:
        return "<div style='text-align: center; font-size: 50px; color: red; font-weight: bold;'>Warning! This mushroom is poisonous.</div>"


# Create Gradio Interface with custom Markdown for large bold output
with gr.Blocks(css=".centered-output {text-align: center;}") as demo:
    # Output section at the top using Markdown
    output = gr.Markdown(value="", elem_id="output_markdown", elem_classes="centered-output")
    

    # Input section in two columns
    with gr.Row():
        with gr.Column():
            cap_shape = gr.Radio(choices=[('convex', 2), ('bell-shaped', 0), ('conical', 1), ('knobbed', 4), ('flat', 3),  ('sunken', 5)], label="Cap Shape")
            # cap_shape = gr.Radio(choices=[('bell', 0), ('conical', 1), ('convex', 2), ('flat', 3), ('knobbed', 4), ('sunken', 5)], label="Cap Shape")
            image = gr.Image(value="mushroom-cap-shapes.png", label="cap shapes")
            cap_surface = gr.Radio(choices=[('fibrous', 0), ('grooves', 1), ('scaly', 2), ('smooth', 3)], label="Cap Surface")
            cap_color = gr.Radio(choices=[('brown', 0), ('buff', 1), ('cinnamon', 2), ('gray', 3), ('green', 4), ('pink', 5), ('purple', 6), ('red', 7), ('white', 8), ('yellow', 9)], label="Cap Color")
            bruises = gr.Radio(choices=[('bruises', 0), ('no', 1)], label="Bruises")
            odor = gr.Radio(choices=[('almond', 0), ('anise', 1), ('creosote', 2), ('fishy', 3), ('foul', 4), ('musty', 5), ('none', 6), ('pungent', 7), ('spicy', 8)], label="Odor")
            gill_spacing = gr.Radio(choices=[('close', 0), ('crowded', 1)], label="Gill Spacing")
            gill_size = gr.Radio(choices=[('broad', 0), ('narrow', 1)], label="Gill Size")
            gill_color = gr.Radio(choices=[('black', 0), ('brown', 1), ('buff', 2), ('chocolate', 3), ('gray', 4), ('green', 5), ('orange', 6), ('pink', 7), ('purple', 8), ('red', 9), ('white', 10), ('yellow', 11)], label="Gill Color")
            veil_type = gr.Radio(choices=['partial', 'universal'], label="Veil Type")
            veil_color = gr.Radio(choices=[('brown', 1), ('orange', 5), ('white', 7), ('yellow', 8)], label="Veil Color")
            spore_print_color = gr.Radio(choices=[('black', 0), ('brown', 1), ('buff', 2), ('chocolate', 3), ('green', 4), ('orange', 5), ('purple', 6), ('white', 7), ('yellow', 8)], label="Spore Print Color")
        with gr.Column():
            ring_number = gr.Radio(choices=['none', 'one', 'two'], label="Ring Number")
            ring_type = gr.Radio(choices=[('evanescent', 0), ('flaring', 1), ('large', 2), ('none', 3), ('pendant', 4)], label="Ring Type")
            stalk_shape = gr.Radio(choices=[('enlarging', 0), ('tapering', 1)], label="Stalk Shape")
            stalk_root = gr.Radio(choices=[('bulbous', 0), ('club', 1), ('equal', 2), ('missing', 3), ('rooted', 4)], label="Stalk Root")
            stalk_surface_above_ring = gr.Radio(choices=[('fibrous', 0), ('scaly', 1), ('silky', 2), ('smooth', 3)], label="Stalk Surface Above Ring")
            stalk_surface_below_ring = gr.Radio(choices=[('fibrous', 0), ('scaly', 1), ('silky', 2), ('smooth', 3)], label="Stalk Surface Below Ring")
            stalk_color_above_ring = gr.Radio(choices=[('brown', 0), ('buff', 1), ('cinnamon', 2), ('gray', 3), ('orange', 4), ('pink', 5), ('red', 6), ('white', 7), ('yellow', 8)], label="Stalk Color Above Ring")
            stalk_color_below_ring = gr.Radio(choices=[('brown', 0), ('buff', 1), ('cinnamon', 2), ('gray', 3), ('orange', 4), ('pink', 5), ('red', 6), ('white', 7), ('yellow', 8)], label="Stalk Color Below Ring")
            population = gr.Radio(choices=[('abundant', 0), ('clustered', 1), ('numerous', 2), ('scattered', 3), ('several', 4), ('solitary', 5)], label="Population")
            habitat = gr.Radio(choices=[('grasses', 0), ('leaves', 1), ('meadows', 2), ('paths', 3), ('urban', 4), ('waste', 5), ('woods', 6)], label="Habitat")

    # Predict button
    predict_button = gr.Button("Predict")

    # Set the prediction function
    predict_button.click(fn=predict_mushroom, inputs=[
        cap_shape, cap_surface, cap_color, bruises, odor, gill_spacing, gill_size, gill_color,
        stalk_shape, stalk_root, stalk_surface_above_ring, stalk_surface_below_ring,
        stalk_color_above_ring, stalk_color_below_ring, veil_type, veil_color, ring_number,
        ring_type, spore_print_color, population, habitat
    ], outputs=output)

demo.launch(server_name="0.0.0.0", server_port=7860)

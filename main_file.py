## Farmaan
import os
import streamlit as st
import pandas as pd
import constants as const
import body_mass as bm
import Position_Velocity_Acceleration as pva
import Video as v
import energy_conservation as ec

# Script folder
script_dir = os.path.dirname(os.path.abspath(__file__))
position_csv_path = os.path.join(script_dir, "binary_star.csv")
Video_path = os.path.join(script_dir, "twobody.mp4")
energy_csv_path = os.path.join(script_dir, "Energy_values.csv")

#Generate simulation only once
if "simulation_done" not in st.session_state:
    pva.delete_csv()
    pva.Create_csv()
    v.video(position_csv_path)
    ec.energy()
    st.session_state.simulation_done = True 

st.title("Two Body Simulation")

# Checkboxes for multiselect
show_position_csv = st.checkbox("Show Position CSV Data")
show_energy_csv = st.checkbox("Show Energy CSV Data")
show_video = st.checkbox("Show Video")

# Only try to read the CSV if it exists
if show_position_csv:
    if os.path.exists(position_csv_path):
        df = pd.read_csv(position_csv_path)
        st.dataframe(df)
    else:
        st.error("CSV file not found! Make sure binary_stars.csv is in the same folder as this script.")

if show_energy_csv:
    if os.path.exists(energy_csv_path):
        df = pd.read_csv(energy_csv_path)
        st.dataframe(df)
    else:
        st.error("CSV file not found! Make sure Energy_values.csv is in the same folder as this script.")

if show_video:
    if os.path.exists(Video_path):
        st.video(Video_path)
    else:
        st.error("Video not found! Make sure twobody.mp4 is in the same folder as this script.")
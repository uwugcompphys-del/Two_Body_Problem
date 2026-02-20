## Farmaan
import os
import streamlit as st
import pandas as pd
import constants as const
import body_mass as bm
import Position_Velocity_Acceleration as pva
import Video as v

# Script folder
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "binary_star.csv")
Video_path = os.path.join(script_dir, "twobody.mp4")

#Generate simulation only once
if "simulation_done" not in st.session_state:
    pva.delete_csv()
    pva.Rk4_method(
        pva.setup_initial_conditions(const.rf_1, const.rf_2,
            bm.body_mass(const.h, const.rf_1, const.p0_1)[1],
            bm.body_mass(const.h, const.rf_2, const.p0_2)[1],
            const.G), 1000/60)
    pva.Create_csv()
    v.video(csv_path)
    st.session_state.simulation_done = True 

st.title("Two Body Simulation")

# Checkboxes for multiselect
show_csv = st.checkbox("Show Raw CSV Data")
show_video = st.checkbox("Show Video")

# Only try to read the CSV if it exists
if show_csv:
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        st.dataframe(df)
    else:
        st.error("CSV file not found! Make sure binary_stars.csv is in the same folder as this script.")

if show_video:
    if os.path.exists(Video_path):
        st.video(Video_path)
    else:
        st.error("Video not found! Make sure twobody.mp4 is in the same folder as this script.")
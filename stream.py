import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
import os

# Set the Streamlit app configuration
st.set_page_config(page_title="CSV Plotter App", page_icon=":rocket:", layout="wide", initial_sidebar_state="expanded")

# Hide the GitHub icon and footer
hide_github_icon = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .css-1v0mbdj.etr89bj0 {
        display: none;
    }
    </style>
"""
st.markdown(hide_github_icon, unsafe_allow_html=True)

# Streamlit app layout
st.title("CSV Plotter App")
st.write("Please enter the path to the folder containing the CSV files.")

# Taking folder path input from the user
folder_path = st.text_input("Folder Path")

# Plotting the graphs when "Go" button is pressed
if st.button("Go"):
    if os.path.isdir(folder_path):
        fig, ax1 = plt.subplots(figsize=(12, 6))
        ax2 = ax1.twinx()

        for filename in os.listdir(folder_path):
            if filename.endswith('.csv'):
                file_path = os.path.join(folder_path, filename)
                df = pd.read_csv(file_path, skiprows=23)

                x = df.iloc[0:9000, 0]  # Column B (Zeit)
                y1 = df.iloc[0:9000, 7]  # Column H (Bruecke_1_filtered)
                y2 = df.iloc[0:9000, 8]  # Column I (Bruecke_4_filtered)

                ax1.plot(x, y1, color='blue')
                ax2.plot(x, y2, color='red', linestyle='--')

        ax1.set_xlabel('Zeit')
        ax1.set_ylabel('Bruecke_1_filtered')
        ax2.set_ylabel('Bruecke_4_filtered')

        plt.title('Plot of 2 Combined')

        # Display the plot in the Streamlit app
        st.pyplot(fig)
    else:
        st.error("The folder path does not exist. Please enter a valid path.")


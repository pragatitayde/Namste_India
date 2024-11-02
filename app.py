import streamlit as st
# from home_page import home_page
# from page_1 import page_1
# from page_2 import page_2
from Profile_page import Profiel
from streamlit_navigation_bar import st_navbar
st.set_page_config(layout="wide")

options = st_navbar(["Home", "Documentation", "Examples", "Community", "About"])
st.write(options)
# Set up page navigation

st.markdown(
    """
    <style>
    body {
        background-color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# options = st_navbar(["Home","Profile", "Member", "Nepal", "UAE", "Event"])
    # st.write(page)

# st.title("Multipage Streamlit App Without Sidebar")

# Navigation buttons at the top
pages = {
   
    "Profile": Profiel
   
}



# Display different pages based on the selection
if options == "Profile":
    pages[options]()
   

# Other content can go here
# st.write("Enjoy navigating through the app!")

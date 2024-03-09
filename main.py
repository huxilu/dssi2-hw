import streamlit as st
from inference import get_prediction

#Initialise session state variable
if 'input_features' not in st.session_state:
    st.session_state['input_features'] = {}

def app_sidebar():
    st.sidebar.header('Car Details')
    Age = st.sidebar.text_input('Age')
    KM = st.sidebar.text_input('KM')
    HP = st.sidebar.text_input('HP')
    MetColor = st.sidebar.text_input('Metcolor, 0/1')
    Automatic = st.sidebar.text_input('Automatic, 0/1')
    CC = st.sidebar.text_input('CC')
    Doors = st.sidebar.text_input('Doors, 2-5')
    Weight = st.sidebar.text_input('Weight, 1000-1700')

    def get_input_features():
        input_features = {'Age': Age,
                          'KM': KM,
                          'HP': HP,
                          'MetcColor': MetColor,
                          'Automatic': Automatic,
                          'CC': CC,
                          'Doors': Doors,
                          'Weight': Weight,
                         }
        return input_features
    sdb_col1, sdb_col2 = st.sidebar.columns(2)
    with sdb_col1:
        predict_button = st.sidebar.button("Assess", key="predict")
    with sdb_col2:
        reset_button = st.sidebar.button("Reset", key="clear")
    if predict_button:
        st.session_state['input_features'] = get_input_features()
    if reset_button:
        st.session_state['input_features'] = {}
    return None

def app_body():
    title = '<p style="font-family:arial, sans-serif; color:Black; font-size: 40px;"><b> Welcome to DSSI Loan Assessment</b></p>'
    st.markdown(title, unsafe_allow_html=True)
    default_msg = '**System assessment says:** {}'
    if st.session_state['input_features']:
        assessment = get_prediction(st.session_state['input_features'])
        st.success(default_msg.format(f'{assessment}'))
    return None

def main():
    app_sidebar()
    app_body()
    return None

if __name__ == "__main__":
    main()
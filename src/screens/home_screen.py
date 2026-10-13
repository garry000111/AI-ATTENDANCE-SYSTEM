import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home

def custom_heading(text):
    st.markdown(
        f"""
        <h2 style="
            color: #1E293B;
            font-family: 'Climate Crisis', sans-serif;
            text-align: center;
        ">
            {text}
        </h2>
        """,
        unsafe_allow_html=True,
    )

def home_screen():


    header_home()
    style_background_home()
    style_base_layout()


     
    col1, col2 = st.columns(2, gap="large")

    with col1:
        custom_heading("I'm Student")
        st.image("https://i.ibb.co/844D9Lrt/mascot-student.png", width=120)
        if st.button('Student Portal', type='primary', icon=':material/arrow_outward:', icon_position='right'):
            st.session_state['login_type']='student'
            st.rerun()

    with col2:
        custom_heading("I'm Teacher")
        st.image("https://i.ibb.co/CsmQQV6X/mascot-prof.png", width=145)
        if st.button('Teacher Portal', type='primary', icon=':material/arrow_outward:', icon_position='right'):
            st.session_state['login_type']='teacher'
            st.rerun()

    footer_home()
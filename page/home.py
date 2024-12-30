import streamlit as st
import os
import pandas as pd
from PIL import Image

st.markdown('### CRECI 0010-F')

box = st.container(border=True, height=100, key=1)
with box:
    col1, col2, col3 = st.columns(3, gap='large', vertical_alignment='center')
    with col1:
        st.text("Seja bem vindo!!!")
        st.markdown("**Corretor Felipe Carlos**", unsafe_allow_html=True)

    with col3:
        st.link_button(label='Contato',
                       url='https://www.karinagaldinoimoveis.com.br/imovel/apartamento-com-3-quartos-a-venda-e-2-vagas-bairro-canto-do-forte-em-praia-grande/AP761')


 # gap: Literal["small", "medium", "large"] = "small",
 #            vertical_alignment: Literal["top", "center", "bottom"] = "top",
 #            border: bool = False) -> list[DeltaGenerator]
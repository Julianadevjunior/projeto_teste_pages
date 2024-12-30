import streamlit as st
import os
import pandas as pd
from PIL import Image
from functions import moeda

cod = 3
bd = pd.read_csv('bd.csv', sep=',')
st.markdown(f"""**Apartamento no bairro {bd['bairro'].loc[cod]}** por **R${moeda(bd['valor'].loc[cod])}**🏡\n
O imovel tem **{bd['quarto'].loc[cod]:.0f}** quarto(s) **{bd['banheiro'].loc[cod]:.0f}** banheiro(s) **{bd['vaga'].loc[cod]:.0f}** vaga(s) com **{bd['area'].loc[cod]:.0f}m²** à **{bd['mar'].loc[cod]:.0f}** metros do mar\n
Financiamento -> {bd['financiamento'].loc[cod]}\n
Permuta -> {bd['permuta'].loc[cod]}\n
**IPTU**: R${moeda(bd['iptu'].loc[cod])}\n
**Cond.**: R${moeda(bd['cond'].loc[cod])}\n""")
st.divider()
# Lista de imagens
caminho = f'./image/image_{cod}'
images = os.listdir(caminho)

tamanho_fixo = (300, 300)

# Divisão em linhas com 3 imagens por linha
colunas_por_linha = 3
for i in range(0, len(images), colunas_por_linha):
    cols = st.columns(colunas_por_linha)
    for j, image in enumerate(images[i:i+colunas_por_linha]):
        with cols[j]:
            imagem = Image.open(os.path.join(caminho, image))
            imagem_resized = imagem.resize(tamanho_fixo, Image.Resampling.LANCZOS)
            st.image(imagem_resized)

st.divider()
st.markdown("""<div style='font-size:25px; text-align:center'>Outros imóveis</div>""", unsafe_allow_html=True)

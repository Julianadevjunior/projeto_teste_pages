import streamlit as st
import os
import pandas as pd
from PIL import Image

bd = pd.read_csv('bd.csv', sep=',')
# st.dataframe(bd)

images = []
for doc in os.listdir("image"):
    if 'jpeg' in doc:
        images.append(doc)

home = st.Page('./page/home.py')
st.page_link(page=home, label='Home')
st.divider()

def moeda(n):
    num = str(f"{n:,.2f}")
    if ',' in num:
        num = num.replace(',', '-')
    if '.' in num:
        num = num.replace('.', ',')
    if '-' in num:
        num = num.replace('-', '.')
    return num

# Caminho das páginas
caminhos = []

for local in bd['caminho'].items():
    id, link = local
    caminhos.append(link)

#Lista de páginas
pages = []
for id, caminho in enumerate(caminhos):
    if id == 0:
        pages.append(st.Page(page=caminho, title=f"ID:{bd['id'].loc[0]} Fotos "))
    else:
        pages.append(st.Page(page=caminho, title=f"ID:{bd['id'].loc[id-1]} »»» {st.markdown('**VER FOTOS**', unsafe_allow_html=True)}"))


pg = st.navigation(pages, position='hidden', expanded=False)
pg.run()

tamanho_fixo = (300, 300)
colunas = st.columns(len(bd)-1)
colunas_por_linha = 2

cont = 1

colunas_por_linha = 2

for i in range(0, len(images), colunas_por_linha):
    cols = st.columns(colunas_por_linha)
    for j, image in enumerate(images[i:i+colunas_por_linha]):
        with cols[j]:
            bloco = st.container(border=True, key=cont + 10)
            with bloco:
                imagem = Image.open(os.path.join(f"./image/{bd['image'].loc[cont]}").lower())
                imagem_resized = imagem.resize(tamanho_fixo, Image.Resampling.LANCZOS)
                st.image(imagem_resized)
                col1, col2 = st.columns([2, 2])
                with col1:
                    st.markdown(f"""R$<b style='font-size:25px'>{moeda(bd['valor'].loc[cont])}</b>""", unsafe_allow_html=True)
                    st.markdown(f"""<b style='font-size:20px'>{bd['bairro'].loc[cont]}</b>""", unsafe_allow_html=True)
                    st.markdown(f"""<b style='font-size:15px'>IPTU R${moeda(bd['iptu'].loc[cont])}</b>""", unsafe_allow_html=True)
                    st.markdown(f"""<b style='font-size:15px'>Cond. R${moeda(bd['cond'].loc[cont])}</b>""", unsafe_allow_html=True)
                    st.page_link(bd['caminho'].loc[cont], use_container_width=True)
                with col2:
                    st.markdown(f"""<b style='font-size:20px'>{bd['quarto'].loc[cont]:.0f}</b> 🛏️<b style='font-size:10px'>DORM.</b>""", unsafe_allow_html=True)
                    st.markdown(f"""<b style='font-size:20px'>{bd['area'].loc[cont]:.0f}m²</b> 📐<b style='font-size:10px'>ÁREA.</b>""", unsafe_allow_html=True)
                    st.markdown(f"""<b style='font-size:20px'>{bd['banheiro'].loc[cont]:.0f}</b> 🚽<b style='font-size:10px'>BANHEIROS.</b>""", unsafe_allow_html=True)
                    st.markdown(f"""<b style='font-size:20px'>{bd['vaga'].loc[cont]:.0f}</b> 🚘<b style='font-size:10px'>VAGAS.</b>""", unsafe_allow_html=True)
                    st.page_link(label='Visitar', page='https://linktr.ee/imoveisfelipecarlos?fbclid=PAZXh0bgNhZW0CMTEAAaY0dJ3FL0eO8Z8ja4Yva-1PmZjEcyrmoAhD-599O3C1mekzS1po-Va6jow_aem_dNdNNOYRiW-W4r82YOZO3A', use_container_width=True)
        cont += 1



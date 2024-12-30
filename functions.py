import streamlit as st
import os
import pandas as pd
from PIL import Image

def moeda(n):
    num = str(f"{n:,.2f}")
    if ',' in num:
        num = num.replace(',', '-')
    if '.' in num:
        num = num.replace('.', ',')
    if '-' in num:
        num = num.replace('-', '.')
    return num
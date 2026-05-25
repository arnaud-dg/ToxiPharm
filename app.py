"""Entrée principale du Streamlit Toxi'Pharm.

Atelier « Gouvernance et Human Oversight en environnement BPL ».
Quatre pages déclarées via st.navigation pour préserver l'ordre et les titres.
"""
from pathlib import Path

import streamlit as st


ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"


st.set_page_config(
    page_title="Toxi'Pharm — Atelier Gouvernance IA",
    page_icon=str(ASSETS / "logo.png") if (ASSETS / "logo.png").exists() else "🧪",
    layout="wide",
    initial_sidebar_state="expanded",
)


pages = [
    st.Page(
        "app_pages/accueil.py",
        title="Accueil",
        icon=":material/home:",
        default=True,
    ),
    st.Page(
        "app_pages/contexte.py",
        title="Contexte et mission",
        icon=":material/description:",
    ),
    st.Page(
        "app_pages/analystai.py",
        title="AnalystAI — Groupe 1",
        icon=":material/science:",
    ),
    st.Page(
        "app_pages/reportflow.py",
        title="ReportFlow — Groupe 2",
        icon=":material/edit_note:",
    ),
]


navigation = st.navigation(pages, position="sidebar", expanded=True)
navigation.run()

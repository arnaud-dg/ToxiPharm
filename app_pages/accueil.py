"""Page 1 : Accueil de l'atelier."""
import base64
from pathlib import Path
import streamlit as st
from app_pages.utils import (
    ASSETS_DIR,
    TOXI_BLUE,
    TOXI_PURPLE,
    sidebar_branding,
)

def render() -> None:
    sidebar_branding()

    st.markdown(
        f"""
        <div style='text-align: center; margin-top: 24px;'>
            <h1 style='color: {TOXI_BLUE}; margin-bottom: 4px;'>Bienvenue chez Toxi'Pharm</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Bandeau visuel principal avec le mockup d'entrée du laboratoire.
    mockup = ASSETS_DIR / "ToxiPharm_Mockup.png"
    if mockup.exists():
        _, col, _ = st.columns([1, 4, 1])
        with col:
            st.image(str(mockup), width=600)

    st.divider()

    col1, col2 = st.columns([3, 2], gap="large")
    with col1:
        st.markdown(
            """
            ### Le pitch de l'atelier

            Toxi'Pharm est un laboratoire d'études toxicologiques précliniques sous BPL OCDE.
            L'entreprise Toxi'Pharm a récemment déployé deux outils d'IA afin de gagner en productivité et de démontrer son envie d'innovation.
            - Le premier module d'IA est un module d'IA traditionnelle, il porte sur l'analyse chromatographique (**AnalystAI**) 
            - Le second est un agent de rédaction de rapports basé sur un LLM (**ReportFlow**).

            Récemment, un sponsor a relevé des incohérences dans un rapport d'étude. L'investigation interne a révélé que les problèmes étaient liés à l'IA et qu'ils sont bien plus grave qu'attendu.
            """
        )

    with col2:
        with st.container(border=True):
            st.markdown(f"<h4 style='color: {TOXI_PURPLE}; margin-top: 0;'>Format</h4>", unsafe_allow_html=True)
            st.markdown(
                """
                - **Durée** : 80 à 90 minutes
                - **2 groupes en parallèle** : **AnalystAI** (ML/DL) et **ReportFlow** (GenAI)
                - **50 minutes** d'analyse et de diagnostic
                - **20 minutes** de débrief croisé
                """
            )

    st.divider()

    st.markdown("### Votre mission")

    mission_img, mission_txt = st.columns([1, 4], gap="medium")
    with mission_img:
        we_want_you = ASSETS_DIR / "We want you.jpg"
        if we_want_you.exists():
            img_b64 = base64.b64encode(we_want_you.read_bytes()).decode()
            st.markdown(
                f"<div style='text-align: center;'>"
                f"<img src='data:image/jpeg;base64,{img_b64}' width='120'>"
                f"</div>",
                unsafe_allow_html=True,
            )
    with mission_txt:
        st.markdown(
            """
            Vous appartenez aux équipes QA de Toxi'Pharm mais travaillez sur un autre site.
            Vous allez devoir enquêter sur l'un des deux outils, afin :

            - Identifier les malfaçons lors de la mise en place des projets
            - Cartographier les défaillances avérées ou possibles en matière de gouvernance et de supervision
            - Formuler un plan d'action et des principes structurants pour une future politique IA
            """
        )

    st.divider()

    st.markdown("### Comment naviguer dans cet atelier")

    nav_cols = st.columns(3, gap="medium")
    with nav_cols[0]:
        with st.container(border=True, height=250):
            st.markdown(f"<h4 style='color: {TOXI_BLUE};'>1. Contexte et mission</h4>", unsafe_allow_html=True)
            st.markdown(
                "**Récupérez votre briefing de mission !** "

                "Découvrez Toxi'Pharm, ses enjeux, la chronologie du déploiement de l'IA dans l'entreprise et le déclencheur de l'investigation."
            )
            st.caption("Lecture commune")

    with nav_cols[1]:
        with st.container(border=True, height=250):
            st.markdown(f"<h4 style='color: {TOXI_BLUE};'>2. Outil AnalystAI</h4>", unsafe_allow_html=True)
            st.markdown(
                "Outil ML/DL d'aide au traitement des chromatogrammes. "
                "La solution, le flowchart actuel, l'avis des équipes."
            )
            st.caption("Travail Groupe 1")

    with nav_cols[2]:
        with st.container(border=True, height=250):
            st.markdown(f"<h4 style='color: {TOXI_BLUE};'>3. Outil ReportFlow</h4>", unsafe_allow_html=True)
            st.markdown(
                "Assistant interne de rédaction basé sur un LLM. "
                "La solution, le flowchart actuel, l'avis des équipes."
            )
            st.caption("Travail Groupe 2")

    st.divider()
    st.info(
        "Bon atelier. Pour démarrer, ouvrez la page **Contexte et mission** dans la barre latérale.",
        icon="🧭",
    )


render()

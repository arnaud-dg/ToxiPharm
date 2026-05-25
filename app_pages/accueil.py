"""Page 1 : Accueil de l'atelier."""
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

    # Bandeau visuel principal avec le mockup d'entrée du laboratoire.
    mockup = ASSETS_DIR / "ToxiPharm_Mockup.png"
    if mockup.exists():
        st.image(str(mockup), use_container_width=True)

    st.markdown(
        f"""
        <div style='text-align: center; margin-top: 24px;'>
            <h1 style='color: {TOXI_BLUE}; margin-bottom: 4px;'>Bienvenue chez Toxi'Pharm</h1>
            <h3 style='color: {TOXI_PURPLE}; font-weight: 400; margin-top: 0;'>
                Atelier — Gouvernance et Human Oversight en environnement BPL
            </h3>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    col1, col2 = st.columns([3, 2], gap="large")
    with col1:
        st.markdown(
            """
            ### Le pitch de l'atelier

            Toxi'Pharm est un laboratoire d'études toxicologiques précliniques sous BPL OCDE.
            Comme beaucoup d'organisations régulées, il a déployé deux outils d'IA pour gagner en productivité :
            un module ML d'analyse chromatographique (**AnalystAI**) et un assistant de rédaction de rapports
            basé sur un LLM (**ReportFlow**).

            Un sponsor a relevé des incohérences dans un rapport d'étude livré il y a quelques semaines.
            L'investigation interne révèle progressivement que le problème dépasse largement la rédaction.

            Votre mission : enquêter sur l'un des deux outils, cartographier les défaillances de gouvernance
            et de Human Oversight, et formuler des principes structurants pour une future politique IA.
            """
        )

    with col2:
        with st.container(border=True):
            st.markdown(f"<h4 style='color: {TOXI_PURPLE}; margin-top: 0;'>Format</h4>", unsafe_allow_html=True)
            st.markdown(
                """
                - **Durée** : 80 à 90 minutes
                - **2 groupes en parallèle** : AnalystAI (ML/DL) et ReportFlow (GenAI)
                - **3 livrables** par groupe en 50 minutes
                - **20 minutes** de débrief croisé
                """
            )

    st.divider()

    st.markdown("### Comment naviguer dans cet atelier")

    nav_cols = st.columns(3, gap="medium")
    with nav_cols[0]:
        with st.container(border=True):
            st.markdown(f"<h4 style='color: {TOXI_BLUE};'>1. Le contexte</h4>", unsafe_allow_html=True)
            st.markdown(
                "Découvrez Toxi'Pharm, les enjeux, la chronologie du déploiement IA, "
                "et le déclencheur de l'investigation. Récupérez votre mission."
            )
            st.caption("Onglet « Contexte et mission »")

    with nav_cols[1]:
        with st.container(border=True):
            st.markdown(f"<h4 style='color: {TOXI_BLUE};'>2. AnalystAI — Groupe 1</h4>", unsafe_allow_html=True)
            st.markdown(
                "Outil ML/DL d'aide au traitement des chromatogrammes. "
                "La solution, le flowchart actuel, l'avis des équipes."
            )
            st.caption("Onglet « AnalystAI »")

    with nav_cols[2]:
        with st.container(border=True):
            st.markdown(f"<h4 style='color: {TOXI_BLUE};'>3. ReportFlow — Groupe 2</h4>", unsafe_allow_html=True)
            st.markdown(
                "Assistant interne de rédaction basé sur un LLM. "
                "La solution, le flowchart actuel, l'avis des équipes."
            )
            st.caption("Onglet « ReportFlow »")

    st.divider()
    st.info(
        "Bon atelier. Pour démarrer, ouvrez la page **Contexte et mission** dans la barre latérale.",
        icon="🧭",
    )


render()

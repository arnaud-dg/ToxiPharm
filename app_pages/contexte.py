"""Page 2 : Descriptif de l'entreprise et Votre mission."""
import streamlit as st
from app_pages.utils import (
    load_markdown,
    page_header,
    render_markdown_with_mermaid,
    sidebar_branding,
    split_h2_sections,
)

# Affichage du contenu de la page
def render() -> None:
    sidebar_branding()
    page_header(
        "Contexte et mission",
    )

    sections = split_h2_sections(load_markdown("page1_accueil.md"))

    # Bloc A — Présentation
    with st.container(border=True):
        st.markdown("### Quelques mots sur Toxi'Pharm")
        st.markdown(sections.get("Bloc A — ToxiPharm : présentation de l'entreprise", ""))

    # Bloc B — Enjeux
    with st.container(border=True):
        st.markdown("### Les enjeux")
        st.markdown(sections.get("Bloc B — Les enjeux de ToxiPharm", ""))

    # Bloc C — Déclencheur (mise en valeur car c'est l'amorce narrative)
    st.markdown("### Le déclencheur")
    with st.container(border=True):
        render_markdown_with_mermaid(sections.get("Bloc C — La problématique : le déclencheur", ""))

    # Bloc D — Frise chronologique
    st.markdown("### Chronologie du déploiement IA")
    render_markdown_with_mermaid(
        sections.get("Bloc D — Frise chronologique du déploiement IA chez ToxiPharm", ""),
        mermaid_height=420,
    )

    # Bloc E — Vos missions
    st.markdown("### Vos missions")
    with st.container(border=True):
        st.markdown(sections.get("Bloc E — Vos missions", ""))

    # Annexe — Grille HITL
    with st.expander("Annexe — Grille HITL (commune aux deux groupes)", expanded=False):
        st.markdown(sections.get("Annexe — Grille HITL (commune aux deux groupes)", ""))


render()

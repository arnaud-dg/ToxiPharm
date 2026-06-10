"""Page 3 : AnalystAI (Groupe 1 — sujet ML/DL)."""
import streamlit as st

from app_pages.utils import (
    load_markdown,
    page_header,
    render_markdown_with_mermaid,
    render_verbatim_cards,
    sidebar_branding,
    split_h2_sections,
)

def render() -> None:
    sidebar_branding()
    page_header(
        "AnalystAI — Groupe 1",
        "Traitement automatisé des chromatogrammes (Deep Learning)",
    )

    sections = split_h2_sections(load_markdown("page2_analystai.md"))

    tab_solution, tab_flowchart, tab_verbatim = st.tabs(
        ["La solution informatique", "Le flowchart actuel", "L'avis des équipes"]
    )

    with tab_solution:
        st.markdown(sections.get("Onglet 2.1 — Comment fonctionne le système", ""))

    with tab_flowchart:
        render_markdown_with_mermaid(
            sections.get("Onglet 2.2 — Flowchart d'AnalystAI", ""),
            mermaid_height=620,
        )

    with tab_verbatim:
        st.markdown(
            "Voici 6 témoignages que vous avez pu receuillir lors de votre investigation terrain."
        )
        st.markdown("")
        render_verbatim_cards(sections.get("Onglet 2.3 — Verbatim AnalystAI", ""))


render()

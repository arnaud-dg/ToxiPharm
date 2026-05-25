"""Page 4 : ReportFlow (Groupe 2 — sujet IA Générative)."""
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
        "ReportFlow — Groupe 2",
        "Assistant interne de rédaction des rapports d'étude (LLM)",
    )

    sections = split_h2_sections(load_markdown("page3_reportflow.md"))

    tab_solution, tab_flowchart, tab_verbatim = st.tabs(
        ["La solution", "Le flowchart actuel", "L'avis des équipes"]
    )

    with tab_solution:
        st.markdown(sections.get("Onglet 3.1 — Comment fonctionne le système", ""))

    with tab_flowchart:
        render_markdown_with_mermaid(
            sections.get("Onglet 3.2 — Flowchart de ReportFlow", ""),
            mermaid_height=720,
        )

    with tab_verbatim:
        st.markdown(
            "Six personnes interagissent au quotidien avec ReportFlow. "
            "Lisez leurs témoignages, notez ce qui interroge."
        )
        st.markdown("")
        render_verbatim_cards(sections.get("Onglet 3.3 — Verbatim ReportFlow", ""))


render()

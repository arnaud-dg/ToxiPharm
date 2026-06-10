"""Outils partagés par les pages : chargement des contenus markdown et rendu."""
from __future__ import annotations

import base64
import re
import textwrap
from pathlib import Path

import streamlit as st
from streamlit_mermaid import st_mermaid


ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "content"
ASSETS_DIR = ROOT / "assets"

# Couleurs de l'identité Toxi'Pharm (dégradé du logo).
TOXI_PURPLE = "#6E2DCC"
TOXI_BLUE = "#2A4FB8"


def load_markdown(name: str) -> str:
    """Charge le contenu brut d'un fichier markdown du dossier content/."""
    return (CONTENT_DIR / name).read_text(encoding="utf-8")


def split_h2_sections(md: str) -> dict[str, str]:
    """Découpe un markdown sur ses titres de niveau 2 (## Titre).

    Retourne un dict {titre_section: contenu_markdown_sans_le_titre}.
    Tout ce qui précède le premier ## est rangé sous la clé "__header__".
    """
    sections: dict[str, str] = {}
    current = "__header__"
    buffer: list[str] = []
    for line in md.splitlines():
        if line.startswith("## "):
            sections[current] = "\n".join(buffer).strip()
            current = line[3:].strip()
            buffer = []
        else:
            buffer.append(line)
    sections[current] = "\n".join(buffer).strip()
    return sections


def split_h3_subsections(md: str) -> list[tuple[str, str]]:
    """Découpe un markdown sur ses titres de niveau 3 (### Titre).

    Retourne une liste ordonnée de (titre, contenu).
    """
    parts: list[tuple[str, str]] = []
    current: str | None = None
    buffer: list[str] = []
    for line in md.splitlines():
        if line.startswith("### "):
            if current is not None:
                parts.append((current, "\n".join(buffer).strip()))
            current = line[4:].strip()
            buffer = []
        else:
            buffer.append(line)
    if current is not None:
        parts.append((current, "\n".join(buffer).strip()))
    return parts


_MERMAID_PATTERN = re.compile(r"```mermaid\n(.*?)```", re.DOTALL)
_IMAGE_PATTERN = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")


def _resolve_local_images(md: str) -> str:
    """Remplace les images locales par des data URIs base64 pour Streamlit."""
    def replace(match: re.Match) -> str:
        alt, path_str = match.group(1), match.group(2)
        path = ASSETS_DIR / Path(path_str).name
        if not path.exists():
            return match.group(0)
        ext = path.suffix.lstrip(".").lower()
        mime = {"jpg": "jpeg", "jpeg": "jpeg", "png": "png", "gif": "gif"}.get(ext, "png")
        b64 = base64.b64encode(path.read_bytes()).decode()
        return f'<img src="data:image/{mime};base64,{b64}" alt="{alt}" style="max-width:100%;height:auto;"/>'
    return _IMAGE_PATTERN.sub(replace, md)


def render_markdown_with_mermaid(md: str, *, mermaid_height: int = 500) -> None:
    """Affiche un markdown en remplaçant les blocs ```mermaid``` par st_mermaid."""
    md = _resolve_local_images(md)
    last_end = 0
    for match in _MERMAID_PATTERN.finditer(md):
        before = md[last_end : match.start()]
        if before.strip():
            st.markdown(before, unsafe_allow_html=True)
        st_mermaid(match.group(1).strip(), height=mermaid_height)
        last_end = match.end()
    tail = md[last_end:]
    if tail.strip():
        st.markdown(tail, unsafe_allow_html=True)


def render_verbatim_cards(md: str) -> None:
    """Affiche la sous-section verbatim sous forme de cartes (st.container border)."""
    items = split_h3_subsections(md)
    for title, body in items:
        with st.container(border=True):
            # La première ligne après ### est habituellement une légende en italique
            # (ex : "*Celui qui a validé les lots #14, #17 et #21*").
            lines = [line for line in body.splitlines() if line.strip()]
            caption = ""
            rest_start = 0
            if lines and lines[0].startswith("*") and lines[0].endswith("*"):
                caption = lines[0].strip("*").strip()
                rest_start = body.find(lines[0]) + len(lines[0])
            st.markdown(f"#### {title}")
            if caption:
                st.caption(caption)
            quote = body[rest_start:].strip()
            st.markdown(quote)


def page_header(title: str, subtitle: str | None = None) -> None:
    """En-tête uniforme pour toutes les pages."""
    st.markdown(
        f"""
        <div style='border-left: 6px solid {TOXI_PURPLE}; padding: 4px 16px; margin-bottom: 16px;'>
            <h1 style='margin: 0; color: {TOXI_BLUE};'>{title}</h1>
            {f"<p style='margin: 4px 0 0 0; color: #555;'>{subtitle}</p>" if subtitle else ""}
        </div>
        """,
        unsafe_allow_html=True,
    )


def sidebar_branding() -> None:
    """Logo et bandeau de l'atelier dans la sidebar (commun à toutes les pages)."""
    logo_path = ASSETS_DIR / "logo.png"
    if not logo_path.exists():
        return
    logo_b64 = base64.b64encode(logo_path.read_bytes()).decode()
    css = f"""
    <style>
        [data-testid="stSidebarNav"]::before {{
        content: "";
        display: block;
        height: 200px;
        margin: 10px 10px 10px 10px;
        background-image: url("data:image/png;base64,{logo_b64}");
        background-repeat: no-repeat;
        background-size: contain;
        background-position: center;
        }}
    </style>
    """
    st.sidebar.markdown(textwrap.dedent(css), unsafe_allow_html=True)

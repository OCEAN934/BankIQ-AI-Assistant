import streamlit as st

from pathlib import Path

from components.sidebar import render_sidebar
from components.uploader import render_uploader
from components.chat_ui import render_chat


st.set_page_config(
    page_title="BankIQ",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)


def load_css():

    css_path = (
        Path(__file__).parent
        / "assets"
        / "styles.css"
    )

    with open(
        css_path,
        encoding="utf-8"
    ) as file:

        st.markdown(
            f"<style>{file.read()}</style>",
            unsafe_allow_html=True
        )


load_css()

render_sidebar()


# HERO SECTION
st.markdown("""
<div class="hero-container">

<div class="hero-badge">
AI-Powered Banking Intelligence Platform
</div>

<h1 class="hero-title">
<span style="
color:#60A5FA;
margin-right:10px;
">
◉
</span>
BankIQ AI Assistant
</h1>

<p class="hero-subtitle">
Enterprise-grade Retrieval-Augmented Generation (RAG)
system for intelligent banking policy understanding,
contextual reasoning, and grounded AI responses.
</p>

</div>
""", unsafe_allow_html=True)


# =========================================
# LIVE SYSTEM METRICS
# =========================================

uploaded_doc = st.session_state.get(
    "uploaded_filename",
    "No document"
)

conversation_count = len(
    st.session_state.get("messages", [])
)

source_count = 0

for msg in st.session_state.get("messages", []):

    if isinstance(msg, dict) and "sources" in msg:

        source_count += len(msg["sources"])


col1, col2, col3, col4 = st.columns(4)

cards = [

    (
        "⬢",
        "Active Document",
        uploaded_doc[:24] + "..."
        if len(uploaded_doc) > 24
        else uploaded_doc
    ),

    (
        "◉",
        "Conversation Memory",
        f"{conversation_count} interactions tracked"
    ),

    (
        "✦",
        "Retrieval Pipeline",
        "Semantic reranking active"
    ),

    (
        "⌘",
        "Grounded Citations",
        f"{source_count} source references"
    )
]


for col, card in zip(
    [col1, col2, col3, col4],
    cards
):

    icon, title, desc = card

    with col:

        st.markdown(
            f"""
<div class="metric-card">

<h2>{icon}</h2>

<h3>{title}</h3>

<p>{desc}</p>

</div>
""",
            unsafe_allow_html=True
        )

# MAIN CONTENT
left_col, right_col = st.columns(
    [1, 2],
    gap="large"
)


with left_col:

    render_uploader()


with right_col:

    render_chat()
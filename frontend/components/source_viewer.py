import streamlit as st


def render_sources(sources):

    with st.expander("📚 Sources & Citations"):

        for source in sources:

            st.markdown(
                f"""
                <div class="source-box">
                    📄 <b>{source['document']}</b><br>
                    📑 Page: {source['page']}
                </div>
                """,
                unsafe_allow_html=True
            )
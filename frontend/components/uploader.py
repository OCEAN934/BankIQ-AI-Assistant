import streamlit as st

from services.api_client import upload_document


def render_uploader():

    st.subheader("📄 Upload Documents")

    uploaded_file = st.file_uploader(
        "Upload PDF or TXT or DOCX",
        type=["pdf", "txt", "docx"]
    )

    if uploaded_file is not None:

        with st.spinner(
            "Processing and indexing document..."
        ):

            response = upload_document(
                uploaded_file
            )

        # STORE ACTIVE DOCUMENT NAME
        st.session_state["uploaded_filename"] = (
            uploaded_file.name
        )

        st.success(
            response["message"]
        )
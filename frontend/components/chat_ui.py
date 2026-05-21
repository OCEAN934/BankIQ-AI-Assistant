import time

import streamlit as st

from services.api_client import (
    send_chat_message,
    fetch_suggestions
)

from components.source_viewer import (
    render_sources
)


def render_message(message):

    with st.chat_message(message["role"]):

        if message["role"] == "user":

            st.markdown(
                f"""
                <div class="user-message">
                    {message["content"]}
                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                f"""
                <div class="assistant-message">
                    {message["content"]}
                </div>
                """,
                unsafe_allow_html=True
            )

            # CONFIDENCE BADGE
            if "confidence" in message:

                confidence = message["confidence"]

                badge_color = {
                    "High": "#22C55E",
                    "Medium": "#F59E0B",
                    "Low": "#EF4444"
                }.get(confidence, "#F59E0B")

                st.markdown(
                    f"""
                    <div class="confidence-badge"
                         style="
                         border-color:{badge_color};
                         color:{badge_color};
                    ">
                        Confidence: {confidence}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            if "sources" in message:

                render_sources(
                    message["sources"]
                )


def generate_response(user_input, session_id):

    # STORE USER MESSAGE
    user_message = {
        "role": "user",
        "content": user_input
    }

    st.session_state.messages.append(
        user_message
    )

    # STORE CURRENT ACTIVE CHAT
    st.session_state.current_chat = {
        "question": user_input,
        "answer": None,
        "sources": None,
        "confidence": None
    }

    # CALL BACKEND
    response = send_chat_message(
        session_id,
        user_input
    )

    answer = response["answer"]

    sources = response["sources"]

    confidence = response.get(
        "confidence",
        "Medium"
    )

    # STORE ASSISTANT MESSAGE
    assistant_message = {
        "role": "assistant",
        "content": answer,
        "sources": sources,
        "confidence": confidence
    }

    st.session_state.messages.append(
        assistant_message
    )

    # UPDATE CURRENT ACTIVE CHAT
    st.session_state.current_chat = {
        "question": user_input,
        "answer": answer,
        "sources": sources,
        "confidence": confidence
    }


def render_current_analysis():

    if (
        "current_chat" not in st.session_state or
        not st.session_state.current_chat
    ):
        return

    current_chat = st.session_state.current_chat

    st.markdown(
        """
        <div class="conversation-title">
        Current Analysis
        </div>
        """,
        unsafe_allow_html=True
    )

    # CURRENT QUESTION
    render_message(
        {
            "role": "user",
            "content": current_chat["question"]
        }
    )

    # SINGLE ASSISTANT CONTAINER
    with st.chat_message("assistant"):

        thinking_placeholder = st.empty()

        thinking_steps = [

            "🔍 Retrieving relevant context...",

            "🧠 Understanding uploaded documents...",

            "📚 Validating grounded sources...",

            "🤖 Generating intelligent response..."
        ]

        for step in thinking_steps:

            thinking_placeholder.markdown(
                f"""
                <div class="assistant-message">
                    {step}
                </div>
                """,
                unsafe_allow_html=True
            )

            time.sleep(0.01)

        thinking_placeholder.empty()

        response_placeholder = st.empty()

        streamed_text = ""

        for word in current_chat["answer"].split():

            streamed_text += word + " "

            response_placeholder.markdown(
                f"""
                <div class="assistant-message">
                    {streamed_text}▌
                </div>
                """,
                unsafe_allow_html=True
            )

            time.sleep(0.01)

        response_placeholder.markdown(
            f"""
            <div class="assistant-message">
                {current_chat["answer"]}
            </div>
            """,
            unsafe_allow_html=True
        )

        # CONFIDENCE BADGE
        confidence = current_chat.get(
            "confidence",
            "Medium"
        )

        badge_color = {
            "High": "#22C55E",
            "Medium": "#F59E0B",
            "Low": "#EF4444"
        }.get(confidence, "#F59E0B")

        st.markdown(
            f"""
            <div class="confidence-badge"
                 style="
                 border-color:{badge_color};
                 color:{badge_color};
            ">
                Confidence: {confidence}
            </div>
            """,
            unsafe_allow_html=True
        )

        if current_chat["sources"]:

            render_sources(
                current_chat["sources"]
            )


def render_conversation_history():

    if not st.session_state.messages:
        return

    if len(st.session_state.messages) <= 2:
        return

    st.markdown(
        """
        <div class="conversation-title">
        Conversation History
        </div>
        """,
        unsafe_allow_html=True
    )

    # EXCLUDE CURRENT ACTIVE CHAT
    history_messages = st.session_state.messages[:-2]

    for message in history_messages:

        render_message(message)


def render_chat():

    st.subheader(
        "💬 Banking Intelligence Chat"
    )

    if "messages" not in st.session_state:

        st.session_state.messages = []

    if "current_chat" not in st.session_state:

        st.session_state.current_chat = None

    session_id = "streamlit_user"

    # =========================================================
    # 1. SUGGESTED QUESTIONS
    # =========================================================

    suggestions_data = fetch_suggestions()

    suggestions = suggestions_data.get(
        "suggestions",
        []
    )

    if suggestions:

        st.markdown(
            """
            <div class="suggested-title">
            Suggested Questions
            </div>
            """,
            unsafe_allow_html=True
        )

        cols = st.columns(2)

        for idx, question in enumerate(suggestions):

            with cols[idx % 2]:

                if st.button(
                    question,
                    key=f"suggestion_{idx}"
                ):

                    generate_response(
                        question,
                        session_id
                    )

                    st.rerun()

    # =========================================================
    # 2. INPUT BOX
    # =========================================================

    user_input = st.chat_input(
        "Ask a banking question..."
    )

    if user_input:

        generate_response(
            user_input,
            session_id
        )

        st.rerun()

    # =========================================================
    # 3. CURRENT ANALYSIS
    # =========================================================

    render_current_analysis()

    # =========================================================
    # 4. CONVERSATION HISTORY
    # =========================================================

    render_conversation_history()
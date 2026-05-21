conversation_memory = {}


def add_message(session_id, message):

    if session_id not in conversation_memory:

        conversation_memory[session_id] = []

    conversation_memory[session_id].append(
        message
    )


def get_conversation(session_id):

    return conversation_memory.get(
        session_id,
        []
    )


def clear_memory():

    global conversation_memory

    conversation_memory = {}
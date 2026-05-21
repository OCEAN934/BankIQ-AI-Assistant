suggestions_store = []


def save_suggestions(suggestions):

    global suggestions_store

    suggestions_store = suggestions


def get_suggestions():

    return suggestions_store
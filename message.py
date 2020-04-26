class Message:
    def __init__(self, application_id, session_id, message_id, participants, content):
        self.application_id = application_id
        self.session_id = session_id
        self.message_id = message_id
        self.participants = participants
        self.content = content


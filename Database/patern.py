class Email:  # Builder
    def __init__(self):
        self.sender = None
        self.recipient = None
        self.subject = None
        self.body = None

    def set_sender(self, sender):
        self.sender = sender
        return self

    def set_recipient(self, recipient):
        self.recipient = recipient
        return self

    def set_subject(self, subject):
        self.subject = subject
        return self

    def set_body(self, body):
        self.body = body
        return self


class EmailSender:  # Facade
    def server_connect(self):
        pass

    def send_email(self, _email):
        self.server_connect()
        print('Sending email')
        print('From...', _email.sender)
        print('To...', _email.recipient)
        print('Subject...', _email.subject)
        print('Body...', _email.body)
        print('Message sent...')


email_builder = Email()
email = email_builder.set_sender('bob@gmail.com').set_recipient('jack@gmail.com').set_subject('Hi').set_body('Hi, jack')

# print(email.sender)
# print(email.recipient)
# print(email.subject)
# print(email.body)
email_sender = EmailSender()
email_sender.send_email(email)

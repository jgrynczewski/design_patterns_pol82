class EmailNotifier:
    def send_mail(self, content, email):
        ...


class PhoneNotifier:
    def send_sms(self, content, phone_nr):
        ...


###################################################

notifier = EmailNotifier()

if isinstance(notifier, EmailNotifier):
    notifier.send_mail("Cześć", "test@test.com")
elif isinstance(notifier, PhoneNotifier):
    notifier.send_sms("Cześć", '111-111-111')

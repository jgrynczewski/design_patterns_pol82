import abc


class INotifier(abc.ABC):
    @abc.abstractmethod
    def send(self, content, receiver):
        ...


class EmailNotifier(INotifier):
    def send_mail(self, content, notifier):
        print(f"Wysyłame mail")


class PhoneNotifier(INotifier):
    def send(self, content, phone_nr):
        print(f"Wysyłam sms")


###################################################

notifier: INotifier = EmailNotifier()
notifier.send(...)

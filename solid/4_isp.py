# ISP - Interface Segragation Principle
class Machine:
    def print(self, doc):
        ...

    def scan(self, doc):
        ...

    def fax(self, doc):
        ...


class MultifunctionalMachine(Machine):
    def print(self, doc):
        print("Drukuje")

    def scan(self, doc):
        print("Skanuję")

    def fax(self, doc):
        print("Wysyłam fax")


class OldFashionedPrinter(Machine):
    "Drukarka starego typu, która nie potrafi skanować"
    def print(self, doc):
        print("Drukuję")

    def fax(self, doc):
        print("Wysyłam fax")

    def scan(self, doc):
        pass


# OldFashionedPrinter().scan()


# Zachowujemy ISP
import abc


class IPrintable(abc.ABC):
    @abc.abstractmethod
    def print(self, doc):
        ...


class IScanable(abc.ABC):
    @abc.abstractmethod
    def scan(self, doc):
        ...


class IFaxable(abc.ABC):
    @abc.abstractmethod
    def fax(self, doc):
        ...


class OldFashionedMachine(IPrintable, IFaxable):
    def print(self, doc):
        print("Drukuję")

    def fax(self, doc):
        print("Wysyłam faks")


# class PhotoCopier(IPrintable, IScanable):
#     ...


# class MultifunctionalMachine(IPrintable, IScanable, IFaxable):
#     ...

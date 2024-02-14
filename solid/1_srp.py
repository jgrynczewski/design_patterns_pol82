# SRP - Single Responsible Principle
# Chodzi o zachowanie wysokiej spójności w kodzie

class Journal:
    def __init__(self):
        self._entries: list = []
        self.count: int = 0

    def add_entry(self, entry: str):
        self.count += 1
        self._entries.append(f"{self.count}: {entry}")

    def remove_entry(self, pos: int):
        self._entries.remove(pos)

    def __str__(self):
        return "\n".join(self._entries)

    # # Łamiemy srp
    # def save(self, filename: str):
    #     file = open(filename,'w', encoding='utf-8')
    #     file.write(str(self))
    #     file.close()
    #
    # def load(self, filename):
    #     pass
    #
    # def load_from_web(self, uri):
    #     pass
    #
    # ...


# Przywracamy SRP (zwiększamy spójność poprzez zastosowanie Pure fabrication (GRASP))
class PersistenceManager:
    def save(self, journal, filename: str):
        file = open(filename, 'w', encoding='utf-8')
        file.write(str(journal))
        file.close()

    def load(self, filename):
        pass

    def load_from_web(self, uri):
        pass


j = Journal()
j.add_entry("Witaj, świecie!")
j.add_entry("Słońce świecie.")

print(f"Zawartość pamiętnika: \n{j}")
# j.save("data.txt")

pm = PersistenceManager()
pm.save(j, 'data.txt')

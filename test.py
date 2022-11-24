class Toto:
    def toto(self):
        self.tata()

    def tata(self):
        print("tata")


une_instance = Toto()
une_instance.toto()


def new_tata(self):
    print("SUPER")


Toto.tata = new_tata

une_instance.toto()

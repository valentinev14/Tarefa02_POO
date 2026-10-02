from datetime import datetime, timedelta

class Treino:
    def __init__(self, id_treino, data, distancia, tempo):
        self.id = id_treino
        self.data = data
        self.distancia = distancia
        self.tempo = tempo

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, valor):
        self._id = valor

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, valor):
        self._data = valor

    @property
    def distancia(self):
        return self._distancia

    @distancia.setter
    def distancia(self, valor):
        self._distancia = valor

    @property
    def tempo(self):
        return self._tempo

    @tempo.setter
    def tempo(self, valor):
        self._tempo = valor

    def pace(self):
        if self.distancia <= 0:
            return timedelta(0)
        segundos_por_km = self.tempo.total_seconds() / self.distancia
        return timedelta(seconds=segundos_por_km)

    def __str__(self):
        data_formatada = self.data.strftime('%d/%m/%Y')
        return f"ID: {self.id} | Data: {data_formatada} | Distância: {self.distancia}km | Tempo: {self.tempo} | Pace: {self.pace()}/km"


class TreinoUI:
    treinos = []

    @classmethod
    def main(cls):
        while True:
            opcao = cls.menu()
            if opcao == 1:
                cls.inserir()
            elif opcao == 2:
                cls.listar()
            elif opcao == 3:
                cls.listar_id()
            elif opcao == 4:
                cls.atualizar()
            elif opcao == 5:
                cls.excluir()
            elif opcao == 6:
                cls.mais_rapido()
            elif opcao == 0:
                break

    @classmethod
    def menu(cls):
        print("\n--- Menu de Treinos ---")
        print("1 - Inserir novo treino")
        print("2 - Listar todos")
        print("3 - Listar por ID")
        print("4 - Atualizar")
        print("5 - Excluir")
        print("6 - Treino mais rápido")
        print("0 - Sair")
        return int(input("Opção: "))

    @classmethod
    def inserir(cls):
        id_treino = int(input("ID: "))
        data_str = input("Data (DD/MM/AAAA): ")
        data = datetime.strptime(data_str, "%d/%m/%Y")
        distancia = float(input("Distância (km): "))
        minutos = int(input("Tempo (minutos): "))
        segundos = int(input("Tempo (segundos): "))
        
        tempo = timedelta(minutes=minutos, seconds=segundos)
        novo_treino = Treino(id_treino, data, distancia, tempo)
        cls.treinos.append(novo_treino)

    @classmethod
    def listar(cls):
        for treino in cls.treinos:
            print(treino)

    @classmethod
    def listar_id(cls):
        id_busca = int(input("ID do treino: "))
        for treino in cls.treinos:
            if treino.id == id_busca:
                print(treino)
                return
        print("Treino não encontrado.")

    @classmethod
    def atualizar(cls):
        id_busca = int(input("ID a atualizar: "))
        for treino in cls.treinos:
            if treino.id == id_busca:
                data_str = input("Nova data (DD/MM/AAAA): ")
                treino.data = datetime.strptime(data_str, "%d/%m/%Y")
                treino.distancia = float(input("Nova distância (km): "))
                minutos = int(input("Novo tempo (minutos): "))
                segundos = int(input("Novo tempo (segundos): "))
                treino.tempo = timedelta(minutes=minutos, seconds=segundos)
                return
        print("Treino não encontrado.")

    @classmethod
    def excluir(cls):
        id_busca = int(input("ID a excluir: "))
        for treino in cls.treinos:
            if treino.id == id_busca:
                cls.treinos.remove(treino)
                return
        print("Treino não encontrado.")

    @classmethod
    def mais_rapido(cls):
        if not cls.treinos:
            return
        treino_rapido = min(cls.treinos, key=lambda t: t.pace())
        print(treino_rapido)

if __name__ == "__main__":
    TreinoUI.main()
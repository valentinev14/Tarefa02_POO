from datetime import datetime, timedelta

class PlayList:
    def __init__(self, id_playlist, nome, descricao):
        self.id = id_playlist
        self.nome = nome
        self.descricao = descricao

    @property
    def id(self): return self._id
    @id.setter
    def id(self, valor): self._id = valor
    
    @property
    def nome(self): return self._nome
    @nome.setter
    def nome(self, valor): self._nome = valor
    
    @property
    def descricao(self): return self._descricao
    @descricao.setter
    def descricao(self, valor): self._descricao = valor

    def tempo_total(self, itens_playlist, musicas):
        total = timedelta()
        for item in itens_playlist:
            if item.id_playlist == self.id:
                for musica in musicas:
                    if musica.id == item.id_musica:
                        total += musica.duracao
        return total

    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome} | Descrição: {self.descricao}"


class Musica:
    def __init__(self, id_musica, titulo, artista, album, duracao):
        self.id = id_musica
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.duracao = duracao

    @property
    def id(self): return self._id
    @id.setter
    def id(self, valor): self._id = valor
    
    @property
    def titulo(self): return self._titulo
    @titulo.setter
    def titulo(self, valor): self._titulo = valor
    
    @property
    def artista(self): return self._artista
    @artista.setter
    def artista(self, valor): self._artista = valor
    
    @property
    def album(self): return self._album
    @album.setter
    def album(self, valor): self._album = valor
    
    @property
    def duracao(self): return self._duracao
    @duracao.setter
    def duracao(self, valor): self._duracao = valor

    def __str__(self):
        return f"ID: {self.id} | Título: {self.titulo} | Artista: {self.artista} | Duração: {self.duracao}"


class PlayListItem:
    def __init__(self, id_item, id_playlist, id_musica, data_inclusao, sequencia):
        self.id = id_item
        self.id_playlist = id_playlist
        self.id_musica = id_musica
        self.data_inclusao = data_inclusao
        self.sequencia = sequencia

    @property
    def id(self): return self._id
    @id.setter
    def id(self, valor): self._id = valor
    
    @property
    def id_playlist(self): return self._id_playlist
    @id_playlist.setter
    def id_playlist(self, valor): self._id_playlist = valor
    
    @property
    def id_musica(self): return self._id_musica
    @id_musica.setter
    def id_musica(self, valor): self._id_musica = valor
    
    @property
    def data_inclusao(self): return self._data_inclusao
    @data_inclusao.setter
    def data_inclusao(self, valor): self._data_inclusao = valor
    
    @property
    def sequencia(self): return self._sequencia
    @sequencia.setter
    def sequencia(self, valor): self._sequencia = valor

    def __str__(self):
        data_formatada = self.data_inclusao.strftime('%d/%m/%Y')
        return f"ID: {self.id} | Playlist: {self.id_playlist} | Música: {self.id_musica} | Seq: {self.sequencia} | Inclusão: {data_formatada}"


class UI:
    playlists = []
    musicas = []
    itens = []

    @classmethod
    def main(cls):
        while True:
            print("\n--- Sistema de Playlists ---")
            print("1 - Inserir Playlist")
            print("2 - Listar Playlists")
            print("3 - Inserir Música")
            print("4 - Listar Músicas")
            print("5 - Vincular Música a Playlist (Item)")
            print("6 - Listar Itens de Playlist")
            print("7 - Tempo Total de uma Playlist")
            print("0 - Sair")
            opcao = int(input("Opção: "))
            
            if opcao == 1: cls.inserir_playlist()
            elif opcao == 2: cls.listar_playlists()
            elif opcao == 3: cls.inserir_musica()
            elif opcao == 4: cls.listar_musicas()
            elif opcao == 5: cls.inserir_item()
            elif opcao == 6: cls.listar_itens()
            elif opcao == 7: cls.mostrar_tempo_total()
            elif opcao == 0: break

    @classmethod
    def inserir_playlist(cls):
        id_pl = int(input("ID da Playlist: "))
        nome = input("Nome: ")
        descricao = input("Descrição: ")
        cls.playlists.append(PlayList(id_pl, nome, descricao))

    @classmethod
    def listar_playlists(cls):
        for pl in cls.playlists:
            print(pl)

    @classmethod
    def inserir_musica(cls):
        id_musica = int(input("ID da Música: "))
        titulo = input("Título: ")
        artista = input("Artista: ")
        album = input("Álbum: ")
        minutos = int(input("Duração (minutos): "))
        segundos = int(input("Duração (segundos): "))
        
        duracao = timedelta(minutes=minutos, seconds=segundos)
        cls.musicas.append(Musica(id_musica, titulo, artista, album, duracao))

    @classmethod
    def listar_musicas(cls):
        for m in cls.musicas:
            print(m)

    @classmethod
    def inserir_item(cls):
        id_item = int(input("ID do Vínculo: "))
        id_pl = int(input("ID da Playlist: "))
        id_musica = int(input("ID da Música: "))
        sequencia = int(input("Sequência na Playlist: "))
        data_inclusao = datetime.now()
        
        cls.itens.append(PlayListItem(id_item, id_pl, id_musica, data_inclusao, sequencia))

    @classmethod
    def listar_itens(cls):
        for item in cls.itens:
            print(item)

    @classmethod
    def mostrar_tempo_total(cls):
        id_busca = int(input("ID da Playlist para calcular o tempo: "))
        for pl in cls.playlists:
            if pl.id == id_busca:
                tempo = pl.tempo_total(cls.itens, cls.musicas)
                print(f"Tempo total da playlist '{pl.nome}': {tempo}")
                return
        print("Playlist não encontrada.")

if __name__ == "__main__":
    UI.main()
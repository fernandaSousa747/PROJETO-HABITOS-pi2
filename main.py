class Habito:
    def __init__(self, nome, descricao, frequencia):
        self.nome = nome
        self.descricao = descricao
        self.frequencia = frequencia

    def exibir(self):
        return f"{self.nome} - {self.descricao} ({self.frequencia})"


class Usuario:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.habitos = []

    def adicionar_habito(self, habito):
        self.habitos.append(habito)

    def listar_habitos(self):
        for h in self.habitos:
            print(h.exibir())


class Sistema:
    def __init__(self):
        self.usuarios = []

    def cadastrar_usuario(self, nome, idade):
        usuario = Usuario(nome, idade)
        self.usuarios.append(usuario)
        return usuario

    def listar_usuarios(self):
        for u in self.usuarios:
            print(u.nome)


# Execução
sistema = Sistema()

usuario = sistema.cadastrar_usuario("Maria", 20)

habito1 = Habito("Estudar", "Estudar programação", "Diário")
usuario.adicionar_habito(habito1)

usuario.listar_habitos()

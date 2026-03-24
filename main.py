class Habito:
    def __init__(self, nome, descricao, frequencia):
        self.nome = nome
        self.descricao = descricao
        self.frequencia = frequencia

    def __str__(self):
        return f"{self.nome} - {self.descricao} ({self.frequencia})"


class Usuario:
    def __init__(self, nome, idade):
        if idade < 0:
            raise ValueError("Idade inválida")
        self.nome = nome
        self.idade = idade
        self.habitos = []

    def adicionar_habito(self, habito):
        self.habitos.append(habito)

    def remover_habito(self, nome):
        self.habitos = [h for h in self.habitos if h.nome != nome]

    def listar_habitos(self):
        return [str(h) for h in self.habitos]


class Sistema:
    def __init__(self):
        self.usuarios = []

    def cadastrar_usuario(self, nome, idade):
        usuario = Usuario(nome, idade)
        self.usuarios.append(usuario)
        return usuario

    def listar_usuarios(self):
        return [u.nome for u in self.usuarios]


# Execução
if __name__ == "__main__":
    sistema = Sistema()

    usuario = sistema.cadastrar_usuario("Maria", 20)

    habito1 = Habito("Estudar", "Estudar programação", "Diário")
    usuario.adicionar_habito(habito1)

    print("Hábitos do usuário:")
    for h in usuario.listar_habitos():
        print("-", h)

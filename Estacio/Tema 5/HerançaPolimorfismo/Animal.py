# Classe base para todos os animais
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        pass

    def mover(self):
        pass


# Subclasse Cachorro que sobrescreve os métodos falar e mover
class Cachorro(Animal):
    def falar(self):
        return "Au!"

    def mover(self):
        return f"{self.nome} está andando."


# Subclasse Gato que sobrescreve os métodos falar e mover
class Gato(Animal):
    def falar(self):
        return "Miau!"

    def mover(self):
        return f"{self.nome} está andando."


# Subclasse Vaca que sobrescreve os métodos falar e mover
class Vaca(Animal):
    def falar(self):
        return "Muu!"

    def mover(self):
        return f"{self.nome} está andando."


class Voador:
    # Nota: Assumindo que self.nome é inicializado na classe Animal
    def voar(self):
        return f"{self.nome} está voando."


# Mixin para animais que podem nadar
class Nadador:
    # Nota: Assumindo que self.nome é inicializado na classe Animal
    def nadar(self):
        return f"{self.nome} está nadando."


# Subclasse Pato que herda de Animal, Voador e Nadador
class Pato(Animal, Voador, Nadador):

    def falar(self):
        return "Quack!"

    def mover(self):
        # Chama os métodos andar, nadar e voar
        return f"{self.andar()}, {self.nadar()} E {self.voar()}"

    def andar(self):
        return f"{self.nome} está andando."


# --- NOVA CLASSE: JACARÉ ---
class Jacare(Animal, Nadador):

    def falar(self):
        return "Sssszzzz (som de réptil e sibilo)"

    def mover(self):
        # O jacaré anda e nada, então combinamos as duas ações.
        return f"{self.andar()} E {self.nadar()}"

    def andar(self):
        return f"{self.nome} está rastejando/andando."


# --- FIM DA NOVA CLASSE ---


# Função que usa polimorfismo para chamar o método falar
def fazer_som(animal):
    return animal.falar()


# Função que usa polimorfismo para chamar o método mover
def fazer_movimento(animal):
    return animal.mover()


# Instâncias das classes
cachorro = Cachorro('Lug')
gato = Gato('Floquinho')
vaca = Vaca('Mimosa')
pato = Pato("Pato Donald")

# --- NOVA INSTÂNCIA ---
jacare = Jacare("Croc")

# Chamando os métodos polimórficos
print("\n--- Teste de Som (Falar) ---")
print(fazer_som(cachorro))
print(fazer_som(gato))
print(fazer_som(vaca))
print(fazer_som(pato))
print(fazer_som(jacare))  # Saída: Sssszzzz (som de réptil e sibilo)

print("\n--- Teste de Movimento (Mover) ---")
print(fazer_movimento(cachorro))
print(fazer_movimento(gato))
print(fazer_movimento(vaca))
print(fazer_movimento(pato))
print(fazer_movimento(jacare))  # Saída: Croc está rastejando/andando E Croc está nadando.
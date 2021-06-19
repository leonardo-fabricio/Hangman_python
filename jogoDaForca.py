# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:
    # Método Construtor
    def __init__(self,word):
        self.word = word
        self.cont = 0

	# Método para verificar se o jogo terminou
    def hangman_over(self): 
        if(self.cont == 7): 
            return True

    def increment(self):
        self.cont += 1

    def getCont(self):
        return self.cont
    def getWord(self):
        return self.word

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self): 
        print(board[self.cont])

    # Método para adivinhar a letra
    def guess(self, letter):
        lista = list(self.word)
        for x in lista:
            if(x == letter):
                return True
    def __len__(self):
        return len(list(self.word))

	# Método para verificar se o jogador venceu
    def hangman_won(self,word_aux): 
        aux = 0
        lista = list(word_aux)
        lista2 = list(self.word)
        for x in range(0,len(lista2)-1):
            for y in range(0,len(lista)):
                if lista2[x] == lista[y]:
                    aux += 1
        if(aux == len(lista2)-1):
            return True
        else:
            return False

	# # Método para não mostrar a letra no board
	# def hide_word(self):
		
			

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word(): 
    with open("palavras.txt", "rt") as f: 
        bank = f.readlines() 
    return bank[random.randint(0,len(bank)-1)].strip()


# Função Main - Execução do Programa
def main():

	# Objeto
    game = Hangman(rand_word()) 
    
    #print(rand_word()) TESTE
	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	

	# Verifica o status do jogo
    letra_certas = " "
    letra_errada = " "
    game.print_game_status()
    print("A PALAVRA CONTEM ",len(game), " LETRAS")
    while game.getCont() != 6:
        
        in_user_word = input("Digite uma letra: ")
        
        if not (game.guess(str(in_user_word))):
            game.increment()
            letra_errada += in_user_word 
        else:
            letra_certas += in_user_word
            
        print("Letras Certas: "+ letra_certas)
        print("Letras Erradas: "+ letra_errada)
        # De acordo com o status, imprime mensagem na tela para o usuário
        if game.hangman_won(letra_certas):
            print('\nParabéns! Você venceu!!')
            break
        game.print_game_status()
        print("A PALAVRA CONTEM ",len(game), " LETRAS")
        
    print("Palavra Certa: ", game.getWord())
    print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa		
if __name__ == "__main__":
	main()

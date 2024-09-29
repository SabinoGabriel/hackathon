from random import randint








class Personagem():
    def __init__(self, nome, classe, ataque, defesa, vida, arma):
        self.nome = nome
        self.classe = classe
        self.ataque = ataque
        self.defesa = defesa
        self.vida = vida
        self.arma = arma








class Monster:
    def __init__(self, nome, ataque, defesa, vida):
        self.nome = nome
        self.ataque = ataque
        self.defesa = defesa
        self.vida = vida








def dado():
    return randint(1,20)








def battle(player, monster):
    while player.vida > 0 and monster.vida > 0:
        print(f"\n{player.nome} vs {monster.nome}")
        print(f"Vida do jogador: {player.vida}")
        print(f"Vida do monstro: {monster.vida}")
        turno = input("Você quer bater ou correr?\n1.Bater\n2.Correr\n")
        if turno == "1":
            tentativa_jogador = dado()
            tentativa_monstro = dado()
            print("Rolem os dados:")
            if tentativa_jogador - monster.defesa > 4:
                monster.vida -= player.ataque
                print(f"\033[92mSeu ataque foi bem sucedido\033[0m, o monstro possui {monster.vida} pontos de vida.")
            else:
                print("\033[31mAtaque falho\033[0m, a vida do monstro permanece a mesma")
            if monster.vida > 0:
                   
                if tentativa_monstro - player.defesa > 4:
                    player.vida -= monster.ataque
                    print(f"\033[91mO ataque do monstro foi bem sucedido\033[0m, você possui {player.vida} pontos de vida.")
                else:
                    print("\033[31mAtaque falho\033[0m, a sua vida permanece a mesma")
       
        elif turno == "2":
            print("\033[7mVocê escolheu correr, você é um derrotado por natureza!\033[0m")
            player.vida = 0
           
           
           
    if player.vida > 0:
        print(f"\033[33mVocê venceu o combate contra\033[0m {monster.nome}!")
    else:
        print(f"\033[31mVocê perdeu o combate contra\033[0m {monster.nome}!")
















def main():
    print("\033[40m==>\033[0m \033[1;33mBem-vindo a Dungeon Infinity\033[0m \033[40m<==\033[0m")
    nome = input("Me diga seu nome jovem.\n")
    personagem = input("\033[33mEscolha seu personagem:\033[0m\n1.Guerreiro\n2.Mago\n")
    if personagem == "1":
        player = Personagem(nome, "Guerreiro", 7, 8, 20, "Espada")
    elif personagem == "2":
        player = Personagem(nome, "Mago", 5, 9, 20, "Cajado")
   
    print(f"Seja bem vindo poderoso {player.classe}")








    monstro_1 = Monster("Goblin", 5, 5, 20)
    monstro_2 = Monster("Orc", 7, 7, 30)
    monstro_3 = Monster("Dragão", 9, 9, 40)
    monsters = [monstro_1, monstro_2, monstro_3]
    historias = ["\033[33mA missão é aprender a usar o fogo para caçar e proteger-se, estabelecendo um primeiro contato pacífico. Um goblin aparece devastando a vila!\033[0m",
                 "\033[33mConflitos surgem entre humanos e elfos, mas uma antiga criatura mágica desperta, obrigando-os a unir forças para enfrentá-la em uma batalha épica contra os Orcs!!\033[0m",
                 "\033[33mA magia retorna, mas uma organização secreta tenta erradicá-la. Os jogadores devem unir humanos e elfos para enfrentar essa ameaça em uma batalha decisiva contra o Dragão\033[0m"
                 ]








    contador = 0
    while True:
       
        monster = monsters[contador]
        print(historias[contador])
        battle(player, monster)
        if player.vida > 0:
            contador += 1
            player.vida = 20
            player.ataque += 2
            player.defesa += 2
        else:
            print("== \033[91mGame Over!\033[0m ==")
            break
        if contador > 2:
            print("\033[93mParabéns\033[0m, \033[90mvocê finalizou a aventura e derrotou todos os inimigos!\033[0m")
            break
       








main()





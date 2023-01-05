import time
import emoji
import random

#inicio do clean code

def backpack(list):
    for x, e in enumerate(list):
        print(emoji.emojize(f"\nMochila :backpack: :\n[{x+1}] {e}"))
    time.sleep(1)

#terminar depois

Local1 = [emoji.emojize("Quarto:house:"), emoji.emojize("Casa:house:"), emoji.emojize("Cidade Inicial: Fortaleza Town :cityscape:")]
team = []
box = []
pb = 0
bag = [f"pokebola x{pb}"]
count = 0
grama_alta = [emoji.emojize("Pidgey:feather:"),emoji.emojize("Pidgeotto :eagle:"),emoji.emojize("Rattata :rat:"),emoji.emojize("Zubat :bat:"),emoji.emojize("Gengar :ghost:"),emoji.emojize("Magikarp :tropical_fish:"),emoji.emojize("Tentacool :octopus:"),emoji.emojize("Butterfree :butterfly:"),emoji.emojize("Beedrill :honeybee:"),emoji.emojize("Exeggtor :palm_tree:"),emoji.emojize("Magnemite :magnet:"),emoji.emojize("Sunflora :sunflower:"),emoji.emojize("Riolu :curly_loop:"),emoji.emojize("Growlith :dog:"),emoji.emojize("Mareep :ewe:"),emoji.emojize("Noctawl :owl:"),emoji.emojize("Rayquaza :dragon:"),emoji.emojize("Krabby :crab:"),emoji.emojize("Tentacruel :squid:"),emoji.emojize("Lucario :cyclone:"),emoji.emojize("Pikachu :part_alternation_mark:"),emoji.emojize("Geodude :rock:"),]
x = 0
print(emoji.emojize('Bem vindo ao mundo pokemon :grinning_face:', language='en'))
time.sleep(1)
print(emoji.emojize("\nMeu nome é professor Paul Brasil :man_raising_hand:", language='en'))
time.sleep(1)
print(emoji.emojize("\nAntes de iniciar, me diga, você é menino :boy: ou menina :girl:", language='en'))
time.sleep(0.5)

while True:
    ask = input("Insira B para Menino ou G para Menina: ")
    time.sleep(0.5)
    if ask == "B" or ask == "b":
        print(emoji.emojize("\nEntão você é um menino :boy: \n", language='en'))
        time.sleep(0.5)
        print("Qual o seu nome?")
        time.sleep(1)
        name = input("Insira seu nome:")
        time.sleep(0.5)
        print(emoji.emojize(f"\nEntão você é um menino :boy: e seu nome é {name}"))
        you = emoji.emojize(f"{name} :boy:")

        break

    if ask == "G" or ask == "g":
        print(emoji.emojize("\nEntão você é uma menina :girl: \n", language='en'))
        time.sleep(0.5)
        print("Qual o seu nome?")
        time.sleep(1)
        name = input("Insira seu nome:")
        time.sleep(0.5)
        print(emoji.emojize(f"\nEntão você é uma menina :girl: e seu nome é {name}"))
        you = emoji.emojize(f"{name} :girl:")
        break
    else:
        print("Tente novamente, você digitou errado!")

print("\nVamos começar sua aventura no mundo pokemon\n")
print("------------------------------------------------------")
time.sleep(1)

print(emoji.emojize(f"\nLocal:triangular_flag: = {Local1[x]}  | Time Pokemon :red_circle: = [Nenhum Pokemon]"))
print("\n------------------------------------------------------\n")
time.sleep(1)

print(emoji.emojize(f"\nMãe :woman:: 'Filho(a) Você precisa descer e ir no Laboratório do Professor Paul BR'"))
time.sleep(1)
while True:
    print("\nOPÇÕES:\nB: Mochila | P: Ver Seu Time | Y: Você | A: Ir para outro cômodo")
    time.sleep(0.5)
    resp = input("\nEscolha o que fazer:") 
    listresp = ["A", "a", "B", "b", "P", "p", "Y", "y"]
    if resp == "Y" or resp == "y":
        print(you)
        time.sleep(1)
    if resp == "B" or resp == "b":
        print(backpack(bag))
    if resp =="P" or resp == "p":
        print(emoji.emojize("Você ainda não tem nenhum pokemon! :cross_mark:"))
        time.sleep(1)
    if resp =="A" or resp == "a":
        print(emoji.emojize("\nVocê está descendo as escadas! :down_arrow:\n"))
        x += 1
        time.sleep(1)
        break
    if resp not in listresp: 
        print("Tente novamente, você digitou errado!")

print("------------------------------------------------------")
time.sleep(1)

print(emoji.emojize(f"\nLocal:triangular_flag: = {Local1[1]}  | Time Pokemon :red_circle: = [Nenhum Pokemon]"))
print("\n------------------------------------------------------\n")
time.sleep(1)

print(emoji.emojize(f"\nMãe :woman:: '{name}, você precisa ir ao Laboratório do Professor Paul para pegar seu inícial'"))
time.sleep(1)

while True:
    print("\nOPÇÕES:\nB: Mochila | P: Ver Seu Time | Y: Você | A: Sair de Casa | V: Voltar para o Quarto")
    time.sleep(0.5)
    resp = input("\nEscolha o que fazer:") 
    listresp = ["A", "a", "B", "b", "P", "p", "Y", "y", "V", "v"]
    if resp == "Y" or resp == "y":
        print(you)
        time.sleep(1)
    if resp == "B" or resp == "b":
        for x, e in enumerate(bag):
            print(emoji.emojize(f"\nMochila :backpack: :\n[{x+1}] {e}"))
        time.sleep(1)
    if resp =="P" or resp == "p":
        print(emoji.emojize("Você ainda não tem nenhum pokemon! :cross_mark:"))
        time.sleep(1)
    if resp =="A" or resp == "a":
        print(emoji.emojize("\nVocê está saindo de casa:right_arrow:!\n"))
        x += 1
        time.sleep(1)
        break
    if resp == "V" or resp == "v":
        
        print(emoji.emojize("\nVocê está subindo as escadas!:up_arrow:"))
        time.sleep(1)
        while True:

            print("\nOPÇÕES:\nB: Mochila | P: Ver Seu Time | Y: Você | A: Ir para outro cômodo")
            time.sleep(0.5)
            resp = input("\nEscolha o que fazer:") 
            listresp2 = ["A", "a", "B", "b", "P", "p", "Y", "y"]
            if resp == "Y" or resp == "y":
                print(you)
                time.sleep(1)
            if resp == "B" or resp == "b":
                for x, e in enumerate(bag):
                    print(emoji.emojize(f"\nMochila :backpack: :\n[{x+1}] {e}"))
                time.sleep(1)
            if resp =="P" or resp == "p":
                print(emoji.emojize("Você ainda não tem nenhum pokemon! :cross_mark:"))
                time.sleep(1)
            if resp =="A" or resp == "a":
                print(emoji.emojize("\nVocê está descendo as escadas! :down_arrow:\n"))
                x == 2
                time.sleep(1)
                break
            if resp not in listresp2: 
                print("Tente novamente, você digitou errado!")
    
    if resp not in listresp: 
        print("Tente novamente, você digitou errado!")
print("------------------------------------------------------")

print(emoji.emojize(f"\nLocal:triangular_flag: = {Local1[2]}  | Time Pokemon :red_circle: = [Nenhum Pokemon]"))
print("\n------------------------------------------------------\n")
time.sleep(1)
Local2 = [emoji.emojize("Sua Casa :house: "), emoji.emojize("Casa do Kauã :house: "), emoji.emojize("Lab. do Professor Paul :department_store: "), emoji.emojize("Rota01 :world_map: ")]
x = 0
while len(team) != 1:
    print(f"OPÇÕES:\nB: Mochila | P: Ver Seu Time | Y: Você |\n\nOu Escolha um dos Locais Abaixo para ir\nLocais > V: Para voltar Para {Local2[0]} | K: P/ ir para {Local2[1]} | L: P/ ir ao {Local2[2]} | R: P/ ir à {Local2[3]} ")

    time.sleep(0.5)
    resp = input("\nEscolha o que fazer:")
     
    listresp = ["A", "a", "B", "b", "P", "p", "Y", "y", "V", "v", "K","k","R","r","L","l"]
    if resp == "Y" or resp == "y":
        print(you)
        time.sleep(1)
    if resp == "B" or resp == "b":
        for x, e in enumerate(bag):
            print(emoji.emojize(f"\nMochila :backpack: :\n[{x+1}] {e}"))
        time.sleep(1)
    if resp =="P" or resp == "p":
        print(emoji.emojize("Você ainda não tem nenhum pokemon! :cross_mark:"))
        time.sleep(1)
    if resp =="A" or resp == "a":
        print(emoji.emojize("\nVocê está saindo de casa:right_arrow:!\n"))
        x += 1
        time.sleep(1)
        break
    if resp == "K" or resp == "k":

        print(emoji.emojize("\nVocê está entrando na casa de Kauã:right_arrow:!\n"))
        time.sleep(1)
        print("------------------------------------------------------")
        print(emoji.emojize(f"\nLocal:triangular_flag: = {Local2[1]}  | Time Pokemon :red_circle: = [Nenhum Pokemon]"))
        print("\n------------------------------------------------------\n")
        while True:
            figs = [emoji.emojize("Júlio :man_beard:"), emoji.emojize("Guilherme :child:"), emoji.emojize("Kauã :child:"), emoji.emojize("Gabriel :boy:"), emoji.emojize("Crispim :child:"), emoji.emojize("Suquin :man_bald:"), emoji.emojize("Luan :man_blond_hair:")]  
            print("\nOPÇÕES:\nB: Mochila | P: Ver Seu Time | Y: Você | A: Sair da Casa\n\nOu Fale com os NpC's\nNPC'S > 'J' falar com Júlio | 'G'p/ falar com Guilherme | 'K' falar com Kauã | 'H' falar com Gabriel | 'C' falar com Crispim | 'S' falar com Suquin | 'L'falar com Luan")
            time.sleep(0.5)
            resp = input("\nEscolha o que fazer:") 
            listresp3 = ["A", "a", "B", "b", "P", "p", "Y", "y", "J","j","K","k","G","g","H","h","L","l","S","s","C","c"]    
            if resp not in listresp3: 
                print("Tente novamente, você digitou errado!")
            if resp == "Y" or resp == "y":
                print(you)
                time.sleep(1)
            if resp == "B" or resp == "b":
                for x, e in enumerate(bag):
                    print(emoji.emojize(f"\nMochila :backpack: :\n[{x+1}] {e}"))
                    time.sleep(1)
            if resp =="P" or resp == "p":
                print(emoji.emojize("Você ainda não tem nenhum pokemon! :cross_mark:"))
                time.sleep(1)
            if resp =="A" or resp == "a":
                print(emoji.emojize("\nVocê está saindo da casa de Kauã:left_arrow:!\n"))
                time.sleep(1)
                print("------------------------------------------------------")
                print(emoji.emojize(f"\nLocal:triangular_flag: = {Local1[2]}  | Time Pokemon :red_circle: = [Nenhum Pokemon]"))
                print("\n------------------------------------------------------\n")
                break
            if resp =="J" or resp == "j":
                print()
                print(f"{figs[0]}: 'Inscrevam-se no Canal Júlio Tech'")
                time.sleep(1.3)
            if resp =="G" or resp == "g":
                print()
                print(f"{figs[1]}: 'Eu ia ser Jogador de Futebol, mas torci o tornozelo '")
                time.sleep(1.3)
            if resp =="K" or resp == "k":
                print()
                print(f"{figs[2]}: 'Digamos que minha bebida favorita é tampico'")
                time.sleep(1.3)
            if resp =="H" or resp == "h":
                print()
                print(f"{figs[3]}: 'Eu quero ser um mestre pokemon igual o Campeão MessiMon'")
                time.sleep(1.3)
            if resp =="C" or resp == "c":
                print()
                print(f"{figs[4]}: 'Ah! Estação...'")
                time.sleep(1.3)
            if resp == "S" or resp == "s":
                print()
                print(f"{figs[5]}: 'kkkkkkkkkkkkkkkkkkkk'")
                time.sleep(1.3)
            if resp == "L" or resp == "l":
                print()
                print(f"{figs[6]}: 'Vou trabalhar, pq se depender do flamengo...'")
                time.sleep(1.3)
    
                
    if resp == "R" or resp == "r":
        time.sleep(0.5)
        print(emoji.emojize("\nVocê ainda não pode ir nessa rota sem ter nenhum pokemon :cross_mark:!\n"))   
        time.sleep(1)
    if resp == "L" or resp == "l":
        print(emoji.emojize(f"Entrando no Laboratório"))
        time.sleep(1)
        print("------------------------------------------------------")
        print(emoji.emojize(f"\nLocal:triangular_flag: = {Local2[2]}  | Time Pokemon :red_circle: = [Nenhum Pokemon]"))
        print("\n------------------------------------------------------\n")
        time.sleep(1)
        print(emoji.emojize(f"Prof Paul :man_raising_hand:: 'Então, {name} você vai finalmente começar sua jornada!' "))
        time.sleep(2)
        print(emoji.emojize(f"\nNo mundo dos pokemon, treinadores iniciam sua jornada escolhendo um pokemon inicial!"))
        time.sleep(2)
        print(emoji.emojize("Por conta disso, você iniciará sua jornada escolhendo um dos três iniciais\n\nBulbasaur:herb: do tipo Grama | Squirtle :droplet: do tipo água | Charmander :fire: do tipo fogo"))        
        time.sleep(2)
        while True:
            print("\nOPÇÕES:\nB: P/ escolher Bulbasaur | S: P/ Squirtle | C: P/ Charmander")
            time.sleep(1)
            resp = input("\nInsira sua escolha:")
            resps = ["B", "b", "S", "S","C", "c"]
            if resp == "B" or resp == "b":
                print(emoji.emojize("Você escolheu o Bulbassaur:herb:"))
                a = input("Tem certeza de sua resposta 'Sim' ou 'Não' > ")
                if a == "sim" or a == "Sim":
                    time.sleep(1)
                    print("Gotcha! Você pegou o Bulbassaur!")
                    time.sleep(1)
                    team.append(emoji.emojize("Bulbassaur:herb:"))
                    print(f"Time: {team}")
                    time.sleep(1)
                    break
                if a == "Não" or a == "não" or a == "Nao" or a == "nao":
                    time.sleep(1)

            if resp == "S" or resp == "s":
                print(emoji.emojize("Você escolheu o Squirtle:droplet:"))
                a = input("Tem certeza de sua resposta 'Sim' ou 'Não' > ")
                if a == "sim" or a == "Sim":
                    time.sleep(1)
                    print("Gotcha! Você pegou o Squirtle!")
                    time.sleep(1)
                    team.append(emoji.emojize("Squirtle:droplet:"))
                    print(f"Time: {team}")
                    time.sleep(1)
                    break
                if a == "Não" or a == "não" or a == "Nao" or a == "nao":
                        time.sleep(1)
 
            if resp == "C" or resp == "c":
                print(emoji.emojize("Você escolheu o Charmander:fire:"))
                a = input("Tem certeza de sua resposta 'Sim' ou 'Não' > ")
                if a == "sim" or a == "Sim":
                    time.sleep(1)
                    print("Gotcha! Você pegou o Charmander!")
                    time.sleep(1)
                    team.append(emoji.emojize("Charmander:fire:"))
                    print(f"Time: {team}")
                    time.sleep(1)
                    break
                if a == "Não" or a == "não" or a == "Nao" or a == "nao":
                    time.sleep(1)

            if resp not in resps:
                print("Tente novamente!")
    
         
    if resp == "V" or resp == "v":
        
        print(emoji.emojize("\nVocê está entrando em casa! :left_arrow: "))
        time.sleep(1)
        while True:
            c = 0
            print("\nOPÇÕES:\nB: Mochila | P: Ver Seu Time | Y: Você | A: Sair de Casa | V: Voltar para o Quarto")
            time.sleep(0.5)
            resp = input("\nEscolha o que fazer:") 
            listresp = ["A", "a", "B", "b", "P", "p", "Y", "y", "V", "v"]
            if resp == "Y" or resp == "y":
                print(you)
                time.sleep(1)
            if resp == "B" or resp == "b":
                for x, e in enumerate(bag):
                    print(emoji.emojize(f"\nMochila :backpack: :\n[{x+1}] {e}"))
                time.sleep(1)
            if resp =="P" or resp == "p":
                print(emoji.emojize("Você ainda não tem nenhum pokemon! :cross_mark:"))
                time.sleep(1)
            if resp =="A" or resp == "a":
                print(emoji.emojize("\nVocê está saindo de casa:right_arrow:!\n"))
                time.sleep(1)
                print("------------------------------------------------------")
                print(emoji.emojize(f"\nLocal:triangular_flag: = {Local1[2]}  | Time Pokemon :red_circle: = [Nenhum Pokemon]"))
                print("\n------------------------------------------------------\n")
                time.sleep(1)                        
                time.sleep(1)
                break
            
      
            
            if resp == "V" or resp == "v":
                
                print(emoji.emojize("\nVocê está subindo as escadas!:up_arrow:"))
                time.sleep(1)
                while True:
                    x = 0
                    print("\nOPÇÕES:\nB: Mochila | P: Ver Seu Time | Y: Você | A: Ir para outro cômodo")
                    time.sleep(0.5)
                    resp = input("\nEscolha o que fazer:") 
                    listresp2 = ["A", "a", "B", "b", "P", "p", "Y", "y"]
                    if resp == "Y" or resp == "y":
                        print(you)
                        time.sleep(1)
                    if resp == "B" or resp == "b":
                        for x, e in enumerate(bag):
                            print(emoji.emojize(f"\nMochila :backpack: :\n[{x+1}] {e}"))
                        time.sleep(1)
                    if resp =="P" or resp == "p":
                        print(emoji.emojize("Você ainda não tem nenhum pokemon! :cross_mark:"))
                        time.sleep(1)
                    if resp =="A" or resp == "a":
                        print(emoji.emojize("\nVocê está descendo as escadas! :down_arrow:\n"))
                        break
                    if resp not in listresp2: 
                        print("Tente novamente, você digitou errado!")
            

            if resp not in listresp: 
                print("Tente novamente, você digitou errado!")
    if len(team) == 1:
        break
print(emoji.emojize("Prof Paul:man_raising_hand:: Espere, eu ainda tenho mais uma coisa para lhe dar\nReceba isso:"))
time.sleep(2)
print("\nVocê recebeu 100 pokebolas!")
pb = 100
bag = [f"pokebola x{pb}"]
time.sleep(1)
print(emoji.emojize("Prof Paul:man_raising_hand:: Agora você pode seguir sua jornada para a rota 1!"))
time.sleep(1)
print(emoji.emojize("\nSaindo do laboratório :left_arrow:\n"))

while True:
    time.sleep(1)
    print("------------------------------------------------------")
    print(emoji.emojize(f"\nLocal:triangular_flag: = {Local1[2]}  | Time Pokemon :red_circle: = {team}"))
    print("\n------------------------------------------------------\n")
    time.sleep(1)
    print(f"OPÇÕES:\nB: Mochila | P: Ver/editar Seu Time | Y: Você | D: Para mexer na box |\n\nOu Escolha um dos Locais Abaixo para ir\nLocais > V: Para voltar Para {Local2[0]} | K: P/ ir para {Local2[1]} | L: P/ ir ao {Local2[2]} | R: P/ ir à {Local2[3]} ")
    time.sleep(1)
    resp = input("\nEscolha o que fazer:")

    
    if resp == "Y" or resp == "y":
        print(you)
        time.sleep(1)
    if resp == "B" or resp == "b":
        for x, e in enumerate(bag):
            print(emoji.emojize(f"\nMochila :backpack: :\n[{x+1}] {e}"))
        time.sleep(1)
    if resp =="P" or resp == "p":
        print("\nSelecione 'V' para Ver e 'E' para editar:")
        z = input("Insira sua escolha: ")
        if z == "V" or z == "v":
            print(emoji.emojize(f"\nTime pokemon: :\n")) 
                
            for x, e in enumerate(team):
                print(f"[{x+1}] {e}")
            time.sleep(1)
        if z == "E" or z == "e":
            for x, e in enumerate(team):
                print(f"[{x+1}] {e}") 
            while True:
                f = int(input("\nSelecione o número de um pokemon(0 p/sair):"))
                if f == 0:
                    break
                print(f"\nVocê selecionou {team[f-1]}")
                print("\nOPÇÕES:\n'B' Para colocar na Box\n'A' para abandona-lo\n'S' p/ sair\n" )
                esc = input("insira sua escolha:")
                if esc == "B" or esc == "b":
                    operação = team.pop(f-1)
                    box.append(operação)
                    print(f"\nSeu time:{team}\n")
                    print(f"\nSua box:{box}\n")
                    break
                if esc == "A" or esc == "a":
                    print(f"Adeus! {team[f-1]}")
                    del team[f-1]
                    break
                if esc == "S" or esc == "s":
                    print("Desligando!")
                    break               
                       
    if resp =="A" or resp == "a":
        print(emoji.emojize("\nVocê está saindo de casa:right_arrow:!\n"))
        x += 1
        time.sleep(1)
        break
    if resp == "K" or resp == "k":

        print(emoji.emojize("\nVocê está entrando na casa de Kauã:right_arrow:!\n"))
        time.sleep(1)
        print("------------------------------------------------------")
        print(emoji.emojize(f"\nLocal:triangular_flag: = {Local2[1]}  | Time Pokemon :red_circle: = {team}"))
        print("\n------------------------------------------------------\n")
        while True:
            figs = [emoji.emojize("Júlio :man_beard:"), emoji.emojize("Guilherme :child:"), emoji.emojize("Kauã :child:"), emoji.emojize("Gabriel :boy:"), emoji.emojize("Crispim :child:"), emoji.emojize("Suquin :man_bald:"), emoji.emojize("Luan :man_blond_hair:")]  
            print("\nOPÇÕES:\nB: Mochila | P: Ver Seu Time | Y: Você | A: Sair da Casa\n\nOu Fale com os NpC's\nNPC'S > 'J' falar com Júlio | 'G'p/ falar com Guilherme | 'K' falar com Kauã | 'H' falar com Gabriel | 'C' falar com Crispim | 'S' falar com Suquin | 'L'falar com Luan")
            time.sleep(0.5)
            resp3 = input("\nEscolha o que fazer:") 
            listresp3 = ["A", "a", "B", "b", "P", "p", "Y", "y", "J","j","K","k","G","g","H","h","L","l","S","s","C","c"]    
            if resp3 not in listresp3: 
                print("Tente novamente, você digitou errado!")
            if resp3 == "Y" or resp3 == "y":
                print(you)
                time.sleep(1)
            if resp3 == "B" or resp3 == "b":
                for x, e in enumerate(bag):
                    print(emoji.emojize(f"\nMochila :backpack: :\n[{x+1}] {e}"))
                    time.sleep(1)
            if resp3 =="P" or resp3 == "p":
                print(emoji.emojize(f"\nTime pokemon: :\n")) 
                for x, e in enumerate(team):
                    print(f"")
                time.sleep(1)                  
            if resp3 =="A" or resp3 == "a":
                print(emoji.emojize("\nVocê está saindo da casa de Kauã:left_arrow:!\n"))
                time.sleep(1)
                print("------------------------------------------------------")
                print(emoji.emojize(f"\nLocal:triangular_flag: = {Local1[2]}  | Time Pokemon {team}"))
                print("\n------------------------------------------------------\n")
                break
            if resp3 =="J" or resp3 == "j":
                print()
                print(f"{figs[0]}: 'Inscrevam-se no Canal Júlio Tech'")
                time.sleep(1.3)
            if resp3 =="G" or resp3 == "g":
                print()
                print(f"{figs[1]}: 'Eu ia ser Jogador de Futebol, mas torci o tornozelo '")
                time.sleep(1.3)
            if resp3 =="K" or resp3 == "k":
                print()
                print(f"{figs[2]}: 'Digamos que minha bebida favorita é tampico'")
                time.sleep(1.3)
            if resp3 =="H" or resp3 == "h":
                print()
                print(f"{figs[3]}: 'Eu quero ser um mestre pokemon igual o Campeão MessiMon'")
                time.sleep(1.3)
            if resp3 =="C" or resp3 == "c":
                print()
                print(f"{figs[4]}: 'Ah! Estação...'")
                time.sleep(1.3)
            if resp3 == "S" or resp3 == "s":
                print()
                print(f"{figs[5]}: 'kkkkkkkkkkkkkkkkkkkk'")
                time.sleep(1.3)
            if resp3 == "L" or resp3 == "l":
                print()
                print(f"{figs[6]}: 'Vou trabalhar, pq se depender do flamengo...'")
                time.sleep(1.3)
        if resp == "A" or resp == "a":
        
            print(emoji.emojize("\nVocê está entrando em casa! :left_arrow: "))
            time.sleep(1)
            while True:
                c = 0
                print("\nOPÇÕES:\nB: Mochila | P: Ver Seu Time | Y: Você | A: Sair de Casa | V: Voltar para o Quarto")
                time.sleep(0.5)
                resp = input("\nEscolha o que fazer:") 
                listresp = ["A", "a", "B", "b", "P", "p", "Y", "y", "V", "v"]
                if resp == "Y" or resp == "y":
                    print(you)
                    time.sleep(1)
                
                if resp == "V" or resp == "v":
        
                    print(emoji.emojize("\nVocê está subindo as escadas!:up_arrow:"))
                    time.sleep(1)
                    while True:

                        print("\nOPÇÕES:\nB: Mochila | P: Ver Seu Time | Y: Você | A: Ir para outro cômodo")
                        time.sleep(0.5)
                        resp = input("\nEscolha o que fazer:") 
                        listresp2 = ["A", "a", "B", "b", "P", "p", "Y", "y"]
                        if resp == "Y" or resp == "y":
                            print(you)
                            time.sleep(1)
                        if resp == "B" or resp == "b":
                            for x, e in enumerate(bag):
                                print(emoji.emojize(f"\nMochila :backpack: :\n[{x+1}] {e}"))
                            time.sleep(1)
                        if resp =="P" or resp == "p":
                            for x, e in enumerate(bag):
                                print(emoji.emojize(f"\nMochila :backpack: :\n[{x+1}] {e}"))
                            time.sleep(1)
                        if resp =="A" or resp == "a":
                            print(emoji.emojize("\nVocê está descendo as escadas! :down_arrow:\n"))
                            x == 2
                            time.sleep(1)
                            break
                        if resp not in listresp2: 
                            print("Tente novamente, você digitou errado!")


                if resp == "B" or resp == "b":
                    for x, e in enumerate(bag):
                        print(emoji.emojize(f"\nMochila :backpack: :\n[{x+1}] {e}"))
                    time.sleep(1)
                if resp =="P" or resp == "p":
                    for x, e in enumerate(bag):
                        print(emoji.emojize(f"\nMochila :backpack: :\n[{x+1}] {e}"))
                        time.sleep(1)
                if resp =="A" or resp == "a":
                    print(emoji.emojize("\nVocê está saindo de casa:right_arrow:!\n"))
                    time.sleep(1)
                    print("------------------------------------------------------")
                    print(emoji.emojize(f"\nLocal:triangular_flag: = {Local1[2]}  | Time Pokemon :red_circle: = [Nenhum Pokemon]"))
                    print("\n------------------------------------------------------\n")
                    time.sleep(1)                        
                    time.sleep(1)
                    break
    if resp == "L" or resp == "l":
        time.sleep(1)
        print("Laboratório fechado! :cross_mark:")
        time.sleep(1)

    if resp =="D" or resp == "d":
        if len(box) >= 1:
            print("\nSelecione 'V' para Ver e 'E' para editar:")
            z = input("Insira sua escolha: ")
            if z == "V" or z == "v":
                print(emoji.emojize(f"\nBox pokemon: :\n")) 
                    
                for x, e in enumerate(box):
                    print(f"[{x+1}] {e}")
                    time.sleep(1)

            if z == "E" or z == "e":
                for x, e in enumerate(box):
                    print(f"[{x+1}] {e}") 
                if len("box") > 1:
                    while True:
                        f = int(input("\nSelecione o número de um pokemon(0 p/sair):"))
                        if f == 0:
                            break
                        print(f"Você selecionou {box[f-1]}")
                        print("\nOPÇÕES:\n'T' Para colocar no time\n'A' para abandona-lo\n'S' p/ sair\n" )
                        esc = input("insira sua escolha:")
                        
                        
                        if len(team) == 6:
                            print("\nprimeiramente remova um pokemon do seu time!\n")
                            break
                        
                        
                        if esc == "T" or esc == "t" and len(team) < 6:
                            operação = box.pop(f-1)
                            team.append(operação)
                            print(f"\nSeu time:{team}")
                            print(f"\nSua box:{box}\n")
                            break

                        if esc == "A" or esc == "a":
                            print(f"Adeus! {box[f-1]}")
                            del box[f-1]
                            break
                        if esc == "S" or esc == "s":
                            print("Desligando!")
                            break
        else:
            print(emoji.emojize("\nvocê não tem pokemon na box! :cross_mark:\n"))          


    if resp == "R" or resp == "r":
        print(emoji.emojize("Entrando na rota 01 :right_arrow:"))
        resprot = 0

            
        time.sleep(1)
        print("------------------------------------------------------")
        print(emoji.emojize(f"\nLocal:triangular_flag: = {Local2[3]}  | Time Pokemon : {team}"))
        print("\n------------------------------------------------------\n")
        time.sleep(1)
        
        while True:

            print(f"OPÇÕES:\nB: Mochila | T: Ver/editar Seu Time | Y: Você | P: Para procurar pokemon | D: para mexer na box |\n\nOu aperte 'V' para voltar para a cidade")
            time.sleep(1)
            listresprot = ["A", "a", "B", "b", "P", "p", "Y", "y", "V", "v", "T","t", "D","d"]
            resprot = input("\nInsira sua escolha:")
            if resprot not in listresprot: 
                print("Tente novamente, você digitou errado!")
            if resprot == "V" or resprot == "v":
                print("voltando para a cidade")
                time.sleep(1)
                break
            if resprot == "Y" or resprot == "y":
                print(you)
                time.sleep(1)
            if resprot == "B" or resprot == "b":
                for x, e in enumerate(bag):
                    print(emoji.emojize(f"\nMochila :backpack: :\n[{x+1}] {e}"))
                time.sleep(1)
            if resprot =="T" or resprot == "t":
                print("\nSelecione 'V' para Ver e 'E' para editar:")
                z = input("Insira sua escolha: ")
                if z == "V" or z == "v":
                    print(emoji.emojize(f"\nTime pokemon: :\n")) 
                
                    for x, e in enumerate(team):
                        print(f"[{x+1}] {e}")
                    time.sleep(1)
                if z == "E" or z == "e":
                    for x, e in enumerate(team):
                        print(f"[{x+1}] {e}") 
                    while True:
                        f = int(input("\nSelecione o número de um pokemon(0 p/sair):"))
                        if f == 0:
                            break
                        print(f"\nVocê selecionou {team[f-1]}")
                        print("\nOPÇÕES:\n'B' Para colocar na Box\n'A' para abandona-lo\n'S' p/ sair\n" )
                        esc = input("insira sua escolha:")
                        if esc == "B" or esc == "b":
                            operação = team.pop(f-1)
                            box.append(operação)
                            print(f"\nSeu time:{team}\n")
                            print(f"\nSua box:{box}\n")
                            break
                        if esc == "A" or esc == "a":
                            print(f"Adeus! {team[f-1]}")
                            del team[f-1]
                            break
                        if esc == "S" or esc == "s":
                            print("Desligando!")
                            break



            if resprot =="D" or resprot == "d":
                if len(box) >= 1:
                    print("\nSelecione 'V' para Ver e 'E' para editar:")
                    z = input("Insira sua escolha: ")
                    if z == "V" or z == "v":
                        print(emoji.emojize(f"\nBox pokemon: :\n")) 
                    
                        for x, e in enumerate(box):
                            print(f"[{x+1}] {e}")
                        time.sleep(1)
                    if z == "E" or z == "e":
                        print("BOX:")
                        for x, e in enumerate(box):
                            print(f"[{x+1}] {e}") 
                        if len("box") > 1:

                            while True:
                                f = int(input("\nSelecione o número de um pokemon(0 p/sair):"))
                                if f == 0:
                                    break
                                print(f"Você selecionou {box[f-1]}")
                                print("\nOPÇÕES:\n'T' Para colocar no time\n'A' para abandona-lo\n'S' p/ sair\n" )
                                esc = input("insira sua escolha:")
                                if len(team) == 6:
                                    print("\nprimeiramente remova um pokemon do seu time!\n")
                                    break
                                if esc == "T" or esc == "t" and len(team) < 6:
                                
                                    operação = box.pop(f-1)
                                    team.append(operação)
                                    print(f"\nSeu time:{team}")
                                    print(f"\nSua box:{box}\n")
                                    break

                                if esc == "A" or esc == "a":
                                    print(f"Adeus! {box[f-1]}")
                                    del box[f-1]
                                    break
                                if esc == "S" or esc == "s":
                                    print("Desligando!")
                                    break
                else:
                    print(emoji.emojize("\nvocê não teCLEm pokemon na box! :cross_mark:\n"))                



            if resprot == "P" or resprot == "p":
                while True:    
                    capt = [R"ERRO", "GOTCHA", "GOTCHA", "GOTCHA", "ERRO"]
                    a = random.randint(0, 21)
                    time.sleep(0.5)
                    print(f"Um {grama_alta[a]} apareceu!!!!!\n")
                    time.sleep(0.5)
                    print(f"OPÇÕES:\nC: Capturar | F: Fugir\n")
                    time.sleep(0.5)
                    resp3 = input("Insira sua escolha:")
                        
                    if resp3 == "C" or resp3 == "c":
                        N = random.choice(capt)
                        if N == "GOTCHA":
                            if len(team) < 6:
                                time.sleep(1)
                                print(".")
                                time.sleep(1)
                                print(".")
                                time.sleep(1)
                                print(".")
                                print(emoji.emojize(":check_mark:\n"))
                                print(f"Gotcha! Você pegou um {grama_alta[a]}!")
                                time.sleep(1)
                                team.append(grama_alta[a])
                                print(f"Time: {team}")
                                pb -= 1
                                bag = [f"pokebola x{pb}"]
                                break

                            if len(team) == 6:
                                time.sleep(1)
                                print(".")
                                time.sleep(1)
                                print(".")
                                time.sleep(1)
                                print(".")
                                print(emoji.emojize(":check_mark:\n"))
                                print(f"Gotcha! Você pegou um {grama_alta[a]}!")
                                print(f"\nMas como seu time está cheio o {grama_alta[a]} irá ser transportado para sua BOX")
                                time.sleep(1)
                                box.append(grama_alta[a])
                                print(f"BOX: {box}")
                                pb -= 1
                                bag = [f"pokebola x{pb}"]
                                break
                        if N == "ERRO":
                            time.sleep(1)
                            print(".")
                            time.sleep(1)
                            print(".")
                            time.sleep(1)
                            print(".")
                            print(emoji.emojize(":cross_mark:\n"))
                            print("ahh, você NÃO pegou!")
                            time.sleep(1)
                            pb -= 1
                            bag = [f"pokebola x{pb}"]
                            break
                    if resp3 == "F" or "f": 
                        print("\nVocê fugiu!\n")
                        break            
                    else: 
                        print("inválido, tente novamente")
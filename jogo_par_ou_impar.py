from random import randint
from time import sleep
maquina_escolha = " "
contador_vitorias = 0
while True:
	usuario_escolha = " "	
	sleep(0.5)
	while usuario_escolha not in "PIÍ":
		usuario_escolha = str(input("Par ou Ímpar ?\nDigite aqui: ")).upper().strip()[0]		
		sleep(0.5)	
  	        print("~" * 30)
	if usuario_escolha == "P":
		maquina_escolha = "I"
	elif usuario_escolha in "IÍ":
		maquina_escolha = "P"
	sleep(0.5)
	usuario_numero = int(input("Digite um número: "))
	maquina_numero = randint(1, 15)
	soma = usuario_numero + maquina_numero
	sleep(0.5)
	print("~" * 30)
	print("PROCESSANDO...")
	sleep(2)
	print("~" * 30)
	if soma % 2 == 0 and usuario_escolha == "P" or soma % 2 != 0 and usuario_escolha in "IÍ":
		print("Você ganhou. Parabéns.")	
		contador_vitorias += 1
	else:
		print("Você perdeu. :(")
		break
	sleep(0.5)
	continuar = " "
	while continuar not in "SN":
		continuar = str(input("Deseja continuar ?\nDigite aqui: ")).upper().strip()[0]
		print("~" * 30)
		if continuar == "N":	
			break
sleep(0.5)
print()
print(f"A máquina escolheu o número {maquina_numero}, a soma de ambos resulta em {soma}.")
sleep(0.5)
print("~" * 30)
if contador_vitorias == 1:	
	print("Você ganhou uma vez.")
else:
	print(f"Você ganhou {contador_vitorias} vezes consecutivas.")
sleep(0.5)
print("~" * 30)

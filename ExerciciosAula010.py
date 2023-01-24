#Descobrir o número aleatório
from random import randint as rd
pc = rd(0,5)
usuario = int(input('Advinhe o número que o computador escolheu! '))
if usuario == pc:
    print('Você acertou!!! O número escolhido foi {}'.format(pc))
else:
    print('Você errou!!! O número escolhido foi {} e você chutou o número {}'.format(pc,usuario))


#Caso a velocidade ultrapasse 80km, o motorista receberá uma multa, a multa é R$7 a cada 1Km ultrapassado.
vel = int(input('Qual a velocidade do carro? '))
if vel > 80:
    multa = 7 * (vel - 80)
    print('>>>>> VOCÊ FOI MULTADO! <<<<<')
    print('O limite de velocidade é de 80Km/h e você ultrapassou com {}Km/h,'.format(vel),'{}Km/h a mais que o permitido'.format(vel-80))
    print('A multa é de R${}'.format(multa))
else:
    print('Você não foi multado. Sua velocidade estava abaixo de 80Km/h e era de {}Km/h'.format(vel))


#Representar se o número é par ou impar
numero = int(input('Digite um número: '))
x = numero % 2
if x == 0:
    print('O número é par')
else:
    print('O número é impar')

#Caso a distância da passagem ultrapasse 200Km, o preço será R$0,50 vezes a distância da passagem, senão, será R$0,45
passagem = int(input('Digite a distância da viagem: '))
if passagem <= 200:
    preco = 0.5 * passagem
    print('O valor ficaria R${:.2f} por {}Km'.format(preco, passagem))
else:
    preco = 0.45 * passagem
    print('O valor ficaria R${:.2f} por {}Km'.format(preco, passagem))
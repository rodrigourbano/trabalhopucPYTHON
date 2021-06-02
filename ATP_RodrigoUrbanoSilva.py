from datetime import date
from time import sleep
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m'   }

#ETAPA 1 E 2
def obter_limite():
        
    cargo = str(input('Qual cargo você ocupa na empresa que trabalha? '))
    salario = input('Qual é o seu salário atual? R$')

    # VERIFICAÇÃO SE SALARIO É FLOAT 
    while salario.isalpha() == True:
        salario = input('Digite seu salário em númeral! Ex: 1000.00.\nPor favor, informe o seu salário atual? R$')
    salario = float(salario)
    while salario <= 0:
        salario = input('Seu salário não pode ser igual ou menor que R$0,00. Por favor, informe o seu salário atual? R$')
        while salario.isalpha() == True:
            salario = input('Digite seu salário em númeral! Ex: 1000.00.\nPor favor, informe o seu salário atual? R$')
        salario = float(salario)

    anonasc = int(input('Em que ano você nasceu? '))
    
    # VERIFICAÇÃO SE ANO DE NASCIMENTO É MAIOR QUE 0 E MENOR QUE ANO ATUAL!

    while anonasc <= 0 or anonasc > date.today().year:
        if anonasc <= 0:
            anonasc = int(input('Não aceitamos números abaixo de 0. Em que ano você nasceu? '))
        if anonasc > date.today().year:
            anonasc = int(input('Não aceitamos viajantes do tempo!. Insira um ano de nascimento válido! Em que ano você nasceu? '))

    idade = date.today().year - anonasc

    print('-='*30)
    print('CARGO: {}{}{}'.format(cores['azul'], cargo, cores['limpa']))
    print('SALÁRIO: R${}{:.2f}{}'.format(cores['azul'], salario, cores['limpa']))
    print('ANO DE NASCIMENTO: {}{}{} '.format(cores['azul'], anonasc, cores['limpa']))
    print('-='*30)

    
    print('Sua idade atual aproximada é {} anos'.format(idade))

    
    gasto_permitido = salario * (idade / 1000) + 100
    print('Estamos realizando sua análise de crédito! Aguarde...')
    
    sleep(1.5)

    return gasto_permitido, idade

#ETAPA 3

def verificar_produto(valor):
    
    if valor <= limite * 0.6:
        print('Liberado!')
    elif valor > limite * 0.6 and valor <= limite * 0.9:
        print('Liberado ao parcelar em até 2x')
    elif valor > limite * 0.9 and valor < limite:
        print('Liberado ao parcelar em 3 ou mais vezes')
    elif valor >= limite:
        print('Bloqueado!')

    #DESCONTO ESPECIAL
    nome_completo = 'Rodrigo Urbano Silva'
    nome_short = 'Rodrigo'
    desconto_nome = 1

    if len(nome_completo) <= price <= idade or idade <= price <= len(nome_completo):
        desconto_nome = len(nome_short) / 100
        new_price = price * (1 - desconto_nome )
        print('Novo preço com desconto de {:.0f}% será de R${:.2f}'.format(desconto_nome*100, new_price))
    else:
        new_price = price
        print('Seguindo...')
    
    return desconto_nome
    

######################################################################################################################
print('-=' * 42)
print('\tBem-vindo à Loja do Urahara! Aqui quem fala é o Rodrigo Urbano Silva!')
print('-=' * 42)
print('Primeiramente iremos realizar uma análise de crédito, para isso vamos pedir alguns dados')

limite, idade = obter_limite()
print('Segundo a nossa análise de crédito, O(a) sr(a) poderá gastar ate R${}{:.2f}{} na nossa loja!'.format(cores['azul'], limite, cores['limpa']))   
print('-='*30)



nome_completo = 'Rodrigo Urbano Silva'

while True:
    valor = 0
    n = input('Quantos produtos deseja cadastrar? ')
    while n.isnumeric() == False:
        n = input('Quantos produtos deseja cadastrar? Somente números ')
    n = int(n)
    for x in range(n):
        produto = str(input('Digite o nome do produto que deseja comprar: '))
        price = input('Agora digite o preço do produto: R$')
        while price.isalpha() == True:
            price = input('Digite o preço do produto usando apenas números. R$')
        price = float(price)
        valor += price
        desconto_esp = verificar_produto(valor)
        if len(nome_completo) <= price <= idade or idade <= price <= len(nome_completo):
            valor = valor - (price * desconto_esp)
        lim_sobra = limite - valor
        if lim_sobra > 0:
            print('Você ainda tem R${:.2f} para gastar na loja!'.format(lim_sobra))
        if lim_sobra == 0:
            print('Você atingiu o limite de gasto!')
        if lim_sobra <= 0:
            print('Infelizmente você estourou o limite de gasto em R${:.2f}'.format(lim_sobra * -1))
        print(f'Valor total da compra: R${valor:.2f}')
        print('-='*20)
    option = str(input('Deseja iniciar uma nova compra do zero? [S/N] ')).upper().strip()[0]
    while option not in 'SN':
        option = str(input('Escolha entre [S/N] ')).upper().strip()[0]
    if option == 'N':
        break
    else: 
        print('Limpando seu carrinho...')
        sleep(0.5)
        print('Pronto! Vamos iniciar a sua nova compra!')
        print('-='*20)
        

print('OBRIGADO E VOLTE SEMPRE!')
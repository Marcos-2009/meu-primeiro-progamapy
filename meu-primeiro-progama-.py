def hello():
  print('Hello World!')

def saudacao():
  resposta = input('Qual seu nome? ')
  print('Olá, ' + resposta)

def soma2valores():
  soma = 0
  valor1 = int(input('Digite um valor: '))
  valor2 = int(input('Digite outro valor: '))
  soma = valor1 + valor2
  print('A soma é: %d', %soma)
  testa50(soma)

def soma5valores():
  soma = 0
  for i in range(5):
    resposta = int(input('Digite um valor: '))
    soma = soma + resposta
    print('A soma é: %d', %soma)
    testa50(soma)

def testa50(soma):
  if (soma > 50):
    print('%d é maior que 50' %soma)
  elif (soma < 50):
    print('%d é menor que 50' %soma)
  else:
    print('%d é igual a 50' %soma)
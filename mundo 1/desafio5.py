escrito = input('Digite algo: ')

print('O tipo primitivo é ', type(escrito))
print('O que foi escrito é um numero ? ', escrito.isnumeric())
print('O que foi escrito é uma string ? ', escrito.isalpha())
print('O foi digitado é somente espaço ? ', escrito.isspace())
print('É alfabético ? ', escrito.isalpha())
print('É alfanumerico ? ', escrito.isalnum())
print('É maiúscula ? ', escrito.isupper())
print('É minuscula ? ', escrito.islower())
print('Esta capitalizada ? ', escrito.istitle()) #nem maiscula nem minuscula
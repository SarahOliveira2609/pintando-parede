#Faça um programa que leia a largura e a altura de uma parde em metros, calcule a sua área e a quantidade de tinta necessária para cada litro de tinta, pinta uma área de 2m2

l = float(input('Digite a largura:'))
a = float(input('Digite a altura:'))
p = l * a

print(f'A área da sua parede é {p}')

t = p/2

print(f'Você irá precisa de {t} litros de tinta para pintar sua parede')
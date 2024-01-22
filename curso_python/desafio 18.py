from math import radians, cos, sin, tan
ang = int(input('Digite o ângulo : '))
radians = radians(ang)
seno = sin(radians)
cosseno = cos(radians)
tang = tan(radians)
print('Considerando o ângulo de {:.0f}°,o seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(ang, seno, cosseno, tang))

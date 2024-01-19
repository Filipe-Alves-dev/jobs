larg = float(input('Digite a largura da parede : '))
alt = float(input('Digite a altura da parede : '))
area = larg * alt
litro = area / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².\nPara pintar essa area você irá gastar {:.1f}L de tinta .'.format(larg, alt, area, litro))

    


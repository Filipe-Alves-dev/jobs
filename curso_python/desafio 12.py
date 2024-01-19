preco = float(input('Digite o preço do produto para saber o valor do desconto : '))
desconto = preco - (preco / 100 * 5)
print('O preço deste produto com desconto de 5% é : {}$ .'.format(desconto))
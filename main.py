from api import cpf, cnpj, rg, cep_consulta

print("""
1- Gerador de CPF
2- Gerador de CNPJ
3- Gerador de RG
4- Consulta CEP
	""")

menu = int(input('Digite uma opção: '))

if menu == 1:
	quant = int(input('Quantidade de CPF: '))
	uf = input('Estado: ')
	resposta = cpf(quant, uf)

elif menu == 2:
	quant = int(input('Quantidade de CNPJ: '))
	resposta = cnpj(quant)

elif menu == 3:
	quant = int(input('Quantidade de RG: '))
	resposta = rg(quant)

elif menu == 4:
	cep_entrada = input('Digite o CEP:')
	resposta = cep_consulta(cep_entrada)

else:
	print('Digite um valor válido: ')
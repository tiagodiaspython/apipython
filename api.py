from requests import post, get


def cpf(quant, uf):
	for i in range(0, quant):
		req = post('https://www.4devs.com.br/ferramentas_online.php', {'acao':'gerar_cpf', 'pontuacao':'S', 'cpf_estado':uf})
		resposta = req.text
		print(resposta)


def cnpj(quant):
	for i in range(0, quant):
		req = post('https://www.4devs.com.br/ferramentas_online.php', {'acao':'gerar_cnpj', 'pontuacao':'S'})
		resposta = req.text
		print(resposta)

def rg(quant):
	for i in range(0, quant):
		req = post('https://www.4devs.com.br/ferramentas_online.php', {'acao':'gerar_rg', 'pontuacao':'S'})
		resposta = req.text
		print(resposta)

def cep_consulta(cep):
	req = get('https://viacep.com.br/ws/{}/json/'.format(cep))
	resposta = req.json()
	if 'erro' in resposta:
		print('CEP INVALIDO')
		exit()
	else:
		print(f'CEP: {resposta["cep"]}')
		print(f'Logradouro: {resposta["logradouro"]}')
		print(f'Complemento: {resposta["complemento"]}')
		print(f'Bairro: {resposta["bairro"]}')
		print(f'Estado: {resposta["uf"]}')


	
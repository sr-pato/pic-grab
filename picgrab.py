import requests
from bs4 import BeautifulSoup as bs
from os import system as cmd
from time import sleep as sonin


def clear():
    cmd('cls||clear')
clear()

url = 'https://pic.obmep.org.br/login?action=login'

data_login = {}

def obter_dados(data_login):
    data_login['login'] = input('Digite seu usuário\n\n-> ')
    data_login['senha'] = input('Digite sua senha\n\n-> ')
    clear()
    sessao()

def sessao():
    print('[#] Tentando fazer login...')
    pic = requests.Session()
    r = pic.post(url, data=data_login)
    soup = bs(r.text, 'html.parser')
    try:
        soup.find('div', {'class':'navbar-brand'}).text
    except:
        print('[#] Falha no login')
        obter_dados(data_login)
    else:
        print('[#] Logado com sucesso')
        tabela(pic)

def tabela(pic):
    print('\n\nTabela de Ações\n\n1. Informações Pessoais\n2. Informações sobre Responsáveis\n3. Dados de Contato e Endereço\n4. Dados Bancários')
    resp = input('\n\n-> ')
    try:
        resp = int(resp)
    except:
        print('Por favor, informe uma resposta com valor inteiro')
        tabela(pic)
    if resp == 1:
        acao_1(pic)
    elif resp == 2:
        acao_2(pic)
    elif resp == 3:
        acao_3(pic)
    elif resp == 4:
        acao_4(pic)
    else:
        print('Insira uma opção entre 1 e 5')
        tabela(pic)

def acao_1(pic):
    dados = {}
    print('Buscando informações pessoais')
    r = pic.get('https://pic.obmep.org.br/aluno/confirmar/resumo')
    page = bs(r.text, 'html.parser')
    dados['nome'] = page.find('div', {'class':'col-md-10'}).find('h3').text.title()
    dados['cpf'] = page.find_all('p', {'class':'form-control-static'})[0].text.strip()
    dados['nascimento'] = page.find_all('p', {'class':'form-control-static'})[1].text.strip()
    dados['sexo'] = page.find_all('p', {'class':'form-control-static'})[2].text.strip()
    dados['nacionalidade'] = page.find_all('p', {'class':'form-control-static'})[3].text.strip()
    dados['RG'] = page.find_all('p', {'class':'form-control-static'})[4].text.strip()
    dados['emissao'] = page.find_all('p', {'class':'form-control-static'})[5].text.strip()
    dados['lattes'] = page.find_all('p', {'class':'form-control-static'})[6].text.strip()
    clear()
    print(f'''Informações Pessoais

Nome: {dados['nome']}
Data de Nascimento: {dados['nascimento']}
Sexo: {dados['sexo']}
Nacionalidade: {dados['nacionalidade']}
CPF: {dados['cpf']}
RG: {dados['RG']}
Emissão: {dados['emissao']}
Link Currículo Lattes: {dados['lattes']}''')
    tabela(pic)

def acao_2(pic):
    dados = {}
    print('[#] Buscando informações sobre os Responsáveis...')
    r = pic.get('https://pic.obmep.org.br/aluno/confirmar/resumo')
    page = bs(r.text, 'html.parser')
    dados['nome_mae'] = page.find_all('p', {'class':"form-control-static"})[7].text.strip()
    dados['cpf_mae'] = page.find_all('p', {'class':"form-control-static"})[8].text.strip()
    dados['nome_pai'] = page.find_all('p', {'class':"form-control-static"})[9].text.strip()
    dados['cpf_pai'] = page.find_all('p', {'class':"form-control-static"})[10].text.strip()
    dados['email_resp'] = page.find_all('p', {'class':"form-control-static"})[11].text.strip()
    clear()
    print(f'''[#] Informações Encontradas!
Nome da Mãe: {dados['nome_mae']}
CPF da Mãe: {dados['cpf_mae']}
Nome do Pai: {dados['nome_pai']}
CPF do Pai: {dados['cpf_pai']}
Email do Responsável: {dados['email_resp']}''')
    tabela(pic)

def acao_3(pic):
    dados = {}
    print('[#] Buscando dados de Contato...')
    r = pic.get('https://pic.obmep.org.br/aluno/confirmar/resumo')
    page = bs(r.text, 'html.parser')
    dados['email_resp'] = page.find_all('p', {'class':"form-control-static"})[11].text.strip()
    dados['email_aluno'] = page.find_all('p', {'class':"form-control-static"})[12].text.strip()
    dados['numeros_trash'] = page.find_all('p', {'class':"form-control-static"})[13].text.strip().split('\n')
    dados['numeros'] = []
    
    for i in dados['numeros_trash']:
        i = i.strip()
        dados['numeros'].append(i)
    
    dados['numeros'] = ' | '.join(dados['numeros'])
    
    dados['endereco_trash'] = page.find_all('p', {'class':"form-control-static"})[14].text.strip().split('\n')
    dados['endereco'] = []
    for i in dados['endereco_trash']:
        i = i.strip()
        dados['endereco'].append(i)
    dados['endereco'] = ', '.join(dados['endereco']).title()    
    clear()
    print(f'''Informações de Contato

Email do Responsável: {dados['email_resp']}
Email do Aluno: {dados['email_aluno']}
Números: {dados['numeros']}
Endereço: {dados['endereco']}''')
    tabela(pic)

def acao_4(pic):
    clear()
    dados = {}
    print('[#] Buscando Informação de Dados Bancários...')
    page = pic.get('https://pic.obmep.org.br/aluno/confirmar/resumo')
    page = bs(page.text, 'html.parser')
    dados['banco'] = page.find_all('p', {'class':"form-control-static"})[19].text.strip().title()
    dados['agencia'] = page.find_all('p', {'class':"form-control-static"})[20].text.strip()
    dados['tipo_conta'] = page.find_all('p', {'class':"form-control-static"})[21].text.strip()
    print(f'''Informações de Banco

Banco: {dados['banco']}
Nº Agência: {dados['agencia']}
Tipo de Conta: {dados['tipo_conta']}''')
    tabela(pic)
   
    

obter_dados(data_login)
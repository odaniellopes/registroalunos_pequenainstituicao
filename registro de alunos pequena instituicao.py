#Objetivo: criar um progama que registra e persistir (inserir) e ler os dados de notas de alunos em arquivos.
'''
Aluno: Daniel Lopes da Costa // matrícula: 202108093785
Estácio maracanã noite
'''
import time

#painel de acesso
usuario = 'Insira o que você deseja fazer.'
usuario+= '\n1- "cadastrar" para cadastrar um novo aluno.'
usuario+= '\n2- "listar" para listar alunos cadastrados.'
usuario+='\n3- "buscar" para buscar o nome de um aluno.'
print(usuario)
entrada = input('Insira a operação desejada: ').upper().strip()
print('\n')



#funcionamento do código
def cadastrar_alunos():
    nome_aluno = str(input('Insira o nome completo do aluno: ')).upper()
    email_aluno = str(input('Insira o email do aluno: ')).upper()

    #validando email
    padrao = '@' and '.'
    if padrao in email_aluno:
        curso_aluno = str(input('Insira o curso do aluno: ')).upper()

        #verificando se já existe ou cadastrando novo
        arquivo = open('registroalunos.txt', 'a')
        arquivo.close()

        with open('registroalunos.txt') as f:
            if nome_aluno in f.read():
                print(f"Ops! {nome_aluno} já está cadastrado!")

            else:
                arquivo = open('registroalunos.txt', 'a')
                arquivo.write(
                    'NOME DO ALUNO:' + ' ' + nome_aluno + ' \n' + 'EMAIL:' + ' ' + email_aluno + ' \n' + 'CURSO:' + ' ' + curso_aluno + '\n\n')
                arquivo.close()
                print('Aluno cadastrado coom sucesso!')

    else:
        print('\n')
        print('\t \tEmail inválido. Tente novamente!')
        print('\n')
        cadastrar_alunos()

def listar_alunos():
    print('\n\t\t abrindo lista de alunos, aguarde...')
    time.sleep(2)

    arquivo = open('registroalunos.txt', 'r')
    linha = '.'
    while linha != '':
        linha= arquivo.readline()
        print(linha)

    print('\n\t\t Lista exibida com sucesso!')
    arquivo.close()


def buscar_alunos():
    nome_aluno = str(input('Insira o nome do aluno: ')).upper()
    arquivo = open('registroalunos.txt', 'r')
    arquivo.readline()
    arquivo.close()

    with open('registroalunos.txt') as f:
        if nome_aluno in f.read():
            print(f"{nome_aluno} Está cadastrado!")

        else:
            print('Este aluno não está cadastrado.')
            print('Deseja cadastra-lo?')
            cadastro = input('sim / não: ').upper().split()
            if cadastro == 'SIM':
                cadastrar_alunos()
            else:
                print('Fim do progama!')



#condições do painel de acesso
if entrada ==('CADASTRAR'):
    cadastrar_alunos()

elif entrada ==('LISTAR'):
    listar_alunos()

elif entrada ==('BUSCAR'):
    buscar_alunos()

else:
    print('Insíra o comando corretamete!')


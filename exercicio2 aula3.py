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



#funcionamento do código
def cadastrar_alunos():
    nome_aluno = str(input('Insira o nome completo do aluno: ')).upper()
    email_aluno = str(input('Insira o email do aluno: ')).upper()
    curso_aluno = str(input('Insira o curso do aluno: ')).upper()

    arquivo = open('registroalunos.txt', 'a')
    arquivo.write('NOME DO ALUNO:'+ ' ' +nome_aluno +' \n'+ 'EMAIL:'+ ' ' +email_aluno +' \n'+ 'CURSO:'+ ' ' +curso_aluno +'\n\n')

    arquivo.close()
    print('Aluno cadastrado coom sucesso!')


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



#condições do painel de acesso
if entrada ==('CADASTRAR'):
    cadastrar_alunos()

elif entrada ==('LISTAR'):
    listar_alunos()

elif entrada ==('BUSCAR'):
    buscar_alunos()

else:
    print('Insíra o comando corretamete!')

#fim da codificação.
#observações finais:
'''
Protótipo inicial de um registrador de alunos de uma pequena instituição, temporariamente sem interface gráfica.
Utilizei de um painel simples para pedir o que o usuário deseja fazer. O cadastro é guardado em um arquivo txt, mas a 
exibição da lista de alunos cadastrados é feita no terminal. Ao buscar um aluno pelo nome ele exibe o nome completo do
aluno e informa que ele está cadastrado.
Com as informações dada pelo usuário, foi possível projetar esse protótipo e entregar ao usuário e com sua opinião, 
podemos criar um novo protótipo 2.0 com interface gráfica, botões e uma forma mais adequada de busca exibindo as 
informações do usuário.
'''
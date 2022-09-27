#Objetivo: criar um progama que registra e persistir (inserir) e ler os dados de notas de alunos em arquivos .
#Foi pedido pelo usuário os seguintes requisitos nesta versão 2.0 do código:
'''
(A) Manipulações de Strings:
 (i) tratar entradas vazias, (ii) tratar nomes de alunos que contém números e (iii) tratar
número de matrículas com caracteres.
(B) Tratamento de exceções:
 (i) Tratar fechamento de arquivos que não foram abertos, (ii) tentar escrever em arquivos
com permissão para somente leitura, (iii) tentar ler dados de arquivos inexistentes
'''

#Informações do desenvolvedor
'''
Aluno: Daniel Lopes da Costa // matrícula: 202108093785
Estácio maracanã noite
'''

#painel de acesso
usuario = '''Insira o que você deseja fazer.
1- "cadastrar" para cadastrar um novo aluno.
2- "listar" para listar alunos cadastrados.
3- "buscar" para buscar o nome de um aluno.'''
print(usuario)
entrada = input('Insira a operação desejada: ').upper().strip()
print('\n')



#funcionamento do código
def cadastrar_alunos():
    nome_aluno = (input('Insira o nome completo do aluno: ')).upper().strip()
    email_aluno = (input('Insira o email do aluno: ')).upper().strip()
    matricula = (input('Insíra a matrícula do aluno: ')).strip()
    curso_aluno = (input('Insira o curso do aluno: ')).upper()

    #tratamento das entradas
    def check_nome(nome_aluno):
        nome_aluno = nome_aluno.replace(' ', '')
        if nome_aluno.isalpha() and nome_aluno.isascii():
            return True
        else:
            return False

    def check_email(email_aluno):
        if email_aluno.find('@') != -1 and email_aluno.find('.', email_aluno.find('@')) != -1:
            return True
        else:
            return False

    def check_curso(curso_aluno):
        curso_aluno = curso_aluno.replace(' ', '')
        if curso_aluno.isalpha() and curso_aluno.isascii():
            return True
        else:
            return False

    def check_matricula(matricula):
        matricula = matricula.replace(' ', '')
        if matricula.isnumeric() and matricula.isascii():
            return True
        else:
            return False

    check_nome(nome_aluno)
    check_email(email_aluno)
    check_matricula(matricula)
    check_curso(curso_aluno)

    if check_nome(nome_aluno) and check_email(email_aluno) and check_curso(curso_aluno) and check_matricula(matricula):
        #verificando se já existe ou cadastrando novo

        try:
            with open('registroalunos.txt') as f:
                if nome_aluno in f.read():
                    print(f"Ops! {nome_aluno} já está cadastrado!")

                else:
                    arquivo = open('registroalunos.txt', 'a', encoding='UTF-8')
                    arquivo.write(
                         nome_aluno + ', ' + email_aluno + ', ' + curso_aluno + ', ' + matricula +'\n\n')
                    arquivo.close()
                    print('Aluno cadastrado coom sucesso!')

        except PermissionError:
            print('O arquivo não está aberto no modo escrita. Verifique se não está permitido para somente leitura.')

    else:
        print('\n')
        print('''\t \tPreencha as informações corretamente!
        DICA: Verifique se todas as informações foram preenchidas corretamente e se o email é válido(se contém "@" e ".").''')
        print('\n')
        cadastrar_alunos()

def listar_alunos():
    print('\n\t\t abrindo lista de alunos, aguarde...')

    try:
        arquivo = open('registroalunos.txt', 'r')
        linha = '.'
        while linha != '':
            linha= arquivo.readline()
            print(linha)

        print('\n\t\t Lista exibida com sucesso!')

        arquivo.close()
        print('O arquivo não foi aberto para que seja fechado!')

    except FileNotFoundError:
        print('O arquivo não foi aberto ou não existe.')

def buscar_alunos():
    busca = str(input('Insira o nome do aluno: ')).upper()

    def check_nome(busca):
        nome_aluno = busca.replace(' ', '')
        if busca.isalpha() and busca.isascii():
            return True
        else:
            return False
    check_nome(busca)

    if check_nome(busca):

        try:
            with open('registroalunos.txt', 'r', encoding='utf-8') as arquivo:
                listaAlunos = arquivo.read().split('\n')
            resultado = None
            for aluno in listaAlunos:
                nomeAluno = aluno.split(',')[0].rstrip()
                if busca == nomeAluno:
                    resultado = aluno
                    break
            if resultado == None:
                print('Este aluno não está cadastrado.')
                print('Deseja cadastra-lo?')
                cadastro = input('sim / não: ').upper().strip()
                if cadastro == 'SIM':
                    cadastrar_alunos()
                else:
                    print('Fim do progama!')
            else:
                print(resultado + '\n')

        except FileNotFoundError:
            print('O arquivo não foi aberto ou não existe.')

    else:
        print('\t \tPreencha as informações corretamente!')
        print('\n')
        buscar_alunos()


#condições do painel de acesso
if entrada ==('CADASTRAR'):
    cadastrar_alunos()

elif entrada ==('LISTAR'):
    listar_alunos()

elif entrada ==('BUSCAR'):
    buscar_alunos()

else:
    print('Insíra o comando corretamete!')


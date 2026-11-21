ARQUIVO = "pacientes.txt"
ARQUIVO_FUNC = "funcionarios.txt"


def cadastrar_paciente():
    print("BEM- VINDO AO CADASTRAMENTO")
    try:
        cpf = input("Digite seu CPF: ").strip()

        if buscar_paciente_cpf(cpf) :
            print("ERRO! Paciente já está cadastrado na base!")
            return
        
        nome = input("Digite o nome do paciente: ").strip()
        contato = input("Digite um contato [telefone ou e-mail]: ").strip()

        with open(ARQUIVO, "a", encoding="utf-8") as arq: 
            arq.write(f"{nome} - {cpf} -  {contato}\n")

        print("Paciente cadastrado com sucesso!")

    except OSError:
         print("ERRO! Não foi possível acessar o arquivo.")


def buscar_paciente_cpf(cpf):
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arq:
            for linha in arq:
                dados = linha.strip().split(" - ")

                if dados[1].strip() == cpf:
                    print(f"CPF pertencente à: {dados[0]}")                    
                    return dados

    except FileNotFoundError:
        return None

    return None


def listar_pacientes():
    print("---- LISTANDO TODOS OS PACIENTES ----")

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arq:
            linhas = arq.readlines()

            if len(linhas) == 0:
                print("Nenhum paciente cadastrado!")
                return

            for paciente in linhas:
                dados = paciente.strip().split(" - ")

                print(f"Nome: {dados[0]} - CPF: {dados[1]} - Contato: {dados[2]}")

    except FileNotFoundError:
        print("Nenhum paciente cadastrado!")        



def cadastrar_funcionario():
    print("---- CADASTRANDO FUNCIONÁRIO -----")
    try:
        crm = input("Digite o CRM do funcionário: ").strip()
        
        if buscar_funcionario_crm(crm):
            print("ERRO! Funcionáro já está cadastrado na base!")
            return
        
        nome = input("Digite o nome do funcionário: ").strip()
        cargo = input("Digite o cargo do funcionário: ").strip()
        
        
        with open(ARQUIVO_FUNC, "a", encoding="utf-8") as arq:
            arq.write(f"{nome} - {crm} - {cargo}\n")
            
        print("Funcionário cadastrado com sucesso!")
        
    except OSError:
        print("ERRO! Não foi possível acessar o arquivo.") 

def buscar_funcionario_crm(crm):
    try:
        with open(ARQUIVO_FUNC, "r", encoding="utf-8") as arq:
            for linha in arq:
                dados = linha.strip().split(" - ")
                
                if dados[1].strip() == crm:
                    print(f"CRM pertencente à: {dados[0]}")
                    return dados
                
                
    except FileNotFoundError:
        return None
         
    
    return None

def listar_funcionarios():
    print("---- LISTANDO TODOS OS FUNCIONÁRIOS ----")

    try:
        with open(ARQUIVO_FUNC, "r", encoding="utf-8") as arq:
            linhas = arq.readlines()
            
            if len(linhas) == 0:
                print("Nenhum funcionário cadastrado!")
                return
            
            for funcionario in linhas:
                dados = funcionario.strip().split(" - ")
                
                print(f"Nome: {dados[0]} - CRM: {dados[1]} - Cargo: {dados[2]}")
                
    except FileNotFoundError:
        print("Nenhum funcionário cadastrado!")  



def registrar_vacinacao():
    pass

def buscar_vacina_codigo(cod):
    pass

def listar_vacina_cpf_paciente(cpf_pac):
    pass

def listar_todos_registros():
    pass
import json

ARQUIVO = "pacientes.txt"
ARQUIVO_FUNC = "funcionarios.txt"
ARQUIVO_VACINAS = "vacinas.json"

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
            linhas = arq.readlines() # transforma o conteúdo em uma lista

            if len(linhas) == 0:
                print("Nenhum paciente cadastrado!")
                return

            for paciente in linhas:
                dados = paciente.strip().split(" - ")

                print(f"Nome: {dados[0]} - CPF: {dados[1]} - Contato: {dados[2]}")

    except FileNotFoundError:
        print("Nenhum paciente cadastrado!")        



def cadastrar_funcionario():
    print("---- CADASTRANDO FUNCIONÁRIO ----")

    try:
        crm = input("Digite o CRM do funcionário: ").strip()

        if buscar_funcionario_crm(crm):
            print("ERRO! Funcionário já está cadastrado na base!")
            return

        nome = input("Digite o nome do funcionário: ").strip()
        cpf = input("Digite o CPF do funcionário: ").strip()
        contato = input("Digite um contato [telefone ou e-mail]: ").strip()
        funcao = input("Digite a função [Agente de saúde ou Enfermeiro(a)]: ").strip()

        try:
            with open(ARQUIVO_FUNC, "r", encoding="utf-8") as arq:
                for linha in arq:
                    dados = linha.strip().split(" - ")
                    print("ERRO! CPF já cadastrado na base!")
                    return

        except FileNotFoundError:
            print("Não encontrado!")

        with open(ARQUIVO_FUNC, "a", encoding="utf-8") as arq:
            arq.write(f"{nome} - {crm} - {cpf} - {contato} - {funcao}\n")

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

            print(f"Nome: {dados[0]} - CRM: {dados[1]} - CPF: {dados[2]} - Contato: {dados[3]} - Função: {dados[4]}")

    except FileNotFoundError:
        print("Nenhum funcionário cadastrado!")


def registrar_vacinacao():
    print("---- REGISTRAR VACINAÇÃO ----")
    try:
        cpf = input("Digite o CPF do paciente: ").strip()
        paciente = buscar_paciente_cpf(cpf)
        if paciente is None:
            print("ERRO! Paciente não encontrado na base! Realize o cadastro!")
            return

        crm = input("Digite o CRM do funcionário: ").strip()
        funcionario = buscar_funcionario_crm(crm)
        if funcionario is None:
            print("ERRO! Funcionário não encontrado na base! Realize o cadastro!")
            return    

        try:
            with open(ARQUIVO_VACINAS, "r", encoding="utf-8") as arq:
                vacinas = json.load(arq)
        except FileNotFoundError:
            vacinas = []
        except json.JSONDecodeError:
            vacinas = []            

        codigo = input("Digite o código da vacina: ").strip()
        for v in vacinas:
            if v["CODIGO"] == codigo:
                print("ERRO! Já existe uma vacina com esse código...")
                return
        tipo = input("Digite o tipo da vacina [ex: Gripe, Sarampo, COVID...]: ")
        vacinas.append({"CODIGO": codigo, "TIPO": tipo, "CPF": cpf, "PACIENTE": paciente[0], "FUNCIONARIO": funcionario[0]})


        with open(ARQUIVO_VACINAS, "w", encoding="utf-8") as arq:
            json.dump(vacinas, arq, indent=4, ensure_ascii=False)
        print("Vacinação registrada com sucesso!")

    except OSError:
        print("ERRO! Não foi possível acessar o arquivo.")        

def buscar_vacina_codigo(cod):
    print("--- BUSCANDO VACINA ---")

    try:
        with open(ARQUIVO_VACINAS, "r", encoding="utf-8") as arq:
            vacinas = json.load(arq)

    except (FileNotFoundError, json.JSONDecodeError):
        print("Nenhuma vacina cadastrada...")
        return

    for v in vacinas:
        if v["CODIGO"] == cod.strip():
            print(f"Código: {v['CODIGO']} - Tipo: {v['TIPO']} - CPF: {v['CPF']} - Paciente: {v['PACIENTE']} - Funcionário: {v['FUNCIONARIO']}")
            return
        
                
    print("Vacina não encontrada na base!")

def listar_vacina_cpf_paciente(cpf_pac):
    print("--- LISTAR VACINAS PELO CPF DO PACIENTE ---") 

    try:
        with open(ARQUIVO_VACINAS, "r", encoding="utf-8") as arq:
            vacinas = json.load(arq)

    except FileNotFoundError:
        print("Nenhuma vacinação cadastrada!")
        return

    except json.JSONDecodeError:
        print("Arquivo de vacinações vazio ou inválido!")
        return

    encontrou = False

    for v in vacinas:
        if v["CPF"] == cpf_pac.strip():

            print(f"Código: {v['CODIGO']} - Tipo: {v['TIPO']} - CPF: {v['CPF']} - Paciente: {v['PACIENTE']} - Funcionário: {v['FUNCIONARIO']}")
            encontrou = True

    if not encontrou:
        print("Nenhuma vacinação encontrada para esse paciente!")

def listar_todos_registros():
    print("--- LISTANDO TODOS OS REGISTROS DA VACINA ---")
    try:
        with open(ARQUIVO_VACINAS, "r", encoding="utf-8") as arq:
            registros = json.load(arq) #ler e converte os arquivos. Dados estão em json e a função load converte para dicionário
    except FileNotFoundError:
        print("Nenhuma vacinação cadastrada!")
        return
    
    except json.JSONDecodeError:
        print("Arquivo de vacinações vazio ou inválido!")
        return

    if not registros:
        print("Nenhuma vacinação cadastrada!")
        return

    for r in registros:
        print(f"Código: {r['CODIGO']} - Tipo: {r['TIPO']} - CPF: {r['CPF']} - Paciente: {r['PACIENTE']} - Funcionário: {r['FUNCIONARIO']}")
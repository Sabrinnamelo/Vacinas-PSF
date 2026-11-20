from menu import *
from model import *

def main():

    while True:
        menu_principal()
        op = int(input(">> "))

        if op == 0:
            print("Saindo do programa!")
            break

        elif op == 1:
            while True:
                menu_paciente()
                op1 = int(input(">> "))

                if op1 == 0:
                    print("Voltando ao menu principal!")
                    break
                elif op1 == 1:
                    cadastrar_paciente()
                elif op1 == 2:
                    cpf = int(input("Digite o cpf do paciente para a verificação: "))
                    buscar_paciente_cpf(cpf)
                elif op1 == 3:
                    listar_pacientes()
                else:
                    print("Opção inválida, digite novamente.")

        elif op == 2:
            while True:
                menu_funcionario()
                op2 = int(input(">> "))

                if op2 == 0:
                    print("Voltando ao menu principal!")
                    break
                elif op2 == 1:
                    cadastrar_funcionario()
                elif op2 == 2:
                    crm = int(input("Digite o crm do funcionário para a verificação: "))
                    buscar_funcionario_crm(crm)
                elif op2 == 3:
                    listar_funcionarios()
                else:
                    print("Opção inválida, digite novamente.")

        elif op == 3:
            while True:
                menu_vacinacao()
                op3 = int(input(">> "))

                if op3 == 0:
                    print("Voltando ao menu principal!")
                    break
                elif op3 == 1:
                    registrar_vacinacao()
                elif op3 == 2:
                    cod = input("Digite o código: ")
                    buscar_vacina_codigo(cod)
                elif op3 == 3:
                    cpf_pac = int(input("Digite o cpf do paciente para listar registro das vacinas: "))
                    listar_vacina_cpf_paciente(cpf_pac)
                elif op3 == 4:
                    listar_todos_registros()
                else:
                    print("Opção inválida, digite novamente.")

        else:
            print("Opção inválida! Digite novamente.")

main()

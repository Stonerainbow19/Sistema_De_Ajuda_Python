from time import sleep
#NO VS CODE ESTÁ DANDO PROBLEMAS, NO PYCHARM ESTÁ NORMAL

c = ("\033[m", "\033[1;39;41m","\033[1;39;44m", "\033[1;39;45m", "\033[1;39;46m")


def escreva(str, cor=0):
    """
    Função que faz um print especial, usada em textos destacados
    :param str: texto utilizado pela função

    CRIADO POR: Wesley Gonçalves Ribeiro

    """
    tam = len(str) + 4
    print(c[cor], end="")
    print("~" * tam)
    print(f"  {str}")
    print("~" * tam)
    print(c[0], end="")


while True:

    escreva("Sistema de Ajuda no Python S.A.P", 1)

    e = str(input("Função ou biblioteca => "))
    if e.upper() == "FIM":
        break
    else:
        sleep(1)
        escreva(f"Acessando o manual de comando de {e}",2)
        sleep(1)
        print(c[4], end="")
        help(e) 
        print("\033[m")
        print(c[0], end="")
        sleep(1)

escreva("Obrigado por utilizar meu programa!!! Até logo",3)
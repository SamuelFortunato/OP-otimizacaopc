import os
import time
from tqdm import tqdm

#otimizações

def funcao1():
    os.system("rd /s /q %temp%")
    os.system("md %temp%")
    
def funcao2():
    os.system("ipconfig /flushdns")

while True:
    print("SISTEMA DE OTIMIZAÇÃO DE COMPUTADORES (OP)")
    print("VERSÃO 1.0 [BETA] - LISTA DE COMANDOS")
    print("")
    print("1. Otimizações Basicas")
    print("2. Otimização Internet")
    chat = input(">>>")
    if chat == '1':
        funcao1()
    if chat == '2':
        for i in tqdm(range(5)):
            time.sleep(0.2)
        funcao2()
        print("Otimização de Internet Concluida;")
        time.sleep(2)
        os.system("cls")
    else:
        os.system("cls")
        print("Comando não reconhecido, tente novamente!")
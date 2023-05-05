import os
import time
from tqdm import tqdm

#otimizações

def regs1():
    os.system("""REG add "HKCU\Control Panel" /v ForegroundLockTimeout /t REG_DWORD /d 0 /f""")
    os.system("""REG add "HKCU\Control Panel" /v MenuShowDelay /t REG_SZ /d 100 /f""")
    os.system("""REG add "HKLM\SYSTEM\CurrentControlSet\Control" /v WaitToKillServiceTimeout /t REG_SZ /d 5000 /f""")

def funcao1():
    os.system("rd /s /q %temp%")
    os.system("md %temp%")
    os.system("Del /S /F /Q %Windir%\Temp")
    os.system("sfc /scannow")
    os.system("DISM /Online /Cleanup-image /Restorehealth")
    
def funcao2():
    os.system("ipconfig /flushdns")
    
def error1():
    os.system("cls")
    print("COMANDO NÃO RECONHECIDO, TENTE NOVAMENTE!")
    time.sleep(2)
    os.system("cls")

while True:
    print("SISTEMA DE OTIMIZAÇÃO DE COMPUTADORES (OP)")
    print("VERSÃO 1.2 [BETA] - LISTA DE COMANDOS")
    print("")
    print("1. Otimizações Basicas")
    print("2. Otimização Internet")
    chat = input(">>>")
    if chat == '1':
        for i in tqdm(range(5)):
            time.sleep(0.2)
        regs1()
        funcao1()
        time.sleep(1)
        os.system("cls")
        print("Otimizações Basicas Concluidas!")
        time.sleep(5)
        os.system("cls")
    if chat == '2':
        for i in tqdm(range(5)):
            time.sleep(0.2)
        funcao2()
        print("Otimização de Internet Concluida;")
        time.sleep(2)
        os.system("cls")
    elif chat == '':
        error1()
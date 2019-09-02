import os, requests
import subprocess

print("Welcome to Cry Toolkit beta\n")
print("Created by Joas Antonio\n")
print("1 - Aircrack\n2 - Wifite\n3 - Fluxion\n4 - Pyrit")
menu = input("Digite a opcao desejada: ")       
if menu == "1":
        print("\nAircrack-ng\n")
        menu2 = input("Digite a sua interface de rede: ")
        menu3 = input("\nDigite Start ou Stop\n")
        if menu3 == "start":    
                subprocess.run(["airmon-ng start {menu2}"])
        if menu3 == "stop":
                os.system("airmon-ng stop {menu2}")
                print("\n")


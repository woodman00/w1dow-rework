#!/usr/bin/env python3
import os
import json
import requests
from Core import nickF, decor
from colorama import Fore, Style, init

init(autoreset=True)

# Цвета
fore = Fore
decor.res = Style.RESET_ALL
decor.lye = Fore.LIGHTYELLOW_EX
decor.red = Fore.LIGHTRED_EX

def main():
    while True:
        os.system('clear')
        print(decor.banner)
        print(f"{decor.lye}w1idow")
        print(f"{decor.lye}[1] - Nick Information")
        print(f"{decor.lye}[2] - IP Information")
        print(f"{decor.lye}[3] - Phone or Car Number Information")
        print(f"{decor.lye}[4] - Exit")
        ans = input(f"{decor.lye}[w1dow/main] >> {decor.res}")

        if ans == '1':
            os.system('clear')
            nick = input(f"{decor.lye}Enter Nickname >> ")
            print(f"{decor.lye}Messagers and Social Networks:")
            nickF.osint(nickF.snm, nick)
            print(f"{decor.lye}Videohostings:")
            nickF.osint(nickF.vh, nick)
            print(f"{decor.lye}Games:")
            nickF.osint(nickF.games, nick)
            print(f"{decor.lye}Forums:")
            nickF.osint(nickF.forums, nick)
            print(f"{decor.lye}Wallets:")
            nickF.osint(nickF.money, nick)
            print(f"{decor.lye}Other:")
            nickF.osint(nickF.other, nick)
            input(f"{decor.lye}Press Enter to continue...")

        elif ans == '2':
            os.system('clear')
            ip = input(f"{decor.lye}Enter IP >> ")
            url = f"https://ipinfo.io/{ip}/json"
            try:
                response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=5)
                data = response.json()
                print(f"{Fore.LIGHTGREEN_EX}City: {data.get('city', 'N/A')}")
                print(f"Region: {data.get('region', 'N/A')}")
                print(f"Location: {data.get('loc', 'N/A')}")
                print(f"Operator: {data.get('org', 'N/A')}")
            except Exception as e:
                print(f"{decor.red}Error: {e}")
            input(f"{decor.lye}Press Enter to continue...")

        elif ans == '3':
            os.system('clear')
            print(f"{decor.lye}[1] - Phone Information")
            print(f"{decor.lye}[2] - Car Information")
            sub = input(f"{decor.lye}[Gideon/main/carNphone/category] >> {decor.res}")
            if sub == '1':
                phone = input(f"{decor.lye}Enter Phone Number >> ")
                url = f"https://htmlweb.ru/geo/api.php?json&telcod={phone}"
                try:
                    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=5)
                    data = response.json()
                    print(f"{Fore.LIGHTGREEN_EX}Country: {data.get('country', 'N/A')}")
                    print(f"Region: {data.get('region', 'N/A')}")
                    print(f"City: {data.get('city', 'N/A')}")
                    print(f"Operator: {data.get('operator', 'N/A')}")
                except Exception as e:
                    print(f"{decor.red}Error: {e}")
            elif sub == '2':
                car_num = input(f"{decor.lye}Enter Car Number (a111aa77) >> ")
                car_nums = car_num.upper()
                print(f"{decor.lye}Checking: https://avto-история.рф/num/{car_nums}//")
                print(f"{decor.lye}Checking: https://www.230km.ru/{car_num.lower()}.{car_num[6:]}")
                # Здесь можно добавить парсинг, но пока просто выводим ссылки
            else:
                print(f"{decor.red}Invalid choice")
            input(f"{decor.lye}Press Enter to continue...")

        elif ans == '4':
            break
        else:
            print(f"{decor.red}Invalid option")
            input(f"{decor.lye}Press Enter to continue...")

if __name__ == "__main__":
    main()

import json
import requests

from pathlib import Path
from colorama import Fore
from functools import partial
from concurrent.futures import ThreadPoolExecutor

from Core.classes.load_config import LoadConfig

class NickF:
    def __init__(self, nick: str, timeout: int):
        self.nick = nick
        self.timeout = timeout
    
    def _check_response(self, req, key, url):
        """
        Обрабатывает код ответа от сайта
        """

        if req.status_code == 200:
            return Fore.GREEN + f"[FOUND] {key}: {url}"

        elif req.status_code == 404:
            return Fore.RED + f"[NOT FOUND] {key}"

        elif req.status_code == 403:
            return Fore.YELLOW + f"[FORBIDDEN] {key}"

        return Fore.RED + f"[HTTP {req.status_code}] {key}"


    def _check_website(self, website, prot, headers):

        """
        Отправляет HTTP запрос на сайт, обрабатывает ошибки
        """

        key, site = website
        url = prot + site + self.nick

        try:
            req = requests.get(
                url,
                timeout=self.timeout,
                headers=headers
            )

            return self._check_response(req, key, url)

        except requests.exceptions.Timeout:
            return Fore.RED + f"[TIMEOUT] {key}"
            
        except requests.exceptions.SSLError:
            return Fore.RED + f"[SSL ERROR] {key}"

        except requests.exceptions.ConnectionError:
            return Fore.RED + f"[CONNECTION ERROR] {key}"

        except requests.exceptions.RequestException as ex:
            return Fore.RED + f"[REQUEST ERROR] {key}: {ex}"

    def run(self):
        """
        Запускает проверку сайтов многопоточно
        """


        config = LoadConfig.load_config()

        if config is None:
            return

        site, headers = config

        if not site or not headers:
            print(Fore.RED + "[ERROR] Configuration is empty")
            return

        try:
            platforms = site["nick"]
            prot = platforms["url_protocol"]["protocol"]
        except (KeyError, TypeError):
            print(Fore.RED + "[ERROR] Invalid site configuration")
            return

        for category, sites in platforms.items():
            if category == "url_protocol":
                continue

            print(f"\n{Fore.CYAN}{category.upper()}:{Fore.RESET}")

            check = partial(
                self._check_website,
                prot=prot,
                headers=headers
            )

            with ThreadPoolExecutor(max_workers=10) as executor:
                for result in executor.map(check, sites.items()):
                    print(result + Fore.RESET)
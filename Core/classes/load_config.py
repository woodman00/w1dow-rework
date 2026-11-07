import json
from pathlib import Path

class LoadConfig:
    @staticmethod

    def load_config():
        """
        Загружает список сайтов и HTTP заголовки из json файлов
        """
        json_site = Path(__file__).resolve().parent.parent / "List/site.json" # Путь к site
        json_headers = Path(__file__).resolve().parent.parent / "List/headers.json" # Путь к headers

        try:
            with open(json_site, "r", encoding="utf-8") as file1, \
                open(json_headers, "r", encoding="utf-8") as file2:
                site = json.load(file1)
                headers = json.load(file2)

            return site, headers
        except FileNotFoundError:
            print(Fore.RED + "[ERROR] File not found")
            return None
        except json.JSONDecodeError:
            print(Fore.RED + "[ERROR] Invalid json")
            return None
        except OSError as ex:
            print(Fore.RED + f"[ERROR]: {ex}")
            return None
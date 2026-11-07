import requests
from colorama import Fore

from Core.classes.load_config import LoadConfig

class IpF:
    def __init__(self, ip: str, timeout=5):
        self.ip = ip
        self.timeout = timeout
    
    def _check_website(self, headers, url):
 
        try:
            req = requests.get(
                url,
                timeout=self.timeout,
                headers=headers
            )

        except requests.exceptions.Timeout:
            return Fore.RED + f"[TIMEOUT]"
            
        except requests.exceptions.SSLError:
            return Fore.RED + f"[SSL ERROR]"

        except requests.exceptions.ConnectionError:
            return Fore.RED + f"[CONNECTION ERROR]"

        except requests.exceptions.RequestException as ex:
            return Fore.RED + f"[REQUEST ERROR] : {ex}"
        
        try:
            data = req.json()
        except requests.exceptions.JSONDecodeError:
            return Fore.RED + "[ERROR] Server returned invalid JSON"
        print(f"{Fore.LIGHTGREEN_EX}City: {data.get('city', 'N/A')}")
        print(f"Region: {data.get('region', 'N/A')}")
        print(f"Location: {data.get('loc', 'N/A')}")
        print(f"Operator: {data.get('org', 'N/A')}")
    
    def run(self):

        config = LoadConfig.load_config()

        if config is None:
            return

        site, headers = config

        if not site or not headers:
            print(Fore.RED + "[ERROR] Configuration is empty")
            return
        
        try:
            url = site["ip_link"].replace("{ip}", self.ip)
        except (KeyError, TypeError):
            print(Fore.RED + "[ERROR] Invalid site configuration")
            return
        
        result = self._check_website(
            headers={"User-Agent": "Mozilla/5.0"},
            url=url
        )

        if result is not None:
            print(result)
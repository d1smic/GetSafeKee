import hashlib
import requests

class BreachChecker:
    PWNED_PASSWORDS_URL = "https://api.pwnedpasswords.com/range/{prefix}"
    
    def __init__(self,hibp_api_key: str = None): #falta sacar la key de la api gratuita en  https://haveibeenpwned.com/API/Key
       
        self.session = requests.Session()
        self.session.headers.update({"User-Agent":"GetSafeKee-BreachChecker"})
    
    def check_password(self, password: str) -> dict:
        sha1 = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
        prefix, suffix = sha1[:5], sha1[5:]
        
        try:
            response = self.session.get(
                self.PWNED_PASSWORDS_URL.format(prefix=prefix),
                timeout=5
            )
            response.raise_for_status()
        except requests.RequestException as e:
            return {"compromised": False, "count": 0, "error": str(e)}

        for line in response.text.splitlines():
            returned_suffix, _, count = line.partition(":")
            if returned_suffix == suffix:
                return {"compromised": True, "count": int(count), "error": None}

        return {"compromised": False, "count": 0, "error": None}
    
    def check_multiple(self, passwords: dict) -> dict:
        return {
            label: self.check_password(pwd)
            for label, pwd in passwords.items()
        }





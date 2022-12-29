from googletrans import Translator, LANGUAGES
from colorama import *
import requests
import random


kelimeler = requests.get("https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain", headers={
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F69 Safari/600.1.4"
}).text.splitlines()


def rastgele_kelime(dil):
    translator = Translator()
    if (dil.strip() == ""):
        dil = random.choice(list(LANGUAGES.keys()))
    kelime = random.choice(kelimeler)
    return translator.translate(kelime, dest=str(dil)).text


def rastgele_dork():
    dorklar = [
        '("author/admin")',
        '("Just another WordPress site")',
        '("Welcome to WordPress. This is your first post.")',
        '("A WordPress Commenter on Hello world!")'
    ]
    return random.choice(dorklar)


def banner():
    print(f"""{Fore.WHITE}
██╗    ██╗ ██████╗ ██████╗ ██████╗ ██████╗ ██████╗ ███████╗███████╗███████╗     
██║    ██║██╔═══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝     
██║ █╗ ██║██║   ██║██████╔╝██║  ██║██████╔╝██████╔╝█████╗  ███████╗███████╗     
██║███╗██║██║   ██║██╔══██╗██║  ██║██╔═══╝ ██╔══██╗██╔══╝  ╚════██║╚════██║     
╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝██║     ██║  ██║███████╗███████║███████║     
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝     
                                                                                
██████╗  ██████╗ ██████╗ ██╗  ██╗    ███╗   ███╗ █████╗ ██╗  ██╗███████╗██████╗ 
██╔══██╗██╔═══██╗██╔══██╗██║ ██╔╝    ████╗ ████║██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
██║  ██║██║   ██║██████╔╝█████╔╝     ██╔████╔██║███████║█████╔╝ █████╗  ██████╔╝
██║  ██║██║   ██║██╔══██╗██╔═██╗     ██║╚██╔╝██║██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝██║  ██║██║  ██╗    ██║ ╚═╝ ██║██║  ██║██║  ██╗███████╗██║  ██║
╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝{Fore.RED}
> Coded By Will Graham  | Github: @cannibal-hannibal  | Telegram: @wwillgraham{Fore.WHITE}                                                                 
    """)


def main():
    banner()
    sayi = int(input("Oluşturmak istediğiniz dork sayısı: "))
    dil = input("Kelimeler hangi dille oluşturulsun?(örn: en): ")
    dosya = input("Dorkları kayıt etmesini istediğiniz dosya: ")
    kayit = open(dosya, "w", encoding="utf-8")
    d_ = rastgele_kelime(dil)
    dorklar = []
    for _ in range(sayi):
        while True:
            try:
                kelime = rastgele_kelime(dil)
                dork = rastgele_dork()
                print(f"{Fore.LIGHTRED_EX}  +{Fore.WHITE} {dork + kelime}")
                dorklar.append(dork + kelime)
                break
            except:
                continue
    for dork in list(set(dorklar)):
        kayit.write(dork + "\n")
    kayit.close()
    print(f"{Fore.LIGHTCYAN_EX}+{Fore.LIGHTWHITE_EX} {str(len(dorklar))} adet dork {dosya} dosyasına kayıt edildi!")


if __name__=="__main__":
    try:
        init()
        main()
    except KeyboardInterrupt:
        exit()

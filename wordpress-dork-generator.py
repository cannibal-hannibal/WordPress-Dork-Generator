from googletrans import Translator, LANGUAGES
from colorama import *
from fake_useragent import UserAgent
import requests
import random


kelimeler = requests.get("https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain", headers={
    "User-Agent": UserAgent().random
}).text.splitlines()


def rastgele_kelime(dil):
    translator = Translator()
    if (dil.strip() == ""):
        dil = random.choice(list(LANGUAGES.keys()))
    kelime = random.choice(kelimeler)
    return translator.translate(kelime, dest=str(dil)).text


def rastgele_dork():
    dorklar = [
        '("uncategorized")',
        '("Just another WordPress site")',
        '("author/admin")',
        '("My Sýte Wordpress")',
        '("This is my first post")',
        '("Welcome to WordPress. This is your first post.")',
        '("A WordPress Commenter on Hello world!")',
        '("Welcome to WordPress!")',
        '("A WordPress Commenter")',
        '"Proudly powered by WordPress")',
        '("Hello world. This my website!")',
        '("My Wordpress Blog")',
        '("Mr WordPress on Hello world!")'
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
    dorklar = []
    for _ in range(sayi):
        kelime = rastgele_kelime(dil)
        dork = rastgele_dork()
        print(f"{Fore.LIGHTRED_EX}  +{Fore.WHITE} {dork + kelime}")
        dorklar.append(dork + kelime)
    for dork in dorklar:
        kayit.write(dork + "\n")
    kayit.close()
    print(f"{Fore.LIGHTCYAN_EX}+{Fore.LIGHTWHITE_EX} {str(len(dorklar))} adet dork {dosya} dosyasına kayıt edildi!")


if __name__=="__main__":
    try:
        init()
        main()
    except KeyboardInterrupt:
        exit()

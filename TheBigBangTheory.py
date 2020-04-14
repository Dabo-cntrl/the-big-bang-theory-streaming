import webbrowser
import urllib3
from bs4 import BeautifulSoup as bs


def Open(stagione, episodio):
    finelink = ""
    stagione_int = int(stagione)
    codic_brutti_prime_wire = ['tLiLZQRq/8HyvaFuX', 'bBFPD5Pi/JDgFb2Qc', '83NxLGpC/ZBEOMrSr', 'UA43jOqW/WWUQj4G5','hu4cexgV/zvVQQyUm','OjhB5Qp8/wjBPfAJv','mGFPiwyD/LTtonIfk','fy3PjpUi/6tKkZbEx','nIFxr1XD/8zUlKH79','ZK0x4T1Z/VhaZbHfm','kTRe1Lop/9GjJAaUf','BPtTTvB5/xVNNqoXF']
    codice_brutto_prime_wire_classe_a = "_vFDCESHPLi"
    codice_brutto_prime_wire_classe_div="_NLmwGUCtTG _UeVzoJTebK _PirDVMuAck"
    url_completo = "https://primewire.digital/tv-series/the-big-bang-theory-season-" + stagione + "/" + \
                   codic_brutti_prime_wire[stagione_int - 1]
    Chromedir = '/bin/google-chrome'
    html = urllib3.PoolManager()  ##Cerco di raggiungere l'url desiderato per estrarre l'html
    response = html.request('GET', url_completo)
    soup = bs(response.data, "html.parser")  ## html estrattp in soup
    ##print(soup("div",{"class":"_NLmwGUCtTG _UeVzoJTebK _PirDVMuAck"}))
    for post in soup("div", {"class": codice_brutto_prime_wire_classe_div}):
        for post2 in post("a", {"class": codice_brutto_prime_wire_classe_a}):
            episodio_estratto = post2.find("span").text[8:10]
            episodio_estratto = int(episodio_estratto)
            if (episodio_estratto == int(episodio)):
                finelink = post2["href"]

    url_completo = "https://primewire.digital" + finelink
    webbrowser.get(Chromedir).open(url_completo)


def menu():
    stagione = 0
    episodio = 0
    decisione = ''
    print("Vuoi guardare The Big Bang Theory?(y/n)")
    decisione = input()
    print(decisione)
    if (decisione == 'y'):
        print("Perfetto, che stagione?")
        stagione = input()
        print("Ok, che episodio?")
        episodio = input()
        Open(stagione, episodio)
    if (decisione == 'n'):
        print("Peccato, alla prossima")


menu()

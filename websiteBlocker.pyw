import time
from datetime import datetime as dt
hosts_yolu=r"C:\Windows\System32\drivers\etc\hosts"
yonlendirme="127.0.0.1"
website_liste=["https://www.google.com","google.com","www.google.com"]
baslangicSaati=8
bitisSaati=18


while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,baslangicSaati) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,bitisSaati):
        with open(hosts_yolu,"r+") as dosya:
            icerik=dosya.read()
            for website in website_liste:
                if website in icerik:
                    pass
                else:
                    dosya.write("\n"+yonlendirme+" "+website)
    else:
        with open(hosts_yolu,"r+") as dosya:
            icerik=dosya.readlines()
            dosya.seek(0)
            for satir in icerik:
                if not any(website in satir for website in website_liste):
                    dosya.write(satir)
            dosya.truncate()
    time.sleep(5)
import requests,os,sys,time
from time import sleep
b="\033[94m"
c="\033[96m"
g="\033[92m"
r="\033[91m"
p="\033[1;97m"
d="\033[00m"
ab="\033[90m"
dn=f"{d}[{g}√{d}]{p}"
er=f"{d}[{r}!{d}]{p}"
pr=f"{d}[{c}?{d}]{p}"
def clear():
    os.system("cls" if os.name == "nt" else "clear")
def baner():
    clear()
    print(f"""\033[33;1m============================================
 \033[31;1m____  ____   _    __  ____     __  _
/ ___||  _ \ / \  |  \/  \ \   / / / |
\___ \| |_) / _ \ | |\/| |\ \ / /  | |
\033[37;1m ___) |  __/ ___ \| |  | |_\ V /   | |
|____/|_| /_/   \_\_|  |_(_)\_/    |_|
{p}{g}
\033[33;1m============================================
\033[32;1m(\033[31;1m●\033[32;1m) {c}By   : R{r}A{c}M{r}A{c}D{r}H{c}A{r}N{c}I
\033[32;1m(\033[31;1m●\033[32;1m) {c}Gt   : github.com/RAMA-XD
\033[32;1m(\033[31;1m●\033[32;1m) {c}Jan Di Salah Gunakan !
\033[32;1m(\033[31;1m●\033[32;1m) {c}Pastikan Kartu Korban Aktif dan Tidak Di 
\033[32;1m(\033[31;1m●\033[32;1m) {c}Mode Pesawat
\033[33;1m============================================{b}""")
def cblg():
    lg=input(f"{pr}Coba lagi? ({d}{c}y{d}/{c}n{p}) : {c}")
    if lg == "y" or lg == "Y":
       sleep(5)
       os.system("python SpamSms.py")
    elif lg == "n" or lg == "N":
       sys.exit(f"{er}Terima Kasih Telah Menggunakan Tools ini :)")
    else:
       print(f"{er}Betapa Gobloxnya Aku ")
       cblg()

def spam(nomor):
    req=requests.get("https://ainxbot-sms.herokuapp.com/api/spamsms",params={"phone":nomor}).text
    if "terkirim" in req:
       print(f"{dn}Spam ke {c}{nomor} berhasil")
    else:
       print(f"{er}Spam ke {c}{nomor} gagal")
if __name__=="__main__":
    baner()
    nomor=input(f"{er}Contoh Input No :{c}{p} 85812345678\n{er}Batas Spam : -\n{pr}{ab} Input No Target ! :{c}")
    spam(nomor)
    cblg()
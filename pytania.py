from tkinter import *
from tkinter import messagebox
import random

licznik = 0
b=0
numer_pytania = []

while b != 12:
    r = random.randint(1,26)
    if r not in numer_pytania:
        numer_pytania.append(r)
        b = b+1

p = 0

kwoty = ["500 zł","1 000 zł", "2 000 zł", "5 000 zł", "10 000 zł", "20 000 zł", "40 000 zł", "75 000 zł", "125 000 zł", "250 000 zł", "500 000 zł", "1 000 000 zł"]
pytania=["Jak określa się osobę na pozór spokojną i nieśmiałą?:\n A.ogień i woda B.Słomiany ogień C.Anielska woda D.Cicha woda",
"Umowa cywilnoprawna, zawierana zazwyczaj zamiast umowy o pracę,\n to tak zwana umowa:\n A.odpadkowa B.śmieciowa C.resztkowa D.okrawkowa",
"Co zalewa ten, kto nie wylewa za kołnierz?:\nA.fundamenty B.ognisko C.zioła D.robaka",
"Co ma na nogach panczenista?:\n A.korki B.narty C.łyżwy D.płetwy",
"Czym bez obaw mozna popić zażywane lekarstwa?:\n A.sokiem z grejfruta B.letnią wodą C.mocną kawą D.gorącą herbatą",
"Jaką cześć liter w wyrazie 'bajzel' stanowią samogłoski?:\nA.jedną piątą B.jedną czwartą C.jedną trzecią D.jedną drugą",
"Litr chłodnej wody waży w przybliżeniu:\nA.10 funtów B.kilogram C.2 dekagramy D.10 uncji",
"Przydomek wiedźmina Geralta wskazuje na to,\n że bohater sagi Andrzeja Sapkowskiego pochodzi z...\nA.Vengerbergu B.Oxenfurtu C.Rivii D.Tretogoru",
"Ile linii metra jest w Warszawie?\nA.1 B.2 C.3 D.4",
"Pierwsze litery tablicy rejestracyjnej jakiego powiatu tłumaczy się\n żartobliwie jako Centrum Tadeusza R. albo Co Tu Robisz?\nA.tarnobrzeskiego B.toruńskiego C.tyskiego D.tureckiego",
"Agata Duda witała się ze swoimi uczniami, mówiąc:\nA.Guten Morgen B.Good Morning C.Bonjour D.Boungiorno",
"Które z państw na Bliskim Wschodzie nie graniczy z pozostałymi?\nA.Arabia Saudyjska B.Oman C.Jemen D.Syria",
"Zje pozostałe:\nA.kijanka B.żyworódka rzeczna C.rzęsorek rzeczek D.larwa chruścika",
"Ferruccio Lamborghini, zanim zajął się produkcją samochodów, był producentem przede wszystkim:\nA.motocykli B.tokarek C.ciągników D.maszyn przędzalniczych",
"Dokończ słowa Agnieszki Osieckiej:\nDo domu wrócimy, w piecu napalimy, nakarmimy psa. Przed nocą zdążymy...\nA.szkopom dołożymy B.tylko zwyciężymy C.wojna to nie gra D.w oku błyśnie łza",
"Robert Pasut, Rafał Masny i Czarek Jóźwik to youtuberzy:\nA.Lekcewarzy B.Abstrachuje C.Ignoróje D.Ómniejsza",
"Płetwą grzbietową nie pruje wody:\nA.Długoszpar B.Kosogon C.Orka D.Wal grenlandzki",
"Który utwór Juliusza Słowackiego napisany jest prozą?\n A.'Godzina myśli' B.'W Szwajcarii' C.'Anheli' D.'Arab'",
"Likier maraskino produkuje się z maraski, czyli odmiany:\nA.wiśni B.jabłoni C.Figi D.Gruszy",
"Który aktor urodził się w roku opatentowania kinematografu braci Lumière?:\nA.Rudolph Valentino B.Humphrey Bogart C.Charlie Chaplin D.Fred Astaire",
"Komiksowym 'dzieckiem' rysownika Boba Kane'a jest:\nA.Superman B.Batman C.Spider-Man D.Captain America",
"Kto jest mistrzem tego samego oręża, w jakim specjalizowała się mitologiczna Artemida?:\nA.Zorro B.Legolas C.Don Kichot D.Longinus Podbipięta",
"Mowa w obronie poety Archiasza przeszła do historii\n jako jeden z najświetniejszych popisów retorycznych:\nA.Izokratesa B.Cycerona C.Demostenesa D.Kwintyliana",
"Rybą nie jest:\nA.Świnka B.Rozpiór C.Krasnopiórka D.Kraska",
"Odrażający drab z Kabaretu Starszych Panów dubeltówkę weźmie, wyjdzie i...\nA.Rach-ciach! B.Buch,Buch! C.Z rur dwóch D.Bum w brzuch",
"Kto był nadwornym malarzem króla Filipa IV Habsburga?:\nA.Marcello Bociarelli B.Jan van Eyck C. Diego Velazquez D.Jaques-Louis David",
"Z gry na jakim instrumencie słynie Czesław Mozil?:z\nA.Na kornecie B.Na akordeonie C.Na djembe D.Na ksylofonie"]

odpowiedzi=["D","B","D","C","B","C","B","C","B","B","A","D","C","C","B","B","D","C","A","A","B","B","D","D","B","C","D"]



def wynik():
    if wartosc.get()==1:
        if odpowiedzi[pytanie] == "A":
            messagebox.showinfo("Wynik","To dobra odpowiedź!")
        else:
            messagebox.showinfo("Wynik","To zła odpowiedź!\nGAME OVER!")
    elif wartosc.get()==2:
        if odpowiedzi[pytanie] == "B":
            messagebox.showinfo("Wynik","To dobra odpowiedź!")
        else:
            messagebox.showinfo("Wynik","To zła odpowiedź!\nGAME OVER!")
    elif wartosc.get()==3:
        if odpowiedzi[pytanie] == "C":
            messagebox.showinfo("Wynik","To dobra odpowiedź!")
        else:
            messagebox.showinfo("Wynik","To zła odpowiedź!\nGAME OVER!")
    elif wartosc.get()==4:
        if odpowiedzi[pytanie] == "D":
            messagebox.showinfo("Wynik","To dobra odpowiedź!")
        else:
            messagebox.showinfo("Wynik","To zła odpowiedź!\nGAME OVER!")

def usunOkno(okno):
    okno.destroy()

while True:
    pytanie = numer_pytania[licznik]
    if p==1:
        break
    glowne_okno = Tk()
    glowne_okno.geometry("500x300")
    glowne_okno.title("MILIONERZY")
    wartosc = IntVar()
    kwotap = str(kwoty[licznik])

    numerp = str(licznik + 1)
    tekst1 = Label(glowne_okno, text="Pytanie numer " + numerp + "\nGrasz o: " + kwotap)
    tekst1.place(x=195,y=20)

    tekst2 = Label(glowne_okno, text=pytania[pytanie])
    tekst2.place(x=40,y=60)

    tekst3 = Label(glowne_okno, text="Jaka jest Twoja odpowiedż?")
    tekst3.place(x=165,y=125)

    przycisk_A = Radiobutton(glowne_okno, text = "A", variable = wartosc, value = 1)
    przycisk_A.place(x=150, y=150)

    przycisk_B = Radiobutton(glowne_okno, text = "B", variable = wartosc, value = 2)
    przycisk_B.place(x=200, y=150)

    przycisk_C = Radiobutton(glowne_okno, text = "C", variable = wartosc, value = 3)
    przycisk_C.place(x=250, y=150)

    przycisk_D = Radiobutton(glowne_okno, text = "D", variable = wartosc, value = 4)
    przycisk_D.place(x=300, y=150)

    przycisk_zatwierdz = Button(glowne_okno, text = "Zatwierdź", command = wynik)
    przycisk_zatwierdz.place(x=215,y=175)

    glowne_okno.mainloop()


    if wartosc.get()==1:
        if odpowiedzi[pytanie] == "A":
            licznik += 1
        else:
            p = 1
    elif wartosc.get()==2:
        if odpowiedzi[pytanie] == "B":
            licznik += 1
        else:
            p = 1
    elif wartosc.get()==3:
        if odpowiedzi[pytanie] == "C":
            licznik += 1
        else:
            p = 1
    elif wartosc.get()==4:
        if odpowiedzi[pytanie] == "D":
            licznik += 1
        else:
            p = 1

    if licznik == 12:
        messagebox.showinfo("Wynik","WYGRAŁEŚ MILION")

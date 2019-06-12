from tkinter import *
from tkinter import messagebox
import random

numer_pytania = random.randint(0,26)

odpowiedzi=["D","B","D","C","B","C","B","C","B","B","A","D","C","C","B","B","D","C","A","A","B","B","D","D","B","C","D"]

def telefon(nr_pytania,odpowiedz):
    m_odpowiedzi = ["A", "B", "C", "D"]
    podpowiedz = 0
    for n in m_odpowiedzi[:]:
        if n == odpowiedz[nr_pytania]:
            m_odpowiedzi.remove(n)
    p3 = [odpowiedz[nr_pytania], m_odpowiedzi[0], m_odpowiedzi[1], m_odpowiedzi[2]]
    if nr_pytania <=5:
        wagi = [0.85,0.05,0.05,0.05]
        podpowiedz = random.choices(p3,wagi)
    elif nr_pytania >=5 and nr_pytania <=9:
        wagi = [0.7,0.1,0.1,0.1]
        podpowiedz = random.choices(p3,wagi)
    if nr_pytania <=5:
        wagi = [0.55,0.15,0.15,0.15]
        podpowiedz = random.choices(p3,wagi)
    return "MAMA: według mnie odpowiedzią będzie: " , podpowiedz

def pnp(nr_pytania,odpowiedz):
    m_odpowiedzi = ["A", "B", "C", "D"]
    podpowiedz = 0
    for n in m_odpowiedzi[:]:
        if n == odpowiedz[nr_pytania]:
            m_odpowiedzi.remove(n)
    podpowiedz = random.choice(m_odpowiedzi)
    return "Pozostawione odpowiedzi to " , odpowiedz[nr_pytania] , " oraz " + podpowiedz

def publicznosc(nr_pytania,odpowiedz):
    m_odpowiedzi = ["A", "B", "C", "D"]
    podpowiedz = 0
    for n in m_odpowiedzi[:]:
        if n == odpowiedz[nr_pytania]:
            m_odpowiedzi.remove(n)
    p3 = [odpowiedz[nr_pytania], m_odpowiedzi[0], m_odpowiedzi[1], m_odpowiedzi[2]]
    if nr_pytania <=5:
        wagi = [0.85,0.05,0.05,0.05]
        podpowiedz = random.choices(p3,wagi)
    elif nr_pytania >=5 and nr_pytania <=9:
        wagi = [0.7,0.1,0.1,0.1]
        podpowiedz = random.choices(p3,wagi)
    if nr_pytania <=5:
        wagi = [0.55,0.15,0.15,0.15]
        podpowiedz = random.choices(p3,wagi)
    return "Wesług publiczności odpowiedzią będzie: " , podpowiedz

telefon_wynik = telefon(numer_pytania,odpowiedzi)
pnp_wynik = pnp(numer_pytania,odpowiedzi)
publicznosc_wynik = publicznosc(numer_pytania, odpowiedzi)

def akcja_przycisk_kola2():
    if wartosc.get()==1:
        okno_telefon = Tk()
        okno_telefon.title("Telefon do przyjaciela")
        okno_telefon.geometry("500x150")
        telefon_tekst = Label(okno_telefon, text="Wybrałeś telefon do przyjaciela\nDzwonimy do Twojej mamy bo nie masz innych przyjaciół!\nPani mamo, jaka według pani będzie odpowiedż na to pytanie?")
        telefon_tekst.place(x=75,y=20)
        telefon_tekst2 = Label (okno_telefon, text = telefon_wynik)
        telefon_tekst2.place(x=125,y=100)
        okno_telefon.mainloop()
    if wartosc.get()==2:
        okno_pnp = Tk()
        okno_pnp.title("Pół na pół")
        okno_pnp.geometry("250x100")
        pnp_tekst = Label(okno_pnp, text="Wybrałeś pół na pół")
        pnp_tekst.place(x=55,y=20)
        pnp_tekst2 = Label (okno_pnp, text = pnp_wynik)
        pnp_tekst2.place(x=10,y=50)
        okno_pnp.mainloop()
    if wartosc.get()==3:
        okno_publicznosc = Tk()
        okno_publicznosc.title("Pytanie do publiczności")
        okno_publicznosc.geometry("300x100")
        publicznosc_tekst = Label(okno_publicznosc, text="Wybrałeś pytanie do publicznosci")
        publicznosc_tekst.place(x=55,y=20)
        publicznosc_tekst2 = Label (okno_publicznosc, text = publicznosc_wynik)
        publicznosc_tekst2.place(x=30,y=50)
        okno_publicznosc.mainloop()

okno_kola = Tk()
wartosc = IntVar()
okno_kola.title("Koła ratunkowe")
okno_kola.geometry("200x175")
kola_tekst = Label(okno_kola, text="Koła ratunkowe")
kola_tekst.place(x=20, y=20)

przycisk_telefon = Radiobutton(okno_kola, text = "Telefon do przyjaciela", variable = wartosc, value = 1)
przycisk_telefon.place(x=20, y=50)

przycisk_pnp = Radiobutton(okno_kola, text = "Pół na pół", variable = wartosc, value = 2)
przycisk_pnp.place(x=20, y=75)

przycisk_publicznosc = Radiobutton(okno_kola, text = "Pytanie do publiczności", variable = wartosc, value = 3)
przycisk_publicznosc.place(x=20, y=100)

przycisk_kola2 = Button(okno_kola, text = "Wybieram", command = akcja_przycisk_kola2)
przycisk_kola2.place(x=75,y=125)
okno_kola.mainloop()

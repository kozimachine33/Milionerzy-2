from tkinter import *
from tkinter import messagebox
import random

komentarz_pytanie = ["Czy to jest Twoja ostateczna odpowiedź?",
"Czy jesteś pewnien swojej odpowiedzi?",
"Jesteś pewien, że nie chcesz zmienić odpowiedzi?",
"Definitywnie?",
"Czy to jest twoja ostateczna decyzja?",
"Obstajesz przy swoim?",
"Czy Twoja mama poparłaby Twój wybór?",
"Zastanowiłeś się dobrze?",
"Rozumiem, że nie zmienisz już zdania?",
"Czy to jest na 100% dobra odpowiedź?",
"Widzę, że się nie wahasz. Mam rację?",
"Na pewno ta odpowiedź?"]

def akcja_powitanie():
    powitanie = Label(glowne_okno1,text = "Witam, nazywam się Hubert Urbański i będę prowadził Twoją dzisiejszą grę. \nPowiedz jak się nazywasz uczestniku!")
    powitanie.place(x=50, y=50)
    imie = Entry(glowne_okno1)
    imie.place(x=185, y=105)
    przycisk1.destroy()
    siema = Button(glowne_okno1, text = "ok", command = akcja_powitanie1)
    siema = Button(glowne_okno1, text = "ok", command = akcja_powitanie1)
    siema.place(x= 230, y=125)

def akcja_powitanie1():
    powitanko = Label(glowne_okno1, text = "Witaj!")
    powitanko.place(x=225, y=180)

glowne_okno1 = Tk()
glowne_okno1.title("Milionerzy")
glowne_okno1.geometry("500x250")
przycisk1 = Button(glowne_okno1, text = "Rozpoczynam grę", command = akcja_powitanie)
przycisk1.place(x=175, y=100)
glowne_okno1.mainloop()

glowne_okno2 = Tk()
glowne_okno2.geometry("500x500")
wartosc = IntVar()
wartosc1 = IntVar()
wartosc2 = IntVar()
def akcja_przycisk():
    if wartosc.get() == 1:
        komentarz1 = Label(glowne_okno2, text = "W takim razie zaznaczam podaną odpowiedź")
        komentarz1.pack()
    elif wartosc.get() == 2:
        komentarz1 = Label(glowne_okno2, text = "Czy w takim razie chcesz zmienić swoją odpowiedź?")
        komentarz1.pack()
        rprzycisk1_tak = Radiobutton(glowne_okno2, text = "Tak!", variable = wartosc1, value = 1)
        rprzycisk1_tak.pack()
        rprzycisk2_nie = Radiobutton(glowne_okno2, text = "Nie!", variable = wartosc1, value = 2)
        rprzycisk2_nie.pack()
        przycisk2 = Button(glowne_okno2, text = "Zatwierdzam", command = akcja_przycisk2)
        przycisk2.pack()

def akcja_przycisk2():
    zmiana_tekst = Label(glowne_okno2, text = "Na jaką odpowiedż chcesz zmienić?")
    zmiana_tekst.pack()

    przycisk_Az = Radiobutton(glowne_okno2, text = "A", variable = wartosc2, value = 1)
    przycisk_Az.pack()
    przycisk_Bz = Radiobutton(glowne_okno2, text = "B", variable = wartosc2, value = 2)
    przycisk_Bz.pack()
    przycisk_Cz = Radiobutton(glowne_okno2, text = "C", variable = wartosc2, value = 3)
    przycisk_Cz.pack()
    przycisk_Dz = Radiobutton(glowne_okno2, text = "D", variable = wartosc2, value = 4)
    przycisk_Dz.pack()
    przycisk3 = Button(glowne_okno2, text = "Zatwierdzam", command = akcja_przycisk3)
    przycisk3.pack()
def akcja_przycisk3():
    if wartosc2.get()==1:
        zmiana_wartosc = Label(glowne_okno2, text = "Odpowiedź została zmieniona na: A")
        zmiana_wartosc.pack()
    elif wartosc2.get()==2:
        zmiana_wartosc = Label(glowne_okno2, text = "Odpowiedź została zmieniona na: B")
        zmiana_wartosc.pack()
    elif wartosc2.get()==3:
        zmiana_wartosc = Label(glowne_okno2, text = "Odpowiedź została zmieniona na: C")
        zmiana_wartosc.pack()
    elif wartosc2.get()==4:
        zmiana_wartosc = Label(glowne_okno2, text = "Odpowiedź została zmieniona na: D")
        zmiana_wartosc.pack()

j = random.randint(0,11)
komentarz = Label(glowne_okno2, text = komentarz_pytanie[j])
komentarz.pack()

rprzycisk1 = Radiobutton(glowne_okno2, text = "Tak!", variable = wartosc, value = 1)
rprzycisk1.pack()
rprzycisk2 = Radiobutton(glowne_okno2, text = "Nie!", variable = wartosc, value =2)
rprzycisk2.pack()


przycisk = Button(glowne_okno2, text = "Zatwierdzam", command = akcja_przycisk)
przycisk.pack()

glowne_okno2.mainloop()

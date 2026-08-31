import numpy as np
import random
#print(np.arange(10))
#mitähS
def TervehdysJaRoolit(rooli):
    rooli = rooli.lower()
    if (rooli == "asiakas"):
        print("Tervehdys asiakas")
    elif (rooli == "tyontekija"):
        print("Tervetuloa töihin")
    else:
        print("Tuntematon rooli")

def TervehdysJaRoolit():
    rooli = input("Anna rooli:")
    rooli = rooli.lower()
    if (rooli == "asiakas"):
        print("Tervehdys asiakas")
    elif (rooli == "tyontekija"):
        print("Tervetuloa töihin")
    else:
        print("Tuntematon rooli")      

def lampotila():
    lampo = float (input("Syota lampotila:"))
    if (lampo < 10):
        print("Mainosta kuumia juomia")  
    elif(lampo > 20):
        print("Mainosta kylmia juomia")
    elif(lampo > 10) and (lampo < 20):
        print("Mainosta sekä kuumia että kylmiä juomia")

def tuotelista():
    tuotelista = ["Karhu","Eversti","Aura","Kupari","Koff"]
    for ind, tuote in enumerate(tuotelista):
        print(f"Kahvilan tuote nro {ind+1} = {tuote}")

def ostoskori():
    thisdict = {}
    while True:
        tuote = input("Syota tuote:")
        if tuote == "":
            break
        hinta = float (input("Syota hinta:"))
        thisdict [tuote] = hinta
    

    print("Tuotteet:")
    yhteissumma = 0

    for tuote, hinta in thisdict.items():
        print(f"{tuote} : {hinta:.2f} euroa")
        yhteissumma += hinta

    print(f"Yhteissumma: {yhteissumma:.2f} euroa")

def tarjous():
    erikoistarjous = ("Erikoisolut", 12.95)
    print(f"Tahdotko ostaa erikoistarjouksen: {erikoistarjous[0]} {erikoistarjous[1]}")

    vastaus = input ("Vastaus: ")
    vastaus =vastaus.lower()
    if vastaus == ("kylla"):
        print("Lisatty ostoskoriin!")
    elif vastaus == ("ei"):
        print("Tuotetta ei lisätty ostokoriin")
    else:
        print("Ei käyvä vastaus!!")

def arvostelut():
    arvostelu = []
    acount = 0
    for i in range (3):
        arvio = input("Syota asiakasarvostelu: ")
        arvostelu.append(arvio)
        for k in arvio:
            if k == "a":
                acount += 1

    
    print("Arvostelusi: ")
    print(arvostelu[0].upper())
    print(arvostelu[1].upper())
    print(arvostelu[2].upper())
    print("Nain monta a-kirjainta arvosteluissasi: ")
    print(acount)


def myyntimaara():
    myynti = []
    paivat = ["ma","ti","ke","to","pe","la","su"]
    for i in range (7):
        p = float (input(f"Syota paivan {paivat[i]} myynti: "))
        myynti.append(p)
    keskiarvo = sum(myynti) / len(myynti)
    suurin = max(myynti)
    paiva = myynti.index(suurin)
    print(f"Myynti yhteensä: {sum(myynti):.2f} euroa")
    print(f"Keskimaarainen myynti: {(keskiarvo):.2f} euroa")
    print(f"Suurin myynti oli: {paivat[paiva]} {(suurin)} euroa")
    

def erikois():
    lista = ["Latty", "Olut", "Bursa", "Matto"]
    erikoistuote = random.choice(lista)

    while True:
        arvaus = input ("Arvaa erikoistuote: ")
        if (arvaus == erikoistuote):
            print("Oikein meni!")
            break
        elif arvaus in lista:
            arvausi = lista.index(arvaus)
            oikeai= lista.index(erikoistuote)

            if arvausi < oikeai:
                print("Arvaus oli ennen oikeaa tuotetta")

            else:
                print("Arvus oli tuotteen jälkeen")

        else:
           print("Tuote ei ole listassa")


            #seuraavaksi tehtava 9

        
            

   



#TervehdysJaRoolit()
#lampotila()
#tuotelista()
#ostoskori()
#tarjous()
#arvostelut()
#myyntimaara()
erikois()

#t = "Kari"
#print (t.lower())
    
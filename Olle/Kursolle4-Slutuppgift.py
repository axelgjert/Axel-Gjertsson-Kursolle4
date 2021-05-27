#Skapa listor
rektangel = []

sidor = []
höjd = []

#skapar funktioner som beräknar våra figurer
def räkna_area(s1, s2):
    return s1*s2

def räkna_volym(s1, s2, höjd):
    return s1*s2*höjd


while True:
    s1 = int(input("rektangelns första sida: ")) #frågar användarenn
    s2 = int(input("Rektangelns andra sida: "))  #frågar användarenn

    while True:
        try:
            höjd = int(input("Ange höjden på ditt rätblock: "))
            break
        except:
            print("Felaktig inmatning! Du måste ha ett heltal.")
            #rätblocket
    if höjd <1:
        höjd = 1
        print("Du matade in ett negativt tal. Höjden sattes till 1!")
    if höjd >10:
        höjd=10
        print("Max höjden är 10! Höjden ändrades.")
#krav för inputen

    sidor.append(s1)
    sidor.append(s2)
    höjd.append(höjd)
    area = räkna_area(s1, s2)

    print(f"Rektangeln har sidorna {s1} & {s2} vilket gör arean till {area}")

    if s1 == s2:
        print("Eftersom att båda sidorna är lika långa så är detta inte en rektangel. Det är en kvadrat.")

    if s1 == s2:
        rektangel.append(f"Rektangeln har sidorna {s1} och {s2} vilket gör arean till {area}, eftersom båda sidorna är lika långa blir denna rektangeln en kvadrat")
    else:
        rektangel.append(f"Rektangeln har sidorna {s1} och {s2} vilket gör arean till {area}")
        


    for i in range(1,höjd+1):
        vol = area*i
        print(f"när höjden är {i} så är volymen {vol}")

    while True:
        svar = str(input("Vill du göra en till beräkning ( Ja / Nej )?: "))
        if svar in ('Ja', 'Nej'):
            break
        print("Fel!")
    if svar == 'Ja':
        continue
    else:
        break

print(*rektangel, sep = "\n")

print(f"Sidor: {sidor}")
print(f"Höjderna: {höjd}")

#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""2011.majus.10-ikei erettsegi megoldas."""
print("1. feladat")
"""Be kell kerni egy szoveget a felhasasznalotol es meg kell hataroznio hogy van e benne maganhangzo. """
szo = str(input("Adjon meg egy szot: "))
maganhangzok = ['A', 'E', 'I', 'O', 'U']
szo2 = szo.upper()
van_benne = False
for a in maganhangzok:
    if a in szo2:
        van_benne = True
        break
    else:
        van_benne = False
if van_benne == True:
    print("Van benne maganhangzo.")
else:
    print("Nincs benne maganhangzo.")

print("2. feladat")
"""Ki kell irni a kepernyore a szoveg.txt leghosszabb szavat es hogy hany karakterbol all ha a leghosszabbol tobb van akkkor eleg egyet kiirni. """
"""Igy nezne ki a szotar amibe beolvassuk:
szotar={
    Hanyadik szo{
    "szo":abbahadjuk
    "szo hossza":10
    "Hany maganhangzo van bennne":4
    }
}
"""
n = 0
szotar = {}
with open("szoveg.txt","rt+",encoding="utf-8") as f:
    for s in f:
        sor = s.replace("\n", "")
        n += 1
        szotar[n] = {}
        szotar[n]["szo"] = sor
        szotar[n]["szo hossza"] = int(len(sor))
        szamlalo = 0
        for szor in sor.upper():
            for ma in maganhangzok:
                if ma == szor:
                    szamlalo+=1
        szotar[n]["Hany maganhangzo van benne"] = int(szamlalo)
        szotar[n]["Hany massalhangzo van benne"] = int(len(sor)) - int(szamlalo)

#print(szotar)

print("3. feladat")
"""Ki kell gyujteni azokat a szavakat amikben tobb a maganhangzo mint a massalhangzo. """
szavak = []
for a in szotar.values():
    if a["Hany massalhangzo van benne"] < a["Hany maganhangzo van benne"]:
        szavak.append(a["szo"])

print(" ".join(szavak))
print("Ennyi szot talaltam: {}".format(len(szavak)))
print("Osszesen egyi szo van az allomanyban: {}".format(len(szotar)))
print("{0}/{1} : {2}%".format(len(szavak),len(szotar),round(len(szavak)/len(szotar),2)))

print("4. feladat")
"""5.betus szavakat ki kell gyujteni es be kell kerni egy 3 betus szot a felhasznalotol es meg kell hatarozni azoknak a szolepcsoit."""
"""Kigyujtom a szoletrakoz az osszes 3 etuset az alabbi modon:
ot={
"kozepso 3 betu" : [hozza tartozo szolepcsok]
"kozepso 3 betu" : [hozza tartozo szolepcsok]
}
"""
ot = {}
n = 0
for a in szotar.values():
    if a['szo hossza'] == 5:
        elozo3 = "".join(list(a['szo'])[1:4])
        if elozo3 not in ot:
            ot[elozo3] = []
            ot[elozo3].append(a['szo'])
        else:
            ot[elozo3].append(a['szo'])

#print(ot)
szoreszlet = str(input("Kerem adjon be egy szoreszletet: "))
print("{}".format(" ".join(ot[szoreszlet])))

print("5. feladat")
"""Ki kell irni a letra.txt alomanyban azokat a szavakat amelyiknek van legalabbe egy parja egy szokozzel elvalaszva"""
with open("letra.txt", "wt",encoding="utf-8") as h:
    for a, s in ot.items():
        if len(s) > 2:
            for d in s:
                h.write(str(d)+"\n")
            h.write("\n")




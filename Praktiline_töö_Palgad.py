from module1 import *
palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]

print("Palgad")
print("MENU\n",
      "1. Lisada mitu inimest ja nende palgad;\n",
      "2. Isiku ja tema palga kustutada(nimi sisestab kasutaja);\n",
      "3. Leida kes saab kätte suurim palk;\n",
      "4. Leida kes saab kätte kõige väiksem palk ja milline ta on;\n",
      "5. Järjestada palgad kasvavas ja kahanevas järjekorras koos nimedega;\n",
      "6. Teada saada, kes saavad võrdset palka, leida, kui palju neid on ja kuvada nende andmed ekraanile;\n",
      "7. Teha palgaotsing isiku nime järgi. Pange tähele, et nimed võivad korduda;\n",
      "11. Arvutage palk, mille inimene saab kätte pärast tulumaksu arvestamist;\n",
      "12. Sorteeri nime järgi (kasutajale võib anda valiku: A-st Z-ni või Z-st A-ni);\n",
      "13. Leida need, kes saavad alla keskmise palka, ja eemaldada nad nimekirjadest;\n",
      "14. Muuda nimekirju nii, et inimeste nimekirjas kirjutatakse nimed suure algustähega, palkade kohta int formaadis;\n",
      "20. Väljumine.")
while 1:
    try:
        valik=int(input("Valik: "))
        if valik==1:
            valik1(palgad, inimesed)
        elif valik==2:
            valik2(palgad, inimesed)
        elif valik==3:
            valik3(palgad, inimesed)
        elif valik==4:
            valik4(palgad, inimesed)
        elif valik==5:
            valik5(palgad, inimesed)
        elif valik==6:
            valik6(palgad, inimesed)
        elif valik==7:
            valik7(palgad, inimesed)
        elif valik==11:
            valik11(palgad, inimesed)
        elif valik==12:
            valik12(palgad, inimesed)
        elif valik==13:
            valik13(palgad, inimesed)
        elif valik==14:
            valik14(palgad, inimesed)
        elif valik==20:
            break
        else:
            print("Ввебире от 1 до 20!")
    except ValueError:
        print("valik on arv!")
   
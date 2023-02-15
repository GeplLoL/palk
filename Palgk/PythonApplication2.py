from modul1 import *
palgad=[1200,2500,750,750,3200,1000]
inimesed=["A","B","C","D","D","A"]
while True:
    print(inimesed)
    print(palgad)
    menu=int(input("Valik:\n1-Lisa andmed\n2-Kustuta andmed\n3-Suurim palk\n4-Min palk kellel\n5-Sort\n6-Võrdsed palkad kellel on\n7-otsi palka inimese nime järgi\n8-Kuva nimekiri inimestest (palgaga), kes saavad määratud summast rohkem/vähem.\n9-3 vaesemat ja rikkaimat inimest\n10-Keskmine palk ja selle saaja nimi\n11-Arvutage välja palk, mille inimene pärast tulumaksu arvestamist oma kätte saab.\n12-Sorteeri nime järgi\n13-Otsige üles need, kes saavad alla keskmise palka ja eemaldage nad nimekirjadest.\n14-kirjutatud suure algustähega, palkade kohta int formaadis.\n15-milline saab olema teatud töötaja palk/palk T aasta pärast.\n16-Nimeta ümber iga kolmas isik."))
    if menu==0:
        break
    elif menu==1:
        inimesed,palgad=Lisa_andmed(inimesed,palgad)
    elif menu==2:
        inimesed,palgad=Kustutamine(inimesed,palgad)
    elif menu==3:
        palk,nimi=Suurim_palk(inimesed,palgad)
        print(f"Suurim palk on {palk} {nimi}´l")
    elif menu==4:
        print(maks(inimesed,palgad))
    elif menu==5:
        inimesed,palgad=Sorteerimine(inimesed,palgad)
    elif menu==6:
        Vordsed_palgad(inimesed,palgad)
    elif menu==7:
        leia_palga_summa(inimesed,palgad)
    elif menu==8:
        listok(inimesed,palgad)
    elif menu==9:
        suurem_vaiksem(inimesed,palgad)
    elif menu==10:
        keskmine(inimesed,palgad)
    elif menu==11:
        tulumaks(inimesed,palgad)
    elif menu==12:
        palgad,inimesed=Sorteerimine(palgad,inimesed)
    elif menu==13:
        inimesed,palgad=Kustuta(inimesed,palgad)
    elif menu==14:
        inimesed,palgad=Inlet(inimesed,palgad)
        print(inimesed,palgad)
    elif menu==15:
        upZP(inimesed,palgad)
    elif menu==16:
        inimesed=rename(inimesed)
        print(inimesed,palgad)
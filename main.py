from parametry.databaze import seznam_druhu, seznam_uvod, nazvy_druhu
import time
print(seznam_uvod)

while True:
    def vypocet_paleni(rychlost, delka_zapalu, celkova_delka, pocet_zapalu):

        vypaleni_1ks = round(
            ((celkova_delka / rychlost) + ((delka_zapalu+2) * pocet_zapalu) / 60), 3)
        return vypaleni_1ks

    druh_plechu = input("Pro výpočet zadej číslo požadovaného materiálu:")
    if str(druh_plechu).isdigit() == False:
        print("Vložil jste zakázaný znak. Program příjmá pouze čísla v rozsahu 1 -",
              (len(seznam_druhu)+1), ".")
        break
    elif int(druh_plechu) >= (len(seznam_druhu)+1) or druh_plechu == 0:
        print("Zadal jste číslo menší než 1, nebo větší než",
              len(seznam_druhu), ".")
        break
    nazev_vyrobku = input("Zadejte název výrobku:")
    celkova_delka = float(input("Zadej celkovou délku(v mm):"))
    pocet_zapalu = int(input("Zadej počet zápalů:"))
    pocet_kusu_celkem = int(input("Zadej celkový počet kusů:"))
    # Aby čísla druhů plechů začínali jedničkou, a ne nulou.
    druh_plechu = int(druh_plechu) - 1
    print("\nPro výrobek", nazev_vyrobku, "jste zvolil materiál",
          nazvy_druhu[druh_plechu], ".", "\n\nCelková délka je:", celkova_delka, "\nPočet zápalů je:", pocet_zapalu, "\nCelkový počet kusů je:", pocet_kusu_celkem, "ks")

    vysledek = vypocet_paleni(
        seznam_druhu[druh_plechu][0], seznam_druhu[druh_plechu][1], celkova_delka, pocet_zapalu)

    timestr = time.strftime("%d.%m.%Y \n")
    tohlepripravkprevodu = f"Jeden kss se vypálí za {vysledek} minuty. {pocet_kusu_celkem} ks se vypálí za", round(
        (pocet_kusu_celkem * vysledek), 3,)
    prevedeno = str(tohlepripravkprevodu)
    prevedeno1 = timestr + prevedeno + "." + ("\n")
    prevedeno2 = prevedeno1.replace("(", "").replace(
        ")", "").replace(",", "").replace("'", "")
    print("Jeden ks výrobku ", nazev_vyrobku,
          "se vypálí za", vysledek, "minut.")
    print(pocet_kusu_celkem, "kusů se vypálí za", round(
        (pocet_kusu_celkem * vysledek), 3), "minuty.")
    f = open("Kalkulace.txt", "a")
    f.write(prevedeno2)
    f.close()

    pokracovat = input(
        'Chcete provést kalkulaci pálení pro další výrobek? (a/n)')
    if pokracovat == 'n':
        print("Děkujeme za využívání softwaru LasKal. Výstup/y byli uloženy do složky C:\Program Files\LasKal\Kalkulace.txt.")
        break
    elif pokracovat != "a":
        print("Zvolil/a jste nesprávný znak. Program se teď ukončí.")
        break
    elif pokracovat == "a":
        False

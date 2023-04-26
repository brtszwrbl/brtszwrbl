# dzien = "1"
# miesiac = 5
# rok = 2023
# print(f"siemaneczko {dzien} ziomeczki {miesiac} z tej strony gamergamer123pl {rok}")
# print(dzien+miesiac)
# print(dzien + "pies" + "1")

# print("Ile masz lat?")
# wiek = input()

# print(f"Masz {wiek} lat")
# print(f"Za rok będzie mieć {int(wiek)+1} lat")


# print("Jak masz na imię?")
# imie = input()
# print(f"Siema {imie}! ")
# print("Ile masz lat?")
# wiek = int(input())
# print(f"Za rok będziesz mieć {wiek+1} lat!")


# print("Podaj pierwszą liczbę:")
# liczba = int(input())
# print("Podaj drugą liczbę:")
# liczba1 = int(input())
# print(f"Wynikiem dodawania tych liczb jest: {liczba + liczba1}")
# print(f"Wynikiem odejmowania tych liczb jest: {liczba - liczba1}")
# print(f"Wynikiem mnożenia tych liczb jest: {liczba * liczba1}")
# print(f"Wynikiem dzielenia tych liczb jest: {liczba / liczba1}")


# print("Ile masz lat?")
# wiek = int(input())
# print(f"Żyjesz już {wiek * 31 536 000 ")
# print(f"To składa się na {wiek * 365} dni")
# print(f"{wiek * 365 * 24} godzin")


# print("Ile masz lat?")
# wiek = int(input())
# if wiek >= 18:
#     print("Gratulacje!")
#     print("Jesteś pełnoletni!")
# else:
#     print("dziabadziaba")
# print("siemanko")


# print("Ile masz lat?")
# wiek = int(input())
# if wiek <= 3:
#     print("Jesteś maluczki")
# elif wiek < 12:
#     print("Jestś dzieciak i tyle")
# elif wiek < 20:
#     print("Jesteś teenage dirtbag")
# else:
#     print("Parostatkiem w piękny rejs")


# print("Podaj wartość pierwszego wyrazu logicznego:")
# p=int(input())
# print("Podaj wartość drugiego wyrazu logicznego:")
# q=int(input())

# if p and q:
#     print("Prawda")
# else:
#     print("Fałsz")


# print("Czy masz ochotę napić się piwa?")
# decyzja1=input()

# if decyzja1 == "tak":
#     print("Czy masz 18 lat?")
#     decyzja2=input()
#     if decyzja2 == "tak":
#         print("Śmiało!")
#     elif decyzja2 == "nie":
#         print("Lipa, młody")
#     else:
#         print("Naucz się pisać")
# elif decyzja1 == "nie":
#     print("Bardzo dobrze")
# else:
#     print("Naucz się pisać")

# print("Podaj liczbe")
# licz = int(input())
# if licz % 2 == 0:
#     print("gj")
# if licz % 2 > 0:
#     print("asdasd")


# print("Podaj pierwszą liczbę")
# l1 = int(input())
# print("Podaj drugą liczbę:")
# l2 = int(input())
# print("Co chcesz zrobić z tymi liczbami? (dodać, odjąć, pomnożyć, podzielić)")
# odp = input()
# if odp == "dodać":
#     print(f"Wynikiem dodawania tych liczb jest: {l1 + l2}")
# elif odp == "odjąć":
#     print(f"Wynikiem odejmowania tych liczb jest: {l1 - l2}")
# elif odp == "pomnożyć":
#     print(f"Wynikiem mnożenia tych liczb jest: {l1 * l2}")
# elif odp == "podzielić":
#     print(f"Wynikiem dzielenia tych liczb jest: {l1 / l2}")
# else:
#     print("Naucz się pisać")




# def dodawanie(liczba1,liczba2):
#     suma = liczba1 + liczba2
#     return suma
# def mnozenie(liczba1,liczba2):
#     iloczyn = liczba1 * liczba2
#     return iloczyn

# # print("Podaj liczby:")
# # pierwsza=int(input())
# # druga = int(input())
# # dodawanie(pierwsza, druga)
# # mnozenie(pierwsza,druga)

# print("Podaj liczby:")
# liczba1= int(input())
# liczba2 = int(input())
# dodawanie(liczba1,liczba2)
# wynik1 = dodawanie(liczba1,liczba2)
# wynik2 = mnozenie(liczba1,liczba2)
# print(dodawanie(liczba1,liczba2))
# print(mnozenie(liczba1,liczba2))
# print(wynik1)
# print(wynik2)

# 4,5,2,3,6,7,8,9,11,12

# def dlugosc(x):
#     dlg = 0
#     for element in lista:
#         dlg += 1
#     return dlg


# def maksimum(lista):
#     najwiekszy = lista[0]
#     for element in lista:
#         if element > najwiekszy:
#             najwiekszy = element
#     return najwiekszy


# def minimum(lista):
#     najmniejszy = lista[0]
#     for element in lista:
#         if element < najmniejszy:
#             najmniejszy=element
#     return najmniejszy
 
# def ostatni(lista):
#     ostatni_element = lista[-1]
#     return ostatni_element


# def ogon(lista):
#     del(lista[0])
#     return lista
#     # return lista[1:]


# def nta(lista,n):
#     return lista[n]


# def alternatywa(p,q):
#     if p == 1 or q == 1:
#         return 1
#     else:
#         return 0
#     # if p+q > 0:
#     #     return 1
#     # else:
#     #     return 0

# def koniunkcja(p,q):
#     if p == 1 and q == 1:
#         return 1
#     else:
#         return 0


# def implikacja(p,q):
#     if p == 1 and q == 0:
#         return 0
#     else:
#         return 1
        # if p > q:
        #     return 0
        # else:
        #     return 1


# def tydzien(x):
# SŁOWNIK
#     if x == 1:
#         print("poniedziałek")
#     elif x == 2:
#         print("wtorek")
#     elif x == 3:
#         print("środa")
#     elif x == 4:
#         print("czwartek")
#     elif x == 5:
#         print("piątek")
#     elif x == 6:
#         print("sobota")
#     elif x == 7:
#         print("niedziela")
# RETURN SŁOWNIK(CHOICE)

# def gwiazdki(liczba):
#     return "*"*liczba



# lista = [1,2,3,4,7,5,2,62,54]
# dlugosc_listy = dlugosc(lista)
# maksimum_listy = maksimum(lista)
# minimum_listy = minimum(lista)
# ostatni_element_listy = ostatni(lista)
# bezpierwszego = ogon(lista)
# print(dlugosc_listy)
# print(maksimum_listy)
# print(minimum_listy)
# print(ostatni_element_listy)
# print(bezpierwszego)
# print("wpisz dzien")
# dzien = int(input())
# tydzien(dzien)
# print("wpisz liczbe")
# liczba = int(input())
# print(gwiazdki(liczba))



# def prostokąt(dlg,szr,element=4):
#         for i in range(dlg):
#                 for j in range(szr):
#                         print(element,end=' ')
#                 print()

# prostokąt(2,3)
# prostokąt(2,4,'ojoj')


# def silnia(liczba):
#         if liczba == 5:
#                 return 120
#         else:
#                 return liczba * silnia(liczba-1)

# wynik = silnia(7)
# print(wynik)


# def sumowanie(listaliczb):
#         if len(listaliczb) > 0:
#                 return listaliczb[0] + sumowanie(listaliczb[1:])
#         else:
#                 return 0

# lista=[1,2,3,4,5,7]
# wynik=sumowanie(lista)
# print(wynik)


# def dlugosc(x):
        # if not lista == []:
#         if len(x) > 0:
#                 return 1 + dlugosc(x[1:])
#         else:
#                 return 0

# lista=[1,2,3,4,5,6,7,8,9]
# wynik=dlugosc(lista)
# print(wynik)


# def ostatni(x):
#         if len(x) > 1:
#                 return ostatni(x[1:])
#         else:
#                 return x

# lista=[9,5,2,88]
# wynik=ostatni(lista)
# print(wynik)


# def sprawdzanie(lista,x):
#         if len(lista) == 0:
#                 return "nie"
#         elif lista[0] == x:
#                 return "tak"
        
#         else:
#                 return sprawdzanie(lista[1:],x)

# lista=[1,2,3,4,5,6]
# wynik = sprawdzanie(lista,87)
# print(wynik)
                
        

# def nta(lista,x):
#         if  x == 1:
#                 return lista[0]
#         else:
#                 return nta(lista[1:],x-1)

# lista=[13,32,631,114,51]
# wynik=nta(lista,4)
# print(wynik)


def potega(liczba, wykladnik):
        if wykladnik == 0:
                return 1
        elif wykladnik == 1:
                return liczba
        elif wykladnik < 0:
                return 1/liczba*potega(liczba,wykladnik-1)
        elif wykladnik > 1:
                return liczba*potega(liczba, wykladnik -1)

liczba = int(input("Wpisz liczbę: "))
wykladnik = int(input("Wpisz wykładnik: "))
wynik = potega(liczba, wykladnik)
print(wynik)




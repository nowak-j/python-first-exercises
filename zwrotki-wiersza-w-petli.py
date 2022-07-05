# Rozważmy następujący tekst piosenki: 

#     10 mrówek maszeruje raz i dwa,
#     bucikami przytupuje raz i dwa
#     jedna przystanęła, by zawiązać but
#     9 poszło dalej tup, tup, tup

#     9 mrówek maszeruje raz i dwa,
#     bucikami przytupuje raz i dwa
#     jedna przystanęła, by zawiązać but
#     8 poszło dalej tup, tup, tup
#     ...
#     5 mrówek maszeruje raz i dwa,
#     bucikami przytupuje raz i dwa
#     jedna przystanęła, by zawiązać but
#     4 poszło dalej tup, tup, tup

#     4 mrówki maszerują raz i dwa,
#     bucikami przytupują raz i dwa
#     jedna przystanęła, by zawiązać but
#     3 poszły dalej tup, tup, tup
#     ...
#     2 mrówki maszerują raz i dwa,
#     bucikami przytupują raz i dwa
#     jedna przystanęła, by zawiązać but
#     druga poszła dalej tup, tup, tup

#     1 mrówka maszeruje raz i dwa,
#     bucikami przytupuje raz i dwa
#     jedna przystanęła, by zawiązać but
#     9 do niej doszło tup, tup, tup

# Jak można zaobserwować powyższy tekst powtarza się w wielu miejscach. 
# Napisz program, który jako argument podany przez użytkownika poda dwie liczby aa i bb. Wynikiem działania skryptu ma być wyświetlenie zwrotki od aa do bb. 
# W przypadku nieprawidłowych danych program ma wypisać komunikat BŁĄD. Program nie ma wychodzić w tym przypadku z kodem błędu.

liczby = list(map(int,input().split()))
a = liczby[0]
b= liczby[1]

if a > 10 or a < 1 or b > 10 or b < 1:
    print("BŁĄD")
    exit()

for zwrotka in range(a, b-1, -1):
    if zwrotka == 1:
        print (f"{zwrotka} mrówka maszeruje raz i dwa,\nbucikami przytupuje raz i dwa\njedna przystanęła, by zawiązać but\n9 do niej doszło tup, tup, tup")
    elif zwrotka == 2:
        print (f"{zwrotka} mrówki maszerują raz i dwa,\nbucikami przytupują raz i dwa\njedna przystanęła, by zawiązać but\ndruga poszła dalej tup, tup, tup")
        print("")
    elif zwrotka > 2 and zwrotka <= 4:
        print (f"{zwrotka} mrówki maszerują raz i dwa,\nbucikami przytupują raz i dwa\njedna przystanęła, by zawiązać but\n{zwrotka -1} poszły dalej tup, tup, tup")
        print("")
    elif zwrotka > 4 and zwrotka <= 10:
        print (f"{zwrotka} mrówek maszeruje raz i dwa,\nbucikami przytupuje raz i dwa\njedna przystanęła, by zawiązać but\n{zwrotka -1} poszło dalej tup, tup, tup")
        print("")

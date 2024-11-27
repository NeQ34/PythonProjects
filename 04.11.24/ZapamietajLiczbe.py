import random
import time

proby = 0
punkty = 0
delay = 2

print("Witaj w grze zapamiętaj liczbę!")
print(f"Użytkownik musi zapamiętać wylosowaną przez komputer 5-cio cyfrową liczbę, jest to {delay} sekund")
print("Jest 5 rund, każda zapamiętana liczba to +1 punkt")
print("Powodzenia!")
time.sleep(delay)
while proby < 5:
    a,b,c,d,e = [random.randint(0, 9) for _ in range(5)]
    print("\n")
    print(f"Liczba do zapamiętania: {a} {b} {c} {d}")
    time.sleep(delay)
    for _ in range(10):
        print("\n")
    liczba = input("Podaj zapamiętaną liczbę: ")
    if(int(liczba) == int(f"{a}{b}{c}{d}")):
        print("Poprawnie zapamiętałeś liczbę!")
        punkty += 1
    else:
        print("Źle zapamiętałeś liczbę!")
    proby += 1
    time.sleep(2)
    for _ in range(10):
        print("\n")

print(f"Koniec gry, zdoyłeś {punkty} punkty na {proby} prób")
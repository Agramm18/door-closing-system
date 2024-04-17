

Status = input("Geben sie an ob die Türe offen oder geschlossen ist: ")

while True:
    if Status == "offen":
        tuer_status = True
        Ergebnis = print("Türe ist offen", tuer_status)
        break

    elif Status == "geschlossen":
        tuer_status = False
        Ergebnis = print("Die Türe ist geschlossen", tuer_status)
        break

    elif Status == "":
        tuer_status = False
        Ergebnis = input("Geben sie bitte offen oder geschlossen an: ")

    else:
        Status = "Ende" or "ende"
        break

if tuer_status:
    Anfrage = input("Wollen sie die Türe offen oder geschlossen lassen?: ")

    if Anfrage.lower() == "schließen":
        tuer_status = False
        print(tuer_status, "Türe wird geschlossen")

    else:

        tuer_status = True
        print(tuer_status, "Türe ist bereits geschlossen")



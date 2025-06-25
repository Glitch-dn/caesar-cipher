'''CIFRARIO DI CESARE
Questo modulo implementa il cifrario di Cesare, un semplice metodo di cifratura a sostituzione.'''


from utility import *


def menu():
    """
    MOSTRA UN MENÙ ALL'UTENTE PER SCEGLIERE SE CIFRARE O DECIFRARE UN MESSAGGIO.

    RITORNA:
    - 'CIFRA' SE L'UTENTE SCEGLIE 1
    - 'DECIFRA' SE L'UTENTE SCEGLIE 2
    """
    while True:
        print("\n" + "-" * 30)
        print("       CIFRARIO DI CESARE")
        print("-" * 30 + "\n")
        print("SCEGLI UN'OPZIONE:")
        print("0. MOSTRA I MESSAGGI CIFRATI E DECIFRATI")
        print("1. CIFRA UN MESSAGGIO")
        print("2. DECIFRA UN MESSAGGIO")
        print("3. ESCI\n")
        scelta = input("SCEGLI UN'OPZIONE (1, 2, 3):\n ")
        if scelta == "0":
            mostra_messaggi("files")
        elif scelta == "1":
            # INIZIA A CIFRARE IL MESSAGGIO
            messaggio = leggi_messaggio()
            print(f"\nMESSAGGIO DA CIFRARE: {messaggio}\n")
            chiave = scegli_chiave()
            messaggio_cifrato = cifra_messaggio(messaggio, chiave)
            salva_su_file("files", "messaggio_cifrato", messaggio_cifrato)
        elif scelta == "2":
            # INIZIA A DECIFRARE IL MESSAGGIO
            messaggio_cifrato = leggi_messaggio()
            chiave = scegli_chiave()
            messaggio_decifrato = decifra_messaggio(messaggio_cifrato, chiave)
            salva_su_file("files", "messaggio_decifrato", messaggio_decifrato)
        elif scelta == "3":
            print("👋 ARRIVEDERCI!")
            return
        else:
            print("❌ SCELTA NON VALIDA. RIPROVA.")

# Avvia il programma
menu()


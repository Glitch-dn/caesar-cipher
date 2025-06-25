
import os

def salva_su_file(cartella, prefisso, contenuto, estensione=".txt"):
    """
    SALVA IL CONTENUTO IN UN FILE NELLA CARTELLA SPECIFICATA.
    IL NOME DEL FILE SARÀ BASATO SU UN PREFISSO E UN NUMERO PROGRESSIVO.

    PARAMETRI:
    - cartella: la directory dove salvare il file
    - prefisso: il prefisso del nome file (es. 'messaggio_cifrato')
    - contenuto: il testo da scrivere
    - estensione: estensione del file (default '.txt')
    """
    os.makedirs(cartella, exist_ok=True)

    # Trova file esistenti con lo stesso prefisso
    esistenti = [
        f for f in os.listdir(cartella)
        if f.startswith(prefisso) and f.endswith(estensione)
    ]
    prossimo_idx = len(esistenti) + 1

    nome_file = f"{prefisso}{prossimo_idx}{estensione}"
    percorso = os.path.join(cartella, nome_file)

    with open(percorso, "w", encoding="utf-8") as file:
        file.write(contenuto)

    print(f"✅ {prefisso.upper()} SALVATO IN: {percorso}\n")

def mostra_messaggi(cartella="files"):
    """
    MOSTRA I MESSAGGI CIFRATI E DECIFRATI PRESENTI NELLA CARTELLA SPECIFICATA.

    PARAMETRI:
    - cartella: la directory da cui leggere i file (default 'files')
    """
    try:
        files = os.listdir(cartella)
        if not files:
            print("❌ NESSUN MESSAGGIO TROVATO.")
            return

        print("\n--- MESSAGGI TROVATI ---\n")
        for file in files:
            if file.endswith(".txt"):
                print(f"- {file}")
        scelta = input("\nINSERISCI IL NOME DEL FILE (con estensione) PER VISUALIZZARNE IL CONTENUTO:\n ")
        percorso_file = os.path.join(cartella, scelta)
        if os.path.isfile(percorso_file):
            with open(percorso_file, 'r', encoding='utf-8') as file:
                contenuto = file.read()
            print(f"\nCONTENUTO DI '{scelta}':\n{contenuto}\n")
        else:
            print(f"❌ IL FILE '{scelta}' NON ESISTE NELLA CARTELLA '{cartella}'.")
    except FileNotFoundError:
        print(f"❌ LA CARTELLA '{cartella}' NON ESISTE.")

def scegli_chiave():
    """
    CHIEDE ALL'UTENTE DI INSERIRE UNA CHIAVE PER LA CIFRATURA O DECIFRATURA.

    RITORNA:
    - LA CHIAVE INSERITA DALL'UTENTE COME INTERO
    """
    while True:
        try:
            chiave = int(input("INSERISCI LA CHIAVE (NUMERO INTERO):\n "))
            return chiave
        except ValueError:
            print("❌ VALORE NON VALIDO. RIPROVA.")

def leggi_messaggio():
    """
    CHIEDE ALL'UTENTE DI INSERIRE UN MESSAGGIO DA CIFRARE O DECIFRARE TRAMITE INSERIMENTO MANUALE O DA FILE.

    RITORNA:
    - IL MESSAGGIO INSERITO DALL'UTENTE
    """
    while True:
        print("\n--- INSERISCI IL MESSAGGIO DA CIFRARE O DECIFRARE:\n ---")
        print("1. MANUALMENTE")
        print("2. CARICA DA FILE\n")
        scelta = input("SCEGLI UN'OPZIONE (1, 2):\n ")

        if scelta == "1":
            return input("INSERISCI IL MESSAGGIO:\n ")
        elif scelta == "2":
            nome_file = input("INSERISCI IL PERCORSO DEL FILE:\n ")
            try:
                with open(nome_file, 'r', encoding='utf-8') as file:
                    return file.read().strip()
            except FileNotFoundError:
                print(f"❌ IL FILE '{nome_file}' NON ESISTE. RIPROVA.")
        else:
            print("❌ SCELTA NON VALIDA. RIPROVA.")

def cifra_messaggio(messaggio, chiave):
    """
    CIFRA UN MESSAGGIO UTILIZZANDO IL CIFRARIO DI CESARE.

    PARAMETRI:
    - messaggio: Il messaggio da cifrare.
    - chiave: La chiave di cifratura (numero intero).

    RITORNA:
    - Il messaggio cifrato.
    """
    cifrato = ""
    for char in messaggio:
        if char.isalpha():  # Verifica se il carattere è una lettera
            offset = 65 if char.isupper() else 97  # Determina l'offset per lettere maiuscole o minuscole, se la condizione è vera, l'offset viene impostato a 65, che corrisponde al valore ASCII della lettera maiuscola 'A'. In caso contrario, l'offset viene impostato a 97, che corrisponde al valore ASCII della lettera minuscola 'a'.
            cifrato += chr((ord(char) - offset + chiave) % 26 + offset)
            # Converte il carattere in ASCII, calcola la posizione relativa (maiusc/minusc), applica la chiave con modulo 26, riconverte in carattere e lo aggiunge alla stringa cifrata
        else:
            cifrato += char  # Mantiene i caratteri non alfabetici invariati
    return cifrato

def decifra_messaggio(messaggio, chiave):
    """
    DECIFRA UN MESSAGGIO UTILIZZANDO IL CIFRARIO DI CESARE.

    PARAMETRI:
    - messaggio: Il messaggio da decifrare.
    - chiave: La chiave di decifratura (numero intero).
    RITORNA:
    - Il messaggio decifrato.
    """
    return cifra_messaggio(messaggio, -chiave)  # Inverte la chiave per decifrare

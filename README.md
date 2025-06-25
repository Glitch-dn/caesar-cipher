# Cifrario di Cesare

Questo progetto implementa il **Cifrario di Cesare** in Python, un semplice metodo di crittografia a sostituzione in cui ogni lettera del messaggio originale viene sostituita da un'altra lettera, spostata di un numero fisso di posizioni nell'alfabeto.

## Funzionalità

- **Cifratura** di un messaggio testuale tramite chiave numerica (shift)
- **Decifratura** di un messaggio cifrato usando la stessa chiave
- Salvataggio automatico dei messaggi cifrati/decifrati su file, con numerazione progressiva
- Possibilità di leggere un messaggio da cifrare/decifrare sia da input manuale che da file
- Gestione di caratteri non alfabetici (che restano invariati)
- Menu interattivo per scegliere le varie opzioni

## Come funziona

Avvia il programma per accedere al menu, che permette di:

1. **Mostrare i messaggi cifrati e decifrati** presenti nella directory `files/`
2. **Cifrare un nuovo messaggio** (da tastiera o da file)
3. **Decifrare un messaggio** (da tastiera o da file)
4. **Uscire dal programma**

Ogni messaggio cifrato/decifrato viene salvato automaticamente in un file di testo nella cartella `files/`.

## Esempio d’uso

```bash
python main.py
```

### Esempio di cifratura

```
SCEGLI UN'OPZIONE (1, 2, 3): 1
INSERISCI IL MESSAGGIO: CIAO MONDO
INSERISCI LA CHIAVE (NUMERO INTERO): 3
✅ MESSAGGIO_CIFRATO SALVATO IN: files/messaggio_cifrato1.txt
```

### Esempio di decifratura

```
SCEGLI UN'OPZIONE (1, 2, 3): 2
INSERISCI IL MESSAGGIO: FÏDR PRQGR
INSERISCI LA CHIAVE (NUMERO INTERO): 3
✅ MESSAGGIO_DECIFRATO SALVATO IN: files/messaggio_decifrato1.txt
```

## Struttura del progetto

- `main.py` — Script principale con il menu e le funzioni di cifratura/decifratura
- `utility.py` — Funzioni di utilità usate dal programma
- `files/` — Directory dove vengono salvati i messaggi cifrati e decifrati

## Requisiti

- Python 3.x

## Avvio

1. Clona il repository:
    ```bash
    git clone https://github.com/Glitch-dn/caesar-cipher.git
    cd caesar-cipher
    ```

2. Esegui il programma:
    ```bash
    python main.py
    ```

## Note

- I file di output (messaggi cifrati/decifrati) sono tutti in `files/`.
- Puoi scegliere la chiave che preferisci: valori negativi decaleranno le lettere all’indietro.
- Il programma gestisce sia lettere maiuscole che minuscole; tutti gli altri caratteri non vengono modificati.

## Licenza

Questo progetto è distribuito con licenza MIT.

---

**Autore:** [Glitch-dn](https://github.com/Glitch-dn)

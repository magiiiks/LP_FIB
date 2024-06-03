# L'analitzador de tipus HinNer

## Descripció
Aquest projecte és un "Compilador" d'un llenguatge tipus Haskell per a la assignatura de Llenguatges de programació de la FIB.

## Continguts

- Arxiu hm.g4 on està definida la gramàtica del llenguatge.
- Arxiu hm.py amb el programa del intèrpret i el seu visitador.

## Requisits

- antlr4 instalat al ordinador
- streamlit per a poder executar el programa

## Ús

Per a poder executar aquest programa hem de compilar la gramàtica amb la comanda:

```bash
antlr4 -Dlanguage=Python3 -no-listener -visitor hm.g4

```
Després hem d'executar el programa principal amb streamlit amb la comanda:

```bash
streamlit run hm.py
```

Cal destacar que hi ha funcionalitats de l'analitzador que només es duen a terme si son possibles. Per exemple: No es realitza inferència de tipus si no tenim tipus emmagatzemats en la taula. Per tant si volem que l'analitzador realitzi totes les funcions possibles, primer s'han de declarar els tipus i després les funcions a analitzar.

## Autor

**Magí Rull Jiménez** - *L'analitzador de tipus HinNer* - [GitHub](https://github.com/magiiiks/LP_FIB)
# L'analitzador de tipus HinNer

## Descripció
Aquest projecte és un "Compilador" d'un llenguatge tipus Haskell per a la assignatura de Llenguatges de programació de la FIB.

## Continguts

- Arxiu .g4 on està definida la gramàtica del llenguatge.
- Arxiu hm.py amb el programa del intèrpret i els seu visitador.

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

## Autor

**Magí Rull Jiménez** - *L'analitzador de tipus HinNer* - [GitHub](https://github.com/magiiiks/LP_FIB)
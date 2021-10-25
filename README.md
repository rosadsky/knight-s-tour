
#  Zadanie 2 - Prehľadávanie stavového priestoru  
Roman Osadský
Predmet: Umelá inteligencia 
Cvičiaci: Ing. Boris Slíž
IDE: PyCharm 2021.2.2
CPU: 2,3 GHz Dual-Core Intel Core i5
RAM: 8 GB 2133 MHz LPDDR3
Jazyk: Python
Operačný systém: MacOS
## Riešený problém

**Eulerov kôň** - Úlohou je prejsť šachovnicu legálnymi ťahmi šachového koňa tak, aby každé políčko šachovnice bolo prejdené (navštívené) práve raz. Riešenie treba navrhnúť tak, aby bolo možné problém riešiť pre štvorcové šachovnice rôznych veľkostí (minimálne od veľkosti 5 x 5 do 20 x 20) a aby cestu po šachovnici bolo možné začať na ľubovoľnom východziom políčku.

## Riešenie 

###  Stručný opis riešenia 

Riešenie je rekurzívna metóda vyhľadávania do hĺbky, do ktorej je zakomponované Warnsdorfe pravidlo.  Program načítava zo vstupu veľkosť šachovnice zo vstupu, a X,Y súradnice políčka z ktorého bude program začínať. 

### Postup fungovania algoritmu:

 1. Funkcia `solveDPS` sa zavolá
 2.  Program do premennej `positions` načíta pomocou `checkHorseInChessboard(chessboard_size, position_x, position_y, x_move, y_move, chessboard)` všetky možné políčka kam môže kôň isť 
 3.  `positions` sa zoradia  poďla Warnsdorfoveho pravidla od tých ktoré na majú najmenej dalších krokov toto zabezpečí metóda `bubblesort`
 4.  Cyklus ktorý iteruje cez `positions` a ide sa presunúť na nové políčko 
 5. Ak je daná pozícia správna tak sa na nu pripíše číslo iterácie a kôň sa na nu presunie
 6. Následne sa zavolá znova funckia `solveDPS `
 7. Ak už riešenia neexistujú tak program sa postupne vracia a hľadá riešenia
 
### Reprezentácia údajov	

#### Možné pohyby koňa sú reprezentované
```python
x_move = [2, 1, -1, -2, -2, -1, 1, 2]  
y_move = [1, 2, 2, 1, -1, -2, -2, -1]
```
#### Vytvorenie poľa vyplneného -1
```python
chessboard = [[-1 for i in range(chessboard_size)] for i in range(chessboard_size)]
```

#### Presun po šachovnici

```python
new_postion_x = i[0]  
new_postion_y = i[1]
``` 



### Dôležité metódy 

#### checkHorseInChessbord()
Táto metóda vráti pole v ktorom sú všetky možné pohyby koňa a taktiež sa v tejto metóde používa metóda `moveValidation` aby nenastala kombinácia ktorá je mimo hracej plochy.
```python
def checkHorseInChessboard(chessboard_size, position_x, position_y, x_move, y_move,chessboard):  
    layout = []  
    for i in range(8):  
        if moveValidation(position_x + x_move[i], position_y + y_move[i], chessboard_size,chessboard):  
            layout.append([position_x + x_move[i], position_y + y_move[i]])  
    return layout
```
#### moveValidation()

Metóda overuje či daná súradnica sa nachádza v šachovnici a či na danej súracnici sa nachádza -1 aby sa kôň mohol na nu presunúť. 
```python
def moveValidation(position_x, position_y, chessboard_size,chessboard):  
    if position_x >= 0 and position_x < chessboard_size and position_y >= 0 and position_y < chessboard_size and chessboard[position_x][position_y] == -1:  
        return True  
 else:  
        return False
```




# Testovanie
Testovanie programu prebiehali vo vývojovom prestredí PyCharm. Všetky otestované vstupy poli načítane z konzole PyCharm. Z testov je pekne vydieť kedy sa program musel vrátiť a skúšať iné pozície ako napríklad test č.3 kde program musel vykonať až 1734 krokov narozdiel od testu č.1 kde stačilo len 25 krokov.
|Test|Veľkosť šachovnice  | Pozícia X | Pozícia Y | Vykonaný čas (ms)  | Počet pohybov|
|--|--|--|--|--|--|
|1| 5x5 | 0 | 0 | 1.014 | 25 |
|2|5x5|1|2|8558.137|1028893*|
|3|5x5|0|2|24.71 |**1734**|
|4|5x5|2|2|1.22|25||
|5|6x6|3|3|4.002|**63**|
|6|6x6|5|5|1.56|36|
|7|7x7|0|0|2.205|**49**|
|8|8x8|1|1|2.791|64|
|9|8x8|3|7|3.14|64|
|10|10x10|3|5|8.317|100|
||1125x25|1|3|41.473|625|

*pre tento vstup program nenašiel riešenie 

# Zhodnotenie riešenia

Samotné Warnsdorfe pravidlo je veľmi efektívne a dokáže nájsť veľmi rýchlo správne riešenie. Ale pri niektorých vstupoch nestačilo na to aby cestu našlo. Vďaka prehladávaniu do hĺbky program sa dokáže vrátiť a skúšať iné cesty ktoré ktoré sú možno a pravdepodobnosť že riešenie program nájde sa omnoho zvýši. Nevýhodou prehľadávania do hĺbky je to že program má vyššiu časovú a pamäťovú náročnosť. 
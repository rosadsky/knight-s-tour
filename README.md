
#  Zadanie 2 - Prehľadávanie stavového priestoru  
Roman Osadský
Predmet: Umelá inteligencia 
Cvičiaci: Ing. Boris Slíž

## Riešený problém

**Eulerov kôň** - Úlohou je prejsť šachovnicu legálnymi ťahmi šachového koňa tak, aby každé políčko šachovnice bolo prejdené (navštívené) práve raz. Riešenie treba navrhnúť tak, aby bolo možné problém riešiť pre štvorcové šachovnice rôznych veľkostí (minimálne od veľkosti 5 x 5 do 20 x 20) a aby cestu po šachovnici bolo možné začať na ľubovoľnom východziom políčku.

## Riešenie 

Načíta sa zo vstupu veľkosť poľa následne zadá štartovací bod z ktorého sa kôň začne pohybovať. Vytvorí sa šachovnica, ktorá je repzrezentovaná na začiatku array `chessboard` kde na každom indexe sa nachádza číslo 0. 
Následne sa zovolá funkcia `windstoffAlgorithm(starting_position_x,starting_position_y,chessboard,x_move, y_move,chessboard_size):` kde sa celé riešenie problému odohráva. Program najprv vypočíta koľko možných pohybov musí vykonať aby zaplnil všetky políčka na šachovnici. Toto sa vypočíta pomocou `iterations = chessboard_size * chessboard_size - 1`


### For  v ktorom sa hľadá riešenie 

```python
for x in range(iterations):  
    positions = checkHorseInChessboard(chessboard_size, position_x, position_y, x_move, y_move, chessboard)  
    if(len(positions) == 0):  
        print("NO SOLUTION FOR THIS INPUT TRY ANOTHER ONE")  
        break  
  minimum = positions[0]  
  
    for possible_move in positions:  
        possible_move_positions = checkHorseInChessboard(chessboard_size,possible_move[0],possible_move[1],x_move,y_move,chessboard)  
        possible_minimum = checkHorseInChessboard(chessboard_size,minimum[0],minimum[1],x_move,y_move,chessboard)  
  
        if(len(possible_minimum) >= len(possible_move_positions) or len(minimum) == 0):  
            minimum = possible_move  
  
    moves_counter += 1  
  position_x = minimum[0]  
    position_y = minimum[1]  
    chessboard[position_x][position_y] = moves_counter
```

### Algoritmus 
Tento for cyklus sa opakuje toľko krát koľko krokov môže kôň pre daný rozmer šachovnice vykonať.
Program funguje tak že sa pozrie na to čo je stav do ktorého sa pozrieme a ako veľa dalších možných
stavov sa môže vytvoriť v ňom. Ďalší krok teda bude taký že sa vyberie ten stav ktorý ma najmenej možných
nasledujúcich krokov. Ako sa správna pozícia nájde kôň sa na nu prepisuje a `moves_counter` sa zvýši o 1.
Ako náhle prejdu všetky iterácie a nikde sa program nenastavil riešenie sa vypíše spolu s časovým údajom koľko trvalo
aby program našiel všetky cesty. Ako posledné sa zavolá funkcia finalCheck ktorá ešte preistotu prejde celú šachovnicu
a skontroluje či tam nieje 0. 

# Testovanie
|Veľkosť šachovnice  | Pozícia X | Pozícia Y | Vykonaný čas (ms)  | Počet pohybov|
|--|--|--|--|--|
| 5x5 | 0 | 0 | 0.709 | 25 |
|5x5|1|2|XXX|XXX*|
|5x5|3|4|XXX|XXX*|
|5x5|2|2|0.868|25||
|7x7|0|0|2.205|49|
|8x8|1|1|3.0|64|
|10x10|3|5|5.485|100|
|10x10|6|1|4.603|100|
|15x15|5|5|7.65|225|
|100x100|0|0|390.915|10000|
|255x255|50|50|2549.646|65025

*pre tento vstup program nenašiel riešenie 

## Zhrnutie

Na zlepšenie výsledku aby mohlo viac vstupov fungovať by bolo možno lepšie skúšať všetky možné možnosti ktoré 
kôň môže prejsť čo by ale zapríčinilo veľmi vysoký počet operácií a program by sa vykonával veľmi dlho.
Toto riešenie podľa Winsoff rule je celkom časovo nenáročné a s vysokou úspešnosťou, pretože program dokázal vyriešiť
šachovnicu o veľkosti 255x255 pomerne za dobrý čas. 
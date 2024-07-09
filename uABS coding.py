from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from fractions import Fraction
from math import floor, ceil
from random import randint
import struct

#ustalenie wartości x startowego
def codingBase(q:Fraction) -> int:
    (a, b) = (q.numerator, q.denominator)
    return ceil(Fraction(a, b - a))

#funkcja odpowiedzialna bezpośrednio za kodowanie
def coding(q:Fraction, s:int, x:int) -> int:
    if q <= Fraction(0, 1) or q >= Fraction(1, 1): return 0
    if s == 0:
        return ceil(Fraction(x + 1) / (Fraction(1) - q)) - 1
    if s == 1:
        return floor(Fraction(x) / q)
    return 0

#funkcja zwracająca wartość x, napisana na potrzeby testów
def codingSeq(q:Fraction, seq:[int]) -> int:
    x = codingBase(q)
    for i in seq:
        x = coding(q, i, x)
    return x

#funkcja zwracająca wartość kolejnego odkodowanego elementu w ciągu
def decodingS(q:Fraction, x:int) -> int:
    if x <= codingBase(q):
        return -1
    return ceil(Fraction(x + 1) * q) - ceil(Fraction(x) * q)

#funkcja zwracająca wartość kolejnej odkodowanej wartości x
def decodingX(q:Fraction, x:int) -> int:
    if x <= codingBase(q):
        return -1
    s = decodingS(q, x)
    x1 = ceil(Fraction(x) * q)
    x0 = x - x1
    if s == 1:
        return x1
    else:
        return x0

#funkcja odpowiedzialna za dekodowanie
def decoding(q:Fraction, x:int) -> (int, int):
    return (decodingS(q, x), decodingX(q, x))


#funkcja zwracająca kolejno odkodowywaną listę wartości x, napisana na potrzeby testów
def decodingSeq(q:Fraction, x:int) -> [int]:
    x0 = codingBase(q)
    if x <= x0:
        return []
    list = []
    while x > x0:
        s, x = decoding(q, x)
        list = [s] + list
    return list


#pomocnicza funkcja kodująca, napisana na potrzeby testów
def codingB(q:Fraction, s:int, x:int) -> int:
    return coding(1 - q, 1 - s, x)


#funkcja biorąca udział w dekodowaniu, napisana na potrzeby tesów, zwraca kolejną odkodowaną wartość w ciągu
def decodingSB(q:Fraction, x:int) -> int:
    return 1 - decodingS(1 - q, x)


#funkcja biorąca udział w dekodowaniu, napisana na potrzeby tesów, zwraca kolejną odkodowaną wartość x
def decodingXB(q:Fraction, x:int) -> int:
    return decodingX(1 - q, x)


#pomocnicza funkcja biorąca udział w dekodowaniu, napisana na potrzeby tesów
def decodingB(q:Fraction, x:int) -> (int, int):
    return (decodingSB(q, x), decodingXB(q, x))


#funkcja pomocnicza kodująca pierwszy wariant (wzór) kodowania na potrzeby testów
def testCodingA(inList, q:Fraction):
    x = x0 = codingBase(q)
    codingSequence = []
    decodedList = []
    for i in inList:
        codingSequence = [(i, x)] + codingSequence
        x = coding(q, i, x)
    x = coding(q, codingSequence[0][0], codingSequence[0][1])
    while x > x0:
        s, x = decoding(q, x)
        if (s, x) != codingSequence[0]:
            print('Error in decoding')
            return False
        codingSequence = codingSequence[1:]
        decodedList = [s] + decodedList
    print('Test results')
    print(f'Coded seq  : {inList}')
    print(f'Decoded seq: {decodedList}')
    if inList != decodedList:
        return False
    return True

#funkcja kodująca pierwszy wariant (wzór) kodowania na potrzeby testów
def testGenCodingA(n:int, length:int) -> bool:
    out = True
    b = 10
    for k in range(n):
        print(f'Test numer {k}')
        a = randint(1, b - 1)
        # a = randint(1, (b//2)-1)
        print(f'Wartosc q={Fraction(a,b)}')
        list = [randint(0, 1) for _ in range(length)]
        out = out and testCodingA(list, Fraction(a, b))
    return out

#funkcja pomocnicza kodująca drugi wariant (wzór) kodowania na potrzeby testów
def testCodingB(inList, q:Fraction):
    x = x0 = codingBase(1 - q)
    codingSequence = []
    decodedList = []
    for i in inList:
        codingSequence = [(i, x)] + codingSequence
        x = codingB(q, i, x)
    x = codingB(q, codingSequence[0][0], codingSequence[0][1])
    while x > x0:
        s, x = decodingB(q, x)
        if (s, x) != codingSequence[0]:
            print('Error in decoding')
            return False
        codingSequence = codingSequence[1:]
        decodedList = [s] + decodedList
    print('Test results')
    print(f'Coded seq  : {inList}')
    print(f'Decoded seq: {decodedList}')
    if inList != decodedList:
        return False
    return True

#funkcja kodująca drugi wariant (wzór) kodowania na potrzeby testów
def testGenCodingB(n:int, length:int) -> bool:
    out = True
    b = 10
    for k in range(n):
        print(f'Test numer {k}')
        a = randint(1, b - 1)
        print(f'Wartosc q={Fraction(a,b)}')
        list = [randint(0, 1) for _ in range(length)]
        out = out and testCodingB(list, Fraction(a, b))
    return out

#funkcja konwertująca ciąg znaków na sekwencję bajtów oraz zapisująca tę sekwencję do pliku
def write_into_binary_file(ciag_znakow, nazwa_pliku):
   bytes_list = [ciag_znakow[i:i + 8] for i in range(0, len(ciag_znakow), 8)]
   decimal_list = [int(byte, 2) for byte in bytes_list]
   text = ''.join(chr(decimal) for decimal in decimal_list)

   dane_bin = struct.pack("B" * len(text), *map(ord, text))

   with open(nazwa_pliku, "wb") as plik:
      plik.write(dane_bin)

#funkcja odpowiedzialna za procedurę kodowania
def encode_ans(ciag, file_path):
   print('Kodujemy')
   jeden = ciag.count("1")
   list = [int(x) for x in ciag]
   length = len(list)
   q = Fraction(jeden, length)
   start = codingBase(q)
   x = start
   xList = [1]
   lista_kodow = []
   for i in list:
      prev_x = x
      x = coding(q, i, x)
      if (x > (2 ** 64)):
         lista_kodow.append(prev_x)
         x = start
         x = coding(q, i, x)
         xList = [1] + xList
      xList = [x] + xList

   lista_kodow.append(x)
   with open(file_path, "wb") as file:
       file.write(jeden.to_bytes(8, 'big'))
       file.write(length.to_bytes(8, 'big'))
       for item in lista_kodow:
           file.write(item.to_bytes(8, 'big'))


#funkcja odpowiedzialna za procedurę dekodowania
def decode_ans(jeden, length, compressed_data, new_file_path):
    print("Dekodujemy")
    outList = []

    q = Fraction(jeden, length)
    start = codingBase(q)

    for x in compressed_data:
        tmp_outlist = []
        yList = [x]
        while x > start:
            t = decodingS(q, x)
            tmp_outlist = [t] + tmp_outlist
            y = decodingX(q, x)
            yList = [y] + yList
            x = y
        outList = outList + tmp_outlist
    odkodowany_ciag = ''.join([str(x) for x in outList])
    write_into_binary_file(odkodowany_ciag, new_file_path)

#funkcja pobierająca od użytkownika ścieżkę do pliku który ma być kodowany oraz wczytująca zawartość pliku
def encode_file():
   messagebox.showinfo("Kodowanie", "Wybierz plik, który chcesz zakodować")
   while (True):
      file_path = filedialog.askopenfilename(
         title="Wybierz plik",
      )

      if file_path != "":
         break
      else:
         print("Wybierz plik")

   f = open(file_path, 'rb')
   file_content = bytearray(f.read())
   f.close()
   binary = ""
   for one_byte in file_content:
      binary += bin(one_byte)[2:].rjust(8, '0')

   messagebox.showinfo("", "Wybierz gdzie chcesz zapisać zakodowany plik.")
   file_path = filedialog.asksaveasfilename(
      defaultextension='.ans',
   )

   encode_ans(binary, file_path)
   messagebox.showinfo("", "Zakodowany plik został zapisany.")
   exit(0)

#funkcja pobierająca od użytkownika ścieżkę do pliku który ma być odkodowany, wczytująca zawartość pliku i zamieniająca
#zawartość pliku na listę kodów
def decode_file():
   messagebox.showinfo("Dekompresja", "Wybierz plik, który chcesz odkodować")
   while (True):
      file_path = filedialog.askopenfilename(
         title="Select file",
      )

      if file_path != "":
         break
      else:
         print("Wybierz plik")

   f = open(file_path, 'rb')
   file_bytes = bytearray(f.read())
   f.close()

   # ilośc jedynek
   jeden = int.from_bytes(file_bytes[0:8],'big')
   # ilość danych
   length = int.from_bytes(file_bytes[8:16],'big')

   rest_len = int(len(file_bytes[16:])/8)
   compressed_data = struct.unpack('>'+rest_len*'Q', file_bytes[16:])

   messagebox.showinfo("", "Wybierz gdzie chcesz zapisać odkodowany plik.")
   file_path = filedialog.asksaveasfilename()

   decode_ans(jeden, length, compressed_data, file_path)
   messagebox.showinfo("", "Zakodowany plik został zapisany.")
   exit(0)

##############################################################
##########################-TESTY-#############################
##############################################################

#funkcja obsługująca testowanie
def tests():
    print('Testujemy')
    out = True
    for k in range(7):
        print(f'Test numer {k}')
        a = randint(1, 4)
        q = Fraction(a, 10)
        print(f'Wartosc q={q}')
        list = [randint(0, 1) for _ in range(7)]
        outList = decodingSeq(q, codingSeq(q, list))
        tmp = (list == outList)
        if tmp != True:
            print('Coding error')
            print(f'inList : {list}')
            print(f'outList: {outList}')
            out = out and tmp
    print(f'Wynik testow: {out}\n')
    print('Testy testGenCoding')
    print(f'Wynik testow: {testGenCodingA(20, 6)}')

    print('Testujemy drugi sposob')
    print(f'Wynik testow: {testGenCodingB(10, 7)}')

##############################################################
#############-URUCHOMIENIE GLOWNEGO PROGRAMU-#################
##############################################################

#funkcja obsługująca podstawową komunikację z użytkownikiem i wywołująca kolejne funkcje
def main():
    root = Tk()
    root.eval('tk::PlaceWindow . center')

    kompresja = Button(root, text="Kodowanie", command=encode_file)
    kompresja.pack()

    dekompresja = Button(root, text="Dekodowanie", command=decode_file)
    dekompresja.pack()

    root.mainloop()

#wywołanie głównej funkcji, jako inną opcję wywołać można testowanie
main()
# tests()



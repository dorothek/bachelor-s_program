uABS coding
----------------------
(ENGLISH VERSION BELOW)

[PL]
Aby przybliżyć czytelnikowi sposób działania algorytmu kodowania uABS powstał program przy pomocy którego użytkownik może samodzielnie zakodować plik lub odkodować wcześniej zakodowany plik. 
Ponadto zostały napisane testy wykazujące poprawność działania implementowanego algorytmu uABS.
Po uruchomieniu programu na ekranie pojawia się okienko z dwiema opcjami wyboru Kodowanie oraz Dekodowanie. Użytkownik wybiera jedną z opcji przy pomocy lewego przycisku myszki. 
Po wyborze jednej z opcji użytkownik proszony jest o wybranie pliku, który chce skompresować (lub zdekompresować), a następnie o wybór folderu w którym ma być przechowywany skompresowany (lub zdekompresowany) plik. 
Po zapisaniu nowego pliku na ekranie wyświetla się komunikat o ukończeniu wybranej akcji. Po zakodowaniu pliki zostają zapisane z domyślnym rozszerzeniem .ans.
Program został napisany w języku Python. Do obsługi graficznego interfejsu użytkownika użyto biblioteki tkinter. Inne biblioteki których użyto, to fractions w celu zapewnienia 
precyzyjnych operacji na ułamkach podczas wyliczania częstości występowania symboli (definiowania w programie pseudoparzystości i pseudonieparzystości); biblioteki math w celu umożliwienia 
operacji matematycznych na występujących liczbach zmiennoprzecinkowych; biblioteki random wykorzystanej podczas tworzenia testów funkcji działających zgodnie z 
algorytmem uABS oraz biblioteki struct w celu umożliwienia pracy z danymi w postaci binarnej.

Struktura programu składa się z funkcji main() odpowiedzialnej za działanie głównej, kodującej pliki części programu oraz tests() odpowiedzialnej za testy wykazujące poprawność 
zaimplementowanego algorytmu. Można wywołać jedną z dwóch wyżej wymienionychfunkcji w zależności od tego w jakim celu uruchamiany jest program. Po wywołaniu funkcji 
main() w zależności od wyboru użytkownika wywoływana jest funkcja encode_file() lub 
decode_file(). W funkcji encode_file() następuje wczytanie zawartości pliku który będzie kodowany i przekazanie jej w postaci binarnej do funkcji encode_ans() wraz ze ścieżką do 
miejsca w którym zakodowany plik ma zostać zapisany. W funkcji encode_ans() zostaje ustalona wartość q (definicja pseudoparzystości dla konkretnego ciągu) zgodnie z którą 
będzie odbywało się kodowanie a następnie przy użyciu funkcji pomocniczej codingBase()zostaje ustalona wartość początkowa zmiennej int x która reprezentuje liczbę do której 
kodowany jest ciąg. Następnie w pętli for rozpoczyna się kodowanie za które odpowiedzialna bezpośrednio jest funkcja coding(). W celu uniknięcia problemów związanych z 
przepełnieniem tworzona jest lista kodów – gdy wartość x przekracza 264 wcześniejsza wartość zmiennej x zapisywana jest na listę kodów. Po zakończeniu kodowania do pliku w 
postaci bajtów zapisywana jest kolejno ilość jedynek w kodowanym ciągu, długość kodowanego ciągu a następnie lista kodów. Zakodowany plik przyjmuje domyślne 
rozszerzenie .ans. W funkcji decode_file() wczytana zostaje zawartość zakodowanego pliku a następnie zamieniona na postać dziesiętną i zapisana w postaci listy. Odczytana zostaje także ilość
jedynek i długość oryginalnego, zakodowanego w pliku ciągu. Wartości te wraz ze ścieżką do miejsca gdzie ma zostać zapisany odkodowany plik zostają przekazane podczas wywołania do funkcji decode_ans(). 
W fukcji decode_ans() zostaje ustalone odpowiednie q (na podstawie ilości jedynek i długości oryginalnego ciągu) oraz wartość startowa (𝑥0) stanowiąca zmienną pomocniczą w procesie dekodowania 
ciągu reprezentowanego przez konkretną liczbę. Następnie w pętli for przechodzimy przez każdy kod znajdujący się na liście kodów. W funkcji decodingS() następuje określenie, czy kolejny odkodowany symbol to 0 czy 1, 
natomiast wywołanie funkcji decodingX() powoduje określenie jaka będzie wartość x po odkodowaniu kolejnego symbolu ciągu. Odkodowane fragmenty ciągu zapisywane są do zmiennej outList, a następnie łączone w zmienną formatu str. 
Następnie całość odkodowanego ciągu zapisywana jest do pliku przy użyciu funkcji write_into_binary_file().
Program obsługuje dobrze małe pliki. Działanie programu testowane było na plikach o wielkości do 50KB. Przy większych plikach program kończy poprawnie swoje działanie, lecz wymaga to większej ilości czasu.

-----------------------------------

[ENG]
To provide the reader with an understanding of how the uABS encoding algorithm works, a program has been created that allows users to encode a file or decode a previously encoded file. 
Additionally, tests have been written to demonstrate the correctness of the implemented uABS algorithm.
Upon launching the program, a window with two options, Encoding and Decoding, appears on the screen. The user selects one of these options using the left mouse button. 
After selecting an option, the user is asked to choose a file to compress (or decompress) and then to choose a folder where the compressed (or decompressed) file will be stored. 
After saving the new file, a message indicating the completion of the selected action is displayed. Encoded files are saved with the default extension .ans.
The program is written in Python. The Tkinter library is used for the graphical user interface. Other libraries used include fractions for precise operations on fractions 
when calculating symbol frequencies (defining pseudoevenness and pseudooddness in the program); math for mathematical operations on floating-point numbers; random for creating tests of functions 
according to the uABS algorithm; and struct for working with binary data.

The program structure consists of the main() function responsible for the main file-encoding part of the program and the tests() function responsible for tests demonstrating the correctness 
of the implemented algorithm. One of these two functions can be called depending on the program's purpose. After calling the main() function, the encode_file() or decode_file() function 
is invoked based on the user's choice. In the encode_file() function, the contents of the file to be encoded are read and passed in binary form to the encode_ans() function along with 
the path where the encoded file is to be saved. In the encode_ans() function, the value of q (definition of pseudoevenness for a specific sequence) is determined, according to which encoding will take place, 
and then using the auxiliary function codingBase(), the initial value of the variable int x representing the number to which the sequence is encoded is determined. Then, in a for loop, the encoding begins, 
for which the coding() function is directly responsible. To avoid overflow issues, a code list is created – when the value of x exceeds 2^64, the previous value of the variable x is saved to the code list. 
After encoding, the number of ones in the encoded sequence, the length of the encoded sequence, and then the code list are written to the file in bytes. The encoded file takes the default extension .ans.
In the decode_file() function, the contents of the encoded file are read and then converted to decimal form and saved as a list. The number of ones and the length of the original encoded sequence in the file are also read. 
These values, along with the path where the decoded file is to be saved, are passed when calling the decode_ans() function. In the decode_ans() function, the appropriate q is determined (based on the number of ones and 
the length of the original sequence) and the start value (x0) is set as an auxiliary variable in the process of decoding the sequence represented by a specific number. Then, in a for loop, each code on the code list is processed. 
In the decodingS() function, it is determined whether the next decoded symbol is 0 or 1, while calling the decodingX() function determines the value of x after decoding the next symbol of the sequence. 
Decoded parts of the sequence are saved to the outList variable and then concatenated into a string format variable. The entire decoded sequence is then written to the file using the write_into_binary_file() function.
The program handles small files well. Its operation was tested on files up to 50KB in size. For larger files, the program completes correctly, but it requires more time.**

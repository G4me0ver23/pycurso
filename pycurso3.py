var = 0
print(var == 0)
print(var != 0)
var = 1
print(var == 0)
print(var != 0)
n = int(input("N: "))
print(n>=100)
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
 
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2
print("O maior número é:", larger_number)
number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
 
if number1 > number2: larger_number = number1
else: larger_number = number2
print("O maior número é:", larger_number)

number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
number3 = int(input("Digite o terceiro número: "))
largest_number = number1
if number2 > largest_number:
    largest_number = number2
if number3 > largest_number:
    largest_number = number3
print("O maior número é:", largest_number)

number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
number3 = int(input("Digite o terceiro número: "))
largest_number = max(number1, number2, number3)
print("O maior número é:", largest_number)



enter = input("Digite Spathiphyllum: ")
if enter=="Spathiphyllum":
    print("Spathiphyllum é a melhor fábrica de todos os tempos!")
elif enter=="spathiphyllum":
    print("Não, eu quero um grande Spathiphyllum!")
else:
    print("Spathiphyllum! Not",enter,"!")


income = float(input("Entre com os rendimentos anuais "))

if income < 85528:
    tax = income * 0.18 - 556.02
elif income >= 85528:
    tax = 14839.02 + (income-85528)*0.32

tax = round(tax, 0)
if tax <= 0:
    tax=0
print("A taxa é:", tax, "thalers")

year = int(input("Digite um ano: "))
if year < 1582:
    print("Não dentro do período do calendário gregoriano")
if year >= 1582:
    if year%4!=0:
        print("ano comum")
    else:
        if year%400!=0:
            print("ano comum")
        elif year%100!=0:
            print("ano bissexto")
        else:
            print("ano bissexto")


largest_number = -999999999
 

number = int(input("Digite um número ou digite -1 para parar: "))
while number != -1:
    if number > largest_number:
        largest_number = number
    number = int(input("Digite um número ou digite -1 para parar: "))
print("O maior número é:", largest_number)


odd_numbers = 0
even_numbers = 0
number = int(input("Digite um número ou digite 0 para parar: "))
while number != 0:
    if number % 2 == 1:
        odd_numbers += 1
    else:
        even_numbers += 1
    number = int(input("Digite um número ou digite 0 para parar: "))
print("Números ímpares contam:", odd_numbers)
print("Números pares contam:", even_numbers)

counter = 5
while counter:
    print("Dentro do laço.", counter)
    counter -= 1
print("Fora do circuito.", counter)


secret_number = 777

print(
"""
+===================================+
| Bem vindo ao meu jogo, trouxa!    |
| Insira um número inteiro          |
| e adivinhar o número que tenho    |
| escolhidos para você.             |
| Então, qual é o número secreto?   |
+===================================+
""")
number=0
while number!= secret_number:
    number = int(input("Digite o número secreto: "))
    print("Ha ha! Você está preso no meu loop!")
print("Muito bem, trouxa! Você está livre agora.")

for i in range(10):
   print("O valor de i é atualmente", i)
for i in range(2, 8, 3):
  print("O valor de i é atualmente", i)

power = 1
for expo in range(16):
  print("2 à potência de", expo, "é", power)
  power *= 2

print("The break instrução:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro do laço.", i)
print("Fora do loop.")
print("The continue instrução:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro do laço.", i)
print("Fora do loop.")

argest_number = -99999999
counter = 0

while True:
    number = int(input("Digite um número ou digite -1 para terminar o programa: "))
    if number == -1:
        break
    counter += 1
    if number > maior_numero:
        maior_numero = number

if counter != 0:
    print("TO maior número é", maior_numero)
else:
    print("Você não inseriu nenhum número.")

number = int(input("Insira um número ou digite -1 para finalizar o programa: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Insira um número ou digite -1 para finalizar o programa: "))

if counter:
    print("O maior número é",  largest_number)
else:
    print("Você nnão tem inseriu qualquer número.")

palavra=input("Insira a palvra: ")
palavra = palavra.upper()
for letra in palavra:
    if letra == "A":
        continue
    elif letra == "E":
        continue
    elif letra == "I":
        continue
    elif letra == "O":
        continue
    elif letra == "U":
        continue
    else:
        print(letra)

word_without_vowels= ""
palavra=input("Insira a palvra: ")
palavra = palavra.upper()
for letra in palavra:
    if letra == "A":
        continue
    elif letra == "E":
        continue
    elif letra == "I":
        continue
    elif letra == "O":
        continue
    elif letra == "U":
        continue
    else:
        word_without_vowels+=letra

print(word_without_vowels)


i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

for i in range(5):
 print(i)
else:
 print("else:", i)


blocks = int(input("Insira o número de blocos:"))  
altura=0
count=0
while blocks>=0:
    altura+=1
    count=blocks-altura
    if count<0:
        altura-=1
        break
    else:
        blocks=count

print("A altura da pirâmide:", altura)


c0 = int(input("Digite qualquer número diferente de 0: "))
count = 0
while c0 != 1:
    print(c0)
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = 3 * c0 + 1
    count += 1
print(c0)
print("Número de etapas necessárias:", count)
print(var > 0)
print(not (var <= 0))
print(var != 0)
print(not (var == 0))
var = 17
var_right = var >> 1
var_left = var << 2
print (var, var_left, var_right)
x = 1
y = 0
z = ((x == y) and (x == y)) or not(x == y)
print(not(z))
x = 4
y = 1

a = x & y
b = x | y
c = ~x
d = x ^ 5
e = x >> 2
f = x << 2
print(a, b, c, d, e, f)

numbers = [10, 5, 7, 2, 1]
print("Conteúdos originais da lista:", numbers) 
numbers[0] = 111
print("Novo conteúdo da lista: ", numbers)
numbers[1] = numbers[4]
print("Novo conteúdo da lista:", numbers)
print ("\n List length:", len (numbers))
del numbers[1]
print(len(numbers))
print(numbers)
print(numbers[0])
numbers[0] = 1
print(numbers[-1])

hat_list = [1, 2, 3, 4, 5]
mid_number=int(input("Digite o número do meio"))
hat_list[round(len(hat_list)/2)]=mid_number
del hat_list[-1]
print(len(hat_list))
print (hat_list)

numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)
numbers.append (4)
print(len(numbers))
print(numbers)
numbers.insert (0, 222)
print(len (numbers))
print(numbers)
numbers.insert(1, 333)

my_list_append = []
my_list_insert = []
for i in range(5):
   my_list_append.append (i + 1)
   my_list_insert.insert(0, i + 1)
print (my_list_append)
print (my_list_insert)

my_list = [10, 1, 8, 3, 5]
total = 0
for i in range(len(my_list)):
  total += my_list[i]
print(total)

my_list = [10, 1, 8, 3, 5]
my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]
print(my_list)

beatles=[]
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
for i in range(2):
    member = input("Adicione Stu Sutcliffe e Pete Best à banda: ")
    beatles.append(member)
del beatles[-1]
del beatles[-1]
beatles.insert(0, "Ringo Starr")
print(beatles)

lst = [1, 2, 3, 4, 5]
lst.insert(1, 6)
del lst[0]
lst.append(1)
print(lst)

lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0
for number in lst:
    add += number
    lst_2.append(add)
print(lst_2)

lst = []
del lst

lst = [1, [2, 3], 4]
print(lst[1])
print(len(lst))

my_list = [8, 10, 6, 2, 4]
for i in range(len(my_list) - 1):
    if my_list[i] > my_list[i + 1]:
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]


my_list = [8, 10, 6, 2, 4]
swapped = True
while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
print(my_list)


my_list = []
swapped = True
num = int(input("Quantos elementos você deseja embaralhar? "))
for i in range(num):
 val = float(input("Entre com a lista de elementos:"))
 my_list.append(val)
while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
print("\nSorted:")
print(my_list)

my_list = [8, 10, 6, 2, 4]
my_list.sort()
lst.reverse()
print(my_list)
print(lst)

lst = ["D", "F", "A", "Z"]
lst.sort()
print(lst)


a = 3
b = 1
c = 2
lst = [a, c, b]
lst.sort()
print(lst)


a = "A"
b = "B"
c = "C"
d = " "
lst = [a, b, c, d]
lst.reverse()
print(lst)


list_1 = [1]
list_2 = list_1
list_1 [0] = 2
print(list_2)

list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

list_1 = [1]
list_2 = list_1 [:]
list_1 [0] = 2
print (list_2)
my_list = [10, 8, 6, 4, 2]
new_list = my_list [1: 3]
print(new_list)
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)
my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)

my_list = [0, 3, 12, 8, 2]
print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]
for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]
print(largest)


my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]
for i in my_list:
    if i > largest:
        largest = i
print(largest)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False
for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break
if found:
    print("Elemento encontrado no índice", i)
else:
    print("ausente")


my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
uniques_list = []
for n in my_list:
    if n not in uniques_list:
        uniques_list.append(n)
print("A lista com os elementos exclusivos aqui")
print(uniques_list)

list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2
del list_1[0]
del list_2[0]
print(list_3)

list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2
del list_1[0]
del list_2
print(list_3)

list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2
del list_1[0]
del list_2[:]
print(list_3)

list_1 = ["A", "B", "C"]
list_2 = list_1[:]
list_3 = list_2[:]
del list_1[0]
del list_2[0]
print(list_3)

my_list = [1, 2, "in", True, "ABC"]
print(1 in my_list)
print("A" not in my_list)
print(3 not in my_list)
print(False in my_list)


row = [] 
for i in range(8):
    row.append(WHITE_PAWN)

row = [WHITE_PAWN for i in range(8)]
squares = [x ** 2 for x in range(10)]
twos = [2 ** i for i in range(8)]

board = []
for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

board = [[EMPTY for i in range(8)] for j in range(8)]
board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK
board[4][2] = KNIGHT



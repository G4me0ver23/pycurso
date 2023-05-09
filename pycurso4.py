def message(number):
    print("Digite um número:", number)
message(23)

def message(what, number):
    print("Entrar", what, "número", number)
 
message("telefone", 11)
message("preço", 5)
message("número", "número")

def my_function(a, b, c):
    print(a, b, c)
my_function(1, 2, 3)

def introduction(first_name, last_name):
    print("Olá meu nome é", first_name, last_name)
introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")
def introduction(first_name, last_name):
    print("Olá meu nome é", first_name, last_name)
introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")

def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)
adding(1, 2, 3)

def introduction(first_name, last_name="Smith"):
     print("Olá meu nome é", first_name, last_name)
introduction("James", "Doe")
introduction("Henry")


def intro(a="James Bond", b="Bond"):
     print("Meu nome é", b + ".", a + ".")
intro()


def intro(a="James Bond", b="Bond"):
    print("Meu nome é", b + ".", a + ".")
intro(b="Sean Connery")


def intro(a, b="Bond"):
    print("Meu nome é", b + ".", a + ".")
intro("Susan")


def add_numbers(a, b=2, c=5):
    print(a + b + c)
add_numbers(a=1, c=3)


def happy_new_year(wishes = True):
    print("Três...")
    print("Duas...")
    print("Uma...")
    if not wishes:
        return print("Feliz Ano Novo!")
happy_new_year()


def boring_function():
    return 123 
x = boring_function()
print("A aborrecimento_função retornou seu resultado. Isso é:", x)


def boring_function():
    print("'Modo de tédio' ON.")
    return 123
print("Esta lição é interessante!")
boring_function()
print("Essa aula é chata...")

value = None
if value is None:
    print("Desculpe, você não carrega nenhum valor")

def strange_function(n):
    if(n % 2 == 0):
        return True

print(strange_function(2))
print(strange_function(1))

def list_sum(lst):
    s = 0
    for elem in lst:
        s += elem
    return s
print(list_sum([5, 4, 3]))


def strange_list_fun(n):
    strange_list = []
    for i in range(0, n):
        strange_list.insert(0, i)
    return strange_list
print(strange_list_fun(5))


def is_year_leap(year):
    if year%4==0 and year%100!=0:
        return True
    elif year%400==0:
        return True
    else:
        return False

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fracassado")
    

def is_year_leap(year):
    if year%4==0 and year%100!=0:
        return True
    elif year%400==0:
        return True
    else:
        return False

def days_in_month(year, month):
    days=31
    if month == 2:
        if is_year_leap(year):
            days = 29
        else:
            days = 28
    elif month in [4, 6, 9, 11]:
        days = 30
    return days

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fracassado")



def is_year_leap(year):
    if year%4==0 and year%100!=0:
        return True
    elif year%400==0:
        return True
    else:
        return False
def days_in_month(year, month):
    days=31
    if month == 2:
        if is_year_leap(year):
            days = 29
        else:
            days = 28
    elif month in [4, 6, 9, 11]:
        days = 30
    return days
def day_of_year(year, month, day):
    mon=month
    days=0
    for m in range(1,month+1):
        days+=days_in_month(year,m)
    d_m=days_in_month(month, year)
    d=day-d_m
    return days+d

print(day_of_year(2000, 12, 31))


def is_prime(num):
    if num < 2:
        return False
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()


def liters_100km_to_miles_gallon(liters):
    miles = 100/(liters / 3.785411784)
    return miles*0.621371

def miles_gallon_to_liters_100km(miles):
    liters = 3.785411784/(miles / 0.621371)*100
    return liters

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

def hi():
    return
    print("Oi!")
hi()

def is_int(data):
    if type(data) == int:
        return True
    elif type(data) == float:
        return False
print(is_int(5))
print(is_int(5.0))
print(is_int("5"))


def even_num_lst(ran):
    lst = []
    for num in range(ran):
        if num % 2 == 0:
            lst.append(num)
    return lst
print(even_num_lst(11))


def list_updater(lst):
    upd_list = []
    for elem in lst:
        elem **= 2
        upd_list.append(elem)
    return upd_list
foo = [1, 2, 3, 4, 5]
print(list_updater(foo))


def my_function():
 print("Eu conheço aquela variável?", var)
var = 1
my_function()
print(var)


def my_function():
    var = 2
    print("Eu conheço aquela variável?", var)
var = 1
my_function()
print(var)


def my_function():
 global var
 var = 2
 print("Eu conheço aquela variável?", var)
var = 1
my_function()
print(var)


def my_function(n):
 print("Eu obtive", n)
 n += 1
 print("Eu tenho", n)
var = 1
my_function(var)
print(var)


def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    my_list_1 = [0, 1]
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)
my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)


a = 1
def fun():
    a = 2
    print(a)
fun()
print(a)


a = 1
def fun():
    global a
    a = 2
    print(a)
fun()
a = 3
print(a)


a = 1
def fun():
    global a
    a = 2
    print(a)
a = 3
fun()
print(a)


def bmi(weight, height):
    return weight / height ** 2
print(bmi(52.5, 1.65))


def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None
    return weight / height ** 2
print(bmi(352.5, 1.65))


def lb_to_kg(lb):
    return lb * 0.45359237
print(lb_to_kg(1))


def ft_and_inch_to_m(ft, inch):
    return ft * 0.3048 + inch * 0.0254
print(ft_and_inch_to_m(1, 1))


def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254
print(ft_and_inch_to_m(6))



def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254
 
 
def lb_to_kg(lb):
    return lb * 0.4535923
 
 
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
    return weight / height ** 2
print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7)))


def is_a_triangle(a, b, c):
 if a + b <= c:
     return False
 if b + c <= a:
     return False
 if c + a <= b:
     return False
 return True
print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))



def is_a_triangle(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True
print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))


def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b
print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))


def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b
a = float(input('Digite o primeiro lado\'s comprimento: '))
b = float(input('Entre no segundo lado\'s comprimento: '))
c = float(input('Entre no terceiro lado\'s comprimento: '))
if is_a_triangle(a, b, c):
    print('Sim, pode ser um triângulo.')
else:
    print('Não, não pode ser um triângulo.')


def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b
def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5
def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)
print(area_of_triangle(1., 1., 2. ** .5))


def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product
for n in range(1, 6):
    print(n, factorial_function(n))


def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum
for n in range(1, 10):
    print(n, "->", fib(n))


def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)


def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
        return the_sum


def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)
print(fun(25))




my_tuple = (1, 10, 100, 1000)
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])
for elem in my_tuple:
    print(elem)


my_tuple = (1, 10, 100)
t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3
print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)


dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
phone_numbers = {'chefe': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}
print(dictionary)
print(phone_numbers)
print(empty_dictionary)

dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
phone_numbers = {'chefe' : 5551234567, 'Suzy' : 22657854310}
empty_dictionary = {}
print(dictionary['gato'])
print(phone_numbers['Suzy'])
dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
words = ['gato', 'lion', 'cavalo']
for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "não está no dicionário")


dictionary = {
              "gato": "chat",
              "cachorro": "chien",
              "cavalo": "cheval"
}
phone_numbers = {'chefe': 5551234567,
              'Suzy': 22657854310
}


dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
for key in dictionary.keys():
    print(key, "->", dictionary[key])


dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
dictionary['gato'] = 'minou'
print(dictionary)


dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
for french in dictionary.values():
    print(french)


dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
dictionary['swan'] = 'cygne'
print(dictionary)


dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
dictionary.update({"pato": "canard"})
print(dictionary)


dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
del dictionary['cachorro']
print(dictionary)


dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
dictionary.popitem()
print(dictionary)


school_class = {}
while True:
    name = input("Digite o nome do aluno: ")
    if name == '':
        break
    score = int(input("Insira a pontuação do aluno (0-10): "))
    if score not in range(0, 11):
        break
    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)
 
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
        print(name, ":", adding / counter)


my_tup = (1, 2, 3)
print(my_tup[2])


tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)
print(duplicates)


d1 = {'Adão Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}
for item in (d1, d2):
    d3.update(item)
print(d3)


d1 = {'Adão Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}
 
colors = (("green", "#008000"), ("blue", "#0000FF"))
colors_dictionary = dict(colors)
print(colors_dictionary)


my_dictionary = {"A": 1, "B": 2}
copy_my_dictionary = my_dictionary.copy()
my_dictionary.clear()
print(copy_my_dictionary)


colors = {
    "branco": (255, 255, 255),
    "cinza": (128, 128, 128),
    "vermelho": (255, 0, 0),
    "verde": (0, 128, 0)
    }
for col, rgb in colors.items():
    print(col, ":", rgb)

try:
    value= int(input('Insira um número natural:')) 
    print('O recíproco de', valor, 'é', 1 / value) 
except: 
    print('Não sei o que fazer.')


try:
    value = int(input('Digite um número natural: '))
    print('O recíproco de', value, 'é', 1/value)
except ValueError:
    print('Eu não sei o que fazer.')
except ZeroDivisionError:
    print('A divisão por zero não é permitida em nosso Universo.')


try:
    value = int (input('Insira um número natural:')) 
    print('O recíproco de', value, 'é', 1 / value) 
except ValueError:
    print('Não sei o que fazer.' ) 
except ZeroDivisionError:
    print('Divisão por zero não é permitida em nosso universo.') 
except: 
    print('algo de estranho aconteceu aqui ... Desculpe! ')


temperature = float(input('Digite a temperatura atual:'))
if temperature > 0:
    print("Acima de zero")
elif temperature < 0:
    print("Abaixo de zero")
else:
    print("Zero")


try:
    value = int(input("Entre um valor: "))
    print(value/value)
except ValueError:
    print("Entrada incorreta...")
except ZeroDivisionError:
    print("Entrada muito ruim...")
except:
    print("Booo!")






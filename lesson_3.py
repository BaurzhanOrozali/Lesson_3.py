def zadanie1():
# задача номер1 из 3 семинара
    num = int(input('введите свое число: '))
    u = [1, 1]
    lenght_u=len(u)
    count=0
    sum = 0
    if num == 1:
        print(f"{num} = 1" )
    while count < num:
        for i in range(lenght_u):
            sum = u[-2]+u[-1]
            u.append(sum)
            count +=1
            print (u[len(u)-2], end = " ")


def zadanie2():
    fruits = dict( а='абрикос, ананас, апельсин, авокадо, айва', б='банан', в='виноград', г='груша', я='яблоко')
    bukva = input('Введите , букву: ')
    for key, value in fruits.items():
        if key == bukva:
            print("{0} -> {1}".format(key,value))
def zadanie2_1():
    fruits = ['абрикос', 'ананас', 'апельсин', 'авокадо', 'айва', 'банан', 'виноград', 'груша', 'яблоко']
    bukva = input('Введите , букву: ')
    for el in fruits:
        if bukva == el[0]:
            print (el, end = ' ')


def zadanie3():
    razgovor = {}
    razgovor ['name']= input ( 'введите ваше имя: ')
    print('привет', razgovor ['name'])
    razgovor ['mood']= input ( 'как дела? ')

    if razgovor ['mood'] == 'хорошо':
        print('Так держать')
    elif razgovor ['mood'] == 'плохо':
        print('Завтро будет лучше') 
    else:
        print('Мне все равно')
    tut = razgovor ['secret'] = input('Умеешь хранить секреты? ')
    if razgovor ['secret'] == 'да':
        print('А ты надежней чем кажешься)')
    elif razgovor ['secret'] == 'нет':
        print('Я так и знал))') 
    else:
        print('Уже поздно')
    print (razgovor ['name'] , end = '')
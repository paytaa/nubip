#Оголошуємо змінну, і просимо ввести рядок
sttr = input("Input your string: ")
word=''
num=[]
leng=len(sttr)
print('\t')
print("String is:"+sttr)
#Запускаємо цикл для створення масиву. Цикл шукає число і добавляє його в кінець
p=0
for i in range(leng):
    j=sttr[i]
    if '0'<= j<='9':
        num.append(int(j))
        p+=1
        i+=1
    else:
        word+=j
        i+=1
word+=' '
print('\t')
print('Numbers : ' + str(num))
print('String without numbers : ' + word)
#Шукаємо максимальне число в масиві
i=0
Max_Num=0
for i in range(len(num)):
        if num[i]>Max_Num:
            Max_Num=num[i]
            i+=1
        else:
            i+=1
# Записуємо всі числа, крім максимального, підносячи їх до степені по їхньому індексу, в окремий масив.
num_2=[]
i=0
for i in range(len(num)):
         if num[i]!=Max_Num:
              num_2.append(num[i]**i)
              i+=1
         else:
              continue

print('\t')
#Виводимо це число на екран
print('Max number is : ' + str(Max_Num))
print('Number x**i without max : ' + str(num_2))
print('\t')
# Оголошуємо рядок, де будуть записані слова, які починаються і закінчуються великою літерою
# Змінна k буде запам'ятовувати адресу розташування першої букви в слові
Upper_str=''
k=0
i=0
# Змінюємо рядок щоб коже слово починалось і закінчувалось великою літерою
for i in range(len(word)-1):
    j=word[i+1]
    if j==' ':
        Upper_str+=word[k].upper()
        Upper_str+=word[k+1:i]
        Upper_str+=word[i].upper()+' '
        k=i+2
        i+=1
    else:
        i+=1
print('String with upper : ' + Upper_str)
print('\t')
input()

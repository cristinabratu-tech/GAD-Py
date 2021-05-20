# declararea unei liste care să conțină elementele 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (în această ordine)

my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(my_list)

#afișarea unei alte liste ordonată ascendent (lista inițială trebuie păstrată în aceeași formă)

my_sorted_list = my_list.copy()
my_sorted_list.sort()
print(my_sorted_list)

#afișarea unei liste ordonată descendent (lista inițială trebuie păstrată în aceeași formă)

my_sorted_list2 = my_list.copy()
my_sorted_list2.sort(reverse=True)
print(my_sorted_list2)

#afișarea numerelor pare din listă (folosind DOAR slice, altă metodă va fi considerată invalidă)

my_sliced_list = my_list[1:4:2]+my_list[6:8]+my_list[-1:]
print(my_sliced_list)

#afișarea numerelor impare din listă (folosind DOAR slice, altă metodă va fi considerată invalidă)

my_sliced_list2 = my_list[2:9:3]+my_list[:5:4]
print(my_sliced_list2)

#afișarea elementelor multipli ai lui 3

for item in (my_list):
    if item % 3 == 0:
        print(item)



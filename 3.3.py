def  print_params(a=1,b='строка', c="True"):
    print(a,b,c)
    #print(a)
    #print(a,c)
    #print()

# print_params() #Функция с параметрами по умолчанию:
# print_params(b = 25)
# print_params(c = [1,2,3])
#
# values_list =("привет", 2007 , 2.9)#2.Распаковка параметров:
# values_dict ={"a": 5,"b": "str" ,"c": (2,5,10,4.3) }
# print_params(*values_list)
# print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ] #3.Распаковка + отдельные параметры:
print_params(*values_list_2, 42)

# ტრინგს რო რამე ასო მიამატო ბოლოში, მისი აიდი შეიცვლება, მაგრამ სიაში რომ რამე ჩაამატო,
# მისი აიდი იქნება იგივე

# a = [1, 2, 5]
# b = [3, 'a']
# print(id(a))
# a.append(5)
# print(a)
# print(id(a))
# a.append(b)
# print(a)
# a.extend(b)
# print(a)
# a.clear()
# print(a)




# a = [4, 5, 6, 5, 5, 5]
# print(a.count(5))
# print(a.index(6))
# print(a.index(5))
#
# a.insert(3, 'f')
# print(a)
#
# a.pop() #ავტომატურად შლის ბოლო ელემენტს თუ არაფერს არ გადავცემ
# print(a)
#
# print(a.pop(0)) #თუ ინდექსს გადასცემ, მეიმდენეს წაშლის. პრინტით თუ ამოიღე, იმასაც გეუბნება თუ რა წაშალა სიიდან
# print(a)
#
# a.remove(5)
# print(a) # პირველივე რომელიც შეხვდება, იმას შლის. თუ საერთოდ არაა ასეთი წევრი სიაში, მაშინ აერორებს
#
# #ამიტომ სჯობს ასე გამოყენება:
# if 'f' in a:
#     a.remove('f')
#     print(a)
#
# # თუ ყველას წაშლა მინდა რაც კი არის
# for item in a:
#     if item == 5:
#         a.remove(item)
#
# print(a) #რაღაცა ნიტოა


# k = ['a', 'c', 'b', 'd']
# k.sort()
# print(k)
# k.sort(reverse = True)
# print(k)
#
# c = [x**2 for x in range(1,10) if x%3==0]
# print(c)





# fruits = ["apple", "banana", "cherry", "mango"]
#
# aa =[x for x in fruits if "a" == x[1]] #საპრინტავს მხოლოდ იმ სიტყვებს, რომლის მეორე ასოც არის ა
# print(aa)



#
# x = [1,2,3]
# y = x
#
# x.append(7)
# print(x, y) #ორივეს ემატება, იმიტომ რომ იგრეკი როცა უტოლდება იქსს, მისი აიდი იგივეა და იქსს რომ ამატებ წევრს, იგრეკსაც ემატება
#
# # თუ გვინდა რომ გადავაკოპიროტ, ასე ვქნათ
# x = [1,2,3]
# y = x[:]
#
# x.append(7)
# print(x, y)
#
#ან ასე
# x = [1,2,3,[4,9]]
# y = x.copy()
#
# x.append(7)
# print(x, y) #magram amas aqvs problemebi magalitad:
#
# x = [1,2,3,[4,9]]
# y = x.copy()
#
# x[-1].append(7)
# print(x, y) #anu am shemtxvevashi mainc emateba ys xis monacemebi. tu maqximalurad gvinda tavis dazgveva, maSin ess unda vqnaT:
#
# from copy import deepcopy
# x = [1,2,3,[4,9]]
# y = deepcopy(x)
#
# x[-1].append(7)
# print(x, y)

# u = ['s', 'f', 'w']
# for i in enumerate(u):
#     print(i) #listis wevrebis indeqsebi moaqvs

##############################   TUPLE   ##########################
#
# a = (1, 2,2, 2)
# print(a[0])
# try:
#     a[0] = 4
# except:
#     print('Tuple-ში ცვლილებას ვერ შეიტან!')
#
# # თუ გინდა რო თაფლში ცვლილება შეიტანო, მაშინ ჯერ სიად უნდა გადააქციო და მერე უკან დააბუნო
#
# a = list(a)
# a[0] = 4
# a = tuple(a)
# print(a)
#
# print(a.count(2))
# print(a.index(2)) #pirveli orianis indeqss abrunebs


##############################   set   ##########################

# z = {1,2,3,3,3,2,4}
# print(z)
#
# try:
#     z = {1, 2, 3, 2, [9 , 0]} #setshi ar jdeba sia, radgan sia cvalebadia
# except:
#     z = {1, 2, 3, 2, (9, 0)}
# print(z)
#
# z=set()
# z.add(13)
# z.add(10)
# print(z)
#
# t = {2, 55, 10, 10}
# print(z.difference(t))
#
# #pop setshi shemtxvevitad shlis elements, radgan bolo ar icis romelia
# # tu konkretuli ramis washla minda, mashin removit
# t.remove(10)
# print(t)



#####################   Dictionary   ###############################

a = { 'vashli': 2.89, 'marwyvi' : 5.84 }

# print(a.items())
#
# for i in a:
#     print(i)  # marto key-ebi wamoigo
#
# for k in a.values():
#     print(k)   # aq meore nawili wamoigo
#
# for j in a.items():
#     print(j)  # tuplebad wamoigo
#
# for i, j in a.items():
#     print(i, j)
#
#
# #key-ს ადგილას უნდა იყოს უცვლელი ელემენტი. სია ლისტი ვერ იქნება, მარა მეორე მხარეს მოსულა
#
# a["atami"] = 3.4
# print(a) #aaxali wevris damateba. tu arsebul keys dawer, imis values shecvlis

# r = dict.fromkeys(['vashli', 'atami'], 3)
# print(r)

# a.pop('vashli')
# print(a)

p = {'msxali' : 5}
a.update(p)
print(a)
from random import sample,shuffle,randint

lst1 = ["ali" , "MMDSANE" , "alireza" , "samin" ,
         "Anna" , "negin" , "kasra", "Amin" , "zahra" , "khalil"]

lst2 = []
for i in lst1:
    if len(set(i)) == len(i):
        lst2.append(i)
        
shuffle(lst2)

print(sample(lst2 , 1))
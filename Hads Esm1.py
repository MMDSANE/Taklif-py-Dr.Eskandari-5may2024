from random import shuffle , sample
lst1 = ["Raeen" , "Negar" , "Ahmad" , "Negin" , "Ali" , "Samin" , "Alireza" ,
         "Anna" , "MMDSANE" , "Arefe" , "Kourosh" , "Aroosha" , "Kiarash" , "Mohammad"
          , "Farzad" , "Behzad" , "Erfan" , "Farbod" , "Farima" , "Hamid"]
print(lst1)
print("\n")
while True:
    x = input("Hads bezan az beyne list bala: ")

    shuffle(lst1)
    y = sample(lst1 , 1)

    if x == y[0]:
        print("!!! Afarin dorost bood !!!")
        break
    else:
        print("Talash mojadad")

from random import shuffle , sample
lst1 = ["Raeen" , "Negar" , "Ahmad" , "Negin" , "Ali" , "Samin" , "Alireza" ,
         "Anna" , "MMDSANE" , "Arefe" , "Kourosh" , "Aroosha" , "Kiarash" , "Mohammad"
          , "Farzad" , "Behzad" , "Erfan" , "Farbod" , "Farima" , "Hamid"]
print(lst1)
print("\n")
while True:

    shuffle(lst1)
    y = sample(lst1 , 1)
    print(f"Hads man {y} ast")
    inp = input("Aya dorost bood?? (YES / NO):  ").upper()

    if inp == "YES":
        print("Afarin be khodam \n !! BAZI TAMAM !!")
        break
    else:
        lst1.remove(y[0])
        print("OK dobare hads mizanam")

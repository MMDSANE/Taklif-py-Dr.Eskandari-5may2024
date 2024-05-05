from random import sample,shuffle,choice

dolors = 100

lst = ['SHIR' , 'KHAT']

while 0 <= dolors <= 200:
    x = input("SHIR (1) / KHAT (2) ???")
    shuffle(lst)
    y = choice(lst)
    
    if lst[int(x) - 1] == y:
        dolors += 9
        print(f"Afarin Dorost bood pool shoma: {dolors}")
    else:
        dolors -= 10
        print(f"javab shoma nadorost bood pool shoma: {dolors}")

    if dolors >= 200:
        print("!!!! BORDI !!!!")
        break

    elif dolors <= 0:
        print("!!!! BAKHTI !!!!")
        break
    
    else:
        print("edame bede")

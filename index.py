import time
timeLine = []
a = 3
while a >= 0:
   
    cislo = int(input("Zadejte číslo:"))
    
    def timer(cislo):
        while (cislo):
            time.sleep(1)
            cislo = cislo - 1
            print(cislo)
    timer(cislo)
    a = a-1


    
    if cislo:
        timeLine.append(cislo)
    print(timeLine)



index = 0

while index<len(timeLine):
    test = timeLine[index]
    
    while test>0:
            time.sleep(1)
            test = test - 1
            print (test)
            if test == 0:
                index = index + 1
                print("Další číslo")
        
        

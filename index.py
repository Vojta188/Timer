import time
timeLine = []
a = 3
while a >= 0:
    cislo = int(input("Zadejte číslo:"))
    
    def timer(cislo):
        while cislo:
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
    print(test)
    while test>0:
        time.sleep(1)
        test = timeLine[index] - 1
        print (test)
   
        

        
        
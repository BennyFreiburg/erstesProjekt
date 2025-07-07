print('Hallo Freiburg')
print('Das ist eine Veränderung')
summe=0
summe2=0
for i in range(101):
    summe=summe+i
print(summe)
for i in range(100):
    summe2=summe2+1/(i+1)**2
    
print(summe2)
a=temp1=int(input("Geben Sie die erste Zahl ein: "))
b=temp2=int(input("Geben Sie die zweite Zahl ein: "))

while temp2!=0:
    if temp1>temp2:
        temp1=temp1-temp2
    else:
        temp2=temp2-temp1
        
print("Der ggt(größte gemeinsame Teiler) von",a,"und",b,"ist:",temp1)
print("Das kgv(kleinste gemeinsame Vielfache) von",a,"und",b,"ist:",a*b//temp1)


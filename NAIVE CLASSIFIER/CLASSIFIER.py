import pandas as pd
from pandas import DataFrame
df=pd.read_csv("data.txt",sep="\t")
n=len(df.index)

count_gm=0
count_gf=0

x1=df["F"]   
x2=df["T"]
x3=df["R"]
x4=df["H"]     
x5=df["G"]
for line in x5:
    if(line=="M"):
        count_gm=count_gm+1
    else:
        count_gf=count_gf+1
        
print("Enter the details for instance to be classified:")
f=input("Enter Finance_Invest_Promotion(Y/N):")
t=input("Enter Travel_Tour_Promotion(Y/N):")
r=input("Enter Reading Magazine_Promotion(Y/N):")
h=input("Enter Helath/diet_Promotion(Y/N):")
first_par=0
second_par=0
third_par=0
fourth_par=0

for x,y in zip(x1,x5):
    if(x==f and y=="M"):
        first_par=first_par+1
for x,y in zip(x2,x5):
    if(x==t and y=="M"):
        second_par=second_par+1
for x,y in zip(x3,x5):
    if(x==r and y=="M"):
        third_par=third_par+1
for x,y in zip(x4,x5):
    if(x==h and y=="M"):
        fourth_par=fourth_par+1
#print(first_par)
first_par=first_par/count_gm
second_par=second_par/count_gm
third_par=third_par/count_gm
fourth_par=fourth_par/count_gm

ans1=first_par*second_par*third_par*fourth_par*(count_gm/n)
print("ans1(MALE):",ans1)

first_par=0
second_par=0
third_par=0
fourth_par=0

for x,y in zip(x1,x5):
    if(x==f and y=="F"):
        first_par=first_par+1
for x,y in zip(x2,x5):
    if(x==t and y=="F"):
        second_par=second_par+1
for x,y in zip(x3,x5):
    if(x==r and y=="F"):
        third_par=third_par+1
for x,y in zip(x4,x5):
    if(x==h and y=="F"):
        fourth_par=fourth_par+1
first_par=first_par/count_gf
second_par=second_par/count_gf
third_par=third_par/count_gf
fourth_par=fourth_par/count_gf

ans2=first_par*second_par*third_par*fourth_par*(count_gf/n)
print("ans2(FEMALE):",ans2)

if(ans1>ans2):
    print("Customer is more probably MALE")
else:
    print("Customer is more probably FEMALE")      
        
'''
OUTPUT:-

Enter the details for instance to be classified:
Enter Finance_Invest_Promotion(Y/N):N
Enter Travel_Tour_Promotion(Y/N):Y
Enter Reading Magazine_Promotion(Y/N):Y
Enter Helath/diet_Promotion(Y/N):N
ans1(MALE): 0.006944444444444444
ans2(FEMALE): 0.028125
Customer is more probably FEMALE
'''

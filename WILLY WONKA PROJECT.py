# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 23:52:25 2023

@author: user
"""

def Productivity():
    import pandas
    df = pandas.read_csv("   ")    
    print(df)   
    total=df.sum()
    dictionary={}
    Ratios=[] # All ratios 
    machines_name=[]
    
    non_defectives_Chilly=[]
    defectives_Chilly=[]
    
    non_defectives_Nutty=[]
    defectives_Nutty=[]
    
    non_defectives_Caramel=[]
    defectives_Caramel=[]
    
    non_defectives_Fudgemellow=[]
    defectives_Fudgemellow=[]
    
    chilly_machines=[]
    nutty_machines=[]
    caramel_machines=[]
    fudgemellow_machines=[]
    
    chilly_ratios=[]
    nutty_ratios=[]
    caramel_ratios=[]
    fudgemellow_ratios=[]
    
    x=0
    length_file=len(df)
    while length_file>x:
        liste =list(df.loc[x])
        if  liste[1]=="Chilly": 
            non_defective_Chilly=liste[2]
            defective_Chilly= liste[3]
            machine_name_Chilly=liste[0]
            
            non_defectives_Chilly.append(non_defective_Chilly)
            defectives_Chilly.append(defective_Chilly)    
            
            machine_name= df.loc[x, "Machine name"]
            machines_name.append(machine_name_Chilly)
            ratios = defective_Chilly/(defective_Chilly + non_defective_Chilly)
            Ratios.append(ratios)
            dictionary[machine_name]=ratios
            chilly_machines.append(machine_name)
            chilly_ratios.append(ratios)
            
        if liste[1]=="Nutty": 
            non_defective_Nutty=liste[2]
            defective_Nutty= liste[3]
            machine_name_Nutty=liste[0]
            
            non_defectives_Nutty.append(non_defective_Nutty)
            defectives_Nutty.append(defective_Nutty)
            machines_name.append(machine_name_Nutty)
            machine_name= df.loc[x,"Machine name"]
            
            ratios = defective_Nutty/(defective_Nutty + non_defective_Nutty)
            Ratios.append(ratios)
            nutty_machines.append(machine_name)
            dictionary[machine_name]=ratios
            nutty_ratios.append(ratios)
        
        if  liste[1]=="Caramel": 
            non_defective_Caramel=liste[2]
            defective_Caramel= liste[3]
            machine_name_Caramel=liste[0]
            
            non_defectives_Caramel.append(non_defective_Caramel)
            defectives_Caramel.append(defective_Caramel) 
        
            machines_name.append(machine_name_Caramel)
            machine_name= df.loc[x, "Machine name"]
            ratios = defective_Caramel/(defective_Caramel + non_defective_Caramel)
            Ratios.append(ratios)
            dictionary[machine_name]=ratios
            caramel_machines.append(machine_name)
            caramel_ratios.append(ratios)
            
        if  liste[1]=="Fudgemellow" :
            non_defective_Fudgemellow=liste[2]
            defective_Fudgemellow= liste[3]
            machine_name_Fudgemellow=liste[0]
            
            non_defectives_Fudgemellow.append(non_defective_Fudgemellow)
            defectives_Fudgemellow.append(defective_Fudgemellow)
         
            machine_name= df.loc[x, "Machine name"]
            machines_name.append(machine_name_Fudgemellow)
            
            ratios = defective_Fudgemellow/(defective_Fudgemellow + non_defective_Fudgemellow)
            Ratios.append(ratios)
            dictionary[machine_name]=ratios
            fudgemellow_machines.append(machine_name)
            fudgemellow_ratios.append(ratios)               
        x=x+1      
    
    total_non_defectives_Chilly=sum(non_defectives_Chilly)
    total_defectives_Chilly=sum(defectives_Chilly)
    total_net_Chilly=total_non_defectives_Chilly+total_defectives_Chilly
    
    total_non_defectives_Nutty=sum(non_defectives_Nutty)
    total_defectives_Nutty=sum(defectives_Nutty)
    total_net_Nutty =total_non_defectives_Nutty+total_defectives_Nutty
    
    total_non_defectives_Caramel=sum(non_defectives_Caramel)
    total_defectives_Caramel=sum(defectives_Caramel)
    total_net_Caramel=total_non_defectives_Caramel+total_defectives_Caramel
                   
    total_non_defectives_Fudgemellow=sum(non_defectives_Fudgemellow)
    total_defectives_Fudgemellow=sum(defectives_Fudgemellow)  
    total_net_Fudgemellow=total_non_defectives_Fudgemellow+total_defectives_Fudgemellow
    
    print("""
          ************************************************
           Willy Wonka's Production Line Tracking Program
          ************************************************
          Operations:
          1-Display The Owerall Production Quantities
          2-Display The Production Quantities For A Spesific Chocolate
          3-Display The Most Reliable Machine
          4-Display The Most Reliable Machine For A Spesific Chocolate
          5-Display The Production Percentages Of All Machines
          0-EXIT
          """)
    while True:
        answer=input("Select an operation:")
        if answer == "1":
           print("Non defective and defective number of Chilly:", total_non_defectives_Chilly,"and ",total_defectives_Chilly)

           print("Non defective and defective number of Nutty:", total_non_defectives_Nutty,"and ",total_defectives_Nutty)

           print("Non defective and defective number of Caramel:", total_non_defectives_Caramel,"and",total_defectives_Caramel)

           print("Non defective and defective number of Fudgemellow:", total_non_defectives_Fudgemellow,"and",total_defectives_Fudgemellow)
           
        elif answer== "2":
           chocolate_name=input("Enter a name of chocolate:")
           if  chocolate_name== "Chilly":
               print("Non defective number and Defective number  of Chilly:", total_non_defectives_Chilly,",",total_defectives_Chilly)
                  
           elif  chocolate_name=="Nutty":
                print("Non defective number and Defective number of Nutty:", total_non_defectives_Nutty,",",total_defectives_Nutty)
                
           elif  chocolate_name=="Caramel":
                print("Non defective number and Defective number of Caramel:", total_non_defectives_Caramel,",",total_defectives_Caramel)
                
           elif chocolate_name=="Fudgemellow":
                print("Non defective number  and Defective number of Fudgemellow:", total_non_defectives_Fudgemellow,",", total_defectives_Fudgemellow)
                
            
           else:
               print("Please enter a valid chocolate name")
                
        elif answer=="3":       
            min_ratio=min(Ratios)
            keys = list(dictionary.keys())
            vals = list(dictionary.values())
            print("Most reliable machine is "+(keys[vals.index(min_ratio)]),"and it's ratio is", min_ratio )
           
        elif answer=="4":
            chocolate_name=input("Enter a chocolate name:")
            if chocolate_name=="Chilly":
                chilly=dict(zip(chilly_ratios,chilly_machines))
                print("Most efficient machine is ",chilly[min(chilly_ratios)],"and it's ratio is",min(chilly_ratios))
                
            elif chocolate_name=="Nutty":
                nutty=dict(zip(nutty_ratios,nutty_machines))
                print("Most efficient machine is ",nutty[min(nutty_ratios)],"and it's ratio is",min(nutty_ratios))
            
            elif chocolate_name=="Caramel":
                caramel=dict(zip(caramel_ratios,caramel_machines))
                print("Most efficient machine is ",caramel[min(caramel_ratios)],"and it's ratio is",min(caramel_ratios))
        
            elif chocolate_name=="Fudgemellow":
                fudgemellow=dict(zip(fudgemellow_ratios,fudgemellow_machines))
                print("Most efficient machine is ",fudgemellow[min(fudgemellow_ratios)],"and it's ratio is",min(fudgemellow_ratios))
                
            else:
                print("Please enter a valid chocolate name")
    
        elif answer=="5":
            total=df.sum()
            all_chocolates=(total[2]+total[3])
            x=0
            while length_file>x:
                row=list(df.loc[x])
                chocolate=(row[2]+row[3])
                ratio=(chocolate)/(all_chocolates)
                if row[1]=="Chilly":
                    chocolate=(row[2]+row[3])
                    ratio2=chocolate/(total_net_Chilly)
                    print(row[0],"is producing",ratio*100,"%","of all chocolates and",ratio2*100,"%","of Chillies")   
                    
                elif row[1]=="Nutty":
                    chocolate=(row[2]+row[3])
                    ratio2=chocolate/(total_net_Nutty)
                    print(row[0],"is producing",ratio*100,"%","of all chocolates and",ratio2*100,"%","of Nuttys")
                
                elif row[1]=="Caramel":
                    chocolate=(row[2]+row[3])
                    ratio2=chocolate/(total_net_Caramel)
                    print(row[0],"is producing",ratio*100,"%","of all chocolates and",ratio2*100,"%","of Caramels")
                
                elif row[1]=="Fudgemellow":
                    chocolate=(row[2]+row[3])
                    ratio2=chocolate/(total_net_Fudgemellow)
                    print(row[0],"is producing",ratio*100,"%","of all chocolates and",ratio2*100,"%","of Fudgemellows")
                x+=1
        elif answer=="0":
            print("EXIT")
            break
        else:
            print("Please give a valid choice")    
               
def Forecasting():
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    import random
    a=0
    Chilly1=[]
    Caramel1=[]
    Nutty1=[]
    Fudgemallow1=[]
    Total=[]
    
    Nutty=[8000]
    Caramel=[7000]
    Chilly=[9000]
    Fudgemallow=[5000]
    
    Chilly_min_value=(Chilly[len(Chilly)-1])+(Chilly[len(Chilly)-1]/100)*-2
    Chilly_max_value=(Chilly[len(Chilly)-1])+(Chilly[len(Chilly)-1]/100)*5
    
    Caramel_min_value=(Caramel[len(Caramel)-1])+(Caramel[len(Caramel)-1]/100)*-2
    Caramel_max_value=(Caramel[len(Caramel)-1])+(Caramel[len(Caramel)-1]/100)*5
    
    Nutty_min_value=(Nutty[len(Nutty)-1])+(Nutty[len(Nutty)-1]/100)*-2
    Nutty_max_value=(Nutty[len(Nutty)-1])+(Nutty[len(Nutty)-1]/100)*5
    
    Fudgemallow_min_value=(Fudgemallow[len(Fudgemallow)-1])+(Fudgemallow[len(Fudgemallow)-1]/100)*-2
    Fudgemallow_max_value=(Fudgemallow[len(Fudgemallow)-1])+(Fudgemallow[len(Fudgemallow)-1]/100)*5
    
    n=0
    while n <10:   
           new_Caramel=random.randint(Caramel_min_value,Caramel_max_value)
           Caramel.append(new_Caramel)   
           
           new_Fudgemallow=random.randint(Fudgemallow_min_value,Fudgemallow_max_value)
           Fudgemallow.append(new_Fudgemallow)
           
           new_Chilly=random.randint(Chilly_min_value,Chilly_max_value)
           Chilly.append(new_Chilly)   
           
           new_Nutty=random.randint(Nutty_min_value,Nutty_max_value)
           Nutty.append(new_Nutty)    
           
           if a < 10:          
               difference_chilly=(Chilly[len(Chilly)-1])-(Chilly[len(Chilly)-2])
               Chilly1.append(difference_chilly)
               
               difference_caramel=(Caramel[len(Caramel)-1])-(Caramel[len(Caramel)-2])
               Caramel1.append(difference_caramel)   
               
               difference_nutty=(Nutty[len(Nutty)-1])-(Nutty[len(Nutty)-2])
               Nutty1.append(difference_nutty)  
                       
               difference_fudgemallow=(Fudgemallow[len(Fudgemallow)-1])-(Fudgemallow[len(Fudgemallow)-2])
               Fudgemallow1.append(difference_fudgemallow)  
               
               Total.append(difference_chilly+difference_caramel+difference_nutty+difference_fudgemallow)           
               a=a+1
           n=n+1      
    
    d1 = {'Chilly' : Chilly[0], 'Nutty' :Nutty[0],  'Fudgemallow' : Fudgemallow[0], 'Caramel': Caramel[0],"Year":["2020"]}
    df1 = pd.DataFrame(d1, columns = ['Year','Chilly','Nutty','Fudgemallow','Caramel'] ,index=[0])
    d2 = {'Chilly' : Chilly[1], 'Nutty' :Nutty[1],  'Fudgemallow' : Fudgemallow[1], 'Caramel': Caramel[1],"Year":["2021"]}
    df2 = pd.DataFrame(d2, columns = ['Year','Chilly','Nutty','Fudgemallow','Caramel'],index=[1])
    df1=df1.append(df2)
    d3 = {'Chilly' : Chilly[2], 'Nutty' :Nutty[2],  'Fudgemallow' : Fudgemallow[2], 'Caramel': Caramel[2],"Year":["2022"]}
    df3 = pd.DataFrame(d3, columns = ['Year','Chilly','Nutty','Fudgemallow','Caramel'],index=[2])
    df1=df1.append(df3)
    d4 = {'Chilly' : Chilly[3], 'Nutty' :Nutty[3],  'Fudgemallow' : Fudgemallow[3], 'Caramel': Caramel[3],"Year":["2023"]}
    df4 = pd.DataFrame(d4, columns = ['Year','Chilly','Nutty','Fudgemallow','Caramel'],index=[3])
    df1=df1.append(df4)
    d5 = {'Chilly' : Chilly[4], 'Nutty' :Nutty[4],  'Fudgemallow' : Fudgemallow[4], 'Caramel': Caramel[4],"Year":["2024"]}
    df5 = pd.DataFrame(d5, columns = ['Year','Chilly','Nutty','Fudgemallow','Caramel'],index=[4])
    df1=df1.append(df5)
    d6 = {'Chilly' : Chilly[5], 'Nutty' :Nutty[5],  'Fudgemallow' : Fudgemallow[5], 'Caramel': Caramel[5],"Year":["2025"]}
    df6 = pd.DataFrame(d6, columns = ['Year','Chilly','Nutty','Fudgemallow','Caramel'],index=[5])
    df1=df1.append(df6)
    d7 = {'Chilly' : Chilly[6], 'Nutty' :Nutty[6],  'Fudgemallow' : Fudgemallow[6], 'Caramel': Caramel[6],"Year":["2026"]}
    df7 = pd.DataFrame(d7, columns = ['Year','Chilly','Nutty','Fudgemallow','Caramel'],index=[6])
    df1=df1.append(df7)
    d8 = {'Chilly' : Chilly[7], 'Nutty' :Nutty[7],  'Fudgemallow' : Fudgemallow[7], 'Caramel': Caramel[7],"Year":["2027"]}
    df8 = pd.DataFrame(d8, columns = ['Year','Chilly','Nutty','Fudgemallow','Caramel'],index=[7])
    df1=df1.append(df8)
    d9 = {'Chilly' : Chilly[8], 'Nutty' :Nutty[8],  'Fudgemallow' : Fudgemallow[8], 'Caramel': Caramel[8],"Year":["2028"]}
    df9 = pd.DataFrame(d9, columns = ['Year','Chilly','Nutty','Fudgemallow','Caramel'],index=[8])
    df1=df1.append(df9)
    d10 = {'Chilly' : Chilly[9], 'Nutty' :Nutty[9],  'Fudgemallow' : Fudgemallow[9], 'Caramel': Caramel[9],"Year":["2029"]}
    df10 = pd.DataFrame(d10, columns = ['Year','Chilly','Nutty','Fudgemallow','Caramel'],index=[9])
    df1=df1.append(df10)
    d11 = {'Chilly' : Chilly[10], 'Nutty' :Nutty[10],  'Fudgemallow' : Fudgemallow[10], 'Caramel': Caramel[10],"Year":["2030"]}
    df11 = pd.DataFrame(d11, columns = ['Year','Chilly','Nutty','Fudgemallow','Caramel'],index=[10])
    df1=df1.append(df11)
    
    print(df1)
    
    years=np.arange(2020,2031)        
    plt.plot(years, Chilly, color='g')
    plt.plot(years, Nutty, color='orange')
    plt.plot(years, Caramel, color='b')
    plt.plot(years, Fudgemallow, color='r')
    plt.xticks([2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030])
    
    plt.xlabel('years')
    plt.ylabel('Number of products')
    plt.title('Production') 
    
    plt.legend(['Chilly','Nutty','Caramel','Fudgemallow'],loc=1)
    plt.show()
    
    d1 = {'Chilly' : Chilly1[0], 'Nutty' :Nutty1[0],  'Fudgemallow' : Fudgemallow1[0], 'Caramel' : Caramel1[0],'Total': Total[0], 'Year': ["2021"]}
    df1 = pd.DataFrame(d1, columns = ['Year','Chilly','Nutty','Fudgemallow','Caramel','Total'], index=[0])
    d2 = {'Chilly' : Chilly1[1], 'Nutty' :Nutty1[1],  'Fudgemallow' : Fudgemallow1[1], 'Caramel' : Caramel1[1], 'Total': Total[1], 'Year':["2022"]}
    df2 = pd.DataFrame(d2, columns = ['Year','Chilly','Nutty','Fudgemallow','Caramel','Total'], index=[1])  
    df1=df1.append(df2)
    d3 = {'Chilly' : Chilly1[2], 'Nutty' :Nutty1[2],  'Fudgemallow' : Fudgemallow1[2], 'Caramel' : Caramel1[2],'Total': Total[2], 'Year': ["2023"]}
    df3 = pd.DataFrame(d3, columns = ['Year','Chilly','Nutty','Fudgemallow', 'Caramel','Total' ], index=[2]) 
    df1=df1.append(df3)
    d4 = {'Chilly' : Chilly1[3], 'Nutty' :Nutty1[3],  'Fudgemallow' : Fudgemallow1[3], 'Caramel' : Caramel1[3],'Total': Total[3], 'Year': ["2024"]}
    df4 = pd.DataFrame(d4, columns = ['Year','Chilly','Nutty','Fudgemallow','Caramel','Total'], index=[3]) 
    df1=df1.append(df4)
    d5 = {'Chilly' : Chilly1[4], 'Nutty' :Nutty1[4],  'Fudgemallow' : Fudgemallow1[4], 'Caramel' : Caramel1[4],'Total': Total[4], 'Year': ["2025"]}
    df5 = pd.DataFrame(d5, columns = ['Year','Chilly','Nutty','Fudgemallow','Caramel','Total'], index=[4])
    df1=df1.append(df5)
    d6 = {'Chilly' : Chilly1[5], 'Nutty' :Nutty1[5],  'Fudgemallow' : Fudgemallow1[5], 'Caramel' : Caramel1[5],'Total': Total[5], 'Year': ["2026"]}
    df6 = pd.DataFrame(d6, columns = ['Year','Chilly','Nutty','Fudgemallow','Caramel','Total'], index=[5]) 
    df1=df1.append(df6)
    d7 = {'Chilly' : Chilly1[6], 'Nutty' :Nutty1[6],  'Fudgemallow' : Fudgemallow1[6], 'Caramel' : Caramel1[6],'Total': Total[6], 'Year': ["2027"]}
    df7 = pd.DataFrame(d7, columns = ['Year','Chilly','Nutty','Fudgemallow','Caramel','Total'], index=[6]) 
    df1=df1.append(df7)
    d8 = {'Chilly' : Chilly1[7], 'Nutty' :Nutty1[7],  'Fudgemallow' : Fudgemallow1[7], 'Caramel' : Caramel1[7],'Total': Total[7], 'Year': ["2028"]}
    df8 = pd.DataFrame(d8, columns = ['Year','Chilly','Nutty','Fudgemallow','Caramel','Total'], index=[7]) 
    df1=df1.append(df8)
    d9= {'Chilly' : Chilly1[8], 'Nutty' :Nutty1[8],  'Fudgemallow' : Fudgemallow1[8], 'Caramel' : Caramel1[8],'Total': Total[8], 'Year': ["2029"]}
    df9 = pd.DataFrame(d9, columns = ['Year','Chilly','Nutty','Fudgemallow','Caramel','Total'], index=[8]) 
    df1=df1.append(df9)
    d10 = {'Chilly' : Chilly1[9], 'Nutty' :Nutty1[9],  'Fudgemallow' : Fudgemallow1[9], 'Caramel' : Caramel1[9],'Total': Total[9], 'Year': ["2030"]}
    df10 = pd.DataFrame(d10, columns = ['Year','Chilly','Nutty','Fudgemallow','Caramel','Total'], index=[9])
    df1=df1.append(df10)
      
    print(df1)     
    
    import matplotlib.pyplot as plt
    import numpy as np
    years1=np.arange(2021,2031)     
    plt.plot(years1, Chilly1, color='g')
    plt.plot(years1, Caramel1, color='b')
    plt.plot(years1, Nutty1, color='orange')
    plt.plot(years1, Fudgemallow1, color='r')
    plt.plot(years1, Total, color='y')
    plt.xticks([2021,2022,2023,2024,2025,2026,2027,2028,2029,2030])
    plt.xlabel('years')
    plt.ylabel('production differences')
    plt.title('Producing Differences') 
    plt.legend(['Chilly','Nutty','Caramel','Fudgemallow',"Total"],loc=1)
    plt.show()    
        
        
    
    
def Simulation():    
    import random
    knowladge={}
    n=0
    turn=0 #indicates how many times it have completed your mission
    turn2=0 #indicates how many times it have completed your mission
    turn3=0 #indicates how many times it have completed your mission
    tiles=0
    turns=[]
    row_bumblebee1=3
    row_bumblebee2=3
    row_bumblebee3=3
    while n <= 1000000:
       bumblebee1=random.randint(1,100)
       if tiles >=0  and tiles<101:
           if bumblebee1 >= 1 and  bumblebee1 <=80:       
              tiles=tiles+1       
           if bumblebee1 > 80 and  bumblebee1 <=90:
               row_bumblebee1=row_bumblebee1+1
               if row_bumblebee1>5:
                 n=n+1         
                 row_bumblebee1=3
                 tiles=0
                 continue
           if bumblebee1 > 90 and  bumblebee1 <=100:      
              row_bumblebee1=row_bumblebee1-1       
              if row_bumblebee1<1:
                 n=n+1         
                 row_bumblebee1=3
                 tiles=0
                 continue 
       if tiles >=101 and tiles<=200:
             bumblebee1=random.randint(1,100)
             if bumblebee1 >= 1 and  bumblebee1 <=80:
                 tiles=tiles+1         
             if bumblebee1 > 80 and  bumblebee1 <=90:
                 row_bumblebee1=row_bumblebee1+1
                 if row_bumblebee1>5:
                    n=n+1
                    row_bumblebee1=3
                    tiles=0
                    continue
             if bumblebee1 > 90 and  bumblebee1 <=100:
                 row_bumblebee1=row_bumblebee1-1
                 if row_bumblebee1<1:
                    n=n+1
                    row_bumblebee1=3
                    tiles=0
                    continue
       if tiles==201:
           turn=turn+1
           tiles=0
           row_bumblebee1=3
       n=n+1
    tiles=0   
    n=0
    turns.append(turn)    
    while n <=1000000:
       if tiles  >=0 and tiles<101:  
           if row_bumblebee2==3:
               bumblebee2=random.randint(1,100)
               if  bumblebee2 >= 1 and  bumblebee2 <=50:
                  tiles=tiles+1  
               if  bumblebee2 >50 and  bumblebee2 <=75:
                   row_bumblebee2=row_bumblebee2+1            
               if  bumblebee2 >75 and  bumblebee2 <=100: 
                   row_bumblebee2=row_bumblebee2-1            
           if  row_bumblebee2==1 or row_bumblebee2==2: 
               bumblebee2=random.randint(1,100)
               if  bumblebee2 >= 1 and  bumblebee2 <=50:                    
                      row_bumblebee2= row_bumblebee2+1                              
               if  bumblebee2 > 50 and  bumblebee2 <=90:            
                        tiles=tiles+1       
               if  bumblebee2 > 90 and  bumblebee2 <=100:
                          tiles=tiles-1 
                          if tiles==0:
                            n=n+1            
                            row_bumblebee2=3
                            tiles=0
                            continue      
           if  row_bumblebee2==4 or row_bumblebee2==5:
               bumblebee2=random.randint(1,100)
               if  bumblebee2 >= 1 and  bumblebee2 <=50:
                       row_bumblebee2= row_bumblebee2-1                
               if  bumblebee2 > 50 and  bumblebee2 <=90:           
                   tiles=tiles+1               
               if  bumblebee2 > 90 and  bumblebee2 <=100:
                   tiles=tiles-1 
                   if tiles==0:
                        n=n+1            
                        row_bumblebee2=3
                        tiles=0
                        continue     
            
       if tiles >=101 and tiles<=200:      
             if row_bumblebee2==3:
               bumblebee2=random.randint(1,100)  
               if  bumblebee2 >= 1 and  bumblebee2 <=50:
                  tiles=tiles+1          
               if  bumblebee2 >50 and  bumblebee2 <=75:
                   row_bumblebee2=row_bumblebee2+1            
               if  bumblebee2 >75 and  bumblebee2 <=100: 
                   row_bumblebee2=row_bumblebee2-1            
             if  row_bumblebee2==1 or row_bumblebee2==2:
               bumblebee2=random.randint(1,100)
               if  bumblebee2 >= 1 and  bumblebee2 <=50:
                   row_bumblebee2= row_bumblebee2+1            
               if  bumblebee2 > 50 and  bumblebee2 <=90:            
                   tiles=tiles+1                 
               if  bumblebee2 > 90 and  bumblebee2 <=100:
                   tiles=tiles-1 
                   if tiles==100:
                        n=n+1            
                        row_bumblebee2=3
                        tiles=0
                        continue                 
             if  row_bumblebee2==4 or row_bumblebee2==5:
               bumblebee2=random.randint(1,100)
               if  bumblebee2 >= 1 and  bumblebee2 <=50:
                   row_bumblebee2= row_bumblebee2-1            
               if  bumblebee2 > 50 and  bumblebee2 <=90:           
                   tiles=tiles+1                
               if  bumblebee2 > 90 and  bumblebee2 <=100:
                   tiles=tiles-1 
                   if tiles==100:
                        n=n+1            
                        row_bumblebee2=3
                        tiles=0
                        continue     
       if tiles==201:
            turn2=turn2+1
            tiles==0  
            row_bumblebee2=3        
       n=n+1           
    tiles=0   
    n=0      
    turns.append(turn2) 
    while n <= 1000000:
       if tiles >=0 and tiles<101:  
           if row_bumblebee3==3:
               bumblebee3=random.randint(1,100)
               if  bumblebee3 >= 1 and  bumblebee3 <=20:
                   tiles=tiles+1     
               if  bumblebee3 >20 and  bumblebee3 <=60:
                   row_bumblebee3=row_bumblebee3+1                                   
               if  bumblebee3>60 and  bumblebee3 <=100: 
                   row_bumblebee3=row_bumblebee3-1                                              
           if  row_bumblebee3==2 or row_bumblebee3==4: 
               bumblebee3=random.randint(1,100)
               if  bumblebee3 >= 1 and  bumblebee3 <=25:
                   tiles+=1
               if  bumblebee3 >= 25 and  bumblebee3 <=50:
                   tiles-=1
                   if tiles<0:
                            n=n+1            
                            row_bumblebee3=3
                            tiles=0                    
                            continue                
               if  bumblebee3 >= 50 and  bumblebee3 <=75:
                   if row_bumblebee3==2:
                      row_bumblebee3+=1            
               if  bumblebee3 >= 75 and  bumblebee3 <=100:
                   if row_bumblebee3==4:
                      row_bumblebee3-=1       
           if  row_bumblebee3==1 or row_bumblebee3==5: 
                 bumblebee3=random.randint(1,100)
                 if  bumblebee3 >= 1 and  bumblebee3 <=30:
                      tiles+=1
                 if  bumblebee3 >= 30 and  bumblebee3 <=40:
                      tiles-=1
                      if tiles<0:
                         n=n+1            
                         row_bumblebee3=3
                         tiles=0            
                         continue    
                 if  bumblebee3 >= 40 and  bumblebee3 <=100:
                     if row_bumblebee3==1:
                         row_bumblebee3+=1                
                     if row_bumblebee3==5:
                         row_bumblebee3-=1       
       if tiles >=101 and tiles<=200:      
             if row_bumblebee3==3:
                  bumblebee3=random.randint(1,100)  
                  if  bumblebee3 >= 1 and  bumblebee3 <=20:
                     tiles=tiles+1     
                  if  bumblebee3 >20 and  bumblebee3 <=60:
                      row_bumblebee3=row_bumblebee3+1                               
                  if  bumblebee3>60 and  bumblebee3 <=100: 
                      row_bumblebee3=row_bumblebee3-1                                        
             if  row_bumblebee3==2 or row_bumblebee3==4:  
                  bumblebee3=random.randint(1,100)
                  if  bumblebee3 >= 1 and  bumblebee3 <=25:
                      tiles+=1
                  if  bumblebee3 >= 25 and  bumblebee3 <=50:
                      tiles-=1
                      if tiles<101:
                               n=n+1            
                               row_bumblebee3=3
                               tiles=0                     
                               continue     
                  if  bumblebee3 >= 50 and  bumblebee3 <=75:
                      if row_bumblebee3==2:
                         row_bumblebee3+=1
                  if  bumblebee3 >= 75 and  bumblebee3 <=100:
                      if row_bumblebee3==4:
                         row_bumblebee3-=1       
             if  row_bumblebee3==1 or row_bumblebee3==5:
                  bumblebee3=random.randint(1,100)
                  if  bumblebee3 >= 1 and  bumblebee3 <=30:
                      tiles+=1
                  if  bumblebee3 >= 30 and  bumblebee3 <=40:
                      tiles-=1
                      if tiles<101:
                          n=n+1
                          row_bumblebee3=3
                          tiles=0
                          continue
                  if  bumblebee3 >= 40 and  bumblebee3 <=100:
                      if row_bumblebee3==1:
                          row_bumblebee3+=1
                      if row_bumblebee3==5:
                          row_bumblebee3-=1           
       if tiles==201:
            turn3=turn3+1
            tiles==0  
            row_bumblebee3=3   
       n=n+1               
       
    turns.append(turn3)      
    machines=["bumblebee1","bumblebee2","bumblebee3"]
    knowladge=dict(zip(turns,machines))
    print("most efficient machine:",knowladge[max(turns)])
                  
choice = input("Select module: ")
if choice.isdigit():
    choice = int(choice)
else:
    choice = 0    

if choice == 1:
    Productivity()
elif choice == 2:
    Forecasting()
elif choice == 3:
    Simulation()    
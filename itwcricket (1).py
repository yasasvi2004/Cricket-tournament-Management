import random
import numpy as num
def playover():
 list6 = [0,1]
 print("")
 print("                                               TOSS TIME  ")
 print("Random toss will be generated by computer if it is same as your input then computer will bat else you will bat")
 k=int(input("ENTER 0 or 1::"))
 if random.choice(list6)!=k :
  print("")
  print("you have WON the toss and now you are going to bat")
  print("\t\t\t-------------------------------------INSTRUCTION-----------------------------------------------\n")
  print(" For Batting:\n")
  print("1.Choose a number from 1 to 6.\n")
  print("2.If the choosen number is same as number of randon number generated by computer then it result in fall of your wicket.\n")
  print("3.If the choosen number is different form random number generated by computer then that number will be your runs.\n")
  print("4.You will be facing 6 balls.\n\n")
  print("*************************************We are now going to play against computer which is generated in python****************************************")
  list1 = [1, 2, 3, 4, 5, 6]
 #print(random.choice(list1))
  list2 = ["caught","bold","stumped","run out","caught and bold","lbw"]
  print("over started")
  j=1
  score1=0
  while j<7:
    i=int(input("enter a number between 1 to 6::"))
    if i==random.choice(list1) :
     print(random.choice(list2)) 
     print("you are out")
     break
    score1=score1+i
    print("score::"+str(score1)+"in:"+str(j)+"balls")
    j+=1
  print("innings completed thank you for playing with us")   
  print("innings outcome- score::"+str(score1)+"in:"+str(j)+"balls")
  print("")
  print("innings change you are bowling now")
  print("\t\t\t-------------------------------------INSTRUCTION-----------------------------------------------\n")
  print(" For Bowling:\n")
  print("1.Choose a number from 1 to 6.\n")
  print("2.If the number u choosen is same as number of random generated by computer then it will result in fall of wicket of computer.\n")
  print("3.If the number u choosen is different from random number generated by computer then that number will be computers runs.\n")
  print("4.In an over we have to bowl 6 balls.\n\n")
  o=1
  score2=0
  while o<7:
    p=int(input("enter a number between 1 to 6::"))
    if p==random.choice(list1) :
     print(random.choice(list2)) 
     print("computer got out")
     break
    score2=score2+random.choice(list1)
    print("score::"+str(score2)+"in:"+str(o)+"balls")
    o+=1
  print("innings completed thank you for playing with us")   
  print("innings outcome- score::"+str(score2)+"in:"+str(o)+"balls")  
  if score1<score2:
    print("Better luck next time you LOST the match by"+str((score2-score1))+"runs")
    print("")
    print("")
    #print("summary:")
  else:
    print("Hurray You WON the match by"+str((score1-score2))+"runs")  
    print("")
    print("")
 else:
  print("\t\t\t-------------------------------------INSTRUCTION-----------------------------------------------\n")
  print(" For Bowling:\n")
  print("1.Choose a number from 1 to 6.\n")
  print("2.If the number u choosen is same as number of random generated by computer then it will result in fall of wicket of computer.\n")
  print("3.If the number u choosen is different from random number generated by computer then that number will be computers runs.\n")
  print("4.In an over we have to bowl 6 balls.\n\n")
  list1 = [1, 2, 3, 4, 5, 6]
 #print(random.choice(list1))
  list2 = ["caught","bold","stumped","run out","caught and bold","lbw"]
  print("over started")
  j=1
  score1=0
  while j<7:
    i=int(input("enter a number between 1 to 6::"))
    if i==random.choice(list1) :
     print(random.choice(list2)) 
     print("computer got out")
     break
    score1=score1+random.choice(list1)
    print("score::"+str(score1)+"in:"+str(j)+"balls")
    j+=1
  print("innings completed thank you for playing with us")   
  print("innings outcome- score::"+str(score1)+"in:"+str(j)+"balls")  
  print("")
  print("")
  print("innings change now you are going to bat")
  print("\t\t\t-------------------------------------INSTRUCTION-----------------------------------------------\n")
  print(" For Batting:\n")
  print("1.Choose a number from 1 to 6.\n")
  print("2.If the choosen number is same as number of randon number generated by computer then it result in fall of your wicket.\n")
  print("3.If the choosen number is different form random number generated by computer then that number will be your runs.\n")
  print("4.You will be facing 6 balls.\n\n")
  print("*************************************We are now going to play against computer which is generated in python****************************************")
  o=1
  score2=0
  while o<7:
    p=int(input("enter a number between 1 to 6::"))
    if p==random.choice(list1) :
     print(random.choice(list2)) 
     print("you got out")
     break
    score2=score2+p
    print("score::"+str(score2)+"in:"+str(o)+"balls")
    o+=1
  print("innings completed thank you for playing with us")   
  print("innings outcome- score::"+str(score2)+"in:"+str(o)+"balls")  
  if score1<score2:
    print("Hurray You won the match by"+str((score2-score1))+"runs")
    print("")
    print("")
    #print("summary:")
  else:
    print("Better luck next time you LOST the match by"+str((score1-score2))+"runs")  
    print("")
    print("")
 
def toseepreviousyeariplstats():
    def tosee18():
     f = open('2018.txt', 'r')
     content = f.read()
     print(content)
     f.close()
    def tosee19():
     print("2019 stats will be printed from file")
    def tosee20():
     print("2020 stats will be printed from file")
    def default():
     print("you have entered an invalid input")
    
    switcher = {
    18: tosee18,
    19: tosee19,
    20: tosee20,
    4: exit,
    }
    print("  enter 18 to see 2018 stats")
    print("  enter 19 to see 2019 stats")
    print("  enter 20 to see 2020 stats")
    print("  enter 4 to exit")
    print("")

    h=int(input("enter a number by observing above correspndence:"))
    switcher.get(h, default)()
def matchschedules():
    print("")
    print("")
    print("")
    

    print("                                             All teams are divided into TEAMA and TEAMB                                 ")
    print("                         *******                                                                                 *******") 
    print("                         -TEAMA-                                                                                 -TEAMB-")
    print("                         * SRH *                                                                                 * LSG *")
    print("                         * KKR *                                                                                 * RR_ *")
    print("                         * MI_ *                                                                                 * DC_ *")
    print("                         * CSK *                                                                                 * GT_ *")
    print("                         * RCB *                                                                                 * PBK *")
    print("                         *******                                                                                 *******")
    print("")
    print("")
    list3= ["SRH","KKR","MI_","CSK","RCB"]
    list4= ["LSG","RR_","DC_","GT_","PBK"]
    print("                                                   This is schedule of an ipl season")
    print("                                               =========================================")
    print("                                               ||   DATE   ||   TEAM1  ||   TEAM2     ||")
    print("                                               =========================================")    
    i=1
    for x in range(25):
        for y in list3:
            for z in list4:
              if x+i<10:
               print("                                               ||  0"+str(x+i)+"/4/22     "+ y + "     vs    "+ z+"      ||")
              else:
               print("                                               ||  "+str(x+i)+"/4/22     "+ y + "     vs    "+ z+"      ||")

              i+=1
            list3.pop(0)  
            if y!="in":
             break
    print("                                               =========================================")    
def exit_():
    print("exitting")
    exit()
def pointstablecreation():
 def net_rr(n,i):
        result = input('Won(w)/Lost(l)/Draw(d):')
        if (result == 'w') or (result == 'l') or (result == 'd'):
            if result == 'w':
                Table[i][2] += 1
                Table[i][5] += (3*Table[i][2])
            elif result == 'l':
                Table[i][3] += 1
                Table[i][5] += 0*Table[i][3]
            elif result == 'd':
                Table[i][4] += 1
                Table[i][5] += 1*Table[i][4]
            Table[i][0] = n
            Table[i][1] += 1    
            bat_score = float(input('batting score:'))
            ovrs_played = float(input('over batted:'))
            opp_score = float(input('opponent score:'))
            opp_over = float(input('opponent over:'))
            for row in Table:
                print(row)
                print('\n')
 

 for t in range(6):
  def table( ):
    q = input('what do you want to do:')
    if q == 'Entry':
        n = input('Name:')
        if n == 'Team1':
            i = 1
        elif n == 'Team2':
            i = 2
        elif n == 'Team3':
            i = 3
        elif n == 'Team4':
            i = 4
        elif n == 'Team5':
            i = 5
        elif n == 'Team6':
            i = 6
        net_rr(n,i)
    elif q == 'Check':
        for row in Table:
            print(row)
            print('\n')
 table()
def intakeofstats():
 print("enter 1:For batting department\n2:For bowling department\n")
 x=int(input())
 if x==1:
    n=5
    d=dict(input("enter the name of the batsman and his current score  :").split() for i in range(n))
    sortedDict = sorted(d.items())
    result=sortedDict
    data=list(result)
    numpyArray=num.array(data)
    print("the list of batsmans and ")
    print(numpyArray)
    num.sort(numpyArray)
    print("1:To see highest run\n2:To see lowest run for season\n")
    abc=int(input())
    if abc==1:
        print("the orange cap holder for the season is: ")
        print(numpyArray[4])
    elif abc==2:
        print("the lowest scorer for this season is")
        print(numpyArray[0])
 elif x==2:
    n=5
    d=dict(input("enter the name of the bowler and his current wickets  :").split() for i in range(n))
    sortedDict = sorted(d.items())
    result=sortedDict
    data=list(result)
    numpyArray=num.array(data)
    print("the list of bowlers and ")
    print(numpyArray)
    num.sort(numpyArray)
    print("1:To see highest wicket taker\n2:To see lowest wicket taker for season\n")
    abc=int(input())
    if abc==1:
        print("the purple cap holder for the season is: ")
        print(numpyArray[4])
    elif abc==2:
        print("the lowest wickets for this season is")
        print(numpyArray[0])
def exit_():
    print("exitting succesfully")
    exit()
def default():
    print("you have entered an invalid input")
switcher = {
    1: playover,
    2: toseepreviousyeariplstats,
    3: matchschedules,
    4: pointstablecreation,
    5: intakeofstats,
    6: exit_,
    }
Table = [['Name','Played','Won','Lost','Draws','Points','Net_RR'],['Team1',0,0,0,0,0,0],['Team2',0,0,0,0,0,0],['Team3',0,0,0,0,0,0],['Team4',0,0,0,0,0,0],['Team5',0,0,0,0,0,0],['Team6',0,0,0,0,0,0]]
print("Ovierview of the project:This is a mini project titled ipl matches and its schedule making system along with a mini game . Motto of the project Consists of four parts i.e")
print("1)previous year stats of ipl seasons ::")
print("  In this a user will be able to view the stats of a season by selecting the year.Stats includes title winner,runner up,orange cap holder,violet cap holder for the respective season.")
print("2.)Making the schedule of a ipl season::")
print(" In this a user will be asked to enter the number of teams,names of teams by which computer will calculate the number of matches and a schedule of the season will be made.")
print(" User will be able to store schedule for futher purpose.")
print("3.)Points table creation::")

print(" A user will be able to create a points table through this feature by entering the number of teams,names of teams ,no of matches won/lost/drawn by respective team.User will be able to store the points table for future purpose.")
print("4.)Play a minigame::")
print(" Through this a user will be able to play a mini game of cricket match ,instructions to play the match will be displayed sequentially after selection.")
print("5.)Input stats of the present year")
print(" A user will be able to input stats of the present year and we will calculate the highest run scorer lowest run scorer.....")
print("")
print("                                             Please read the above INSTRUCTIONS CAREFULLY")
print("")
print("")
print("")
for t in range(10):    
 print("enter 1 to play an over with computer")
 print("enter 2 to see previous year stats")
 print("enter 3 to print a schedule of ipl")
 print("enter 4 to create a points table")
 print("enter 5 to intake of stats using numpy")
 print("enter 6 to exit")
 print("")
 i=int(input("enter a number between 1 to 6 by observing above correspndence:"))
 switcher.get(i, default)()
 print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
print("")
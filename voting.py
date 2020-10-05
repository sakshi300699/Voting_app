candidate_1 = input("enter the name of first nominee : ")
candidate_2 = input("enter the name of second nominee : ")

votes_1 = 0
votes_2 = 0

voter_id = [1,2,3,4,5,6,7,8,9,10]

no_of_voters = len(voter_id)

while True:
    if voter_id==[]:
        print("voting session over!!")
        if votes_1>votes_2:
            per = (votes_1/no_of_voters)*100
            print(candidate_1," has won", "with", per, " % votes!")
            break
        elif votes_2>votes_1:
            per = (votes_2/no_of_voters)*100
            print(candidate_2," has won", "with", per, " % votes!")
            break

    else:
        voter = int(input("enter your voting id number : "))
        if voter in voter_id:
            print("you are a voter")
            voter_id.remove(voter)
            vote = int(input("enter your vote 1 or 2: "))
            if vote==1:
                votes_1+=1
                print("Thank you for voting!")
            elif vote==2:
                votes_2+=1
                print("Thank you for voting!")

        else:
            print("you are not a voter or you have already voted!")

                
        
   
   
   
   
   
   
    

        

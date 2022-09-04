#  Election voting system

nominee1= input("Enter the name of first nominee: ")
nominee2= input("Enter the name of second nominee: ")

nm_1_votes = 0
nm_2_votes = 0

voter_id = [1,2,3,4,5,6,7,8,9,10]

no_of_voter = len(voter_id)


while True:

    if voter_id==[]:
        print("Voting session is over !!!")
        if nm_1_votes>nm_2_votes:
            percentage = (nm_1_votes/no_of_voter)*100
            print(nominee1, " has won the election with ", percentage,"% of votes")
            break;
        elif nm_2_votes>nm_1_votes:
            percentage = (nm_2_votes/no_of_voter)*100
            print(nominee2, " has won the election with ", percentage,"% votes")
            break;
        else:
            print("Both have equal number of votes and Now Goverment will decide when to have re-election ")
            break;


    voter = int(input("Enter your voter id : "))
    if voter in voter_id:
        print("You are a Voter ")
        voter_id.remove(voter)
        print("--------------------------------------")
        print("To give vote to", nominee1,"Press 1")
        print("To give vote to", nominee2,"Press 2")
        print("--------------------------------------")
        vote=int(input("Enter your precious vote: "))
        if vote == 1:
            nm_1_votes +=1
            print(nominee1,"Thank you for your precious vote")
        elif vote == 2:
            nm_1_votes +=1
            print(nominee2,"Thank you for your precious vote")
        elif vote >2:
            print("You have pressed wrong key, check Your pressed key !!")
        else:
            print("You are not a voter or You have already voted")

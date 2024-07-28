# Voters Qualification Check App

print("Voting Qualification Checker:")

votersName = input("Enter Your Name: ")
votersAge = input("Enter Voters Age: ")
 
# Convects the Voters age to Int to perform operations with it
ageofVoter = int(votersAge)

def checkQualified(name,age):
    if age >= 18 :
        return (f"{name} is Qualified to vote")

    else :
        return (f"{name} is not Qualified to vote")


result = checkQualified(votersName,ageofVoter)
print(result)

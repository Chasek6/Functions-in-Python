# Chase Stratton
# Job Application.py
#10 points
#Functions in Python 



# This is a program that will decide if a candidate will be hired or not based on the candidate years of experience and their interview scores.
# Checking if the conditions are met or not using the code below.

def HireOrReject (experience, interviewScore):
    #  The less experience the candidate has the higher  the score will need to be 85^ if less than 3 years if more than 3 years 70^ if with experience.
    # If, else, statements below to determan what is outputted based on the users input into the system.
    if experience < 3:
        # Candidates with less than 3 years of experience  -->
        if interviewScore > 85: 
            return "HIRED  !"
        else: 
            return "REJECTED!" 
    else:  
        # Candidates with more 3 years of experience  -->
        if interviewScore >70:
            return "HIRED !"
        else: 
            # Candidates with more 3 years of experience   -->
            if interviewScore > 70: 
                return "Hired !" 
            else: 
                return "REJECTED !"
def HireOrReject(experience, interviewScore): 
    # The less experience the candidate has the higher the score will need to be 85 or above if the candidate has than 3 years if more than 3 years than 70^ will be needed.
    if experience < 3:
        # The Candidates with less than 3 years of experience 85^ --->
        if interviewScore > 85: 
            return "HIRED!" 
        else:
            return "REJECTED!" 
    else:
        # The Candidates with more than 3 years of experience 70^ -->
        if interviewScore > 70:
            return "HIRED!" 
        else:
            return "REJECTED!"
        #Main Body of of code the user will interact with. -->
def main():
    # This will prompt the user to enter the candidate's name. -->
    name = input("Enter candidate's name: ") 
# try functions to wrap code that might come off as an error if that were to happen " The try block will look for 
# corresponding (expect block to handle the error)
    try: 
        # This code will prompt the user to enter their years of experience that the candidate has. -->
        experience = int(input(f"Hello {name}, please enter your years of experience : "))
        # This will prompt the user to enter their interview score that the candidate has received. -->
        interviewScore = int(input("Enter your Interview Score (0-100) : ")) 
        # (expect error) this catches value error that might be appear if the user enters a non-numeric input as an answer   
    except ValueError: 

        print("Entered an invalid input, use only numerics for Interview Score and Job Experience!.")
        return
    
    #Checking to make sure the interview score is in the expected range (0-100) -->

    if not (0 <= interviewScore <= 100):
        print("Your Interview Score should be between 0 - 100!")
        return
    
    # Adding a better UI interaction with feedback.-->

    decision = HireOrReject(experience, interviewScore) 

    if decision == "HIRED!": 

        print(f"Congratulations! {name}, You have been Hired!" )
    else:
        print(f"Sorry, {name}, You haven't been selected at this time but keep trying ^-^.") 

if __name__ == "__main__":

    main()

    #


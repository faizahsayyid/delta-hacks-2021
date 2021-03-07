from typing import Optional

def test_matching():
    mentors = [
        Mentor("u1" "1", "A",'none1@gmail.com', 'first', "Physical Science", "Coding", []),
        Mentor("u2" "2", "B", 'none2@gmail.com', 'first' , "Mathematics", "Coding", []),
        Mentor("u3", "3" "C", 'none3@gmail.com', 'second' , "Computer Science", "3D Modelling", [])]

    mentees = [
        Mentee('user1', 'Jo', 'Smith','user1@gmail.com', '9', "Mathematics", "Coding"),
        Mentee('user2', 'Do', 'Smith','user2@@gmail.com', '10', "Physics" , "3D Modelling"),
        Mentee('user3', 'Po', 'Smith', 'user3@gmail.com','11',  "Computer Science", "Disections")]


    pairs = MatchingManager(mentors, mentees)

    assert pairs.matchedPairs(mentors[0], mentees[0]) == 0


class MatchingManager:
    mentors: list[Mentor]
    mentees: list[Mentee] 

    def __init__(self, mentors, mentees):
        #list of mentors and mentees
        self.mentors = mentors
        self.mentees = mentees 

        #empty lists that will hold matched and unmatched mentors and mentees
        self.matchedMentors = set()
        self.matchedMentees = set()
        self.unmatchedMentors = set()
        self.unmatchedMentees = set()
        self.unavailableMentors = set()

        #list of matched mentors and mentees and unmatched mentors
        for mentor in mentors:
            #checks to see if mentor still has space
            if 0 <= len(mentor.mentees) < 2 :
                for mentee in mentor.mentees:
                    #case where both their fields and skills match
                    if matchedPair(mentor, mentee) == 1:
                        self.matchedMentors.append(mentor)
                        self.matchedMentees.append(mentee)
                    #case where only their fields match
                    elif matchedPair(mentor,mentee) == 0.75:
                        self.matchedMentors.append(mentor)
                        self.matchedMentees.append(mentee)
                    #case where neither match up
                    else:
                        self.unmatchedMentors.append(mentor)
            #case where the mentor is at max capacity
            elif  len(mentor.mentees) == 2:
                self.unavailableMentors.append(mentor)                          
        
        #the list of unmatched mentees
        for mentee in self.mentees:
            if mentee not in self.matchedMentees:
                self.unmatchedMentees.add(mentee)
    #people in unmatched categories will go into a waiting list


    def matchedPairs(mentor, mentee):
        #the experices of mentor match mentees
        #will be exchanged with weights later on
        
        if mentor.field_of_study == mentee.field_of_interest:
            for mentor_skills in mentor.skills:
                if mentor_skills == mentee.skills_of_interest: 
                    return 1
                else:
                    pass
            return 0.75
        else:
            return 0     


class Mentor:
    """
    Precondition: 
        - 1 <= len(mentee) <= 2
    """
    mentor_name: str
    mentor_grade: str
    mentor_email: str
    schooling: str 
    field_of_study: str
    skills: list[str]
    experiences : list[str]
    mentee: list[Mentee]
    
    def __init__(self,netId,firstName,lastName,email, year,field_of_study,experiences, skills, mentees):
        self.Id = netId
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.year = year
        self.field_of_study = field_of_study
        self.experiences = list[experiences]
        self.skills = skills
        self.mentees = list[Mentee]


class Mentee:
    mentee_name: str
    mentee_grade: str
    mentee_email: str
    field_of_interest: str
    skills_of_interest: str
    mentor = Optional[Mentor]
    
    def __init__(self, netId, firstName,lastName,email, year,field_of_interest, skills_of_interest, mentor):
        self.Id = netId
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.year = year
        self.field_of_interest = field_of_interest
        self.skills_of_interest = skills_of_interest
        self.mentor = Optional[Mentor]


        '''
        if mentor previous_experiences match with mentee interest
            then match them
            return True
        elif mentor field_of_study match with mentee interests
            match them
            return True
        else:
            don't match them
            return False
        '''


        '''
        weights:
         if more than 3 skills and fields match: 100%
            match that mentor and mentee together
        elif mote than 2 skills and fields match: 75%
            they are a good match unless there are better combinations
        elif (only  1 skill match) or (only fields match): 50%
            match them together if there arent any other better combinations
        else no match: 0%
            neither match then try to find a better mentor
            unless all are matches are the same
        '''

if __name__ == '__main__': 
    import pytest
    pytest.main(['mentor_mentee_classes.py', '-v'])  

from typing import Optional

class MatchingManager:
    mentors: list[Mentor]
    mentees: list[Mentee]

    def __init__(self, mentors, mentees):
        self.mentors = mentors
        self.mentees = mentees 

        self.matchedMentors = set()
        self.matchedMentees = set()
        self.unmatchedMentors = set()
        self.unmatchedMentees = set()
        #self,Id,firstName,lastName,email, year,field_of_study,experiences, skills,  

        #list of matched mentors and mentees and unmatched mentors
        for mentor in mentors:
            if 0 <= len(mentor.mentees) < 2 :
                    if matchedPair(mentor, mentee) == True
                        self.matchedMentors.add(mentor)
                        for mentee in mentor.mentees:
                            self.matchedMentees.add(mentee)
                else
                    self.unmatchedMentors.add(mentor)
            elif  len(mentor.mentees) = 2:
                
        # the list of unmatched mentees
        for mentee in self.mentees:
            if mentee not in self.matchedMentees:
                self.unmatchedMentees.add(mentee)
    

    def matchedPairs(mentor, mentee):
        #the experices of mentor match mentees
        #will be exchanged with weights later on

        for interest in mentee.field_of_interests
            if mentor.field_of_study == interests:
                return True
            for skills in mentee.skills_of_interest:

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
class Mentor:
    """
    Precondition: 
        - 1 <= len(mentee) <= 2
    """
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

        # mentor_name: str
        # mentor_grade: str
        # mentor_email: str
        # schooling: str 
        # field_of_study: str
        # skills: list[str]
        # experiences : list[str]
        # mentee: list[Mentee]

class Mentee:
    def __init__(self, netId, firstName,lastName,email, year,field_of_interests, skills_of_interest, mentor):
        self.Id = netId
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.year = year
        self.field_of_interests = list[field_of_interests]
        self.skills_of_interest = list[skills_of_interest]
        self.mentor = Optional[Mentor]

        # mentee_name: str
        # mentee_grade: str
        # mentee_email: str
        # schooling: str
        # field_of_study: str
        # skills: list[str]
        # experiences: list[str]
        # mentor = Optional[Mentor]






        '''
        weights:
         if more than 2 skills and fields match: 100%
            match that mentor and mentee together
        elif (only skills match) or (only fields match): 50%
            match them together if there arent any other better combinations
        else neither match then try to find a better mentor 

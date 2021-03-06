from typing import Optional

class MatchingManager:
    mentors: list[Mentor]
    mentees: list[Mentee]

    def __init__(self, mentors, mentees):
        self.mentors = []
        self.mentees = []
        


class Mentor:
    """
    Precondition: 
        - 1 <= len(mentee) <= 2
    """
    def __init__(self, name, year,experiences,field_of_study, skills,  ):
        
        mentor_name: str
        mentor_grade: str
        mentor_email: str
        schooling: str 
        field_of_study: str
        skills: list[str]
        experiences : list[str]
        mentee: list[Mentee]

class Mentee:
    def primary_mentee_info():
        mentee_name: str
        mentee_grade: str
        mentee_email: str
        schooling: str
        field_of_study: str
        skills: list[str]
        experiences: list[str]
        mentor = Optional[Mentor]
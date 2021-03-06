class MatchingManager:
    mentors: list[Mentor]
    mentees: list[Mentee]

    def __init__(self):
        mentors = []
        mentees = []
        


class Mentor:
    """

    Precondition: 
        - 1 <= len(mentee) <= 2
    """
    schooling: str
    field_of_stufy: str
    skills: list[str]
    mentee: list[Mentee]

class Mentee:
    schooling: str
    field_of_stufy: str
    skills: list[str]
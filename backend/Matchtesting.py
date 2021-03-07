import os
import sys
import unittest
from backend.mentor_mentee_classes import Mentor
from backend.mentor_mentee_classes import Mentee
from backend.mentor_mentee_classes import MatchingManager

class MatchingTest(unittest.TestCase):

    def __init__(self, methodName='runTest'):
        super(MatchingTest, self).__init__(methodName)
        #self,netId,firstName,lastName,email, year,field_of_study,experiences, skills, mentees
        # Construct basic mentor & mentee structures
        self.mentors = [
            Mentor("u1" "1", "A",'none1@gmail.com', 'first', "Physical Science", "Coding", self.metees),
            Mentor("u2" "2", "B", 'none2@gmail.com', 'first' , "Mathematics", "Coding", self.mentees),
            Mentor("u3", "3" "C", 'none3@gmail.com', 'second' , "Computer Science", "3D Modelling", self.mentees),
        ]
        #self, netId, firstName, lastName, year, email, gpa, mentors
        #self, netId, firstName,lastName,email, year,field_of_interest, skills_of_interest, mentor
        self.mentees = [
            Mentee('user1', 'Jo', 'Smith','user1@gmail.com', '9', "Mathematics", "Coding", self.mentor),
            Mentee('user2', 'Do', 'Smith','user2@@gmail.com', '10', "Physics" , "3D Modelling", self.mentor),
            Mentee('user3', 'Po', 'Smith', 'user3@gmail.com','11',  "Computer Science", "Disections", self.mentor),
        ]


    def testMatchedMentorsAndMentees(self):

        # Construct a matching with no unmatched mentors or mentees
        #self.mentors[].mentees = [self.mentees[0]]
        #self.mentors[].mentees = [self.mentees[2]]
        #self.mentors[].mentees = [self.mentees[1]]

        matching = MatchingManager(self.mentees, self.mentors)
        expectedMatchedMentees = self.mentees
        expectedUnmatchedMentees = []
        expectedMatchedMentors = self.mentors
        expectedUnmatchedMentors = []

        self.assertItemsEqual(expectedMatchedMentees, matching.getMatchedMentees())
        self.assertItemsEqual(expectedMatchedMentors, matching.getMatchedMentors())
        self.assertItemsEqual(expectedUnmatchedMentees, matching.getUnmatchedMentees())
        self.assertItemsEqual(expectedUnmatchedMentors, matching.getUnmatchedMentors())


    def testUnmatchedMenteesAndMentors(self):

        # Construct a matching with no unmatched mentors or mentees
        self.mentors[0].mentees = [self.mentees[0]]
        self.mentors[1].mentees = []
        self.mentors[2].mentees = [self.mentees[1]]

        matching = Matching(self.mentees, self.mentors)
        expectedMatchedMentees = [self.mentees[0],self.mentees[1]]
        expectedUnmatchedMentees = [self.mentees[2]]
        expectedMatchedMentors = [self.mentors[0], self.mentors[2]]
        expectedUnmatchedMentors = [self.mentors[1]]

        self.assertItemsEqual(expectedMatchedMentees, matching.getMatchedMentees())
        self.assertItemsEqual(expectedMatchedMentors, matching.getMatchedMentors())
        self.assertItemsEqual(expectedUnmatchedMentees, matching.getUnmatchedMentees())
        self.assertItemsEqual(expectedUnmatchedMentors, matching.getUnmatchedMentors())

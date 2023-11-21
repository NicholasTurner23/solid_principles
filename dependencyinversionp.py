"""
High-level modules should not depend on low-level modules. Both should depend on abstractions.
Abstractions should not depend on details. Details should depend on abstractions.

"""

from enum import Enum
from abc import abstractmethod

class Clubs(Enum):
    SWIM_CLUB = 1
    CYCLE_CLUB = 2
    RUN_CLUB = 3

class Student():
    def __init__(self, name) -> None:
        self.name = name


class ClubMembershipsLookup():
    @abstractmethod
    def find_all_students_from_club(self, club):
        pass


class ClubMemberships(ClubMembershipsLookup):
    def __init__(self):
        self.club_memberships:list = []

    def add_club_membership(self, student, club):
        self.club_memberships.append((student, club))

    def find_all_students_from_club(self, club):
        for members in self.club_memberships:
            if members[1] == club:
                yield members[0].name

class InspectMemberships():
    def __init__(self, club_membership_lookup):
        for student in club_membership_lookup.find_all_students_from_club(Clubs.SWIM_CLUB):
            print(f"{student} is in the SWIM club.")

        for student in club_membership_lookup.find_all_students_from_club(Clubs.RUN_CLUB):
            print(f"{student} is in the RUN club.")

        for student in club_membership_lookup.find_all_students_from_club(Clubs.CYCLE_CLUB):
            print(f"{student} is in the CYCLE club.")


student_one = Student("Johnny")
student_two = Student("Bobby")
student_three = Student("Amy")

club_memberships = ClubMemberships()
club_memberships.add_club_membership(student_one, Clubs.SWIM_CLUB)
club_memberships.add_club_membership(student_two, Clubs.RUN_CLUB)
club_memberships.add_club_membership(student_three, Clubs.CYCLE_CLUB)

InspectMemberships(club_memberships)
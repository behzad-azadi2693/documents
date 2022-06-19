from abc import ABCMeta, abstractmethod

class Section(metaclass = ABCMeta):

    @abstractmethod
    def describe(self):
        pass

class PersonalSection(Section):

    def describe(self):
        print("PersonalSection")

class AlbumSection(Section):

    def describe(self):
        print("AlbumSection")

class PatentSection(Section):

    def describe(self):
        print("PatentSection")

class PublicationSection(Section):

    def describe(self):
        print("PublicationSection")


#Creator
class Profile(metaclass = ABCMeta):

    def __init__(self):
        self.sections = []
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        pass

    def getSections(self):
        return self.sections

    def addSections(self, section):
        self.sections.append(section)

class linkedin(Profile):

    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(PatentSection())
        self.addSections(PublicationSection())

class facebook(Profile):

    def createProfile(self):
            self.addSections(PersonalSection())
            self.addSections(AlbumSection())

#Client
if __name__ == '__main__':
    profile_input = input("Che profile ro vasat eejad konam?")
    profile = eval(profile_input.lower())()
    print("profile skhte shode:", type(profile).__name__)
    print("profile daraye section haye roberoo mibashad:", profile.getSections())

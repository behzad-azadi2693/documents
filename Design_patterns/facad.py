#Facade
class EventManager():

    def __init__(self):
        print("EventManager:: Bezar Man Ba Tamame afrad hamahang konam\n")

    def arrange(self):
        self.presenter = Presenter()
        self.presenter.setPresentation()

        self.theaterGroup = TheaterGroup()
        self.theaterGroup.setTheater()

        self.caterer = Caterer()
        self.caterer.setCatering()

        self.lecturer = Lecturer()
        self.lecturer.setLecture()

        self.musicGroup = MusicGroup()
        self.musicGroup.setMusic()

#Subsystems
class Presenter():

    def __init__(self):
        print("Maraseme shoma che roozi ast va chand saat va che noe marasemi ast?")

    def setPresentation(self):
        print("4shanbe, 2saat, Jashne voroodi haye jadid")

class TheaterGroup():

    def __init__(self):
        print("Theater tanz bashe ya jedi?")

    def setTheater(self):
        print("Tanz")

class Caterer():

    def __init__(self):
        print("che paziraee?")

    def setCatering(self):
        print("Keyk, abmiveh, sib")

class Lecturer():

    def __init__(self):
        print("Mozooe sokhanrani?")

    def setLecture(self):
        print("Tafavot haye daneshgah ba dabirestan")

class MusicGroup():

    def __init__(self):
        print("chand track ejra konim va az che sabki?")

    def setMusic(self):
        print("2, Sonati")


#Client
class You():

    def __init__(self):
        print("You:: BARGOZARI JASHN NYAZ BE KARHAYE ZYADI DARAD")

    def askEventManager(self):
        print("You:: Tamame karha ro misparam be anjoman")
        em = EventManager()
        em.arrange()

    def __del__(self):
        print("You:: Tashakor az bachehaye anjoman ke tamame kar ha ro anjam dadand")    


you = You()
you.askEventManager()

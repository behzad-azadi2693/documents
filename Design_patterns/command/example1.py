class Installer():

    def __init__(self, source, installation_folder):
        self.choices = []
        self.source = source
        self.installation_folder = installation_folder

    def preferences(self, command):
        self.choices.append(command)

    def execute(self):
        for choice in self.choices:
            if list(choice.values())[0]:
                print("Copying", self.source, "to", self.installation_folder)
            else:
                print("amalyati anjam nashod")

if __name__ == '__main__':
    installer = Installer('python', 'D:')
    installer.preferences({'pyhton': True})
    installer.preferences({'C++': False})
    installer.execute()

class SuperHero():
    def __init__(self,name,superpower):
        self.name=name
        self.superpower=superpower

    def get_superpower(self):
        print(f"I am {self.name} add my power is {self.superpower}")

ironman=SuperHero(
    name="Iron man",
    superpower="suit"
)
ironman.get_superpower()





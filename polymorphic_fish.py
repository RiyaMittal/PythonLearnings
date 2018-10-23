class Shark:
    def swim(self):
        print("The Shark is swimming")

    def swim_backwards(self):
        print("The shark can not swim backwards but can sink backwards")

    def skeleton(self):
        print("The shark's skeleton is made up of cartilage")


class clownfish:
    def swim(self):
        print("The clownfish is swimming")

    def swim_backwards(self):
        print("The clownfish can swim backwards ")

    def skeleton(self):
        print("The clownfish's skeleton is made up of bone")


def in_the_pacific(fish):
    fish.swim()

sammy=Shark()
#sammy.skeleton()
casey=clownfish()
#casey.skeleton()

in_the_pacific(sammy)
in_the_pacific(casey)


# for fish in (sammy,casey):
#     fish.swim()
#     fish.swim_backwards()
#     fish.skeleton()
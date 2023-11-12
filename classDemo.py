# self 代表 java 中的 this

class BuildRobot:
    def __init__(self, armcount, headcount):
        self.armcount = armcount
        self.headcount = headcount

    def paintarm(self, color):
        print(self.__dict__.__class__)
        print("paint arm:", color)



colorful_robot = BuildRobot(2, 1)

colorful_robot.paintarm("red")

test = BuildRobot.paintarm("red")

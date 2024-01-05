class Chair():

    name = '椅子'

    # 建構式
    def __init__(self, c: str):
        self.color = c

    def __eq__(self, other) -> bool:
        print(self == other)
        print(self.color == other.color)

    def seat(self):
        print(f'我的 {self.color} {self.name}很好坐')

class Sofa(Chair):

    name = '沙發'

a_sofa = Sofa('Brown')
a_sofa.seat()
# start modify here

class Car():
    """You may not add any method (def) under this class"""

# end of modify

class Bike():
    wheel = 2
    def get_wheel(self):
        return self.wheel


if __name__ == '__main__':
    bike = Bike()
    assert bike.get_wheel() == 2
    print('PASSED 1')

    car = Car()
    assert car.get_wheel() == 4
    print('PASSED 2')
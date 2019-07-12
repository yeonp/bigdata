# 클래스상속실습과제.py

class Car:

    def __init__(self):
        print('Car 생성자')
        self.car_name = '소나타'
        self.car_drv = '전륜'
        self.car_speed = 0
        self.car_direction = '앞쪽'
        self.car_fuel = '휘발유'
        self.car_state = '정상'

    def set_car_name(self, name):
        self.car_name = name
        print("차종이 [",self.car_name,"]으로 변경 되었습니다")

    def get_car_name(self):
        return self.car_name

    def set_car_drv(self, drv):
        self.car_drv = drv
        print("차의 구동 방식이 [", self.car_drv ,"]으로 변경 되었습니다")

    def get_car_drv(self):
        return self.car_drv

    def set_car_fuel(self, fuel):
        self.car_fuel = fuel
        print("차의 연료 방식이 [", self.car_fuel,"]로 변경 되었습니다")

    def get_car_fuel(self):
        return self.car_fuel

    def set_car_state(self,state):
        self.car_state = state
        print("차의 상태가 [",self.car_state, "]으로 변경 되었습니다")

    def get_car_state(self):
        return self.car_state

    def set_speed(self,speed):
        self.car_speed = speed
        print("자동차의 속력이 시속 [",self.car_speed,"]km 로 변경되었습니다")

    def get_speed(self):
        return self.car_speed

    def turn(self,direction):
        self.car_direction = direction
        print("자동차의 방향이 [",self.car_direction ,"]으로 변경되었습니다")

    def stop(self):
        self.car_direction = '정지'
        print("자동차가 정지 하였습니다")

    def start(self):
        print("자동차가 시동이 걸렸습니다")

    def move_forward(self):
        self.car_direction = '앞쪽'
        print("자동차가 전진합니다 속도는 ",self.car_speed,"km입니다")

    def move_backward(self):
        self.car_direction = '뒤쪽'
        print("자동차가 후진합니다 속도는 ",self.car_speed,"km입니다")

    def __del__(self):
        print('[', self.car_name, "] 자동차가 제거되었습니다")


class Airplane(Car):

    def __init__(self):
        print('Airplane 생성자')

        # < 추가 인스턴스 멤버 >
        self.air_name = 'KAL147'
        self.air_height =  0
        self.air_speed = 0
        self.air_direction = '정지'
        self.air_state = '정상'

        self.car = Car()

    # < 추가 메서드 >
    def set_air_name(self, name):
        self.air_name = name
        print('비행기 기종이 [', self.air_name, ']로 변경 되었습니다')

    def get_air_name(self):
        return self.air_name

    def set_height(self,height):
        self.air_height = height
        print('비행 고도를 [',self.air_height,'] km 로 설정하였습니다')

    def get_height(self):
        return self.air_height

    def land_to_ground(self):
        self.air_direction = '정지'
        print('비행기가 착륙하였습니다')

    # < 메서드 오버라이딩구현 >
    def set_speed(self,speed):
        self.air_speed = speed
        print('비행기의 속력이 시속 [',self.air_speed,'] km 로 변경되었습니다')

    def get_speed(self):
        return self.air_speed

    def move_forward(self):
        self.air_direction = '앞쪽'
        print('비행기가 전진합니다 속도는 [',self.air_speed,
        ']km입니다')

    def move_backward(self):
        self.air_direction = '뒤쪽'
        print('비행기가 후진합니다 속도는 [',self.air_speed,
        '] km 입니다')

    def __del__(self):
        print('[', self.air_name, "] 비행기가 제거되었습니다")


if __name__ == '__main__':
    kal = Airplane()

    kal.set_air_name('아시아나104')
    print(kal.get_air_name())

    kal.set_height(1000)
    print(kal.get_height())

    kal.land_to_ground()

    kal.set_speed(100)
    print(kal.get_speed())

    kal.move_forward()
    kal.move_backward()

    print(kal.car.car_name)



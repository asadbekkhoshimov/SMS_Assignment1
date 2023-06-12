class Car:
    def __init__(self, from_location, to_location):
        self.from_location = from_location
        self.to_location = to_location
        self.speed = 0
        self.weather = None

    def set_weather(self, weather):
        self.weather = weather
        if weather == 'sunny':
            self.speed = 80
        elif weather == 'rainy':
            self.speed = 60
        elif weather == 'snowy':
            self.speed = 50
        elif weather == 'windy':
            self.speed = 70

    def decrease_speed(self, decrease_amount):
        if self.speed - decrease_amount < 0:
            print('Speed cannot be less than zero.')
        else:
            self.speed -= decrease_amount

    def print_status(self):
        print(f'You are travelling from {self.from_location} to {self.to_location}.')
        print(f'Speed: {self.speed} km/h.')
        print(f'Weather condition: {self.weather}.')


from car import Car

def main():
    my_car = Car('New York', 'Los Angeles')
    
    while True:
        print('1. Set Weather')
        print('2. Decrease Speed')
        print('3. Print Status')
        print('4. Exit')
        choice = input('Enter your choice: ')

        if choice == '1':
            weather = input('Enter weather (sunny, rainy, snowy, windy): ')
            my_car.set_weather(weather)
        elif choice == '2':
            decrease_amount = int(input('Enter amount to decrease speed by: '))
            my_car.decrease_speed(decrease_amount)
        elif choice == '3':
            my_car.print_status()
        elif choice == '4':
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 4.\n')

if __name__ == "__main__":
    main()


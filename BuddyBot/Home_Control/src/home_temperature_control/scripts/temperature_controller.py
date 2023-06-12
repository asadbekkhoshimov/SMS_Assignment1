def control_temperature(self):
    if self.current_temp is None:
        return

    if self.mode == 'manual':
        print("Choose a system:")
        print("1. Air Conditioner")
        print("2. Heating System")
        system_choice = int(input("Your choice (1-2): "))

        if system_choice == 1:
            print("Air Conditioner:")
            print("1. On")
            print("2. Off")
            ac_choice = int(input("Your choice (1-2): "))
            if ac_choice == 1:
                self.temperature_change = -0.8
            elif ac_choice == 2:
                self.temperature_change = 0
                print(f"Current room temperature: {self.current_temp} degree Celsius")

        elif system_choice == 2:
            print("Heating System:")
            print("1. On")
            print("2. Off")
            heating_choice = int(input("Your choice (1-2): "))
            if heating_choice == 1:
                self.temperature_change = 0.8
            elif heating_choice == 2:
                self.temperature_change = 0
                print(f"Current room temperature: {self.current_temp} degree Celsius")

    elif self.mode == 'automatic':
        # rest of the code...

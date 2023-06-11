else:
            print(f"\nCity Name: {resp.city_name}")
            print(f"Temperature: {resp.temperature}°C")
            print(f"Humidity: {resp.humidity}%")
            print(f"Description: {resp.description}\n")

            # Define severe conditions
            severe_conditions = ["Extreme", "Thunderstorm", "Heavy Rain"]

            # Check if current weather matches any severe condition
            if resp.description in severe_conditions:
                print(f"Alert: Severe weather condition detected in {resp.city_name}!\n")

        # Sleep for 5 seconds
        time.sleep(5)

def main():
    while True:
        print("\n1. Current Weather")
        print("2. Travel Distance")
        print("3. Alerts/Notifications")
        print("4. Transportation Method")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            city = input("Enter a city name: ")
            resp = weather_client(city)

            if resp.city_name == "Invalid city":
                print("Invalid city")
            else:
                print(f"\nCity Name: {resp.city_name}")
                print(f"Temperature: {resp.temperature}°C")
                print(f"Humidity: {resp.humidity}%")
                print(f"Description: {resp.description}\n")

        elif choice == "2":
            city = input("Where do you want to travel? ")
            resp = weather_client(city)

            if resp.city_name == "Invalid city":
                print("Invalid city")
            else:
                print(f"\nCity Name: {resp.city_name}")
                print(f"Temperature: {resp.temperature}°C")
                print(f"Humidity: {resp.humidity}%")
                print(f"Description: {resp.description}\n")
                print("Recommended Clothes: " + suggest_clothes(resp.temperature))

        elif choice == "3":
            city = input("Enter a city name for alerts: ")
            weather_alerts(city)

        elif choice == "4":
            destination = input("Where would you like to travel to? ")
            directions, distance, time = get_directions(destination)

            if directions is not None and distance is not None and time is not None:
                print(f"\nDistance: {distance} miles")
                print(f"Estimated Travel Time: {time}")
                print("Directions:")
                for direction in directions:
                    print(direction)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.\n")

if name == "__main__":
    main()

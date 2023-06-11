#!/usr/bin/env python3
import rospy
from weather_info.srv import Weather

def weather_client(city_name):
    rospy.wait_for_service('weather_info')
    try:
        weather_info = rospy.ServiceProxy('weather_info', Weather)
        resp = weather_info(city_name)
        return resp
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)

def suggest_clothes(temperature):
    if temperature < 0:
        return "Coat, Hat, Gloves, Warm Pants, Boots"
    elif temperature < 10:
        return "Jacket, Long Sleeve Shirt, Pants, Shoes"
    elif temperature < 20:
        return "Sweater, Jeans, Shoes"
    elif temperature < 30:
        return "T-Shirt, Shorts, Sandals"
    else:
        return "Tank Top, Shorts, Sandals"

# Continuing the code

def main():
    while True:
        print("\n1. Current Weather")
        print("2. Travel Distance")
        print("3. Exit")
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
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 3.\n")

if __name__ == "__main__":
    main()


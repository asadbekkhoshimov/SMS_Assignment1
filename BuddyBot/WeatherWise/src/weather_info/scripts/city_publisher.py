#!/usr/bin/env python3
import rospy
from weather_info.srv import Weather
import time

def weather_client(city_name, service_name='weather_info'):
    rospy.wait_for_service(service_name)
    try:
        weather_info = rospy.ServiceProxy(service_name, Weather)
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

def check_severe_weather(resp):
    if resp.description == "thunderstorm":
        return "Alert: Thunderstorm in the area!"
    elif resp.description == "heavy snow":
        return "Alert: Heavy snowfall in the area!"
    elif resp.temperature < -10:
        return "Alert: Extremely cold temperature!"
    elif resp.temperature > 40:
        return "Alert: Extremely hot temperature!"
    else:
        return "Weather is normal"

def weather_alerts(city):
    while True:
        resp = weather_client(city)

        if resp.city_name == "Invalid city":
            print("Invalid city")
            return

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
        print("4. Exit")
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
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.\n")

if __name__ == "__main__":
    main()

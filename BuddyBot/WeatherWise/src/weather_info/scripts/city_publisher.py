#!/usr/bin/env python3
import rospy
from weather_info.srv import Weather
import time
import json
import requests

def get_directions(destination):
    base_url = "https://www.mapquestapi.com/directions/v2/route?"
    api_key = "JAEpAr2sJYI7LMUM2pSxuXQjEFB1w5cl"
    start_location = "Incheon"

    destination = destination.replace(" ", "+")

    modes = ["fastest", "shortest", "bicycle", "pedestrian"]
    mode_names = ["By Car (Fastest)", "By Car (Shortest Distance)", "By Bicycle", "On Foot"]
    distances = []
    times = []

    directions = None
    for i, mode in enumerate(modes):
        final_url = f"{base_url}key={api_key}&from={start_location}&to={destination}&routeType={mode}"
        try:
            response = requests.get(final_url)
            data = response.json()

            if response.status_code != 200:
                print("Error: Unable to fetch directions. Please try again.")
                return None, None, None

            if "route" not in data or "legs" not in data["route"] or len(data["route"]["legs"]) == 0:
                print("Error: No route found to the specified destination.")
                return None, None, None

            distance = data["route"]["distance"] * 1.60934  # Convert miles to kilometers
            time = data["route"]["time"]

            distances.append(distance)
            times.append(time)

            print(f"{mode_names[i]}: Distance = {distance:.2f} km, Time = {time//3600} hours {(time%3600)//60} minutes")

        except requests.exceptions.RequestException as e:
            print(f"Error: An error occurred while fetching directions. {e}")
            return None, None, None

    best_distance = min(distances)

    if best_distance < 1:
        best_mode = "On Foot"
    elif best_distance < 5:
        best_mode = "By Bicycle"
    elif best_distance < 50:
        best_mode = "By Car"
    elif best_distance < 200:
        best_mode = "By Train or Car"
    else:
        best_mode = "By Plane"

    best_time = times[distances.index(best_distance)]
    best_time_hours = best_time // 3600
    best_time_minutes = (best_time % 3600) // 60

    print(f"\nThe best mode of transportation to {destination} is {best_mode}.")
    print(f"Estimated travel time: {best_time_hours} hours {best_time_minutes} minutes.")
    return directions, best_distance, best_time


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
if __name__ == "__main__":
    main()

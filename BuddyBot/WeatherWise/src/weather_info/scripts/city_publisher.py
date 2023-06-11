import requests

def get_directions(destination):
    base_url = "https://www.mapquestapi.com/directions/v2/route?"
    api_key = "JAEpAr2sJYI7LMUM2pSxuXQjEFB1w5cl"
    start_location = "Incheon"

    # Replace spaces in the destination with '+' for URL encoding
    destination = destination.replace(" ", "+")

    modes = ["fastest", "shortest", "bicycle", "pedestrian"]
    mode_names = ["By Car (Fastest)", "By Car (Shortest Distance)", "By Bicycle", "On Foot"]
    distances = []
    times = []

    for i, mode in enumerate(modes):
        final_url = f"{base_url}key={api_key}&from={start_location}&to={destination}&routeType={mode}"

        try:
            response = requests.get(final_url)
            data = response.json()

            # Check if the request was successful
            if response.status_code != 200:
                print("Error: Unable to fetch directions. Please try again.")
                return None, None, None

            # Check if a route was found
            if "route" not in data or "legs" not in data["route"] or len(data["route"]["legs"]) == 0:
                print("Error: No route found to the specified destination.")
                return None, None, None

            # Get the distance and time from the response
            distance = data["route"]["distance"] * 1.60934  # Convert miles to kilometers
            time = data["route"]["time"]

            distances.append(distance)
            times.append(time)

            # Print out the time and distance for each mode
            print(f"{mode_names[i]}: Distance = {distance:.2f} km, Time = {time//3600} hours {(time%3600)//60} minutes")

        except requests.exceptions.RequestException as e:
            print(f"Error: An error occurred while fetching directions. {e}")
            return None, None, None

    # Determine the best mode of transportation based on distance
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

    # Determine the time for the best mode of transportation
    best_time = times[distances.index(best_distance)]
    best_time_hours = best_time // 3600
    best_time_minutes = (best_time % 3600) // 60

    # Print out the best mode of transportation and time
    print(f"\nThe best mode of transportation to {destination} is {best_mode}.")
    print(f"Estimated travel time: {best_time_hours} hours {best_time_minutes} minutes.")

    return mode_names, best_distance, f"{best_time_hours} hours {best_time_minutes} minutes"

def main():
    while True:
        print("\n1. Current Weather")
        print("2. Travel Distance")
        print("3. Alerts/Notifications")
        print("4. Transportation Method")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Existing code for current weather
            pass
        elif choice == "2":
            # Existing code for travel distance
            pass
        elif choice == "3":
            # Existing code for alerts/notifications
            pass
        elif choice == "4":
            destination = input("Where would you like to travel to? ")
            directions, distance, time = get_directions(destination)

            if directions is not None and distance is not None and time is not None:
                print(f"\nDistance: {distance:.2f} km")
                print(f"Estimated Travel Time: {time}")
                print("Directions:")
                for direction in directions:
                    print(direction)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.\n")

if __name__ == "__main__":
    main()

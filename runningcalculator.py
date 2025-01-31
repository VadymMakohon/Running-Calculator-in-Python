import math

def calculate_pace(time_minutes, distance_miles):
    """Calculate pace in minutes per mile."""
    if distance_miles <= 0:
        raise ValueError("Distance must be greater than zero.")
    return time_minutes / distance_miles

def calculate_time(pace_minutes_per_mile, distance_miles):
    """Calculate time in minutes."""
    if pace_minutes_per_mile <= 0 or distance_miles <= 0:
        raise ValueError("Pace and distance must be greater than zero.")
    return pace_minutes_per_mile * distance_miles

def calculate_distance(time_minutes, pace_minutes_per_mile):
    """Calculate distance in miles."""
    if time_minutes <= 0 or pace_minutes_per_mile <= 0:
        raise ValueError("Time and pace must be greater than zero.")
    return time_minutes / pace_minutes_per_mile

def estimate_vdot(time_minutes, distance_miles):
    """Estimate VDOT based on race performance."""
    # Constants for VDOT estimation (these are empirical and may vary)
    if distance_miles <= 0 or time_minutes <= 0:
        raise ValueError("Time and distance must be greater than zero.")
    vdot = (distance_miles / time_minutes) * 100
    return vdot

def training_paces(vdot):
    """Calculate training paces based on VDOT."""
    if vdot <= 0:
        raise ValueError("VDOT must be greater than zero.")
   
    easy_pace = 1.2 * vdot
    marathon_pace = 1.1 * vdot
    threshold_pace = vdot
    interval_pace = 0.9 * vdot
    repetition_pace = 0.8 * vdot
    return {
        "Easy Pace": easy_pace,
        "Marathon Pace": marathon_pace,
        "Threshold Pace": threshold_pace,
        "Interval Pace": interval_pace,
        "Repetition Pace": repetition_pace
    }

def menu():
    while True:
        print("\nRunning Calculator")
        print("1. Calculate Pace")
        print("2. Calculate Time")
        print("3. Calculate Distance")
        print("4. Estimate VDOT and Training Paces")
        print("5. Exit")
        choice = input("Select an option: ")

        try:
            if choice == '1':
                time = float(input("Enter total time in minutes: "))
                distance = float(input("Enter distance in miles: "))
                pace = calculate_pace(time, distance)
                print(f"Pace: {pace:.2f} minutes per mile")
            elif choice == '2':
                pace = float(input("Enter pace in minutes per mile: "))
                distance = float(input("Enter distance in miles: "))
                time = calculate_time(pace, distance)
                print(f"Time: {time:.2f} minutes")
            elif choice == '3':
                time = float(input("Enter total time in minutes: "))
                pace = float(input("Enter pace in minutes per mile: "))
                distance = calculate_distance(time, pace)
                print(f"Distance: {distance:.2f} miles")
            elif choice == '4':
                time = float(input("Enter recent race time in minutes: "))
                distance = float(input("Enter race distance in miles: "))
                vdot = estimate_vdot(time, distance)
                paces = training_paces(vdot)
                print(f"Estimated VDOT: {vdot:.2f}")
                print("Training Paces:")
                for pace_type, pace_value in paces.items():
                    print(f"{pace_type}: {pace_value:.2f} minutes per mile")
            elif choice == '5':
                print("Exiting the calculator. Happy running!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError as e:
            print(f"Input error: {e}. Please enter valid numbers.")

if __name__ == '__main__':
    menu()

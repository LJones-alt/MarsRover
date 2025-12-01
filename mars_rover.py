import time

class MarsRover:
    def __init__(self, name:str):
        """
        Initializes the rover with a name, starting coordinates (0,0),
        a full battery (100), and an empty list for samples.
        """
        self.name : str = name
        self.x=0
        self.y=0
        self.battery=100
        self.samples=[]

        print(f"System: {self.name} initialized. Ready for mission.")

    def move(self, direction: str):
        """
        Moves the rover in a specific direction (w, a, s, d)
        and consumes battery power.
        """
        # TODO: Check if battery is greater than 0.2 If not, print "Critical Battery" and return.
        
        # TODO: Update self.x or self.y based on the direction:
        # 'w' -> y increases by 1 (North)
        # 's' -> y decreases by 1 (South)
        # 'd' -> x increases by 1 (East)
        # 'a' -> x decreases by 1 (West)

        if "w" in direction:
            # then we are going north, lets increase y by 1

            print(f"Moving NORTH, my new position is {self.x}")


        # TODO: Decrease self.battery by 5
        
        # TODO: Print the movement action (e.g. "Moved North")
        pass

    def collect_sample(self, sample_type:str):
        """
        Adds a geological sample to the rover's storage.
        """
        # TODO: Append the sample_type to the self.samples list
        # TODO: Print a confirmation message
        pass

    def report_status(self):
        """
        Prints the current coordinates, battery level, and collected samples.
        """
        print(f"Current Co-ord: {self.x}, {self.y}")
        print(f"Battery level: {self.battery}")
        print(f"Collected samples : {self.samples}")
        pass

# --- MAIN MISSION CONTROL LOOP ---

# 1. Create the Rover
rover_name = input("Enter Rover Name: ")
rover = MarsRover(rover_name)

mission_active = True

while mission_active:
    print("\n--- AWAITING COMMAND ---")
    print("Controls: 'w', 'a', 's', 'd' to move | 'scan' to report | 'dig' to sample | 'exit' to quit")
    
    command = input("Enter command: ").lower()

    if command == 'exit':
        print("Mission Terminated.")
        mission_active = False
        
    elif command == 'scan':
        # TODO: Call the report_status method
        pass

    elif command == 'dig':
        sample = input("What kind of sample? (rock/dust/ice): ")
        # TODO: Call the collect_sample method
        pass

    elif command in ['w', 'a', 's', 'd']:
        # TODO: Call the move method and pass the command as the direction
        pass

    else:
        print("Invalid Command. Signal lost.")

    # Optional: Add a small delay for realism
    time.sleep(0.5)
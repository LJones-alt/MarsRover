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
        # Check if battery is greater than 0. If not, print "Critical Battery" and return.
        if self.battery <= 0:
            print("Critical Battery! Cannot move.")
            return
        
        # Update self.x or self.y based on the direction:
        if direction == 'w':
            self.y += 1
            print(f"Moved NORTH. New position: ({self.x}, {self.y})")
        elif direction == 's':
            self.y -= 1
            print(f"Moved SOUTH. New position: ({self.x}, {self.y})")
        elif direction == 'd':
            self.x += 1
            print(f"Moved EAST. New position: ({self.x}, {self.y})")
        elif direction == 'a':
            self.x -= 1
            print(f"Moved WEST. New position: ({self.x}, {self.y})")
        
        # Decrease battery by 5
        self.battery -= 5
        print(f"Battery: {self.battery}%")

    def collect_sample(self, sample_type:str):
        """
        Adds a geological sample to the rover's storage.
        """
        self.samples.append(sample_type)
        print(f"Collected sample : {sample_type}")
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
        rover.report_status()
        pass

    elif command == 'dig':
        sample = input("What kind of sample? (rock/dust/ice): ")
        rover.collect_sample(sample)
        pass

    elif command in ['w', 'a', 's', 'd']:
        # Call the move method and pass the command as the direction
        rover.move(command)

    else:
        print("Invalid Command. Signal lost.")

    # Optional: Add a small delay for realism
    time.sleep(0.5)
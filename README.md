🚀 Operation: Red Planet - Mars Rover "Rover-X"
===============================================

🪐 Mission Brief
----------------

**Welcome, Chief Software Engineer.**

The Mars Exploration Program has successfully landed the **Rover-X** in the Jezero Crater. However, the rover's autonomous operating system was corrupted during the descent.

**Your mission:** Restore the core functionality of the rover using Python. You must implement the navigation, power management, and scientific sampling systems to ensure the rover survives the harsh Martian environment.

🛠️ Prerequisites
-----------------

*   **Python 3.x** installed on your machine.
    
*   **Git** installed (for cloning the repository).
    
*   A code editor (VS Code, PyCharm, or IDLE).
    

📥 Getting Started
------------------

### 1\. Clone the Repository

Open your terminal or command prompt and run the following command to download the mission files to your local machine:

```git clone [https://github.com/your-username/mars-rover-mission.git](https://github.com/your-username/mars-rover-mission.git)```   

_(Note: Replace your-username with the actual username where this repo is hosted)_

### 2\. Navigate to the Mission Folder

```   cd MarsRover   ```

### 3\. Launch the Interface

To test the current (broken) system, run:

```python mars_rover.py ```

📝 Your Tasks
-------------

Open mars\_rover\_skeleton.py in your code editor. Look for the comments marked # TODO. You need to implement the following systems:

### Phase 1: Initialization (\_\_init\_\_)

*   \[ \] Set the starting coordinates x and y to 0.
    
*   \[ \] Set the battery level to 100.
    
*   \[ \] Initialize an empty list for samples.
    

### Phase 2: Navigation (move)

*   \[ \] **Power Check:** Ensure the rover has battery (> 0) before moving.
    
*   \[ \] **Coordinate Updates:**
    
    *   'w' (North): Increase Y
        
    *   's' (South): Decrease Y
        
    *   'd' (East): Increase X
        
    *   'a' (West): Decrease X
        
*   \[ \] **Power Consumption:** Every move costs **5% battery**.
    

### Phase 3: Science (collect\_sample)

*   \[ \] Add the sample type (e.g., "Rock", "Dust") to the samples list.
    
*   \[ \] Print a confirmation message.
    

### Phase 4: Telemetry (report\_status)

*   \[ \] Print the current position (x, y).
    
*   \[ \] Print the remaining battery charge.
    
*   \[ \] Print the inventory of collected samples.
    

### Phase 5: Mission Control Loop

*   \[ \] Connect your functions to the main while loop at the bottom of the file so user commands trigger the correct actions.
    

🎮 Command Reference
--------------------

Once your code is running, you can control the rover using the following inputs in the terminal:

**CommandAction**

w, a, s, d

Move North, West, South, or East

scan

Display status report (Position, Battery, Samples)

dig

Collect a geological sample

exit

Terminate mission and close program

⚠️ Hazards & Tips
-----------------

*   **Battery Management:** If your battery hits 0, the rover should stop moving.
    
*   **Map Logic:** Remember that (0,0) is your landing site.
    
    *   Moving North (w) makes Y positive.
        
    *   Moving South (s) makes Y negative.
        
*   **Testing:** Test frequently! Run the code after implementing each function to make sure it works.
    

**Good luck, Engineer. The Red Planet awaits.**
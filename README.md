# process-scheduling-simulator


A simulator for operating system scheduling algorithms built with Python and Streamlit.

## Setup
```bash
git clone https://github.com/IamAbhinav01/process-scheduling-simulator.git
cd process-scheduling-simulator
pip install streamlit
streamlit run main.py

## **Screenshots**
Intial PAGE --> ![image](https://github.com/user-attachments/assets/0508efe1-b87e-4262-a417-87c013445220)

Working PAGE ---> 
## **Project Overview**
The Process Scheduling Simulator is designed to simulate operating system scheduling algorithms, including First-Come-First-Serve (FCFS), Shortest Job First (SJF), Shortest Remaining Time First (SRTF), Priority Scheduling, Round Robin, and Exponential Average SRJF. Built with Python and Streamlit, it allows users to generate random jobs with configurable parameters, select a scheduling algorithm, and visualize the process through an interactive UI. The simulator displays the ready queue, running process, logs, changes, and system metrics, making it an educational tool for understanding scheduling concepts.

## **Module-Wise Breakdown**
This project is divided into three key modules, implemented across separate files:

**Module 1**: Job Generation (job_generator.py)
Purpose: Generates random jobs with attributes like arrival time, priority, and CPU/IO bursts.
Functionality: Uses configurable parameters (e.g., number of jobs, arrival range) to create Job objects, which are then passed to the scheduler.
**Module 2****: Scheduler (scheduler.py)
**Purpose****: Manages the scheduling process using various algorithms.
**Functionality****: Implements the Scheduler class with methods for each algorithm (e.g., round_robin, priority), handling the ready queue, running process, and logging.
**Module 3**: Streamlit UI (main.py)
**Purpose:** Provides an interactive interface for configuration, control, and visualization.
Functionality: Built with Streamlit, it includes sliders, buttons, and progress bars to manage job generation, algorithm selection, and simulation execution.
Functionalities
Job Generation:
Configure parameters via Streamlit sliders (e.g., Number of Jobs = 5, Arrival Time Range = 0 to 50).
Generate jobs with a single click of the "Generate Jobs" button.
Scheduling Algorithms:
Supports FCFS, SJF, SRTF, Priority, Round Robin, and Exponential Average SRJF.
Simulation Control:
Manual stepping with "Next Step" (one time unit) or "Next Change" (to the next event).
Continuous animation with adjustable Animation Speed.
Visualization:
Displays the ready queue and running process with progress bars.
Shows logs (e.g., Process[1] has entered running state) and changes (e.g., Process[1] progress: 2/8) in text areas.
Provides system status (e.g., system time, placeholders for metrics).
Interactivity:
Fully interactive UI built with Streamlit, allowing real-time adjustments.
Technology Used
Programming Languages
Python: The core language for implementing the simulator.
Libraries and Tools
Streamlit: Creates the interactive UI with components like st.slider, st.button, and st.progress.
Random: Generates random values for job attributes.
Time: Controls animation speed with time.sleep.
Other Tools
GitHub: Hosts the public repository for version control and documentation.
Git: Manages commits, branches, and pushes.
VS Code: Used for coding and running the Streamlit app.

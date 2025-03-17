# main for the streamlit app
import streamlit as st
from job_generator import generate_jobs
from scheduler import Scheduler
import time

st.title("Processes Scheduling Simulator")  ##using streamlit as an ui

st.sidebar.header("Job Generation Parameters")
num_jobs = st.sidebar.slider("Number of Jobs", 1, 20, 5)
arrival_range = st.sidebar.slider("Arrival Time Range", 0, 100, (0, 50))
priority_range = st.sidebar.slider("Priority Range", 1, 10, (1, 5))
burst_range = st.sidebar.slider("Burst Range", 1, 50, (1, 20))
num_bursts = st.sidebar.slider("Number of Bursts", 1, 10, 2)
context_switch = st.sidebar.slider("Context Switch Time", 0, 10, 0)
time_quantum = st.sidebar.slider("Time Quantum (for RR)", 1, 10, 2)
tau = st.sidebar.slider("Tau (for Exponential SRJF)", 1, 10, 5)
alpha = st.sidebar.slider("Alpha (for Exponential SRJF)", 0.0, 1.0, 0.5)

if st.sidebar.button("Generate Jobs"):
    jobs = generate_jobs(num_jobs, arrival_range, priority_range, burst_range, num_bursts)
    st.session_state.jobs = jobs
    st.session_state.running = False

if "jobs" in st.session_state:
    algorithm = st.selectbox("Select Scheduling Algorithm", ["FCFS", "SJF", "SRTF", "Priority", "Round Robin", "Exponential Average SRJF"])
    if st.button("Start Simulation"):
        st.session_state.scheduler = Scheduler(algorithm, st.session_state.jobs, context_switch, time_quantum, tau, alpha)
        st.session_state.running = True

if "scheduler" in st.session_state and st.session_state.running:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button("Next Step"):
            st.session_state.scheduler.step()
    with col2:
        speed = st.slider("Animation Speed", 0.1, 2.0, 1.0)
    with col3:
        if st.button("Next Change"):
            while st.session_state.scheduler.changes:
                st.session_state.scheduler.step()
                if not st.session_state.scheduler.changes:
                    break

    if st.checkbox("Enable Animation"):
        while st.session_state.running and st.session_state.scheduler.ready_queue: ##Animations for the simulation
            st.session_state.scheduler.step()
            time.sleep(1 / speed)
            st.rerun()  # Updated to st.rerun()

    st.subheader("Ready Queue")
    ready_queue = [job for job in st.session_state.scheduler.ready_queue]
    for job in ready_queue:
        total = st.session_state.scheduler.jobs[job.pid].bursts[job.current_burst_idx]
        st.write(f"Process {job.pid}")
        st.progress(job.progress / total if total > 0 else 0)

    st.subheader("Running Process")
    if st.session_state.scheduler.running:
        running_job = st.session_state.scheduler.running
        st.write(f"Process ID: {running_job.pid}")
        current_burst = running_job.bursts[running_job.current_burst_idx]
        total_bursts = sum(running_job.bursts)
        st.progress(running_job.progress / current_burst if current_burst > 0 else 0)
        st.progress(running_job.total_progress / total_bursts if total_bursts > 0 else 0)

    st.subheader("Log")
    st.text_area("Log", "\n".join(st.session_state.scheduler.log), height=200)

    st.subheader("Changes")
    st.text_area("Changes", "\n".join(st.session_state.scheduler.changes), height=200)

    st.subheader("System Status")
    metrics = st.session_state.scheduler.get_metrics()
    st.write(f"CPU Utilization: {metrics['CPU Utilization']}")
    st.write(f"Throughput: {metrics['Throughput']}")
    st.write(f"Turnaround Time: {metrics['Turnaround Time']}")
    st.write(f"Waiting Time: {metrics['Waiting Time']}")
    st.write(f"System Time: {st.session_state.scheduler.system_time}")

    if st.button("Stop Simulation"):
        st.session_state.running = False

if "running" not in st.session_state:
    st.session_state.running = False
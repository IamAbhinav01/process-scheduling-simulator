import random

class Job:
    def __init__(self, pid, arrival_time, priority, bursts):
        self.pid = pid
        self.arrival_time = arrival_time
        self.priority = priority
        self.bursts = bursts
        self.current_burst_idx = 0
        self.progress = 0
        self.total_progress = sum(bursts)
        self.state = "new"  # Added a new attribute to track job state

    def __str__(self):
        return f"Process[{self.pid}]"  # Added string representation for logging

def generate_jobs(num_jobs, arrival_range, priority_range, burst_range, num_bursts):
    jobs = []
    for i in range(num_jobs):
        arrival = random.randint(arrival_range[0], arrival_range[1])
        priority = random.randint(priority_range[0], priority_range[1])
        bursts = [random.randint(burst_range[0], burst_range[1]) for _ in range(num_bursts * 2 - 1)]
        jobs.append(Job(i, arrival, priority, bursts))
    jobs.sort(key=lambda x: x.arrival_time)  # Added sorting by arrival time
    return jobs
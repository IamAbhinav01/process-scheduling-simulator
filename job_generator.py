# job_generator.py
import random

class Job:
    def __init__(self, pid, arrival_time, priority, bursts):
        self.pid = pid
        self.arrival_time = arrival_time
        self.priority = priority
        self.bursts = bursts
        self.current_burst_idx = 0
        self.progress = 0
        self.total_progress = 0

    def __str__(self):
        return f"Process[{self.pid}]"

def generate_jobs(num_jobs, arrival_range, priority_range, burst_range, num_bursts):
    jobs = []
    for pid in range(num_jobs):
        arrival_time = random.randint(arrival_range[0], arrival_range[1])
        priority = random.randint(priority_range[0], priority_range[1])
        bursts = []
        for _ in range(num_bursts):
            bursts.append(random.randint(burst_range[0], burst_range[1]))
            if _ < num_bursts - 1:
                bursts.append(random.randint(burst_range[0], burst_range[1]))
        jobs.append(Job(pid, arrival_time, priority, bursts))
    return jobs
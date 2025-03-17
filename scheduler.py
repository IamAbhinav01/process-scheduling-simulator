# scheduler for CPU scheduling algorithms
class Scheduler:
    def __init__(self, algorithm, jobs, context_switch=0, time_quantum=2, tau=5, alpha=0.5):
        self.algorithm = algorithm
        self.jobs = sorted(jobs, key=lambda x: x.arrival_time)
        self.context_switch = context_switch
        self.time_quantum = time_quantum
        self.tau = tau
        self.alpha = alpha
        self.ready_queue = []
        self.running = None
        self.system_time = 0
        self.cpu_utilization = 0
        self.throughput = 0
        self.turnaround_time = 0
        self.waiting_time = 0
        self.log = []
        self.changes = []

    def update_queues(self):
        while self.jobs and self.jobs[0].arrival_time <= self.system_time:
            self.ready_queue.append(self.jobs.pop(0))
            self.log.append(f"{self.ready_queue[-1]} has entered ready queue")

    def fcfs(self):
        if not self.running and self.ready_queue:
            self.running = self.ready_queue.pop(0)
            self.log.append(f"{self.running} has entered running state")

    def sjf(self):
        if not self.running and self.ready_queue:
            self.ready_queue.sort(key=lambda job: job.bursts[job.current_burst_idx])
            self.running = self.ready_queue.pop(0)
            self.log.append(f"{self.running} has entered running state")

    def srtf(self):
        if self.ready_queue:
            self.ready_queue.sort(key=lambda job: job.bursts[job.current_burst_idx])
            if not self.running or (self.running and self.ready_queue and
                                    self.running.bursts[self.running.current_burst_idx] >
                                    self.ready_queue[0].bursts[self.ready_queue[0].current_burst_idx]):
                if self.running:
                    self.ready_queue.append(self.running)
                self.running = self.ready_queue.pop(0)
                self.log.append(f"{self.running} has entered running state (preempted)")

    def priority(self):
        if not self.running and self.ready_queue:
            self.ready_queue.sort(key=lambda job: job.priority)
            self.running = self.ready_queue.pop(0)
            self.log.append(f"{self.running} has entered running state")

    def round_robin(self):
        if not self.running and self.ready_queue:
            self.running = self.ready_queue.pop(0)
            self.log.append(f"{self.running} has entered running state")
        elif self.running and self.system_time % self.time_quantum == 0 and self.ready_queue: ##round robin using Time Quantum
            self.ready_queue.append(self.running)
            self.running = self.ready_queue.pop(0)
            self.log.append(f"{self.running} has entered running state (RR switch)")

    def exponential_average_srtf(self):
        if not self.running and self.ready_queue:
            if not hasattr(self, 'predicted_bursts'):
                self.predicted_bursts = {job.pid: self.tau for job in self.jobs + self.ready_queue}
            self.ready_queue.sort(key=lambda job: self.predicted_bursts[job.pid])
            self.running = self.ready_queue.pop(0)
            self.log.append(f"{self.running} has entered running state")
        if self.running:
            self.predicted_bursts[self.running.pid] = self.alpha * self.running.bursts[self.running.current_burst_idx] + \
                                                    (1 - self.alpha) * self.predicted_bursts[self.running.pid]

    def step(self):
        self.update_queues()
        if self.running:
            burst = self.running.bursts[self.running.current_burst_idx]
            if burst > 0:
                self.running.bursts[self.running.current_burst_idx] -= 1
                self.running.progress += 1
                self.running.total_progress += 1
                self.changes.append(f"{self.running} progress: {self.running.progress}/{burst}")
                if self.running.bursts[self.running.current_burst_idx] == 0:
                    if self.running.current_burst_idx < len(self.running.bursts) - 1:
                        self.running.current_burst_idx += 1
                        self.running.progress = 0
                        self.log.append(f"{self.running} completed burst, moving to next")
                        self.running = None
                    else:
                        self.log.append(f"{self.running} completed all bursts")
                        self.running = None
            else:
                self.running = None
        else:
            if self.algorithm == "FCFS":
                self.fcfs()
            elif self.algorithm == "SJF":
                self.sjf()
            elif self.algorithm == "SRTF":
                self.srtf()
            elif self.algorithm == "Priority":
                self.priority()
            elif self.algorithm == "Round Robin":
                self.round_robin()
            elif self.algorithm == "Exponential Average SRJF":
                self.exponential_average_srtf()
        self.system_time += 1

    def get_metrics(self):
        return {
            "CPU Utilization": self.cpu_utilization,
            "Throughput": self.throughput,
            "Turnaround Time": self.turnaround_time,
            "Waiting Time": self.waiting_time
        }
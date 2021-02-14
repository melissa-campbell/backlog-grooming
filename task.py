class Task:
    def __init__(self, fix_or_enhancement, description, priority, estimate, status):
        self.fix_or_enhancement = fix_or_enhancement
        self.description = description
        self.priority = priority # critical, high, medium, low
        self.estimate = estimate # 4, 8, 40, 80, 200 hours
        self.status = status # todo, in_process, complete
        self.assigned = False
        self.percent_complete = 0.0
        self.rank = 99


    def update_priority(self, priority):
        self.priority = priority

    def update_estimate(self, estimate):
        self.estimate = estimate
    
    def update_status(self, status):
        self.status = status

    def update_perent_complete(self, percent_complete):
        if percent_complete >= 0 and percent_complete <=100:
            self.percent_complete = percent_complete
        else:
            return('Please enter a number between 0 and 100')

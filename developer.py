class Developer:
    def __init__(self, name, skill, rate=60, availability=120):
        self.name = name # mike, matt, sally, kim
        self.skill = skill
        self.rate = rate
        self.availability = availability # hours per person per release
        self.allocation = 0
        
    def assign_developer(self, estimate):
        # if proposed hours < (work week - prior allocation)
        if estimate <= (self.availability - self.allocation):
            self.allocation += estimate
            print('{} successfully allocated to this assignment.'.format(self.name))
            return True
        else:
            print('{} would be overallocated with this assignment.'
                  'Please assign to another developer'.format(self.name))
            return False
            
                 
        


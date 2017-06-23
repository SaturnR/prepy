#!/usr/bin/env python3


class Budget:

    def __init__(self, name, version):
        self.version = version
        self.name = name
        self.jobs = []
        self.__momo__ = {}
        
    def addjob(self, job):
        self.jobs.append(job)

    def sum(self):
        return sum([n.quantity * n.unit_cost for n in self.jobs])
            
    def __str__(self):
        return '120202$'


class Job:

    def __init__(self, name, buget_number, measure_unit, quantity, unit_cost):
        self.name = name
        self.buget_number = buget_number
        self.measure_unit = measure_unit
        self.quantity = quantity
        self.unit_cost = unit_cost

        self.sum = None
        #----------- II ----------
        self.begin_time = None
        self.end_time = None
        #-------------------------

    def start(self):
        if end_time == None:
            self.begin_time = datetime.datetime.now()
        else:
            raise JobTimeException
        
    def end(self):
        if self.begin_time == None:
            self.end_time = datetime.datetime.now()
        else:
            raise JobTimeException
        
    def __str__(self):
        return 'job, job, job'


class JobTimeException(Exception):

    def __str__(self):
        return 'Job time error'

    
class MeasureUnits:

    LITER = 0
    KG = 1
    MEN_HOUR = 3
    NONE = 4
    
    
class JobCategories:

    THINGS = 0
    WORK = 1
    SERVICE = 3
    
    
if __name__ == "__main__":
    test_budget = Budget('TMS', '4.0')
    nodes = Job(name='nodes', buget_number=2, measure_unit=None, quantity=150, unit_cost=33)
    
    test_budget.addjob(nodes)

    print(test_budget.sum())
    

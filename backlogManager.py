from developer import Developer
from task import Task
from assignment import Assignment

developer_list = [ Developer('Billy', 'Java'), Developer('Chris', '.NET')]


def developer_add(name, skill):
    name = Developer(name, skill)
    developer_list.append(name)


developer_add('Tina', 'COBOL')
developer_add('Sam', 'Java')
developer_add('Sheila', '.NET')
developer_add('Matt', 'COBOL')
developer_add('Mike', 'Java')
developer_add('Sally', '.NET')

backlog = []


def task_add(fix_or_enhancement, description, priority, estimate, status):
    backlog_item = Task(fix_or_enhancement, description, priority, estimate, status)
    backlog.append(backlog_item)


task_add('Bug Fix', 'Fix what Tom messed up', 'Medium', 50, 'TODO')
task_add('Bug Fix', 'Everything is on fire', 'Critical', 50, 'TODO')
task_add('Bug Fix', 'System is Down', 'Critical', 40, 'TODO')
task_add('Enhancement','Need new screen', 'High', 100, 'TODO' )


assignment_xref = []

for item in backlog:
    print(f'Backlog item: {item.description}')
    for dev in developer_list:
        print(dev.name)
        if dev.assign_developer(item.estimate):
            Assignment(item, dev)
            item.assigned = True
            break 



for dev in developer_list:
    print(f'Name: {dev.name}, Allocation: {dev.allocation}')

for item in backlog:
    print(f'Decription: {item.description}, Priority: {item.priority}, Assigned: {item.assigned}')

for xref in assignment_xref:
    print(f'Task: {xref.task.description}, Assigned to: {xref.developer.name}')

print(backlog[0].percent_complete)
backlog[0].update_perent_complete(40)
print(backlog[0].percent_complete)


# estimate in $

# dependencies?
# split into smaller chunks?

# view backlog - .csv
# delete task from list
# mark task as duplicate

# update assigned developer
# update percent complete
# remove developer from list
from developer import Developer
from task import Task
from assignment import Assignment
import csv


def developer_add_to_list(name, skill, list):
    name = Developer(name, skill)
    list.append(name)

def developer_add_to_csv(developer_list):
    with open('developer.csv', 'w', newline="") as csvfile:
        fieldnames  = ['name', 'skill', 'rate', 'availability', 'allocation']
        devwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        devwriter.writeheader()
        for item in developer_list:
            devwriter.writerow({"name": item.name, "skill": item.skill, "rate": item.rate, "availability": item.availability, "allocation": item.allocation})


def developer_select_from_csv(skill):        
    with open('developer.csv') as csvfile:
        devreader = csv.DictReader(csvfile)
        # list to store subset of csv, matching skill criteria
        developer_list_by_skill = []
        for row in devreader:
            # if skillset matches skill parameter, add to list
            if row['skill'] == skill:
                print(row['name'], row['skill'])
                developer_add_to_list(row['name'], row['skill'], developer_list_by_skill)
        return developer_list_by_skill


def backlog_add_task(fix_or_enhancement, description, priority, estimate, status):
    backlog_item = Task(fix_or_enhancement, description, priority, estimate, status)
    backlog.append(backlog_item)


developer_list = [ Developer('Billy', 'Java'), Developer('Chris', '.NET')]

developer_add_to_list('Tina', 'COBOL', developer_list)
developer_add_to_list('Sam', 'Java', developer_list)
developer_add_to_list('Sheila', '.NET', developer_list)
developer_add_to_list('Matt', 'COBOL', developer_list)
developer_add_to_list('Mike', 'Java', developer_list)
developer_add_to_list('Sally', '.NET', developer_list)

backlog = []

backlog_add_task('Bug Fix', 'Fix what Tom messed up', 'Medium', 50, 'TODO')
backlog_add_task('Bug Fix', 'Everything is on fire', 'Critical', 50, 'TODO')
backlog_add_task('Bug Fix', 'System is Down', 'Critical', 40, 'TODO')
backlog_add_task('Enhancement','Need new screen', 'High', 100, 'TODO' )
backlog_add_task('Bug Fix', 'Report is incorrect', 'Medium', 50, 'TODO')
backlog_add_task('Bug Fix', 'We are all going to die', 'Critical', 50, 'TODO')
backlog_add_task('Bug Fix', 'System is Down Again', 'Critical', 40, 'TODO')
backlog_add_task('Enhancement','Screen is taking too long', 'High', 100, 'TODO' )
backlog_add_task('Enhancement','Need new report', 'High', 100, 'TODO' )
backlog_add_task('Enhancement','Need updated calculations', 'High', 100, 'TODO' )

assignment_xref = []

for item in backlog:
    print(f'Backlog item: {item.description}')
    for dev in developer_list:
        print(dev.name)
        if dev.assign_developer(item.estimate):
            assignment_xref.append(Assignment(item, dev))
            item.assigned = True
            break 


developer_add_to_csv(developer_list)
developer_list_by_skill = developer_select_from_csv('Java')

for dev_skill in developer_list_by_skill:
    print(f'Name: {dev_skill.name}, Skill: {dev_skill.skill}')

for dev in developer_list:
    print(f'Name: {dev.name}, Allocation: {dev.allocation}')

for item in backlog:
    print(f'Decription: {item.description}, Priority: {item.priority}, Assigned: {item.assigned}')

for xref in assignment_xref:
    print(f'Task: {xref.task.description}, Assigned to: {xref.developer.name}')

print(backlog[0].percent_complete)
backlog[0].update_perent_complete(40)
print(backlog[0].percent_complete)


# FUTURE features
# estimate in $
# dependencies?
# split into smaller chunks?

# view backlog - .csv
# delete task from list
# mark task as duplicate

# update assigned developer
# update percent complete
# remove developer from list
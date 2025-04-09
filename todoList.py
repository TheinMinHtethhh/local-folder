import os
FILE_NAME = 'todolist.txt'
def ensure():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME,'w')as file:
          pass
def load():
    with open(FILE_NAME,'r')as file:
        tasks =[line.strip() for line in file]
    return tasks
def save(tasks):
    with open(FILE_NAME,'w')as file:
        for task in tasks:
            file.write(task+'\n')
def display(tasks):
    for idx,task in enumerate(tasks,start=1):
        print(f'{idx}:{task}')
def add(tasks):
    new_task=input('put the new task to do :')
    tasks.append(new_task)
    save(tasks)
    print('new task added successfully!')
    display(tasks)
def mark(tasks):
    if not tasks:
        print('there is no tasks to mark')
        add(tasks)

    display(tasks)
    task_num = int(input('enter the tasks number to mark'))
    if task_num<1 or task_num>len(tasks):
        print('enter the valid number')
    tasks[task_num-1]=tasks[task_num-1]+'---marked'
    save(tasks)
def main():
    ensure()
    tasks = load()
    while True:
        print('This app can perform 5 functions')
        print('1.Display the tasks')
        print('2.Add the new tasks')
        print('3.mark the tasks that you did')
        print('5.delete the tasks')
        print('5.exict the proogramme')
        try:
            option = int(input('enter number 1~5 to do the function:'))
            if option == 1:
                display(tasks)
            if option is 2:
                add(tasks)
            if option == 3:
                mark(tasks)
            if option == 4:
                pass
            if option == 5:
                break
        except ValueError:
            print('\nenter the valid number!\n')
            return
            
            
main()
        


    
    
# from src.task import Task


task1 = "wash_dishes"
task2 = "clean_window"
task3 = "cook_dinner"
task4 = "do_ironing"
task5 = "wash_clothes"

# def create_dict_tasks(task1, task2, task3):
dict_tasks = {task1 : [task2, task5],
              task2 : [task3, task4],
              task3 : [task1, task4],
              task4 : [task5, task1],
              task5 : [task3, task2]
              }
# dict_tasks = create_dict_tasks(task1, task2, task3)

def task_decider(task1, task2):
    if task1 in dict_tasks[task2]:
            return task2
    else:
            return task1
                

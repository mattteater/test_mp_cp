import json
import os.path

def main():
    try:
        # Constant Variables used for display(action=,) arguement.
        LIST_WITHOUT_NUM = 'LIST_WITHOUT_NUM'
        MENU = 'MENU'
        # Create list of task objects from json file.
        task_list = populate_task_list()
        # Display menu options to user.
        display(MENU, task_list)
        # Get selection.
        menu_selection = int(input('Type a Number to Select-->'))    
        # While program has not be exited
        while menu_selection in {1, 2, 3}:
            match menu_selection:
                case 1:
                    display(LIST_WITHOUT_NUM, task_list)
                case 2:
                    task_list = add_task(task_list)
                case 3:
                    remove_task(task_list)
            display(MENU, task_list)
            menu_selection = int(input('\nType a Number to Select-->'))
        # Save to json.
        save_task_list(task_list)   
    except ValueError:
        return print('Error...')
    except TypeError:
        return print('Type Error Occured')  
    finally:
        print('Exiting Program.')
    
def populate_task_list():
    file_name = './Tasks.json'
    if os.path.exists(file_name):
        with open(file_name) as tasks_json_file:
            try:
                doc = json.load(tasks_json_file)
            except json.JSONDecodeError:
                # Handle the case where the file is empty or not valid JSON
                doc = []
    return doc if isinstance(doc, list) else [{}]

def display(action, task_list):
    if action == 'MENU':
        print('\n1. See Current List.\n2: Add\n3: Remove\n4: Press any other key to exit.\n')
    elif action == 'LIST_WITHOUT_NUM':
        print("\n*** TODO LIST ***\n")
        for item in task_list:
            if item["completed"] == True:
                print(f'{item["name"]} [x]')
            else:
                print(f'{item["name"]} [ ]')
        input("\nPress enter to return to the menu.")
    else:
        i = 1
        for item in task_list:
            print(f'{i}. {item["name"]}')
            i += 1

def add_task(task_list):
    to_add = input('\nEnter Description:-->')
    if to_add != None:
        new_task = {"name": to_add, "completed": False}
        task_json = json.dumps(new_task)  # Convert the dictionary to a JSON string
        task_list.append(json.loads(task_json))  # Append the JSON string as a dictionary
        save_task_list(task_list)  # Save the updated task list
        return task_list

def save_task_list(task_list):
    file_name = './Tasks.json'
    with open(file_name, 'w') as tasks_json_file:
        json.dump(task_list, tasks_json_file)

def remove_task(task_list):
    display('WITH_NUMBERS', task_list)
    index_number = int(input('Select the item to remove: '))
    task_list.pop(index_number - 1)  # Remove the task from the list

'''TODO Implement: 
    mark_done()
'''

'''NOTE Pos. Features: 
    edit_task()
    view_in_web()
    task_duration()
'''


main()
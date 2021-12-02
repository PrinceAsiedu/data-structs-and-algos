todo_items = []

def todo():
    while True:
        user_ip = input('Enter a task for your todo list. Press <enter> when done: ')
        if user_ip == '': break
        else:todo_items.append(str(user_ip)); print('Task added to todo list.')
    if len(todo_items) > 0:
        print('\nYour To-Do List')
        print('---------------')
        for todo_item in todo_items:
            print(todo_item)
        

def run(func):
    func()

if __name__ == '__main__':
    todo = todo()
    run(todo)

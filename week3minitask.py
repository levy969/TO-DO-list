def main():
    tasks={}
    print("welcome to TO-DO list \n \n1. add a task\n2. show all tasks\n3. delete a task\n4. mark a task as done\n5. exit the program")
    while True:
        try:
            s=int(input("enter a valid number according to your needs\n"))
        except ValueError:
            continue
        match s:
            case 1:
                tskname=input('enter a task').strip()
                tskname=tskname.lower()
                if tskname =='':
                    print('please enter a text')
                    continue
                if tskname in tasks:
                    print('this task is already present in to do list')
                    continue

        
                status=input('is it done? (y/n): ').lower().startswith('y')
                tasks[tskname]=status
                
            case 2:
                print('TO DO task list\n',tasks)
                
            case 3:
                tskname=input('enter valid and existing name to remove a task').strip()
                tskname=tskname.lower()
                if not tskname in tasks:
                    print('this task does not exist in to do list')
                    continue
                tasks.pop(tskname)
            case 4:
                tskname=input('enter a taskname to change status ').strip()
                tskname=tskname.lower()
                if not tskname in tasks:
                    print('this task does not exist in to do list first list this task')
                    continue

                status=input('is it done? (y/n): ').lower().startswith('y')
                tasks[tskname]=status
            case 5:
                print('existing...')
                break
                




if __name__=="__main__":
    main()

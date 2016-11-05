import os

class ToDoList:

    #initializing variable and list which will be used in all functions
    def __init__(self):
        self.to_do_list = []
        self.task = ''

    #printing list in easy to read form
    def list_print(self):
        os.system('clear')
        for i, item in enumerate(self.to_do_list):
            print(i+1,'.',item[0], '', item[1])

    #adding input item to the list
    def add(self):
        self.task = input("Add an item: ")
        self.to_do_list.append(['[ ]', self.task])

    #listing item is not needed anymore, I decide to always show the list
    # def listing(self):
    #     if self.to_do_list == []:
    #         print("List is empty, please add task")
    #     else:
    #         print("Saved items")
    #         self.list_print()

    #marking and unmarking item in list
    def marking(self):
        os.system('clear')

        if self.to_do_list == []:
            print("List is empty, please add task")
        else:
            self.list_print()
            mark_item = None

            #checking if user type number of item
            while mark_item is None:
                try:
                    mark_item = int(input("Which one you want to mark as completed (or unmark): "))
                except ValueError:
                    print("Please input number")

            #shown number is higher by 1 than real item id
            mark_item -= 1

            #when user type numer higher than number of items script will rerun
            #user can mark task if is done and unmark if it comes up that task is not done
            if mark_item < len(self.to_do_list):
                mark_item = self.to_do_list[mark_item]
                if mark_item[0] == '[ ]':
                    mark_item[0] = '[X]'
                else:
                    mark_item[0] = '[ ]'
                self.list_print()
            else:
                self.marking()

    #archiving marked items, function will run again if are marked items after first clear
    #because of changing id's of items
    def archive(self):
        for i, task in enumerate(self.to_do_list):
            if task[0] == '[X]':
                self.to_do_list.remove(task)
                self.archive()

    def main(self):
        os.system('clear')

        while True:
            self.list_print()
            choice = input("Please specify a command [list, add, mark, archive]: ")
            if choice == 'add':
                self.add()
            # elif choice == 'list':
            #     self.listing()
            elif choice == 'mark':
                self.marking()
            elif choice == 'unmark':
                self.unmarking()
            elif choice == 'archive':
                self.archive()
            elif choice == 'x':
                exit()



todolist = ToDoList()
todolist.main()

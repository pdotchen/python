def roster(command):
    names = []
    grades = []
    for x in command:
        if x == 'exit':
            break
        if 'update' in x:
            update_list = x.split()
            updated_string = ("Updated", update_list[1] + "'s", "grade")
            no_update = (update_list[1], "does not exist in the roster")
            if update_list[1] in names:
                grades[names.index(update_list[1])] = update_list[2]
                return_update = updated_string
            else:
                return_update = no_update
            print(" ".join(return_update))
        if 'add' in x:
            add_list = x.split()
            if int(add_list[2]) > 100 or int(add_list[2]) < 0:
                failed_add = "Failed to add", add_list[1]
                print(" ".join(failed_add))
                break
            if not add_list[1] in names:
                names.append(add_list[1])
                grades.append(add_list[2])
                return_add = "Added", add_list[1]
                print(" ".join(return_add))
            else:
                print("Failed to add", add_list[1])
        if x == 'print':
            for n in names:
                print(names[names.index(n)] + ':', grades[names.index(n)])


i = []

word = ''
while word != "exit":
    word = input()
    i.append(word)

roster(i)

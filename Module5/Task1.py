try:
    with open('my_text.txt', 'r') as file:
        file_content = file.readlines()
        for index,line in enumerate(file_content):
            print('Line '+ str(index+1) + ":",line)
except FileNotFoundError:
    print('Error: The file \'my_text.txt\' was not found.')
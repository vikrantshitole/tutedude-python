text = input("Enter text to write to the file: ")
with open('output.txt', 'w') as file:
    file.write(text + '\n')
    print('Data successfully written to output.txt')

text = input("Enter additional text to append: ")
with open('output.txt', 'a') as file:
    file.write(text + '\n')
    print('Data successfully appended.')

with open('output.txt', 'r') as file:
    print('Final contents of output.txt:')
    print(file.read())

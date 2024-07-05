# Open a file named hello.txt in write mode
with open('hello.txt', 'w') as file:
    # Write "Hello, World!" to the file
    file.write("Hello, World!")

print("File 'hello.txt' created and written successfully.")

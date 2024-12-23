# File Read & Write Challenge
# Error Handling Lab

def main():
    try:
        # Ask the user for the filename
        input_file = input("Enter the name of the file to read: ")
        
        # Try to open and read the file
        with open(input_file, 'r') as file:
            content = file.read()
        
        # Modify the content (e.g., make all text uppercase)
        modified_content = content.upper()
        
        # Define the output file name
        output_file = "modified_" + input_file
        
        # Write the modified content to a new file
        with open(output_file, 'w') as file:
            file.write(modified_content)
        
        print(f"File has been read and modified content written to {output_file}")
    
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You do not have permission to read or write to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

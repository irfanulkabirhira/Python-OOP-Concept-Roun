class Student:
    def __init__(self):
        self.color = 'blue'

    def hira(self):
        return "Hello from hira"

def main():
    obj = Student() # Creating an Object
    print(obj.color) # Asccesing the instance varibale
    print(obj.hira()) # Calling the method

# Ensuring the script runs only when executed directly
if __name__ == "__main__":
    main()
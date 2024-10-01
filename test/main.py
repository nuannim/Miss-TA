from ClassB import ClassB
# import ClassB, ClassA

def main():
    print('hello')
    # ClassB.call_method_from_class_a()
    objB = ClassB
    objB.call_method_from_class_a(objB) # if dont input objB, have to @classmethod in ClassB.py


    
if __name__ == "__main__":
    main()

# from ClassB import ClassB

# class MainApp:
#     @staticmethod
#     def run():
#         print('hello')
#         ClassB.call_method_from_class_a()

# if __name__ == "__main__":
#     MainApp.run()

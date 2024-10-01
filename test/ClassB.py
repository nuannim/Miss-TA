from ClassA import ClassA

class ClassB:
    # @classmethod
    def call_method_from_class_a(self):
        ClassA.method_in_class_a()
        print("Method in ClassB")

'''Домашнее задание


3) Для класса Box напишите статический метод, который будет подсчитывать
суммарный объем двух ящиков, которые будут его параметрами.'''


# 1) Создайте декоратор, который зарегистрирует декорируемый класс в
# списке классов.

class_list = []


def class_register(cls):
    def adder(*args, **kwargs):
        new_instance = cls(*args, **kwargs)
        class_list.append(new_instance)
        return new_instance
    return adder

# 2) Создайте декоратор класса с параметром. Параметром должна быть
# строка, которая должна дописываться (слева) к результату работы метода
# __str__.


def left_str(str_to_add):
    def decorator(func):
        def inner(*args, **kwargs):
            return f"{str_to_add}+{func(*args, **kwargs)}"
        return inner
    return decorator


def left_str_adder(str_to_add):
    def decorator(cls):
        def inner(*args, **kwargs):

            new_instance = cls(*args, **kwargs)
            cls.__str__ = left_str(str_to_add=str_to_add)(cls.__str__)
            # new_instance.__str__ = left_str(str_to_add=str_to_add)(new_instance.__str__)
            return new_instance

        return inner

    return decorator


@left_str_adder(str_to_add="***")
# @class_register
class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "Box [x = "+str(self.x)+", y = "+str(self.y)+", z = "+str(self.z)+" ]"


b = Box(1, 3, 5)
b1 = Box(2, 4, 6)
b2 = Box(2, 4, 6)
print(class_list)
print(b)
print(b)
print(b1)
print(b1)



def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


test_function()  # Вывел в консоль: "Я в области видимости функции test_function"

inner_function()  # Выдал ошибку:
"""
Traceback (most recent call last):
  File "C:/Users/Nick/PycharmProjects/pythonProject_02/module_4_2.py", line 10, in <module>
    inner_function()
NameError: name 'inner_function' is not defined

'Функция не определена - не видит. Так как она является подфункцией для функции "test_function" и 
 из глобального пространства имен не видна.'

"""

def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


test_function()
inner_function()  # При попытке вызвать inner_function() вне test_function() будет ошибка,
# так как inner_function определена только внутри test_function и не существует вне ее области видимости.

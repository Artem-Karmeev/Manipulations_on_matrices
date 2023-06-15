class MyClass:

    def InputDigit(self, text: str) -> int:

        """Запрашивает число у пользователя """

        while True:
            try:
                number =  int(input(text))
                return number
            except:
                print("""
                Программа принимает только числа!\n
                Повторите ввод:
                """)


    def __str__(self) -> str:
        my_str = ''
        data = self.__dict__
        for k, v in data.items():
            my_str += f'\nMatrix "{k[1: ]}":\n{v}\n'
        return my_str



class Helper(MyClass):

    @staticmethod
    def InputDigit(text: str = 'Введите вариант: ', start: int = 1, finish: int = 10):
        while True:
            try:
                number =  int(input(text))
                if start <= number <= finish:
                    return number
                else:
                    print('Введите число от 1 до 10')
            except:
                print("""
                Программа принимает только числа!\n
                Повторите ввод:
                """)
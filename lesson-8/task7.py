# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте
# перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (
# комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного
# результата.


class ComplexNumber:

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        imaginary = str(self.imaginary)
        if abs(self.imaginary) == 1:
            imaginary = imaginary.replace('1', '')
        return f'{self.real} + {imaginary}i'

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.imaginary * other.real + self.real * other.imaginary
        return ComplexNumber(real, imaginary)


a = ComplexNumber(2, 3)
print(a)
b = ComplexNumber(5, 1)
print(a + b)
print(a * b)

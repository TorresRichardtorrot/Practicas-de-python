from index import Calculator

def test_caculator_operations():
    calculator = Calculator()
    
    #?probar la suma
    result = calculator.add(2,3)
    assert result == 5
    #?probar la suma
    result = calculator.substract(5,2)
    assert result == 3
    #?probar la suma
    result = calculator.multiply(2,3)
    assert result == 6
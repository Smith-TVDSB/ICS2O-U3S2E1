import pytest
import student 

def test_default():
    assert student.distance(0, 3, 4) == 5, "Make sure it works for the test cases given"

def test_Pythagorean_Quads():
    assert distance(8, 0, 15) == 17  
    assert distance(21, 20, 0) == 29  
    assert distance(1, 2, 2) == 3  
    assert distance(2, 3, 6) == 7  
    assert distance(4, 4, 7) == 9
       
def test_negative_solutions():
    assert distance(-1, -4, -8) == 9

def test_decimals():
    assert distance(2, -2, 2) == approx(3.4641016)

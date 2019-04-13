from django.http import HttpResponse
from django.test import TestCase

from AppOne.views import function_one
from .views import multiply, wish_user
import unittest
from  django.test.client import RequestFactory
# Create your tests here.

#print(multiply(10,5))


# class TestBasic(unittest.TestCase):
#
#     def test_basic(self):
#         a = 1
#         self.assertEqual(1,a)
#
#     def test_basic_2(self):
#         a = 1
#         assert a == 1


# class TestMoreComplex(unittest.TestCase):
#
#     def setUp(self) -> None:
#         self.a = 1
#
#     def tearDown(self) -> None:
#         del self.a
#
#     def test_basic_1(self):
#         self.assertNotEqual(self.a, 2)
#
#     def test_basic_2(self):
#         assert self.a != 2
#
#     def test_fail(self):
#         assert self.a == 2


class SimpleTest(unittest.TestCase):
    """Test Cases for AppTwo, the method wish_user returns string and not HttpResponse in order to test the output"""

    def setUp(self):
        self.factory = RequestFactory()

    def test_details(self):
        """pass the test"""
        request = self.factory.get('')
        response = wish_user(request, 10)
        #self.assertEqual(response.status_code, 200) #this requires to return a HttpResponse object
        self.assertEqual(response, 'Good Morning') #works to the exact msg, so wish instead of HttpResponse(wish)

    def test_two_details(self):
        """pass the test"""
        request = self.factory.get('')
        response = wish_user(request, 16)
        self.assertEqual(response, 'Good Evening')

    def test_three_details(self):
        """pass the test"""
        request = self.factory.get('')
        response = wish_user(request, 20)
        self.assertNotEqual(response, "Good Morning")

    def test_four_details(self):
        """Supposed to fail"""
        request = self.factory.get('')
        response = wish_user(request, 5)
        self.assertEqual(response, "Good Night")


class ComplexTest(unittest.TestCase):
    
    def setUp(self) -> None:
        self.factory = RequestFactory()
        
    def test_one(self):
        """will pass if a file named 'file' exist otherwise fail"""
        request = self.factory.get('')
        response = function_one(request, 'file')
        self.assertEqual(response.status_code, 200)
        
    def test_two(self):
        """Will pass as no file_two exists"""
        request = self.factory.get('')
        response = function_one(request, 'file_two')
        self.assertNotEqual(response, HttpResponse('no such file found')) # what the function returns, comparing it with response
        
    def test_three(self):
        """Will fail"""
        request = self.factory.delete('')
        response = function_one(request, 'file_two')
        self.assertEqual(response, HttpResponse('file deleted successfully'))
    
    
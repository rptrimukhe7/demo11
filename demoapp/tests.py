from django.test import TestCase
from demoapp.models import Student
# Create your tests here.

class StudentTestCase(TestCase):
    def setUp(self):
        print('Setup Activity')
        Student.objects.create(first_name='abc',last_name='def',roll_number=1)
        Student.objects.create(first_name='pqr',last_name='stu',roll_number=2)
  
    def test_student_info(self):
        print("Testing Student Information")
        obj=Student.objects.all()
        self.assertEqual(obj.count(),2)
        
        # s1=Student.objects.get(first_name='abc')
        # s2=Student.objects.get(first_name='pqr')
        
        # self.assertEqual(s1.roll_number(),'1')
        # self.assertEqual(s2.roll_number(),'2')    

        # self.assertEqual(s1.get_rollno(),1)
        # self.assertEqual(s2.get_rollno(),2)    


        # stu = Student.objects.get(first_name='abc')
        # self.assertEqual(stu.last_name(),'def')
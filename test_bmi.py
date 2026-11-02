import Lab2.bmi as bmi 

def test_bmi_normal_weight():
   bmi_index = bmi.calculate_bmi(1.60,56.5)
   test_index = 0
   assert(bmi_index == test_index)

def test_bmi_over_weight():
   bmi_index = bmi.calculate_bmi(1.80,88.0)
   test_index = 1 
   assert(bmi_index == test_index)

def test_bmi_under_weight():
   bmi_index = bmi.calculate_bmi(1.75,52.0)
   test_index = -1
   assert(bmi_index == test_index)






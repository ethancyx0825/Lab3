import Lab2.bmi as bmi 

def test_bmi_normal_weight(BMI):
   bmi_index = bmi.calculate_bmi(BMI)
   test_index = 0
   assert(bmi_index == test_index)

def test_bmi_over_weight(BMI):
   bmi_index = bmi.calculate_bmi(BMI)
   test_index = 1 
   assert(bmi_index == test_index)

def test_bmi_under_weight(BMI):
   bmi_index = bmi.calculate_bmi(BMI)
   test_index = -1
   assert(bmi_index == test_index)  



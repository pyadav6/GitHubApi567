from datetime import datetime

#Defining the mybrand function which will print the following details
#=*=*=*= Your name =*=*=*=
#=*=*=*= Course 2023S-SSW567-WS =*=*=*= 
#=*=*=*= The name of the homework assignment =*=*=*= 
#=*=*=*= The date and time at which the function was called, obtained from a library function call =*=*=*= 

start_pattern = "=*=*=*= "
end_pattern = " =*=*=*=\n"
my_name = "Priyanshi Yadav"
course_name = "Course 2023F-SSW567-A"
today_date = str(datetime.now().isoformat(' ', 'seconds'))

def my_brand(hw_assign_name):
    brand = start_pattern+my_name+end_pattern+start_pattern+course_name+end_pattern+start_pattern+hw_assign_name+end_pattern+start_pattern+today_date+end_pattern
    print(brand)

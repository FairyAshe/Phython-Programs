Name = input("Enter your name: ")
print("Welcome to CMDI! {}, kindly choose the course that you want".format(Name))

Courses = ["BSA","BSAIS","BSIS","BSE","BSN","BSTM","BSHM"]
course_choice = input("Enter the course you want to enroll in: ")

if course_choice in Courses:
    Result = course_choice
    print("Congratulations! {}, you're now enrolled in {}".format(Name, Result))

else:
    print("Course is not available")
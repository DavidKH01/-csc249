from Course import Course

def main():
    # TODO: Create Course objects representing your current semester courses
    # Example: course1 = Course("Intro to Python", "CS101", 3)


    course1 = Course("Data Structure & Algorithms","CSC-249", 3)
    course2 = Course("Security Concepts","SEC-110", 3)

    # set intructor names and schedule for courses 
    course1.add_instructorName("Andrew Norris")
    course2.add_instructorName("Phillippe, J")
    course1.add_schedule("M/T/W/TH/F -- Online")
    course2.add_schedule("M/T/W/TH/F -- Online")

    # TODO: Store these Course objects in a list or array
    # Example: courses = [course1, course2, ...]

    courses = [course1, course2]

    # TODO: Loop through the list/array and use the displayCourseInfo() method to print details of each course
    # Example: for course in courses: course.displayCourseInfo()

    for course in courses:
        print(course.displayCourseInfo())

if __name__ == "__main__":
    main()

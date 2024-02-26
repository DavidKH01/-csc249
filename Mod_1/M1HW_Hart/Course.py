class Course:
    def __init__(self, courseName, courseCode, credits):
        # TODO: Initialize the course attributes
        self.courseName = courseName
        self.courseCode = courseCode
        self.credits = int (credits)


    # Getters and Setters for courseName, courseCode, and credits
    def get_courseName(self):
        return self.courseName
    
    def add_courseName(self, courseName):
        self.courseName = courseName
    
    def get_courseCode(self):
        return self.courseCode
    
    def add_courseCode(self, courseCode):
        self.courseCode = courseCode
    
    def get_credits(self):
        return self.credits
    
    def add_credits(self, credits):
        self.credits = credits
    
    
    # TODO: Implement getters and setters for each attribute
    def get_instructorName(self):
        return self.instructorName
    
    def add_instructorName(self, instructorName):
        self.instructorName = instructorName
    
    def get_schedule(self):
        return self.schedule
    
    def add_schedule(self, schedule):
        self.schedule = schedule
        

    def displayCourseInfo(self):
        # TODO: Print the course information
        print("Course Name: " , self.courseName)
        print("Course Code: " , self.courseCode)
        print("Credits: "  , self.credits)
        print("Instructor Name: ", self.get_instructorName())
        print("Class schedule: ", self.get_schedule())
        return

# End of Course class

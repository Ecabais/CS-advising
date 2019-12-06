"""
Created on Fri Dec  6 01:02:56 2019

@author: elyvic
"""

import tkinter as tk
import tkinter.messagebox as msbox

window = tk.Tk()                    #create window

#variables for names and stuff
name = tk.StringVar()
idNo = tk.StringVar()
advisorName = tk.StringVar()
date = tk.StringVar()


"""
variables for currently taking courses
"""
#variables for course number
courseNo1 = tk.StringVar()
courseNo2= tk.StringVar()
courseNo3 = tk.StringVar()
courseNo4 = tk.StringVar()
courseNo5 = tk.StringVar()
courseNo6 = tk.StringVar()

#variables for course number
courseName1 = tk.StringVar()
courseName2 = tk.StringVar()
courseName3 = tk.StringVar()
courseName4 = tk.StringVar()
courseName5 = tk.StringVar()
courseName6 = tk.StringVar()

#variables for credit hours
creditHours1 = tk.StringVar()
creditHours2 = tk.StringVar()
creditHours3 = tk.StringVar()
creditHours4 = tk.StringVar()
creditHours5 = tk.StringVar()
creditHours6 = tk.StringVar()

"""
variables for spring 2020 courses
"""
#variables for course number
springCourseNo1 = tk.StringVar()
springCourseNo2= tk.StringVar()
springCourseNo3 = tk.StringVar()
springCourseNo4 = tk.StringVar()
springCourseNo5 = tk.StringVar()
springCourseNo6 = tk.StringVar()

#variables for course number
springCourseName1 = tk.StringVar()
springCourseName2 = tk.StringVar()
springCourseName3 = tk.StringVar()
springCourseName4 = tk.StringVar()
springCourseName5 = tk.StringVar()
springCourseName6 = tk.StringVar()

#variables for credit hours
springCreditHours1 = tk.StringVar()
springCreditHours2 = tk.StringVar()
springCreditHours3 = tk.StringVar()
springCreditHours4 = tk.StringVar()
springCreditHours5 = tk.StringVar()
springCreditHours6 = tk.StringVar()

"""
variables for summer/fall 2020 courses
"""
#variables for course number
summerCourseNo1 = tk.StringVar()
summerCourseNo2= tk.StringVar()
summerCourseNo3 = tk.StringVar()
summerCourseNo4 = tk.StringVar()
summerCourseNo5 = tk.StringVar()
summerCourseNo6 = tk.StringVar()

#variables for course number
summerCourseName1 = tk.StringVar()
summerCourseName2 = tk.StringVar()
summerCourseName3 = tk.StringVar()
summerCourseName4 = tk.StringVar()
summerCourseName5 = tk.StringVar()
summerCourseName6 = tk.StringVar()

#variables for credit hours
summerCreditHours1 = tk.StringVar()
summerCreditHours2 = tk.StringVar()
summerCreditHours3 = tk.StringVar()
summerCreditHours4 = tk.StringVar()
summerCreditHours5 = tk.StringVar()
summerCreditHours6 = tk.StringVar()

#variablle for notes
notes = tk.StringVar()



window.title("Advising Form")       #Title of window
window.geometry("600x800")          #size of window
window.configure(background = "white")

#import logo
img = tk.PhotoImage(file = "utrgv.png")
imgResize = img.subsample(2, 2)
imgLabel = tk.Label(window, image = imgResize, bg = "white").grid(column = 1, row = 0)

#label for the text next to utrgv logo
label1 = tk.Label(window, text = "UTRGV B.S. Computer Science \n Class Planning Worksheet", bg = "white", font = 50).grid(column = 2, row = 0)

#labels and entries for name 
nameLabel = tk.Label(window, text = "Name:", bg = "white").grid(column = 0, row = 1) 
nameEntry = tk.Entry(window, textvariable = name, bg = "white", justify = tk.LEFT).grid(column = 1, row = 1)

#labels and entries for idNo 
idLabel = tk.Label(window, text = "ID #:", bg = "white").grid(column = 2, row = 1) #Create a Label
idEntry = tk.Entry(window, textvariable = idNo, justify = tk.LEFT).grid(column = 3, row = 1)

#labels and entries for faculty Advisor 
advisorLabel = tk.Label(window, text = "Faculty Advisor:", bg = "white").grid(column = 0, row = 2) #Create a Label
advisorEntry = tk.Entry(window, textvariable = advisorName, bg = "white", justify = tk.LEFT).grid(column = 1, row = 2)

#labels and entries for Date 
dateLabel = tk.Label(window, text = "Date:", bg = "white").grid(column = 2, row = 2) #Create a Label
dateEntry = tk.Entry(window, textvariable = date, bg = "white", justify = tk.LEFT).grid(column = 3, row = 2)

"""
labels and entries for all currently taking classes list
"""
#label for currently taking table title
currentLabel = tk.Label(window, text = "Currently Taking", bg = "white").grid(column = 2, row = 3)

#labels and entries for course Number
courseNoLabel = tk.Label(window, text = "Course Number", bg = "white").grid(column = 1, row = 4)

courseNoEntry1 = tk.Entry(window, textvariable = courseNo1, bg = "white" ).grid(column = 1, row = 5)
courseNoEntry2 = tk.Entry(window, textvariable = courseNo2, bg = "white" ).grid(column = 1, row = 6)
courseNoEntry3 = tk.Entry(window, textvariable = courseNo3, bg = "white" ).grid(column = 1, row = 7)
courseNoEntry4 = tk.Entry(window, textvariable = courseNo4, bg = "white" ).grid(column = 1, row = 8)
courseNoEntry5 = tk.Entry(window, textvariable = courseNo5, bg = "white" ).grid(column = 1, row = 9)
courseNoEntry6 = tk.Entry(window, textvariable = courseNo6, bg = "white" ).grid(column = 1, row = 10)

#labels and entries for course Course Name
courseNameLabel = tk.Label(window, text = "Course Name", bg = "white").grid(column = 2, row = 4)

courseNameEntry1 = tk.Entry(window, textvariable = courseName1, bg = "white" ).grid(column = 2, row = 5)
courseNameEntry2 = tk.Entry(window, textvariable = courseName2, bg = "white" ).grid(column = 2, row = 6)
courseNameEntry3 = tk.Entry(window, textvariable = courseName3, bg = "white" ).grid(column = 2, row = 7)
courseNameEntry4 = tk.Entry(window, textvariable = courseName4, bg = "white" ).grid(column = 2, row = 8)
courseNameEntry5 = tk.Entry(window, textvariable = courseName5, bg = "white" ).grid(column = 2, row = 9)
courseNameEntry6 = tk.Entry(window, textvariable = courseName6, bg = "white" ).grid(column = 2, row = 10)

#labels and entries for Credit Hours
creditHoursLabel = tk.Label(window, text = "Credit Hours", bg = "white").grid(column = 3, row = 4)

creditHoursEntry1 = tk.Entry(window, textvariable = creditHours1, bg = "white" ).grid(column = 3, row = 5)
creditHoursEntry2 = tk.Entry(window, textvariable = creditHours2, bg = "white" ).grid(column = 3, row = 6)
creditHoursEntry3 = tk.Entry(window, textvariable = creditHours3, bg = "white" ).grid(column = 3, row = 7)
creditHoursEntry4 = tk.Entry(window, textvariable = creditHours4, bg = "white" ).grid(column = 3, row = 8)
creditHoursEntry5 = tk.Entry(window, textvariable = creditHours5, bg = "white" ).grid(column = 3, row = 9)
creditHoursEntry6 = tk.Entry(window, textvariable = creditHours6, bg = "white" ).grid(column = 3, row = 10)

"""
labels and entries for all spring 2020 list
"""
#label for spring 2020 table title
springLabel = tk.Label(window, text = "Spring 2020", bg = "white").grid(column = 2, row = 11)

#labels and entries for spring 2020course number
courseNoLabel2 = tk.Label(window, text = "Course Number", bg = "white").grid(column = 1, row = 12)

springCourseNoEntry1 = tk.Entry(window, textvariable = springCourseNo1, bg = "white" ).grid(column = 1, row = 13)
springCourseNoEntry2 = tk.Entry(window, textvariable = springCourseNo2, bg = "white" ).grid(column = 1, row = 14)
springCourseNoEntry3 = tk.Entry(window, textvariable = springCourseNo3, bg = "white" ).grid(column = 1, row = 15)
springCourseNoEntry4 = tk.Entry(window, textvariable = springCourseNo4, bg = "white" ).grid(column = 1, row = 16)
springCourseNoEntry5 = tk.Entry(window, textvariable = springCourseNo5, bg = "white" ).grid(column = 1, row = 17)
springCourseNoEntry6 = tk.Entry(window, textvariable = springCourseNo6, bg = "white" ).grid(column = 1, row = 18)

#labels and entries for course Course Name
courseNameLabel2 = tk.Label(window, text = "Course Name", bg = "white").grid(column = 2, row = 12)

springCourseNameEntry1 = tk.Entry(window, textvariable = springCourseName1, bg = "white" ).grid(column = 2, row = 13)
springCourseNameEntry2 = tk.Entry(window, textvariable = springCourseName2, bg = "white" ).grid(column = 2, row = 14)
springCourseNameEntry3 = tk.Entry(window, textvariable = springCourseName3, bg = "white" ).grid(column = 2, row = 15)
springCourseNameEntry4 = tk.Entry(window, textvariable = springCourseName4, bg = "white" ).grid(column = 2, row = 16)
springCourseNameEntry5 = tk.Entry(window, textvariable = springCourseName5, bg = "white" ).grid(column = 2, row = 17)
springCourseNameEntry6 = tk.Entry(window, textvariable = springCourseName6, bg = "white" ).grid(column = 2, row = 18)

#labels and entries for credit hours
creditHoursLabel2 = tk.Label(window, text = "Credit Hours", bg = "white").grid(column = 3, row = 12)

springCreditHoursEntry1 = tk.Entry(window, textvariable = springCreditHours1, bg = "white" ).grid(column = 3, row = 13)
springCreditHoursEntry2 = tk.Entry(window, textvariable = springCreditHours2, bg = "white" ).grid(column = 3, row = 14)
springCreditHoursEntry3 = tk.Entry(window, textvariable = springCreditHours3, bg = "white" ).grid(column = 3, row = 15)
springCreditHoursEntry4 = tk.Entry(window, textvariable = springCreditHours4, bg = "white" ).grid(column = 3, row = 16)
springCreditHoursEntry5 = tk.Entry(window, textvariable = springCreditHours5, bg = "white" ).grid(column = 3, row = 17)
springCreditHoursEntry6 = tk.Entry(window, textvariable = springCreditHours6, bg = "white" ).grid(column = 3, row = 18)


"""
Labels and entries for all summer/fall list
"""
#label for spring 2020 table title
summerLabel = tk.Label(window, text = "Summer or Fall 2020", bg = "white").grid(column = 2, row = 19)

#labels and entries for spring 2020course number
courseNoLabel2 = tk.Label(window, text = "Course Number", bg = "white").grid(column = 1, row = 20)

summerCourseNoEntry1 = tk.Entry(window, textvariable = summerCourseNo1, bg = "white" ).grid(column = 1, row = 21)
summerCourseNoEntry2 = tk.Entry(window, textvariable = summerCourseNo2, bg = "white" ).grid(column = 1, row = 22)
summerCourseNoEntry3 = tk.Entry(window, textvariable = summerCourseNo3, bg = "white" ).grid(column = 1, row = 23)
summerCourseNoEntry4 = tk.Entry(window, textvariable = summerCourseNo4, bg = "white" ).grid(column = 1, row = 24)
summerCourseNoEntry5 = tk.Entry(window, textvariable = summerCourseNo5, bg = "white" ).grid(column = 1, row = 25)
summerCourseNoEntry6 = tk.Entry(window, textvariable = summerCourseNo6, bg = "white" ).grid(column = 1, row = 26)

#labels and entries for course Course Name
courseNameLabel2 = tk.Label(window, text = "Course Name", bg = "white").grid(column = 2, row = 20)

summerCourseNameEntry1 = tk.Entry(window, textvariable = summerCourseName1, bg = "white" ).grid(column = 2, row = 21)
summerCourseNameEntry2 = tk.Entry(window, textvariable = summerCourseName2, bg = "white" ).grid(column = 2, row = 22)
summerCourseNameEntry3 = tk.Entry(window, textvariable = summerCourseName3, bg = "white" ).grid(column = 2, row = 23)
summerCourseNameEntry4 = tk.Entry(window, textvariable = summerCourseName4, bg = "white" ).grid(column = 2, row = 24)
summerCourseNameEntry5 = tk.Entry(window, textvariable = summerCourseName5, bg = "white" ).grid(column = 2, row = 25)
summerCourseNameEntry6 = tk.Entry(window, textvariable = summerCourseName6, bg = "white" ).grid(column = 2, row = 26)

#labels and entries for credit hours
creditHoursLabel2 = tk.Label(window, text = "Credit Hours", bg = "white").grid(column = 3, row = 20)

summerCreditHoursEntry1 = tk.Entry(window, textvariable = summerCreditHours1, bg = "white" ).grid(column = 3, row = 21)
summerCreditHoursEntry2 = tk.Entry(window, textvariable = summerCreditHours2, bg = "white" ).grid(column = 3, row = 22)
summerCreditHoursEntry3 = tk.Entry(window, textvariable = summerCreditHours3, bg = "white" ).grid(column = 3, row = 23)
summerCreditHoursEntry4 = tk.Entry(window, textvariable = summerCreditHours4, bg = "white" ).grid(column = 3, row = 24)
summerCreditHoursEntry5 = tk.Entry(window, textvariable = summerCreditHours5, bg = "white" ).grid(column = 3, row = 25)
summerCreditHoursEntry6 = tk.Entry(window, textvariable = summerCreditHours6, bg = "white" ).grid(column = 3, row = 26)


#label and entry for notes
noteLabel = tk.Label(window, text = "NOTES", bg = "white", font = 14).grid(column = 0, row = 28)
noteEntry = tk.Entry(window, textvariable = notes, bg = "white").grid(column = 1, row = 28)











window.mainloop()
# This code may tak 20-30 seconds to give the excel file as desired output
import wikipedia
import xlsxwriter
workbook = xlsxwriter.Workbook('Deepanshu2019CS50427.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'Name')
worksheet.write('B1', 'Born')
worksheet.set_column(0,20,30)
famousPeople = ["Albert Einstein", "Narender Modi", "Rahul Gandhi", "Issac Newton", "Thomas Alva Edison", "Nikola Tesla", "Pranab Mukherjee", "Ram Nath Kovind", "Marie Curie", "Stephen Hawking"]
count=1
for person in famousPeople:
    count+=1
    page = wikipedia.page(person)
    cellNameForName = "A" + str(count)
    worksheet.write(cellNameForName, person)
    s = page.content
    l = list(s.split(" "))
    dob = ""
    for i in range(len(l)):
        if(l[i].lower()=="january" or l[i].lower()=="february" or l[i].lower()=="march" or l[i].lower()=="april" or l[i].lower()=="may" or l[i].lower()=="june" or l[i].lower()=="july" or l[i].lower()=="august" or l[i].lower()=="september" or l[i].lower()=="october" or l[i].lower()=="november" or l[i].lower()=="december"):
            dob = dob + l[i-1] + " " + l[i] + " " + l[i+1]
            break
    cellNameForDOB = "B" + str(count)
    worksheet.write(cellNameForDOB, dob)
workbook.close()





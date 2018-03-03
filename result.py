import requests
from bs4 import BeautifulSoup

url = 'http://juadmission.jdvu.ac.in/jums_exam/student/result/view_print_result.jsp?exam_roll=ITE1740'
for i in range(1,73):
    if i < 10:
        roll = url + '0' + str(i)
    else:
        roll = url + str(i)
    page=requests.get(roll)
    soup = BeautifulSoup(page.text, 'html.parser')
    alltable = soup.select('table')
    
    #print(len(alltable))
    if len(alltable) != 0:
        name = alltable[1]
        
        #to find the name, sem, dept, class_roll_no, regn_no, regn_year
        nametext = name.text.replace('\xa0','')
        listname = nametext.split('\n')

        while True:
            try:
                listname.remove('')
            except:
                break
        #print(listname)

        sem = listname[2]
        name = listname[13]
        dept = listname[15]
        classrollno = listname[16]
        examrollno = listname[18]
        regnno = listname[19]
        regnyear = listname[21]
        
        #print(sem, "\n", name, "\n", dept, "\n", classrollno, "\n", examrollno, "\n", regnno, "\n", regnyear)

        #subject name and marks
        score = alltable[4]
        scoretext = score.text.replace('\xa0','')
        scoretext = scoretext.replace(' ','')
        listscore = scoretext.split('\n') #remove all null values
        
        while True:
            try:
                listscore.remove('')
            except:
                break

        #print(listscore)

        #for sgpa
        sgpa = alltable[5]
        sgpatext = sgpa.text.replace('\xa0','')
        sqpatext = sgpatext.replace(' ','')
        listsgpa = sgpatext.split('\n')

        while True:
            try:
                listsgpa.remove('')
            except:
                break
        sgpa = listsgpa[0]
        print(name , " \t ", sgpa, "\n-----\n")

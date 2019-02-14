import requests
from bs4 import BeautifulSoup

url = 'http://juadmission.jdvu.ac.in/jums_exam/student_even_2018/result/view_print_result_be.jsp?exam_roll=ITE1860'
cou=0
for i in range(1,80):
    
    if i < 10:
        roll = url + '0' + str(i)
    else:
        roll = url + str(i)
    page=requests.get(roll)
    
    soup = BeautifulSoup(page.text, 'html.parser')
    alltable = soup.select('table')
    
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

        name = listname[13]
        """sem = listname[2]
        dept = listname[15]
        classrollno = listname[16]
        examrollno = listname[18]
        regnno = listname[19]
        regnyear = listname[21]
        """

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

        sgpa = listsgpa[1]
        if(name!="and Examination Roll No."):
            cou=cou+1
            print("" , "Examination Roll No", cou , "\n" ,name, "\n SGPA ", sgpa , "\n-----\n")
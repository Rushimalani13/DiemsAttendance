from django.shortcuts import render,redirect
from Acadmic_info.models import Branch_Record
from Attendance.models import Attendance_Record
from Lectures.models import Lecture_Record,Subject_Record
from Students.models import Student_Record,acdamic_year
from Teachers.models import Teacher_Record
from datetime import datetime 

# Create your views here.
def Takeattendance(request):
    acadamic_details=acdamic_year.objects.all().values()
    Lecture_details=Lecture_Record.objects.all().values()

    print(acadamic_details)
    print(Lecture_details)
    return render(request, 'attendance_portal/takeattendance.html',{'acadamic_details':acadamic_details,'Lecture_details':Lecture_details})

def Markattendance(request):
    if request.method == 'POST':
        acadmic_year = request.POST.get('acadmic-year')
        lecture_id = request.POST.get('lecture-id')
        lecture_date = request.POST.get('lecture-date')
        lecture_time = request.POST.get('lecture-time')
        lecture_type = request.POST.get('lecture-type')
        class_batch = request.POST.get('class-batch')
        print(acadmic_year)
        print(lecture_id)
        input_string = lecture_id
        split_list = input_string.split(" | ")
        print(split_list)
        lecture_id=split_list[0]
        lec_year=split_list[1]
        lec_branch=split_list[2]
        semester=split_list[3]
        subject_name=split_list[4]
        sem_division=split_list[6]
        subject_teacher=split_list[7]
        lec_data={'acadmic_year':acadmic_year,'lecture_id':lecture_id,'lecture_date':lecture_date,'lecture_time':lecture_time,'lecture_type':lecture_type}
        print(lecture_id,lec_year,lec_branch,semester,subject_name,sem_division,subject_teacher)
        print(lecture_date)
        print(lecture_time)
        print(lecture_type)
        print(class_batch)
        if class_batch=="All Batches":
            Student_Details=Student_Record.objects.filter(year=lec_year,student_branch=lec_branch,sem=semester,div=sem_division).values()
        else:
            Student_Details=Student_Record.objects.filter(year=lec_year,student_branch=lec_branch,sem=semester,div=sem_division,batch=class_batch).values()
            
        print(Student_Details)
        
    return render(request, 'attendance_portal/markattendance.html',{'Student_Details':Student_Details,'lec_data':lec_data})

def checked_attendance(request):
    if request.method == 'POST':
        acadmic_year_entry = request.POST.get('Attendance_info_1')
        lecture_id_entry = request.POST.get('Attendance_info_2')
        lecture_date_entry = request.POST.get('Attendance_info_3')
        lecture_time_entry = request.POST.get('Attendance_info_4')
        lecture_type_entry = request.POST.get('Attendance_info_5')
        record_count_entry = request.POST.get('record_count')
        #print(acadmic_year_entry, record_count_entry,lecture_id_entry,lecture_time_entry)
        for i in range(1,int(record_count_entry)+1):
            record_id="prn_"+str(i)
            record_id_details = request.POST.get(record_id)
            record_checked="checked_"+str(i)
            checked_id = request.POST.get(record_checked)
            if checked_id==None:
                ispresent = "A"
            else:
                ispresent = "P"
            #print(record_id_details)
            #print(ispresent)
              
            Attendance_Record_object=Attendance_Record.objects.create(student_Id=record_id_details,Lecture_Id=lecture_id_entry,Acadmic_year=acadmic_year_entry,default_att_Date=datetime.now(),att_date=lecture_date_entry,att_time=lecture_time_entry,is_present=ispresent,is_type=lecture_type_entry)
            Attendance_Record_object.save()
        
    return render(request, 'attendance_portal/success_attendance.html')
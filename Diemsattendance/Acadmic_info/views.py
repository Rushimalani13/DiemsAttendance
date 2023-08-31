from django.shortcuts import render
from Acadmic_info.models import Branch_Record
from Attendance.models import Attendance_Record
from Lectures.models import Lecture_Record,Subject_Record
from Students.models import Student_Record,acdamic_year
from Teachers.models import Teacher_Record
from datetime import datetime

# Create your views here.
def subject_Attendance(request):
    acadamic_details=acdamic_year.objects.all().values()
    Lecture_details=Lecture_Record.objects.all().values()

    print(acadamic_details)
    print(Lecture_details)
    return render(request, 'show_records/subjectwise_record.html',{'acadamic_details':acadamic_details,'Lecture_details':Lecture_details})

def subject_Attendance_table(request):
    if request.method == 'POST':
        acadmic_year = request.POST.get('acadmic-year')
        lecture_id = request.POST.get('lecture-id')
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
        lec_data={'acadmic_year':acadmic_year,'lecture_id':lecture_id,'lecture_type':lecture_type}
        print(lecture_id,lec_year,lec_branch,semester,subject_name,sem_division,subject_teacher)
        print(lecture_type)
        print(class_batch)
        if class_batch=="All Batches":
            Student_Details=Student_Record.objects.filter(year=lec_year,student_branch=lec_branch,sem=semester,div=sem_division).values()
        else:
            Student_Details=Student_Record.objects.filter(year=lec_year,student_branch=lec_branch,sem=semester,div=sem_division,batch=class_batch).values()
            
        print(Student_Details)
        attendance_Details=Attendance_Record.objects.filter(Lecture_Id=lecture_id).values()
        print(attendance_Details) 
        
        for search in Student_Details:
            search_student_id = search.get('clg_prn')
            # Create a dictionary to store attendance records grouped by student_id
            attendance_records_by_student = {}

            # Convert the attendance_queryset to a dictionary using 'student_Id' as the key
            for attendance in attendance_Details:
                student_id = attendance['student_Id']
                if student_id not in attendance_records_by_student:
                    attendance_records_by_student[student_id] = []
                attendance_records_by_student[student_id].append(attendance)

            # Example student_id to search for
            
            # Search for attendance records by student_id
            if search_student_id in attendance_records_by_student:
                attendance_records = attendance_records_by_student[search_student_id]
            else:
                attendance_records = []

            # Print attendance records for the student
            if attendance_records:
                print(f"Attendance Records for Student {search_student_id}:")
                for record in attendance_records:
                    att_date = record['att_date']
                    att_time = record['att_time']
                    is_present = record['is_present']
                    is_type = record['is_type']
                    formatted_date = datetime.strptime(att_date, '%Y-%m-%d').strftime('%b %d, %Y')
                    print(f"Date: {formatted_date}")
                    print(f"Time: {att_time}")
                    print(f"Present: {'Yes' if is_present == 'P' else 'No'}")
                    print(f"Type: {is_type}")
                    print("---")
            else:
                print("No attendance records found for the student.")
            
            print(attendance_records_by_student)
        ultimatedata={}
        alldates={}
        all_names={}
        onetime=True
        for student_id, records in attendance_records_by_student.items():
            print(f"Student ID: {student_id}")
            superlist={}
            li=[]
            stu_name=Student_Record.objects.filter(clg_prn=student_id).values()
            for stu in stu_name:
                name=stu['full_name']
            all_names.__setitem__(name,name)
            li.append(name)
          
            # Iterate through the attendance records for each student
            for record in records:   
             
                att_date = record['att_date']
                att_time = record['att_time'] 
                is_present = record['is_present']
                # is_type = record['is_type']
                if onetime==True:
                    formatdate_time=att_date+"|"+att_time
                    alldates.__setitem__(formatdate_time,formatdate_time)
                    # alldates.__setitem__(att_time,att_time)
                   
                li.append(is_present)
                # Print or process the attendance record details
          
                print(f"Date: {att_date}")
                print(f"Time: {att_time}")
                print(f"Present: {'Yes' if is_present == 'P' else 'No'}")
                # print(f"Type: {is_type}")
                print("---")
            onetime=False
            superlist.__setitem__(student_id,li)
            #print(superlist)
            ultimatedata.__setitem__(student_id,li)
            #print(ultimatedata)
            print(alldates)
            
            print(all_names)
    return render(request, 'show_records/attendance_table.html',{'Student_Details':Student_Details,'lec_data':lec_data,"attendance_Details":attendance_Details,'attendance_records_by_student':attendance_records_by_student,'ultimatedata':ultimatedata,'alldates':alldates,'all_names':all_names})

    
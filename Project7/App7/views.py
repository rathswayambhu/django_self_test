from django.shortcuts import render

def showIndex(request):
    student_info = {"data":
                    [
                        {"idno": 101, "name": "Ravi", "marks": [89, 56, 74, 15, 45, 56]},
                        {"idno": 102, "name": "Kumar", "marks": [45, 78, 56, 99, 55, 40]},
                        {"idno": 103, "name": "Mohan", "marks": [56, 23, 66, 9, 89, 50]},
                        {"idno": 104, "name": "Rani", "marks": [78, "A", 45, 88, 52, 60]},
                        {"idno": 105, "name": "Rama", "marks": [99, 36, 74, 55, 15, 46]},
                    ]
                   }
    #dict_data = {"data": student_info}
    return render(request,"index.html",student_info)

from django.shortcuts import render

# Create your views here.
from http.client import HTTPResponse
from django.shortcuts import render
import pandas as pd
import os
from django.core.files.storage import FileSystemStorage
from jaiib.models import Question
from django.contrib import messages

# Create your views here.

def Import_Excel_pandas(request):

    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        empexceldata = pd.read_excel(filename)
        dbframe = empexceldata
        for dbframe in dbframe.itertuples():
            obj = Question.objects.create(subcode=dbframe.subcode,questcode=dbframe.questcode, quest=dbframe.quest,
                                            option1=dbframe.option1,option1_correct=dbframe.option1_correct, option2=dbframe.option2,option2_correct=dbframe.option2_correct, option3=dbframe.option3,option3_correct=dbframe.option3_correct, option4=dbframe.option4,option4_correct=dbframe.option4_correct, explanation=dbframe.explanation)
            obj.save()
        messages.success(request, 'Successfully uploaded')
        
        return render(request, 'Import_excel_db.html', {
            'uploaded_file_url': uploaded_file_url
        })


    return render(request, 'Import_excel_db.html',{})

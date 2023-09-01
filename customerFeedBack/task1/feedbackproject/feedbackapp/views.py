from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required



# Create your views here.

from.forms import Feedbackform
from .models import CustomerFeedback

def show_feedback(request):
    feedback_entries = CustomerFeedback.objects.all()
    context = {
        'show': feedback_entries
    }
    return render(request, 'home.html', context)


# @login_required(login_url='feedback')
def feedback_view(request,pk):
    Edit=CustomerFeedback.objects.get(id=pk)
    form=Feedbackform(instance=Edit)
    if request.method == 'POST':
        form = Feedbackform(request.POST,request.FILES,instance=Edit)
        if form.is_valid():
            form.save()
            return redirect('feedback')
    content={
            'form':form
        }
          
    return render(request, 'Edit.html', content)
@login_required(login_url='feedback')
def addfeedback(request):
    form=Feedbackform()

    if request.method=='POST':
        form=Feedbackform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feedback')

    context={
        'form':form
        }
    return render(request,'add.html',context)



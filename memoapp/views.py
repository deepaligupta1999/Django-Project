from django.shortcuts import render,redirect
from .models import TaskModel
from .forms import TaskForm
def Home(req):
    objs=TaskModel.objects.order_by('date').reverse()
    form=TaskForm()
    if req.method=='POST':
        form=TaskForm(req.POST)
        if form.is_valid():
            print("3")
            form.save()
    return render(req,'home.html',{'data':objs,'form':form})
def Update(req,id):
    obj=TaskModel.objects.get(id=id)
    form=TaskForm(instance=obj)
    if req.method=='POST':
        form=TaskForm(req.POST,instance=obj)
        form.save()
        return redirect("home")
        #return redirect('/')
    return render(req,"update.html",{'form':form,'data':obj})

def Delete(req,id):
    obj=TaskModel.objects.get(id=id)
    if req.method=='POST':
        obj.delete()
        return redirect('home')
    return render(req,"delete.html",{'data':obj})

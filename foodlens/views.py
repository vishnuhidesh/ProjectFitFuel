from django.shortcuts import render
from .mingo import prediction
from .forms import ImageForm

# Create your views here.

def foodlensFunction(request):
    form = ImageForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        img_obj = form.instance
            
        return render(request,'foodlens.html',{'form':form,'img_obj':img_obj})
    else:
        form = ImageForm()
        return render(request,'foodlens.html', {'form': form})


def foodlensresultFunction(request):
    
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
                form.save()
                img_obj = form.instance
                value = prediction(img_obj.image)  
        return render(request,'foodlensresult.html',{'form':form,'img_obj':img_obj,'value':value})


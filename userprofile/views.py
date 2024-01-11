from django.shortcuts import render,redirect
from .models import UserProfile
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def userprofileFunction(request):
    return render(request,'userprofile.html')

def editprofileFunction(request): 
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except ObjectDoesNotExist:
        user_profile = UserProfile(user=request.user)

    if request.method == 'POST':
        user_profile.age = request.POST.get('age')
        user_profile.dob = request.POST.get('dob')
        user_profile.mobile = request.POST.get('mobile')
        user_profile.weight = request.POST.get('weight')
        user_profile.height = request.POST.get('height')
        user_profile.abdomen = request.POST.get('abdomen')
        user_profile.diabetic = request.POST.get('diabetic', 'not_sure')
        user_profile.profile_picture = request.FILES.get('profile_picture')

        # #BMI
        # weight_kg = float(user_profile.weight)
        # height_m = float(user_profile.height) / 100  # Convert height to meters
        # user_profile.bmi = round(weight_kg / (height_m ** 2), 2)
        
        user_profile.save()
        
        return redirect('profile')
    return render(request,'editprofile.html')
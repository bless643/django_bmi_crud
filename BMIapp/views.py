from django.shortcuts import render, redirect

from .models import BMI


# Create your views here.
def create(request):
    if request.method=='POST':
        name_var = request.POST['name']
        age_var = request.POST['age']
        weight_var = float(request.POST['weight'])
        height_var = float(request.POST['height'])

        bmi = weight_var/height_var**2
        bmi = round(bmi, 3)
        bmi_status = ""

        if bmi< 18:
            bmi_status = "underweight"
        elif bmi >= 18 and bmi < 25:
            bmi_status ="perfect"
        elif bmi >=25 and bmi <= 30:
            bmi_status = "overweight"
        else:
            bmi_status = "obesity"



        obj = BMI(name=name_var, age=age_var, weight=weight_var, height=height_var, bmi=bmi, bmi_status=bmi_status)
        obj.save()
        return redirect('readpage')

    return render(request, 'create.html')


def read(request):
    all_bmi = BMI.objects.all()
    return render(request, 'read.html', context={"all_objs": all_bmi})




def delete(request, pk):
    delete_obj = BMI.objects.get(id=pk)
    delete_obj.delete()
    return redirect('readpage')



def update(request, pk):
    update_obj = BMI.objects.get(id=pk)
    if request.method=='POST':
        update_obj.name = request.POST['name']
        update_obj.age = request.POST['age']
        update_obj.weight = float(request.POST['weight'])
        update_obj.height = float(request.POST['height'])

        bmi = update_obj.weight/update_obj.height**2
        bmi = round(bmi, 3)


        if bmi < 18:
            bmi_status = 'underweight'
        elif bmi >=18 and bmi< 25:
            bmi_status = "perfect"
        elif bmi >=25 and bmi < 30:
            bmi_status = "overweight"
        else:
            bmi_status = "overweight"

        update_obj.bmi = bmi

        update_obj.bmi_status = bmi_status


        update_obj.save()
        return redirect('readpage')

    return render(request, 'update.html', context={"updated": update_obj})

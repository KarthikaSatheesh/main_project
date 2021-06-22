from django.shortcuts import render
from .models import Userreg,Login,Staff,Gramasabha,Scheme,Application

def home(request):
    data = Scheme.objects.all()
    return render(request,'home.html',{'s':data})


def adminhome(request):
    return render(request,'adminhome.html')


def login(request):
    return render(request,'login.html')


def log(request):
    try:
        m=Login.objects.get(username=request.POST['username'],password=request.POST['pwd'])
        if m.status==1:
            request.session['user']=m.username
            data=Scheme.objects.all()
            return render(request,'uhome.html',{'sch':data})
        elif m.status==0:
            return render(request,'adminhome.html')
        else:
            return render(request,'login.html',{'error':"didnt match"})
    except:
        return render(request, 'login.html', {'error': "Invalid username or password"})


def out(request):
    data=request.session['user']
    return render(request,'login.html',{'data':data})


def ureg(request):
    return render(request,'ureg.html')


def reg(request):
                name = request.POST['name']
                address = request.POST['address']
                email = request.POST['email']
                phone = request.POST['phone']
                caste = request.POST['caste']
                religion = request.POST['religion']
                sex = request.POST['sex']
                wardno = request.POST['wardno']
                place = request.POST['place']
                username = request.POST['username']
                password = request.POST['pwd']
                photo = request.FILES['file']
                data=Userreg(name=name,address=address,email=email,phone=phone,caste=caste,religion=religion,sex=sex,wardno=wardno,place=place,username=username,photo=photo)
                data.save()
                data1=Login(username=username,password=password,status=1)
                data1.save()
                return render(request,'login.html')


def uhome(request):
    return render(request,'uhome.html')


def apply(request):
    data=Scheme.objects.all()
    return render(request,'apply.html',{'d':data})


def applyscheme(request):
    schemeid = request.POST['id']
    userid = request.session['user']
    return render(request,'applyscheme.html',{'s':schemeid,'u':userid})


def applyschemea(request):
    schemeid = request.POST['id']
    instance=Scheme.objects.get(id=schemeid)
    userid = request.POST['userid']
    photo = request.FILES['file']
    residencep = request.FILES['residencep']
    idcardp = request.FILES['idcardp']
    taxp = request.FILES['taxp']
    incomep = request.FILES['incomep']
    castep = request.FILES['castep']
    data = Application(schemeid=instance,userid=userid,photo=photo,residencep=residencep,idcardp=idcardp,taxp=taxp,incomep=incomep,castep=castep,status=0)
    data.save()
    return render(request,'uhome.html')


def updatescheme(request):
    id = request.POST['id']
    data = Scheme.objects.get(id=id)
    data.photo = request.POST['photo']
    data.designation = request.POST['designation']
    data.wardno = request.POST['wardno']
    data.wardname = request.POST['wardname']
    data.address = request.POST['address']
    data.save()
    id = request.POST['id']
    data1 = Scheme.objects.filter(id=id)
    return render(request, 'viewscheme.html', {'d': data1})


def viewuser(request):
    data=Userreg.objects.all()
    return render(request,'viewuser.html',{'d':data})


def addstaff(request):
    data=Staff.objects.all()
    return render(request,'addstaff.html',{'d':data})


def staffd(request):
    name = request.POST['name']
    designation = request.POST['designation']
    wardno = request.POST['wardno']
    wardname = request.POST['wardname']
    address = request.POST['address']
    phone = request.POST['phone']
    age = request.POST['age']
    educationalqualification = request.POST['educationalqualification']
    email = request.POST['email']
    photo = request.FILES['file']
    data=Staff(name=name,designation=designation,wardno=wardno,wardname=wardname,address=address,phone=phone,age=age,educationalqualification=educationalqualification,email=email,photo=photo)
    data.save()
    return render(request,'adminhome.html')


def edit(request):
    id=request.POST['id']
    data=Staff.objects.get(id=id)
    return render(request,'edit.html',{'data':data})


def update(request):
    id=request.POST['id']
    data=Staff.objects.get(id=id)
    data.name=request.POST['name']
    data.designation=request.POST['designation']
    data.wardno=request.POST['wardno']
    data.wardname=request.POST['wardname']
    data.address=request.POST['address']
    data.phone=request.POST['phone']
    data.age=request.POST['age']
    data.educationalqualification=request.POST['educationalqualification']
    data.email=request.POST['email']
    data.photo = request.FILES['file']
    data.save()
    id=request.POST['id']
    data1=Staff.objects.filter(id=id)
    return render(request, 'vieweachstaffdetails.html', {'data1': data1})


def viewstaff(request):
    data=Staff.objects.all()
    return render(request,'viewstaff.html',{'d':data})



def remove(request):
    id=request.POST['id']
    Staff.objects.filter(id=id).delete()
    data = Staff.objects.all()
    return render(request, 'adminhome.html', {'data': data})


def viewstaffuser(request):
    user = request.session['user']
    data = Userreg.objects.get(username=user)
    data=Staff.objects.filter(wardno=data.wardno)
    return render(request,'viewstaffuser.html',{'d':data})


def vieweachstaffdetailsuser(request):
    id=request.POST['id']
    data1=Staff.objects.filter(id=id)
    return render(request, 'vieweachstaffdetailsuser.html', {'data1': data1})


def viewschemeuser(request):
    data=Scheme.objects.all()
    return render(request,'viewschemeuser.html',{'d':data})


def vieweachstaffdetails(request):
    id=request.POST['id']
    data1=Staff.objects.filter(id=id)
    return render(request, 'vieweachstaffdetails.html', {'data1': data1})


def gramapanchayat(request):
    return render(request,'gramapanchayat.html')


def chakkupallamgp(request):
    return render(request,'chakkupallamgp.html')


def addgramasabha(request):
    data=Gramasabha.objects.all()
    return render(request,'addgramasabha.html',{'d':data})


def grama(request):
    place = request.POST['place']
    time = request.POST['time']
    date = request.POST['date']
    wardno = request.POST['wardno']
    data = Gramasabha(place=place,time=time,date=date,wardno=wardno)
    data.save()
    return render(request,'adminhome.html')


def viewgramasabha(request):
    data=Gramasabha.objects.all()
    return render(request,'viewgramasabha.html',{'d':data})

def remove(request):
    id=request.POST['id']
    Gramasabha.objects.filter(id=id).delete()
    data = Gramasabha.objects.all()
    return render(request, 'adminhome.html', {'data': data})


def editgramasabha(request):
    id=request.POST['id']
    data=Gramasabha.objects.get(id=id)
    return render(request,'editgramasabha.html',{'data':data})


def updategramasabha(request):
    id = request.POST['id']
    data = Gramasabha.objects.get(id=id)
    data.place = request.POST['place']
    data.time = request.POST['time']
    data.date = request.POST['date']
    data.wardno = request.POST['wardno']
    data.save()
    id = request.POST['id']
    data1 = Gramasabha.objects.filter(id=id)
    return render(request, 'viewgramasabha.html', {'d': data1})


def addscheme(request):
    data=Scheme.objects.all()
    return render(request,'addscheme.html',{'d':data})


def scheme(request):
    scheme = request.POST['scheme']
    requirements = request.POST['requirements']
    data=Scheme(scheme=scheme,requirements=requirements)
    data.save()
    return render(request,'adminhome.html')


def viewscheme(request):
    data=Scheme.objects.all()
    return render(request,'viewscheme.html',{'d':data})

def remove(request):
    id=request.POST['id']
    Scheme.objects.filter(id=id).delete()
    data = Scheme.objects.all()
    return render(request, 'adminhome.html', {'data': data})


def editscheme(request):
    id=request.POST['id']
    data=Scheme.objects.get(id=id)
    return render(request,'editscheme.html',{'data':data})


def updatescheme(request):
    id = request.POST['id']
    data = Scheme.objects.get(id=id)
    data.scheme = request.POST['scheme']
    data.requirements = request.POST['requirements']
    data.save()
    id = request.POST['id']
    data1 = Scheme.objects.filter(id=id)
    return render(request, 'viewscheme.html', {'d': data1})


def report(request):
    return render(request,'report.html')


def schemewiseappli(request):
    data=Scheme.objects.all()
    return render(request,'schemewiseappli.html',{'d':data})


def showschemewiseuser(request):
    id=request.POST['id']
    data1 = Scheme.objects.get(id=id)
    data=Application.objects.filter(schemeid=data1)
    return render(request,'showschemewiseuser.html',{'data':data})


def userwiseappli(request):
    data=Application.objects.all()
    return render(request,'userwiseappli.html',{'d':data})


def approvedappli(request):
    data=Application.objects.filter(status=1)
    return render(request,'approvedappli.html',{'d':data})


def rejectedappli(request):
    data=Application.objects.filter(status=2)
    return render(request,'rejectedappli.html',{'d':data})


def search(request):
    return render(request,'search.html')


def sear(request):
    n=request.POST['id']
    data=Scheme.objects.filter(id=n)
    return render(request,'search.html',{'s':data})


def myprofile(request):
    user=request.session['user']
    data=Userreg.objects.get(username=user)
    return render(request,'myprofile.html',{'i':data})


def addapplication(request):
    data=Application.objects.filter(status=0)
    return render(request,'addapplication.html',{'d':data})


def approveapplication(request):
    id=request.POST['id']
    Application.objects.filter(id=id).update(status=1)
    data=Application.objects.filter(status=1)
    return render(request,'approveapplication.html',{'d':data})


def reject(request):
    id=request.POST['id']
    Application.objects.filter(id=id).update(status=2)
    data=Application.objects.filter(status=2)
    return render(request,'reject.html',{'d':data})


def status(request):
    user=request.session['user']
    data=Application.objects.filter(userid=user)
    return render(request,'status.html',{'d':data})


def logout(request):
    try:
        del request.session['user']
    except KeyError:
        pass
    return render(request,'login.html')


# Create your views here.

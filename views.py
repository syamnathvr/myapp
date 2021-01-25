from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'./myapp/index.html')

def about(request):
    return render(request,'./myapp/about.html')

from .models import user_login


def admin_login(request):
    if request.method == 'POST':
        uname= request.POST.get('uname')
        passwd = request.POST.get('passwd')
        # Select Query
        user_list = user_login.objects.filter(uname=uname, passwd=passwd, utype='admin')
        if len(user_list) == 1:
            #Setting Session
            request.session['user_name'] = user_list[0].uname
            request.session['user_id'] = user_list[0].id
            context = {'uname': user_list[0].uname.upper()}
            return render(request, './myapp/admin_home.html',context)
        else:
            context = {'msg':'Invalid Credentials!!!'}
            return render(request,'./myapp/admin_login.html',context)
    else:
        return render(request,'./myapp/admin_login.html')


def admin_home(request):
    context = {'uname': 'admin'}
    return render(request, './myapp/admin_home.html', context)


def admin_change_password(request):
    if request.method == 'POST':
        opasswd = request.POST.get('opasswd')
        npasswd = request.POST.get('npasswd')
        try:
            uname = request.session['user_name']
        except:
            return render(request, './myapp/admin_login.html')
        try:
            user1 = user_login.objects.get(uname=uname, passwd=opasswd, utype='admin')
            # Update Query
            user1.passwd = npasswd
            user1.save()
            context = {'msg':'Password Changed'}
            return render(request, './myapp/admin_change_password.html',context)
        except user_login.DoesNotExist:
            context = {'msg':'Invalid Old Password'}
            return render(request, './myapp/admin_change_password.html',context)
    else:
        return render(request,'./myapp/admin_change_password.html')


def admin_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
        return admin_login(request)
    except:
        return admin_login(request)

from .models import job_master
def admin_job_master_view(request):
        obj = job_master.objects.all()
        context = {'job_master':obj}
        return render(request, './myapp/admin_job_master_view.html', context)

def admin_job_master_add(request):
    if request.method == "POST":
        id = request.POST.get('id')
        label = request.POST.get('label')

        obj = job_master(label=label)
        obj.save()
        context = {'msg': 'Label Added Successfully'}
        return render(request, './myapp/admin_job_master_add.html', context)
    else:
        return render(request, './myapp/admin_job_master_add.html')

def admin_job_master_delete(request):
        id = request.GET.get('id')
        job_master_del = job_master.objects.get(id=int(id))
        job_master_del.delete()
        user_list = job_master.objects.all()
        context = {'uname': 'admin'.upper(), 'user_list': user_list, 'msg': 'One Deleted'}
        return render(request, './myapp/admin_job_master_view.html', context)


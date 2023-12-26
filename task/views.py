from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task,Review,ProfilePic,ImageModel
from .forms import TaskForm,ReviewForm,CreateUserForm,LoginForms,ImageForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework import mixins, generics
from .serializers import TaskModelSerializers,ImageModelSerializers
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.response import Response


# Create your views here.
@login_required(login_url='/login/')
def Home(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user)
        reviews = Review.objects.all()
        # profile=ProfilePic.objects.get(user=request.user)
        context = {'tasks': tasks, 'reviews': reviews, 'username': request.user.username}
        return render(request, 'index.html', context=context)
    else:
        return redirect('/login/')

# class TaskListView(ListView):
    model = Task
    template_name ='index.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['priorities'] = ['Low', 'Medium', 'High']
        return context

    def get_queryset(self):
        queryset = Task.objects.all().order_by(F('priority').desc())
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query)
            )

        creation_date = self.request.GET.get('creation_date')
        if creation_date:
            queryset = queryset.filter(
                creation_date__date=creation_date
            )

        due_date = self.request.GET.get('due_date')
        if due_date:
            queryset = queryset.filter(
                due_date__date=due_date
            )

        priority = self.request.GET.get('priority')
        if priority:
            queryset = queryset.filter(
                priority=priority
            )

        is_complete = self.request.GET.get('is_complete')
        if is_complete == '1':
            queryset = queryset.filter(is_complete=True)
        elif is_complete == '0':
            queryset = queryset.filter(is_complete=False)

        return queryset  
      
    
def search_tasks(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            searched = request.POST['searched']
            tasks = Task.objects.filter(user=request.user, title__contains=searched)
            return render(request, 'search_tasks.html', {'searched': searched, 'tasks': tasks})  
        else:
            return render(request, 'index.html', {})
        
        
def filter_tasks(request):
    if request.method == 'POST':
        filter_option = request.POST.get('filter_option', '')

        if filter_option == 'Creation Date':
            tasks = Task.objects.filter(user=request.user).order_by('creation_date')
        elif filter_option == 'Due Date':
            tasks = Task.objects.filter(user=request.user).order_by('due_date')
        elif filter_option == 'Priority':
            tasks = Task.objects.filter(user=request.user).order_by('priority')
        elif filter_option == 'Status':
            tasks = Task.objects.filter(user=request.user).order_by('-is_complete')
        else:
            tasks = Task.objects.filter(user=request.user)
    else:
        tasks = Task.objects.filter(user=request.user)

    context = {'tasks': tasks, 'username': request.user.username}
    return render(request, 'index.html', context=context)

    
def LoginPage(request):
    form=LoginForms()
    
    if request.method=="POST":
        form=LoginForms(request,data=request.POST)
        
        if form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')
            
            user=authenticate(request,username=username,password=password)
            
            if user is not None:
                auth.login(request,user)
                return redirect('/')
    
    context={'form':form}
    return render(request,'login.html',context=context)
    



@login_required(login_url='/login/')
def CreateTask(request):
    form = TaskForm()
    imageform=ImageForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        images = request.FILES.getlist('images')
        # print(images)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Assign the current user to the task
            task.save()
           
            
        for image in images:
            photo = ImageModel.objects.create(task_id=task, image=image)
            photo.save()
        
        return redirect('Home')
    context = {'form': form, 'imageform': imageform}
    return render(request, 'task_form.html', context=context)

@login_required(login_url='/login/')
def CreateReview(request):
    form=ReviewForm()
    
    if request.method=='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    
    return render(request,'create_review.html',context=context)

@login_required(login_url='/login/')
def UpdateTask(request,pk):
    task=Task.objects.get(id=pk)
    form=TaskForm(instance=task)
    if request.method=='POST':
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'update.html',context=context)

@login_required(login_url='/login/')
def DeleteTask(reqeust,pk):
    task=Task.objects.get(id=pk)
    
    if reqeust.method=='POST':
        task.delete()
        return redirect('/')
        
    return render(reqeust,'delete.html')

def ImageDelete(request,pk):
    image=ImageModel.objects.get(id=pk)
    taskid=image.task_id
    if request.method=='POST':
        image.delete()
        return redirect('ViewTask',pk=taskid.id)
    context={'taskid':taskid}
    return render(request,'delete_image.html',context=context)


# @login_required(login_url='/login/')    
def CreateUser(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            current_user=form.save(commit=False)
            form.save()
            profile=ProfilePic.objects.create(user=current_user)
            # task=form.save(commit=False)
            # task.user = request.user
            # # profile=ProfilePic.objects.create(user=task)
            # task.save()
            return redirect('/')
    context={'form':form}
    return render(request,'register.html',context=context)   

@login_required(login_url='/login/')
def user_logout(request):
    auth.logout(request)
    return  redirect('/')


def ViewProfile_Pic(request):
    profile=ProfilePic.objects.get(user=request.user)
    context={'profile':profile}
    return render(request,'index.html',context=context)


def ViewTask(request,pk):
    task=Task.objects.get(id=pk)
    images=ImageModel.objects.filter(task_id=task)
    context={'task':task,'images':images}
    return render(request,'view_task.html',context=context)


class TaskModelAPIView(APIView):
    def get(self,request,*args,**kwargs):
        snippet=Task.objects.all()
        serializers=TaskModelSerializers(snippet,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
    
    def post(self,request,*args,**kwargs):
        serializers=TaskModelSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
class TaskApiVIew(APIView):
    def get_object(self,pk):
        try:
            snippet=Task.objects.get(pk=pk)
            return snippet
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def get(self,request,pk,*args,**kwargs):
        snippet=self.get_object(pk)
        serializers=TaskModelSerializers(snippet)
        return Response(serializers.data)
    
    def put(self,request,pk,*args,**kwargs):
        snippet=self.get_object(pk)
        serializers=TaskModelSerializers(snippet,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
    
    def delete(self,request,pk,*args,**kwargs):
        snippet=self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_100_CONTINUE)



class TaskGenericsAPIView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializers

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # You can override other methods if needed, for example, perform custom logic on GET requests

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    

class TaskModelDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializers
    
    



    
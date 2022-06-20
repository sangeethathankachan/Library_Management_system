from django.shortcuts import render,redirect
import os
from libraryApp.models import books,category,cart,IsedBuks
from django.contrib.auth.models import auth,User
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def index(request):
    
        # u_uid=request.session["uid"]
        # print(u_uid)
        book=books.objects.all()
        return render(request,'index.html',{'book':book})
    

def adminindex(request):
    return render(request,'adminindex.html')

def mylibrary(request):
    return render(request,'addcategory.html')

def addcategory(request):
    if request.method=='POST':
        categoryname=request.POST['categoryname']
        # items=request.FILES['file']
        data=category(categoryname=categoryname)
        data.save()
        messages.success(request,"Category added successfully!")
        redirect('addcategory')
    return render(request,'addcategory.html')

def shcategory(request):
    # if 'uid' in request.session:
        cate=category.objects.all()
        return render(request,'shcategory.html',{'cate':cate})

def deletecat(request,pk):
    cate=category.objects.get(id=pk)
    cate.delete()
    return redirect('shcategory')  

def issue(request):
    std=User.objects.all()
    #book=books.objects.all()
    if request.method=='POST':
        bookname=request.POST['bookname']
        isdate=request.POST['isdate']
        expdate=request.POST['expdate']
        fine=request.POST['fine']
        se=request.POST['se1']
        cou=User.objects.get(id=se)
        st=IsedBuks(fine=fine,
              isdate=isdate,
              expdate=expdate,
              bookname=bookname,
              user=cou)
        st.save()
        return redirect('issue')
    return render(request,'issue.html',{'std':std})

def viewissue(request,pk):
    std=IsedBuks.objects.filter(user_id=pk)
    return render(request,'viewissue.html',{'std':std})

def viewadminis(request):
    # if 'uid' in request.session:
        std=IsedBuks.objects.all()
        return render(request,'viewadminis.html',{'std':std})

def addbook(request):

        cat=category.objects.all()
        if request.method=='POST':
            name=request.POST['name']
            price=request.POST['price']
            image=request.FILES['file']
            catg1=request.POST['sel']
            categ=category.objects.get(id=catg1) 
            ctg=books(category=categ,image=image,name=name,price=price)
            ctg.save()
            messages.success(request,"Book added successfully!")
            return redirect('addbook')
        return render(request,'addbook.html',{'cat':cat})

# @login_required(login_url='login')
def showbooks(request):
    # if 'uid' in request.session:
        book=books.objects.all()
        return render(request,'showbooks.html',{'book':book})
    # return redirect('login')

def editdetails(request,pk):
    book = books.objects.get(id=pk)
    cat = category.objects.all()
    context = {'book':book,'cat':cat}
    if request.method == 'POST':
        book.name = request.POST['name']
        book.price = request.POST['price']
        book.author = request.POST['author']
        book.details = request.POST['details']
        book.image=request.FILES.get('file')
        # if request.FILES.get('file') is not None:
        #     if not pro.image == "/static/image/default.jpg":
        #         os.remove(pro.image.path)
        #         pro.image=request.FILES['file']
        #     else:
        #         pro.image=request.FILES['file']
        # else:
        #     os.remove(pro.image.path)
        #     pro.image = "/static/image/default.jpg"
        c = request.POST['sel']
        book.category = category.objects.get(id=c)
       
        book.save()
        messages.success(request,"Book updated successfully!")
        return redirect(showbooks)
    return render(request,'edit.html',context)

def deletedetails(request,pk):
    std=books.objects.get(id=pk)
    std.delete()
    messages.success(request,"Book Deleted successfully!")
    return redirect('showbooks')  
  
def logout(request):
    auth.logout(request)
    book=books.objects.all()
    return render(request,'index.html',{'book':book})
    #return redirect('index')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def signup(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        address=request.POST['address']
        contact=request.POST['contact']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"This user already exists!!")
                return redirect('signup')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password)
                user.save()
               
                return render(request,'login.html')
        else:
            messages.info(request,"Password does not match!!!")
            return redirect('signup')
        return redirect('loginpage')
    else:
        return render(request,'register.html')
    
def login_user(request):
    
    if request.method=='POST':
                    book=books.objects.all()
                    username=request.POST['username']
                    password=request.POST['password']
                    user=auth.authenticate(username=username,password=password)
                    # request.session["uid"]=user.id
                    if user is not None:
                        if user.is_staff:
                            auth.login(request,user)
                            return render(request,'adminindex.html')
                        else:
                            # login(request,user)
                            auth.login(request,user)
                            messages.info(request,f'Welcome {username}')
                            return render(request,'index.html',{'book':book, 'user':user})
                            # return redirect('userhomepage')
                    else:
                        messages.info(request,'Invalid username and password')
                        return redirect('login')
    else:
                return render(request,'login.html')
            
def cartitems(request,pk,k):
    
    print(cartitems)
    bookobj= book(id=pk)
    userobj= User(id=k)
    t=cart(product=bookobj,user=userobj)
    t.save()
    return redirect('index')
    carts=cart.objects.all()
    return render(request,'cart.html', {'cartitems':carts})
    

def loadcartitems(request,pk):
    c=cart.objects.filter(user=pk)
    return render(request,'cart.html',{'cartitems':c})

def details(request,pk,k):
    book=books.objects.get(id=pk)
    
    return render(request,'details.html',{'book':book, 'u':k})

def profile(request,pk):
    std=User.objects.get(id=pk)
    return render(request,'profile.html',{'std':std,})


def showuser(request):
        std=User.objects.filter(is_staff=0)
        return render(request,'showuser.html',{'std':std})

def deleteuser(request,pk):
    std=User.objects.get(id=pk)
    std.delete()
    return redirect('showuser')

def edituser(request,pk):
    std = User.objects.get(id=pk)
    #crs = course.objects.all()
    context = {'std':std}
    if request.method == 'POST':
        #stu.studentname = request.POST['studentname']
        #stu.date = request.POST['date']
        #stu.address = request.POST['address']
        #stu.age = request.POST['age']
        #c = request.POST['sel']
        std.fine = request.POST['fine']
        
       
        std.save()
        return redirect(showuser)
    return render(request,'edituser.html',context)


def items(request):
    item=cart.objects.all()
    return render(request,'item.html',{'item':item})

def deleteitem(request,pk):
    item=cart.objects.get(id=pk)
    item.delete()
    return redirect('items')


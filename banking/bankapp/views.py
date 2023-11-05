from django.shortcuts import render,redirect
from datetime import date
from .models import Transaction
from . models import Register
from django.utils import timezone
from datetime import datetime
# Create your views here.
def home(request):
    return render(request, 'index.html')

# def registration_form(request):
#     if request.method == 'POST':
#         fname = request.POST['fname']
#         lname = request.POST['lname']
#         bankname = request.POST['bankname']
#         acnumber = request.POST['acnumber']
        
#         ifsc = request.POST['ifsc']
#         zip = request.POST['zip']
#         address = request.POST['addreess']
#         city= request.POST['city']
#         district = request.POST['district']
#         branch = request.POST['branch']
#         dob = request.POST['dob']
#         age = request.POST['age']
#         gender = request.POST['gender']
#         phone = request.POST['phone']
#         email = request.POST['email']
#         type_ac = request.POST['account-type']
#         details = request.POST['materials']

        
        

#         if len(ifsc) != 11 or len(acnumber) < 8 or len(acnumber) > 12 or  len(zip) != 6 :
#             return redirect('bankapp:registration_form')
#         else:
#             register = Register(fname=fname, lname=lname, address=address, city=city, zip=zip, district=district, branch=branch, dob=dob, age=age, bankname=bankname, acnumber=acnumber, ifsc=ifsc, gender=gender, phone=phone, email=email, type_ac=type_ac, details=details )
#             register.save()
#             return redirect('/' ,{"register":register})

#     return render(request, 'form.html')
def registration_form(request):
    if request.method == 'POST':
     
            fname = request.POST['fname']
            lname = request.POST['lname']
            bankname = request.POST['bankname']
            acnumber = request.POST['acnumber']
            ifsc = request.POST['ifsc']
            zip = request.POST['zip']
            address = request.POST['addreess']
            city = request.POST['city']
            district = request.POST['district']
            branch = request.POST['branch']
            dob = request.POST['dob']
            age = int(request.POST['age'])
            gender = request.POST['gender']
            phone = request.POST['phone']
            email = request.POST['email']
            type_ac = request.POST['account-type']
            

            ms = ['Debit Card', 'Credit Card', 'Cheque Book']
            details = request.POST.getlist('materials')

            # Your validation logic here

           
            if len(ifsc) != 11 or len(acnumber) < 8 or len(acnumber) > 12 or  len(zip) != 6 or len(phone) != 10:
                print('error')
                return redirect('bankapp:registration_form')
            else:
                dob_input = request.POST['dob']
                age_input = int(request.POST['age'])

            # Validate Date of Birth and Age

                try:
                    dob = datetime.strptime(dob_input, '%Y-%m-%d').date()
                    current_date = timezone.now().date()
                
                    calculated_age = current_date.year - dob.year - ((current_date.month, current_date.day) < (dob.month, dob.day))
                    if age_input == calculated_age:
                        register = Register(fname=fname, address=address, lname=lname,  city=city, zip=zip, district=district, branch=branch, dob=dob, age=age, bankname=bankname, acnumber=acnumber, ifsc=ifsc, gender=gender, phone=phone, email=email, type_ac=type_ac, details=details )
                        register.save()
                        print(register)
                        return render(request ,'registration_sucess.html')
                    else:
                        return redirect('bankapp:registration_form')
                except:
                    return redirect('bankapp:registration_form')


    return render(request,'form.html')



   
            # # Handle the error, e.g., redirect to the form page with an error message
            # print('errorr')
            # print(fname)
            # print(lname)
            # print(type_ac)
            # print(details)
            # print(acnumber)
            # print(zip)
            # print(ifsc)
            # print(dob)
            # print(age)
            # print(address)
            # print(city)
            # print(district)
            # print(bankname)
            # print(gender)
            # print(phone)
   

def services(request):
    return render(request, 'services.html')

def transfer(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        bankname = request.POST['bankname']
        acnumber = request.POST['acnumber']
        ifsc = request.POST['ifsc']
        amount = request.POST['amount']
        today = date.today()
        amount = int(amount)
        

        if  amount < 0 or len(ifsc) != 11 or len(acnumber) < 8 or len(acnumber) > 12:
            return render(request,'transfer.html')
        else:
            report = Transaction(fname=fname, lname=lname, bank_name=bankname, acnumber=acnumber, ifsc=ifsc, amount=amount, date=today )
            report.save()
              
            return render(request, 'success.html')

    return render(request, 'transfer.html')
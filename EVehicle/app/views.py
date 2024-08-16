from django.shortcuts import render, redirect
from . models import *
from django.contrib import messages
from django.db import connection
def home(request):
	return render(request,'index.html',{})
def public_register(request):
	if request.method == 'POST':
		email = request.POST.get('lastname')
		uname = request.POST.get('username')
		psw = request.POST.get('password')
		pnum = request.POST.get('mail')
		country = request.POST.get('country')
		state = request.POST.get('state')
		city = request.POST.get('city')
		addr = request.POST.get('addr')
		img = request.FILES['image']
		crt = Public_Detail.objects.create(email=email,
		phone_number=pnum,username=uname,password=psw,image=img,
		country=country,state=state,city=city,address=addr)
		if crt:
			messages.success(request,'Registered Successfully')
	return render(request,'public_register.html',{})
def public_login(request):
	if request.session.has_key('public'):
		return redirect("public_dashboard")
	else:
		if request.method == 'POST':
			username = request.POST.get('uname')
			password =  request.POST.get('psw')
			post = Public_Detail.objects.filter(username=username,password=password)
			if post:
				username = request.POST.get('uname')
				request.session['public'] = username
				a = request.session['public']
				sess = Public_Detail.objects.only('id').get(username=a).id
				request.session['p_id']=sess
				return redirect("public_dashboard")
			else:
				messages.success(request, 'Invalid Username or Password')
	return render(request,'public_login.html',{})
def public_dashboard(request):
	if request.session.has_key('public'):
		return render(request,'public_dashboard.html',{})
	else:
		return render(request,'public_login.html',{})
def public_logout(request):
    try:
        del request.session['public']
    except:
     pass
    return render(request, 'public_login.html', {})
def search(request):
	if request.session.has_key('public'):
		public_id = request.session['p_id']
		if request.method == 'GET':
			a = request.GET.get('search')
			ids = EVBunk_Detail.objects.filter(city=a)
			return render(request,'search.html',{'ids':ids})
		else:
			return render(request,'search.html',{})
	else:
		return render(request,'public_login.html',{})
def book_slot(request):
	if request.session.has_key('public'):
		public_id = request.session['p_id']
		a = request.GET.get('id')
		ids = Slot_Detail.objects.filter(bunk_id=int(a),status='Available')
		return render(request,'book_sloat.html',{'ids':ids})	
	else:
		return render(request,'public_login.html',{})
def slot_detail(request):
	if request.session.has_key('public'):
		public_id = request.session['p_id']
		if request.method == 'POST':
			type_of_battery = request.POST.get('type_of_battery')
			date = request.POST.get('date')
			time = request.POST.get('time')
			battery_details = request.POST.get('battery_details')
			type_of_battery = request.POST.get('type_of_battery')
			s_id = request.GET.get('slot')
			bid= request.GET.get('bunk_id')
			bunk_id =EVBunk_Detail.objects.get(id=int(bid))
			slot_id = Slot_Detail.objects.get(id=int(s_id))
			user_id =Public_Detail.objects.get(id=int(public_id))
			ids = Booking.objects.create(type_of_battery=type_of_battery,date=date,time=time,battery_details=battery_details,
			status='Pending',slot_status='Pending',user_id=user_id,bunk_id=bunk_id,slot_id=slot_id)
			if ids:
				messages.success(request,'Submitted Successfully. We Will Contact You Soon.')
			return render(request,'slot_detail.html',{})
		else:
			return render(request,'slot_detail.html',{})
	else:
		return render(request,'public_login.html',{})
def booking_status(request):
	if request.session.has_key('public'):
		public_id = request.session['p_id']
		ids = Booking.objects.filter(user_id=int(public_id))
		return render(request,'manage_query.html',{'form':ids})	
	else:
		return render(request,'public_login.html',{})
def admin_booking(request):
	ids = Booking.objects.all()
	return render(request,'admin_booking.html',{'form':ids})
def accept(request,pk):
	ids = Booking.objects.filter(id=pk).update(status='Approved',slot_status='Booked')
	cursor=connection.cursor()
	sql='''SELECT b.slot_id_id from app_booking as b where b.id='%d' ''' % (pk)
	post = cursor.execute(sql)
	row = cursor.fetchone()
	slot_id = row[0]
	Slot_Detail.objects.filter(id=int(slot_id)).update(status='Booked')
	return redirect('admin_booking')
def reject(request,pk):
	ids = Booking.objects.filter(id=pk).update(status='Rejected',slot_status='Available')
	cursor=connection.cursor()
	sql='''SELECT b.slot_id_id from app_booking as b where b.id='%d' ''' % (pk)
	post = cursor.execute(sql)
	row = cursor.fetchone()
	slot_id = row[0]
	Slot_Detail.objects.filter(id=int(slot_id)).update(status='Available')
	return redirect('admin_booking')		
def payment_status(request,pk):
	ids=Booking.objects.filter(id=pk)
	if request.method == 'POST':
		payment_status =  request.POST.get('payment_status')
		amount = request.POST.get('amount')
		note = request.POST.get('msg')
		up = Booking.objects.filter(id=pk).update(notes=note,payment_status=payment_status,amount=amount)
		if up:
			return redirect('admin_booking')
	return render(request,'update_work_status.html',{'ids':ids})


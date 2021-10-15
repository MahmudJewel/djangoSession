from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, 'home.html')

def setSession(request):
	request.session['name'] = 'Jewel'
	return render(request,'setSession.html')

def getSession(request):
	nm=request.session.get('name')
	context={
		'nm':nm,
	}
	return render(request,'getSession.html',context)

def deleteSession(request):
	nm=request.session.get('name')
	del request.session['name']
	context={
		'nm':nm,
	}
	return render(request,'delSession.html',context)

def flushSession(request):
	nm=request.session.get('name')
	request.session.flush()
	context={
		'nm':nm,
	}
	return render(request,'flushSession.html',context)
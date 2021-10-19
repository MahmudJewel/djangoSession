# Session
A cookie can be used to store a session key. A session is a collection of user state that's stored server side. The session key gets passed back to the server, which allows you to look up that session's state. Most web frameworks (not just Django) will have some sort of session concept built in.

## Cookie VS session
A cookie is something that sits on the client's browser and is merely a reference to a Session which is, by default, stored in your database.
The cookie stores a random ID and doesn't store any data itself. The session uses the value in the cookie to determine which Session from the database belongs to the current browser.
This is very different from directly writing information on the cookie.

## Types:
* i) File based
* ii) Cookie based
* iii) Cache based

## Set Sesstion:
request.session['name'] = 'Jewel'

## Get Session:
* nm=request.session.get('name') # if none, no error
or
* nm=request.session[name'] # if none, raise error

## Delete session:
del request.session['name']  #Available on cookie and database
or
request.session.flush()  #All session will be deleted from all sites

## Pre-requisite:

**settings.py**
```
	INSTALLED_APPS =[
		***
		*** #Default
		'django.contrib.sessions', #Default

		***
]

MIDDLEWARE =[
		***
		*** 
		'django.contrib.sessions.middleware.SessionMiddleware', #Default

		***
]
```


**views.py
```
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
```




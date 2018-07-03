from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm,LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, get_user_model
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User

def home_page(request):
  context = {
  "title" : "Valar Morghulis",
  "Premium Content" : "Valar Dohaeris"
  }
  return render(request,"home_page.html",context)

def about_page(request):
  return render(request,"home_page.html",{})

def contact_page(request):
  contact_form = ContactForm(request.POST or None)
  content = {
  "title" : "Contact Us",
  "content" : "Valar Morghulis",
  "form" : contact_form
  }
  if contact_form.is_valid():
    print(contact_form.cleaned_data)
  return render(request,"contacts.html",content)

# def login_page(request):
#   login_form = LoginForm(request.POST or None)
#   #print(request.user.is_authenticated())
#   content = {
#   "title" : "Login",
#   "content" : "Valar Morghulis",
#   "form" : login_form
#   }
#   if login_form.is_valid():
#     print(login_form.cleaned_data)
#     print(request.user.is_authenticated())
#     username = login_form.cleaned_data.get("username")
#     password = login_form.cleaned_data.get("password")
#     user = authenticate(request, username = username,password = password)
#     #print(username + password)
#     print(user)
#     if user is not None:
#       login(request,user)
#       print(request.user.is_authenticated())
#       #content['form'] = LoginForm()
#       return redirect("/login")
#     print(request.user.is_authenticated())
#   return(render(request,"auth/login.html",content))

@csrf_protect
def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    print("User logged in")
    #print(request.user.is_authenticated())
    if form.is_valid():
        print(form.cleaned_data)
        username  = form.cleaned_data["username"]
        password  = form.cleaned_data["password"]
        #print(username+password)
        user = authenticate(username=username, password=password)
        try:
          assert user.is_active
        except AttributeError as e:
          pass
        print(user)
        #print(request.user.is_authenticated())
        if user is not None:
            print(request.user.is_authenticated())
            login(request, user)
            # Redirect to a success page.
            #context['form'] = LoginForm()
            return redirect("/")
        else:
            # Return an 'invalid login' error message.
            print("Error")

    return render(request, "auth/login.html", context)

#User = get_user_model()
def register_page(request):
  register_form = RegisterForm(request.POST or None)
  content = {
  "title" : "Login",
  "content" : "Valar Morghulis",
  "form" : register_form
  }
  if register_form.is_valid():
    print(register_form.cleaned_data)
    username = register_form.cleaned_data['username']
    email = register_form.cleaned_data['email']
    password = register_form.cleaned_data['password']
    user = User.objects.create_user(username,email,password)
    print(user)
  return(render(request,"auth/register.html",content))

def home_page_old(request):
	_html = """
		<!DOCTYPE html>
<html lang="en"><head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="https://getbootstrap.com/favicon.ico">

    <title>Starter Template for Bootstrap</title>

    <!-- Bootstrap core CSS -->
    <link href="Starter%20Template%20for%20Bootstrap_files/bootstrap.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="Starter%20Template%20for%20Bootstrap_files/starter-template.css" rel="stylesheet">
  </head>

  <body>

    <nav class="navbar navbar-expand-md navbar-dark bg-dark fixed-top">
      <a class="navbar-brand" href="#">Navbar</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarsExampleDefault" aria-controls="navbarsExampleDefault" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarsExampleDefault">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Link</a>
          </li>
          <li class="nav-item">
            <a class="nav-link disabled" href="#">Disabled</a>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="https://example.com/" id="dropdown01" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Dropdown</a>
            <div class="dropdown-menu" aria-labelledby="dropdown01">
              <a class="dropdown-item" href="#">Action</a>
              <a class="dropdown-item" href="#">Another action</a>
              <a class="dropdown-item" href="#">Something else here</a>
            </div>
          </li>
        </ul>
        <form class="form-inline my-2 my-lg-0">
          <input class="form-control mr-sm-2" placeholder="Search" aria-label="Search" type="text">
          <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
        </form>
      </div>
    </nav>

    <main role="main" class="container">

      <div class="starter-template">
        <h1>Bootstrap starter template</h1>
        <p class="lead">Use this document as a way to quickly start any new project.<br> All you get is this text and a mostly barebones HTML document.</p>
      </div>

    </main><!-- /.container -->

    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="Starter%20Template%20for%20Bootstrap_files/jquery-3.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script>window.jQuery || document.write('<script src="../../assets/js/vendor/jquery-slim.min.js"><\/script>')</script>
    <script src="Starter%20Template%20for%20Bootstrap_files/popper.js"></script>
    <script src="Starter%20Template%20for%20Bootstrap_files/bootstrap.js"></script>
 
</body></html>
	"""
	return HttpResponse(_html)
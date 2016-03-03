from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import SignUpForm, ContactForm

# Create your views here.

def home(request):
	title = 'Sign Up now'
	# if request.user.is_authenticated():
	# 	title = "Login user is %s." %(request.user)

	#Add a form
	form = SignUpForm(request.POST or None)
	context = {
		"title": title,
		"form": form
	}

	if form.is_valid():
		#form.save()
		instance = form.save(commit=False)
		# if not instance.full_name:
		# 	instance.full_name = "Prashant"

		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "psy"
		instance.full_name = full_name
		instance.save()
		context = {
			"title": "Thank you"
		}
	return render(request,'home.html', context)


def contact(request):
	title = "Contact us"
	form = ContactForm(request.POST or None)
	if form.is_valid():
		# for key, value in form.cleaned_data.iteritems():
		# 	print key, value
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")
		# print email, message, full_name
		# send_mail(subject, message, from_email, to_list, fail_silently=True)
		subject = "Site contact mail"
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, form_email]
		contact_message = "%s: %s" %(form_full_name,form_message)
		send_mail(subject, contact_message, from_email, to_email, fail_silently=False)
	
	context = {
		"form": form,
		"title": title,
	}
	return render(request,"forms.html", context)













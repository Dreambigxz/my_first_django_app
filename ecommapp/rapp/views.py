from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse
from django.views.generic import (TemplateView,
                                  CreateView,ListView,
                                  DetailView, DeleteView
                                  )
from django.views.generic.edit import FormView

from .models import Reservation
from .forms import ReservationForm

from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.

################################ CLASS BASE VIEW#################################
class indexView(TemplateView):

    template_name = 'rapp/index.html'


class Aboutview(TemplateView):

    template_name = 'rapp/about-us.html'



#
# class ReservationFormView(CreateView):
#
#     template_name = 'rapp/reservation.html'
#     form_class = ReservationForm
#     success_url = 'home'
#
#
#     def form_valid(self, form):
#
#         #get the user cleaned data's
#         expected_date= form.cleaned_data['expected_date']
#         expected_time= ''
#         total_person= ''
#
#         #request the current user posting this form
#         form.instance.user = self.request.user
#
#         #get the  necessary details for sending wmail        return HttpResponse('Form Reserverd')
#
#         email = self.request.user.email
#         name =self.request.user.full_name
#
#
#         messages='Hy {}, this is a message from the admin. Expected date is {}'.format(name, expected_date)
#
#         #send the mail
#         send_mail(
#             'Reservation Form',
#             messages,
#             'admin@foodstore.com',
#             [email],
#             fail_silently=False,
#         )
#
#         return super().form_valid(form)



######## class ReservationFormView(CreateView):
######################### FUNCTION BASE VIEW #################################

def Reservation_form(request,):

    form= ReservationForm

    reserverd = False

    if request.method == 'POST':

        form= ReservationForm(data=request.POST)

        #request the current user posting this form
        user= request.user

        email= request.user.email
        name= request.user.full_name


        print("Hello {}".format(name))
        form= ReservationForm(data=request.POST)

        if form.is_valid():

            expected_date=form.cleaned_data.get('expected_date')
            reservation_form=form.save(commit=False)
            reservation_form.user=user
            reservation_form.save()

            message_content = 'Hy {}, this is a message from the admin. Expected date is {} '.format(name, expected_date)

            send_mail(
                'Subject',
                message_content,
                'from@gmail.com',
                [email],
                fail_silently=False
            )

            reserverd= True
            messages.success(request, 'Your reservation was successful')

            return redirect('home')

    else:
        form=ReservationForm()
    return render(request, 'rapp/reservation.html', {'form':form, 'reserved': reserverd})
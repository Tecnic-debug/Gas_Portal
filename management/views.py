from django.shortcuts import render, redirect

from .models import ServiceRequest
from .forms import ServiceRequestForm

def service_request_create(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user.customer
            service_request.save()
            return redirect('service_request_list')
    else:
        form = ServiceRequestForm()
    return render(request, 'customer/request.html', {'form': form})


def service_request_list(request):
    requests = ServiceRequest.objects.filter(customer=request.user.customer)
    return render(request, 'customer/request_track.html', {'requests': requests})
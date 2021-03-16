from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib import messages


def profile(request):
    """ display the user's profile information """

    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please check if the form is valid.')
    else:
        form = UserProfileForm(instance=user_profile)

    receipts = user_profile.receipts.all()
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'receipts': receipts,
    }

    return render(request, template, context)
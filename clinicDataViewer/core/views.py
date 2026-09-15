from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import ClinicalProfile
from .forms import ClinicalProfileForm
import qrcode
import base64
from io import BytesIO
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    perfil = ClinicalProfile.objects.filter(user=request.user).first()
    qr_code_base64 = None

    if perfil:

        emergency_url = request.build_absolute_uri(f'/emergencia/{perfil.id}/')
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(emergency_url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        qr_code_base64 = base64.b64encode(buffer.getvalue()).decode()

    return render(request, 'core/dashboard.html', {
        'perfil': perfil,
        'qr_code': qr_code_base64
    })

def cadastro_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()

    return render(request, 'core/cadastro.html', {'form': form})

@login_required
def formulario_clinico_view(request):
    perfil = ClinicalProfile.objects.filter(user=request.user).first()

    if request.method == 'POST':
        form = ClinicalProfileForm(request.POST, instance=perfil)
        if form.is_valid():
            clinico = form.save(commit=False)
            clinico.user = request.user
            clinico.save()
            return redirect('dashboard')
    else:
        form = ClinicalProfileForm(instance=perfil)

    return render(request, 'core/formulario_clinico.html', {'form': form})

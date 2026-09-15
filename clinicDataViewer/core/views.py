from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from .models import ClinicalProfile
from .forms import ClinicalProfileForm
import qrcode
import base64
from io import BytesIO


from django.contrib import messages

@login_required
def dashboard_view(request):
    perfil = ClinicalProfile.objects.filter(user=request.user).first()

    if not perfil:
            return redirect('formulario_clinico')

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

def cadastro_usuario_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('formulario_clinico')
    else:
        form = UserCreationForm()

    return render(request, 'core/cadastro_usuario.html', {'form': form})

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

def emergencia_view(request, perfil_id):
    perfil = get_object_or_404(ClinicalProfile, id=perfil_id)

    if request.method == 'POST':
        pin_digitado = request.POST.get('pin')
        if pin_digitado == perfil.pin_code:
            return render(request, 'core/emergencia_dados.html', {'perfil': perfil})
        else:
            erro = "PIN incorreto. Tente novamente."
            return render(request, 'core/emergencia_pin.html', {'perfil': perfil, 'erro': erro})

    return render(request, 'core/emergencia_pin.html', {'perfil': perfil})

@login_required
def excluir_conta_view(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        return redirect('login')
    return redirect('dashboard')

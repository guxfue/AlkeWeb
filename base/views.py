from django.shortcuts import render

def inicio(request):
    return render(request, 'base/inicio.html')

def amenazas(request):
    amenazas_list = [
        {'nombre': 'Phishing', 'descripcion': 'Engaño mediante correos falsos para robar credenciales.', 'icono': '🎣', 'nivel': 'Alto'},
        {'nombre': 'Ransomware', 'descripcion': 'Malware que cifra archivos y exige rescate económico.', 'icono': '🔒', 'nivel': 'Crítico'},
        {'nombre': 'Ingeniería Social', 'descripcion': 'Manipulación psicológica para obtener información sensible.', 'icono': '🧠', 'nivel': 'Alto'},
        {'nombre': 'Ataque DDoS', 'descripcion': 'Saturación de servidores para dejarlos fuera de servicio.', 'icono': '💥', 'nivel': 'Medio'},
        {'nombre': 'SQL Injection', 'descripcion': 'Inserción de código malicioso en formularios web.', 'icono': '💉', 'nivel': 'Alto'},
        {'nombre': 'Man in the Middle', 'descripcion': 'Interceptación de comunicaciones entre dos partes.', 'icono': '🕵️', 'nivel': 'Medio'},
    ]
    return render(request, 'base/amenazas.html', {'amenazas': amenazas_list})

def consejos(request):
    consejos_list = [
        'Usa contraseñas largas y únicas para cada servicio.',
        'Activa la autenticación en dos pasos (2FA) siempre que sea posible.',
        'No abras enlaces sospechosos recibidos por correo o mensajes.',
        'Mantén tu sistema operativo y software siempre actualizados.',
        'Usa una VPN en redes Wi-Fi públicas.',
        'Realiza copias de seguridad periódicas de tus archivos importantes.',
        'Verifica el certificado SSL (candado) antes de ingresar datos en sitios web.',
        'Desconfía de solicitudes urgentes de información personal.',
    ]
    return render(request, 'base/consejos.html', {'consejos': consejos_list})

def easter_egg(request):
    return render(request, 'base/easter_egg.html')
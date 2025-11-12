from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Empleado, Venta

def inicio_personal(request):
    return render(request, 'inicio.html')

# ---------------- CLIENTES ----------------
def ver_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/ver_clientes.html', {'clientes': clientes})

def agregar_cliente(request):
    if request.method == 'POST':
        Cliente.objects.create(
            nombre=request.POST['nombre'],
            email=request.POST['email'],
            telefono=request.POST['telefono'],
            direccion=request.POST['direccion'],
            ciudad=request.POST['ciudad']
        )
        return redirect('ver_clientes')
    return render(request, 'clientes/agregar_cliente.html')

def actualizar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id_cliente=id)
    if request.method == 'POST':
        cliente.nombre = request.POST['nombre']
        cliente.email = request.POST['email']
        cliente.telefono = request.POST['telefono']
        cliente.direccion = request.POST['direccion']
        cliente.ciudad = request.POST['ciudad']
        cliente.save()
        return redirect('ver_clientes')
    return render(request, 'clientes/actualizar_cliente.html', {'cliente': cliente})

def borrar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id_cliente=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_clientes')
    return render(request, 'clientes/borrar_cliente.html', {'cliente': cliente})


# ---------------- EMPLEADOS ----------------
def ver_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados/ver_empleados.html', {'empleados': empleados})

def agregar_empleado(request):
    if request.method == 'POST':
        Empleado.objects.create(
            nombre=request.POST['nombre'],
            puesto=request.POST['puesto'],
            salario=request.POST['salario'],
            nss=request.POST['nss'],
            edad=request.POST['edad']
        )
        return redirect('ver_empleados')
    return render(request, 'empleados/agregar_empleado.html')

def actualizar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id_empleado=id)
    if request.method == 'POST':
        empleado.nombre = request.POST['nombre']
        empleado.puesto = request.POST['puesto']
        empleado.salario = request.POST['salario']
        empleado.nss = request.POST['nss']
        empleado.edad = request.POST['edad']
        empleado.save()
        return redirect('ver_empleados')
    return render(request, 'empleados/actualizar_empleado.html', {'empleado': empleado})

def borrar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id_empleado=id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('ver_empleados')
    return render(request, 'empleados/borrar_empleado.html', {'empleado': empleado})


# ---------------- VENTAS ----------------
def ver_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas/ver_ventas.html', {'ventas': ventas})

def agregar_venta(request):
    clientes = Cliente.objects.all()
    empleados = Empleado.objects.all()
    if request.method == 'POST':
        Venta.objects.create(
            fecha_venta=request.POST['fecha_venta'],
            id_cliente_id=request.POST['id_cliente'],
            id_empleado_id=request.POST['id_empleado'],
            descuento_porcentaje=request.POST['descuento_porcentaje'],
            numero_caja=request.POST['numero_caja'],
            total=request.POST['total']
        )
        return redirect('ver_ventas_personal')
    return render(request, 'ventas/agregar_venta.html', {'clientes': clientes, 'empleados': empleados})

def actualizar_venta(request, id):
    venta = get_object_or_404(Venta, id_venta=id)
    clientes = Cliente.objects.all()
    empleados = Empleado.objects.all()
    if request.method == 'POST':
        venta.fecha_venta = request.POST['fecha_venta']
        venta.id_cliente_id = request.POST['id_cliente']
        venta.id_empleado_id = request.POST['id_empleado']
        venta.descuento_porcentaje = request.POST['descuento_porcentaje']
        venta.numero_caja = request.POST['numero_caja']
        venta.total = request.POST['total']
        venta.save()
        return redirect('ver_ventas_personal')
    return render(request, 'ventas/actualizar_venta.html', {'venta': venta, 'clientes': clientes, 'empleados': empleados})

def borrar_venta(request, id):
    venta = get_object_or_404(Venta, id_venta=id)
    if request.method == 'POST':
        venta.delete()
        return redirect('ver_ventas_personal')
    return render(request, 'ventas/borrar_venta.html', {'venta': venta})

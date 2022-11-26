
from django.shortcuts import render

# Create your views here.
from crm.models import Sotrudnic, Otdel, POL_LIST


def render_spisok_sotrudnikov(request):
    fio = request.GET.get('fio', )
    otdel = request.GET.get('otdel', )
    pol = request.GET.get('pol', )

    sotrudnici = Sotrudnic.objects.all()
    otdel_list = Otdel.objects.all()
    pol_list = []

    for i in POL_LIST:
        pol_list.append({
            'id':i[0],
            'nazvanie':i[1]
        })

    if fio:
        sotrudnici = sotrudnici.filter(fio__icontains=fio)

    if otdel:
        sotrudnici = sotrudnici.filter(otdel__id=otdel)
        try:
            otdel = int(otdel)
        except Exception:
            pass

    if pol:
        sotrudnici = sotrudnici.filter(pol=pol)
        try:
            pol = int(pol)
        except Exception:
            pass

    return render(request, "crm/spisok_sotrudnicov.html", {
        "sotrudnici":sotrudnici,
        'fio':fio,
        'pol':pol,
        'otdel_list':otdel_list,
        'otdel':otdel,
        'pol_list':pol_list
    })

def render_detail_sotrudnic(request, id_sotrudnica):
    try:
        sotrudnic = Sotrudnic.objects.get(id=id_sotrudnica)
        return render(request, "crm/vibrani_sotrudnic.html", {"sotrudnic": sotrudnic})
    except Exception:
        return render(request, "crm/404.html", {})

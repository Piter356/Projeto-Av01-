from django.shortcuts import render


products_list = [
    {
        "name": "Iron man helmet",
        "price": "R$138.14", 
        "description": "Mk5 Iron Man Cosplay Capacete para Adultos e Crianças.",
        "image_url":"https://i.pinimg.com/originals/0a/15/4e/0a154e535166df96ebaf0503144055bd.jpg" ,
        "id":1,
    },
    { 
        "name":"fone bluetooth jbl",
        "price":"R$15.90",
        "description":"um fone sem fio portatil",
        "image_url":"https://images.tcdn.com.br/img/img_prod/1140357/fone_de_ouvido_bluetooth_jbl_wave_buds_preto_jblwbudsblk_3019_1_91328dd1f4fb614ea02382591ecbc110.jpg",
        "id": 2
    } 
        
]

def home_view(request):

    context = {
        "prods": products_list
    }
    return render(request, 'produtos/index.html', context)


def produtos_view(request,id):

    context = {
        "prod": products_list[id - 1]
    }
    return render(request, 'produtos/detailsprod.html', context)
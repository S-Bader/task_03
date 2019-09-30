from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
        "my_list": [{

        "restaurant_name" : "White Robata",
        "food_type" : "Japanese food"},
        {"restaurant_name" : "Chipolte",
        "food_type" : "Mexican food"},
        {"restaurant_name" : "PF Changs",
        "food_type" : "Chinese food"},]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
        "my_object": {

        "restaurant_name": "Mishmash",
        "food_type": "Lebanese food",
  

        }

    }
    return render(request, 'detail.html', context)

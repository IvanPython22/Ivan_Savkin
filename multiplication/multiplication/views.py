from django.http import HttpResponse


def multiplication_table(request):
    table = ""
    for i in range(1, 11):
        for j in range(1, 11):
            table += f"{i} x {j} = {i*j}<br>"
        table += "<br>"
    return HttpResponse(table)

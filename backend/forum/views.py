from django.http import JsonResponse


def forum(request):
    if request.method == 'GET':
        aluno = {
            'id': '1',
            'nome': 'Vitor'
        }
        return JsonResponse(aluno)

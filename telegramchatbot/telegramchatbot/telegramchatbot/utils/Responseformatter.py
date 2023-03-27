from django.http import JsonResponse


class ResponseFormatter:

    @classmethod
    def formatAndReturnResponse(cls, data, status, isUI, pageInfo=None):
        if isUI:
            response = dict()

            if pageInfo:
                response.update(dict(pageInfo=pageInfo))

            response['data'] = data
            return JsonResponse(response, safe=False, status=status)
        else:
            return JsonResponse(data, safe=False, status=status)

   
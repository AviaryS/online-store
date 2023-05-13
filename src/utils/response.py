from rest_framework.response import Response


def make_response(data, status):
    return Response(data, status=status)
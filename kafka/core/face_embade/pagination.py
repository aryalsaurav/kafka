from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    def get_paginated_response(self,data):
        return Response(
            {
                'count':self.page.paginator.count,
                'next':self.get_next_link(),
                'previous':self.get_previous_link(),
                'data':data
            }
        )




def get_paginated_queryset(queryset,request,serializer_class):
    paginator = CustomPagination()
    result_page = paginator.paginate_queryset(queryset,request)
    serializer = serializer_class(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

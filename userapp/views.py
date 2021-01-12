
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin

from rest_framework import status, mixins

from utils.response import APIResponse
from userapp.models import Book

from userapp.serializer import BookModelSerializer
# Create your views here.

# class BookAPIView(APIView):
#     def get(self, request, *args, **kwargs):
#         book_id = request.GET.get('user_id')
#         print(book_id)
#         if book_id:
#             book_obj = Book.objects.filter(pk=book_id).first()
#             data = BookModelSerializer(book_obj).data
#             return Response({
#                 "message": "查询单个成功",
#                 'result': data
#             })
#         else:
#             query_set = Book.objects.all()
#             data = BookModelSerializer(query_set, many=True).data
#             return Response({
#                 'message': '查询成功',
#                 'result': data
#             })
#
#     def post(self, request, *args, **kwargs):
#         request_data = request.data
#         print(request_data)
#         if isinstance(request_data, dict) and request_data != {}:
#             many = False
#         elif isinstance(request_data, list) and request_data != []:
#             many = True
#         else:
#             return Response({
#                 'message': '参数有误'
#             }, status=status.HTTP_400_BAD_REQUEST)
#
#         serializer = BookDeModelSerializer(data=request_data, many=many)
#         serializer.is_valid(raise_exception=True)
#         book_obj = serializer.save()
#         return Response({
#             'message': '新增图书成功',
#             'result': BookModelSerializer(book_obj, many=many).data
#         }, status=status.HTTP_200_OK)
#
#     def delete(self, request, *args, **kwargs):
#         book_id = request.data.get('user_id')
#         print(book_id)
#         if book_id:
#             ids = [book_id]
#         else:
#             ids = request.data.get('ids')
#         response = Book.objects.filter(pk__in=ids, is_delete=False).update(is_delete=True)
#         if response:
#             return Response({
#                 'message': '删除成功'
#             }, status=status.HTTP_200_OK)
#         else:
#             return Response({
#                 'message': '删除失败或者图书不存在'
#             }, status=status.HTTP_400_BAD_REQUEST)
#
#
#     def patch(self, request, *args, **kwargs):
#         request_data = request.data
#         print(request_data)
#         book_id = request.data.get('user_id')
#         print(book_id)
#         try:
#             book_obj = Book.objects.get(pk=book_id)
#         except Book.DoesNotExist:
#             return Response({
#                 'message': '修改的图书不存在'
#             }, status=status.HTTP_400_BAD_REQUEST)
#         serializer = BookDeModelSerializer(data=request_data, instance=book_obj, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer_save = serializer.save()
#         return Response({
#             'message': '修改成功',
#             'result': BookModelSerializer(serializer_save).data
#         }, status=status.HTTP_200_OK)



class BookGenericsAPIView(GenericAPIView,
                            ListModelMixin,
                            RetrieveModelMixin,
                            CreateModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    lookup_field = "id"

    # 通过ListModelMixin 视图中提供了self.list方法完成了查询所有
    # 通过RetrieveModelMixin 提供了self.retrieve查询单个
    def get(self, request, *args, **kwargs):
        if "id" in kwargs:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        response = self.create(request, *args, **kwargs)
        return APIResponse(results=response.data)

    # 全部修改
    def put(self, request, *args, **kwargs):
        response = self.update(request, *args, **kwargs)
        return APIResponse(results=response.data)

    #局部修改
    def patch(self, request, *args, **kwargs):
        response = self.partial_update(request, *args, **kwargs)
        return APIResponse(results=response.data)


    def delete(self, request, *args, **kwargs):
        response = self.destroy(request, *args, **kwargs)
        return APIResponse(results=response.data)
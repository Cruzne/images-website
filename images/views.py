from django.shortcuts import render

class FileUploadView(ListAPIView):
    parser_class = (FileUploadParser,)
    serializer_class = FileSerializer

    def get_queryset(self):
        queryset = File.objects.all()
        return queryset

    def post(self, request, *args, **kwargs):
        print(request.data)
        file_serializer = FileSerializer(data=request.data)
        print(file_serializer)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(
                file_serializer.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                file_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request):
        imageid = self.request.POST.get('id')
        f_obj = File.objects.filter(id=imageid) #File is my model name
        file_serializer = FileSerializer(f_obj, data=request.data)
        print(file_serializer)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(
                file_serializer.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                file_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request):
        imageid = self.request.POST.get('id')
        f_obj = File.objects.filter(id=imageid) #File is my model name
        if f_obj.exists():
            f_obj.delete()
            return Response(
                {
                    "Status": True,
                    "Message": "image deleted"
                }
            )
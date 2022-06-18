class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"
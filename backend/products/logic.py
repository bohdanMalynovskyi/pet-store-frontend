def get_serialized_category(model, key, serializer):
    obj = model.objects.filter(key=key).first()
    return serializer(obj, many=False).data if obj else None

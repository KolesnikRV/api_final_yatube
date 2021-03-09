from rest_framework import viewsets


class ListCreateModelViewSet(viewsets.mixins.CreateModelMixin,
                             viewsets.mixins.ListModelMixin,
                             viewsets.GenericViewSet):
    """
    A viewset that provides default `list()` and `create()` actions.
    """
    pass

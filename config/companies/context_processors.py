

from .models import GetCategory, GetLocation, AvaliableJobs
from Auth.models import AverageUser


def AdditionalInfo(request):
    """доп контекст для шаблона"""
    return {
        'Category': GetCategory(),
        'Location': GetLocation(),
        'AvaliableJobs': AvaliableJobs(),
    }


def ProperUser(request):
    """проврека на авторизованность пользователя"""
    AvgUser = None
    if request.user.is_authenticated:
        AvgUser = AverageUser.objects.filter(user=request.user).select_related().first()

    return {
        'AvgUser': AvgUser,
    }

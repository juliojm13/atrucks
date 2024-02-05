from django.http import JsonResponse
from rest_framework.decorators import api_view

from main_api.utils import (
    is_valid_msisdn,
    get_cellphone_operator_and_region,
)


@api_view(["POST"])
def process_cellphone(request):
    try:
        data = request.data
        cellphone = data.get('cellphone')
        if not cellphone:
            raise ValueError('Cellphone number is required')
        if not is_valid_msisdn(cellphone):
            raise ValueError('Invalid cellphone number')

        operator, region = get_cellphone_operator_and_region(cellphone)

        return JsonResponse(
            {
                'cellphone': cellphone,
                'operator': operator,
                'region': region,
            }
        )
    except (ValueError,) as e:
        return JsonResponse(
            {
                'error': 'Invalid input',
                'detail': str(e),
            },
            status=400,
        )

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import Order, Box
from .services import recommend_box

def health_check(request):
    return JsonResponse(
        {
            "status": "ok",
            "service": "Box Selection System",
        }
    )


@csrf_exempt
def recommend_box_view(request, order_id):
    if request.method != "POST":
        return JsonResponse(
            {
                "error": "Only POST requests are allowed."
            },
            status=405,
        )

    order = get_object_or_404(Order, id=order_id)

    recommended_box = recommend_box(
        order,
        Box.objects.all(),
    )

    if recommended_box is None:
        return JsonResponse(
            {
                "order_id": order.id,
                "recommended_box": None,
                "message": "No suitable box found.",
            },
            status=200,
        )

    return JsonResponse(
        {
            "order_id": order.id,
            "recommended_box": {
                "id": recommended_box.id,
                "name": recommended_box.name,
                "cost": float(recommended_box.cost),
            },
        }
    )
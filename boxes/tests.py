from django.test import TestCase

from .models import Product, Box, Order, OrderItem
from .services import (
    product_fits_in_box,
    calculate_order_weight,
    recommend_box,
)


class BoxSelectionTests(TestCase):

    def setUp(self):
        self.small_box = Box.objects.create(
            name="Small Box",
            internal_length=20,
            internal_width=15,
            internal_height=10,
            max_weight=3,
            cost=30,
        )

        self.medium_box = Box.objects.create(
            name="Medium Box",
            internal_length=50,
            internal_width=30,
            internal_height=20,
            max_weight=10,
            cost=50,
        )

        self.large_box = Box.objects.create(
            name="Large Box",
            internal_length=70,
            internal_width=50,
            internal_height=40,
            max_weight=20,
            cost=80,
        )

    def test_product_fits_in_box(self):
        product = Product.objects.create(
            name="Small Product",
            length=10,
            width=10,
            height=5,
            weight=1,
        )

        self.assertTrue(
            product_fits_in_box(product, self.small_box)
        )

    def test_product_does_not_fit_in_box(self):
        product = Product.objects.create(
            name="Large Product",
            length=30,
            width=20,
            height=10,
            weight=1,
        )

        self.assertFalse(
            product_fits_in_box(product, self.small_box)
        )

    def test_product_fits_after_rotation(self):
        product = Product.objects.create(
            name="Rotatable Product",
            length=30,
            width=20,
            height=10,
            weight=1,
        )

        rotation_box = Box.objects.create(
            name="Rotation Box",
            internal_length=20,
            internal_width=30,
            internal_height=15,
            max_weight=5,
            cost=40,
        )

        self.assertTrue(
            product_fits_in_box(product, rotation_box)
        )

    def test_order_weight(self):
        product = Product.objects.create(
            name="Product",
            length=10,
            width=10,
            height=10,
            weight=2,
        )

        order = Order.objects.create()

        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=3,
        )

        self.assertEqual(
            calculate_order_weight(order),
            6.0,
        )

    def test_box_rejected_when_weight_exceeds_limit(self):
        product = Product.objects.create(
            name="Heavy Product",
            length=10,
            width=10,
            height=10,
            weight=5,
        )

        order = Order.objects.create()

        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=1,
        )

        recommended_box = recommend_box(
            order,
            Box.objects.filter(id=self.small_box.id),
        )

        self.assertIsNone(recommended_box)

    def test_cheapest_suitable_box_is_selected(self):
        product = Product.objects.create(
            name="Laptop",
            length=30,
            width=20,
            height=5,
            weight=2,
        )

        order = Order.objects.create()

        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=1,
        )

        recommended_box = recommend_box(
            order,
            Box.objects.all(),
        )

        self.assertEqual(
            recommended_box,
            self.medium_box,
        )

    def test_no_suitable_box_returns_none(self):
        product = Product.objects.create(
            name="Huge Product",
            length=100,
            width=100,
            height=100,
            weight=50,
        )

        order = Order.objects.create()

        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=1,
        )

        recommended_box = recommend_box(
            order,
            Box.objects.all(),
        )

        self.assertIsNone(recommended_box)

    def test_recommend_box_api_returns_recommended_box(self):
        product = Product.objects.create(
            name="Laptop",
            length=30,
            width=20,
            height=5,
            weight=2,
        )

        order = Order.objects.create()

        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=1,
        )

        response = self.client.post(
            f"/api/orders/{order.id}/recommend-box/"
        )

        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(
            data["recommended_box"]["name"],
            "Medium Box",
        )

    def test_recommend_box_api_requires_post(self):
        order = Order.objects.create()

        response = self.client.get(
            f"/api/orders/{order.id}/recommend-box/"
        )

        self.assertEqual(response.status_code, 405)

    def test_recommend_box_api_returns_404_for_missing_order(self):
        response = self.client.post(
            "/api/orders/99999/recommend-box/"
        )

        self.assertEqual(response.status_code, 404)
    def test_health_check(self):
        response = self.client.get("/api/health/")

        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(data["status"], "ok")
        self.assertEqual(
            data["service"],
            "Box Selection System",
        )
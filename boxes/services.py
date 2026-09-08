from itertools import permutations


def product_fits_in_box(product, box):
    """
    Check whether a product can fit inside a box,
    allowing the product to be rotated.
    """

    product_dimensions = (
        float(product.length),
        float(product.width),
        float(product.height),
    )

    box_dimensions = (
        float(box.internal_length),
        float(box.internal_width),
        float(box.internal_height),
    )

    for dimensions in permutations(product_dimensions):
        if all(
            product_dimension <= box_dimension
            for product_dimension, box_dimension
            in zip(dimensions, box_dimensions)
        ):
            return True

    return False


def calculate_order_weight(order):
    """
    Calculate the total weight of all products in an order.
    """

    total_weight = 0.0

    for item in order.items.select_related("product"):
        total_weight += float(item.product.weight) * item.quantity

    return total_weight


def calculate_order_volume(order):
    """
    Calculate the total volume of all products in an order.
    """

    total_volume = 0.0

    for item in order.items.select_related("product"):
        product_volume = (
            float(item.product.length)
            * float(item.product.width)
            * float(item.product.height)
        )

        total_volume += product_volume * item.quantity

    return total_volume


def box_volume(box):
    """
    Calculate the internal volume of a box.
    """

    return (
        float(box.internal_length)
        * float(box.internal_width)
        * float(box.internal_height)
    )


def recommend_box(order, boxes):
    """
    Recommend the lowest-cost box that satisfies
    the order's weight, volume, and individual-product
    dimension requirements.
    """

    total_weight = calculate_order_weight(order)
    total_volume = calculate_order_volume(order)

    suitable_boxes = []

    for box in boxes:

        # Check weight
        if total_weight > float(box.max_weight):
            continue

        # Check total volume
        if total_volume > box_volume(box):
            continue

        # Check that every product can individually
        # fit inside the box in some orientation
        all_products_fit = True

        for item in order.items.select_related("product"):
            if not product_fits_in_box(item.product, box):
                all_products_fit = False
                break

        if not all_products_fit:
            continue

        suitable_boxes.append(box)

    if not suitable_boxes:
        return None

    # Lowest cost first.
    # If costs are equal, choose the smaller-volume box.
    suitable_boxes.sort(
        key=lambda box: (float(box.cost), box_volume(box))
    )

    return suitable_boxes[0]
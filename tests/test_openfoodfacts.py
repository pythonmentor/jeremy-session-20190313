from app.openfoodfacts import get_products_from_off

def test_get_products_from_off_returns_a_list():
    result = get_products_from_off("pizza")
    assert isinstance(result, list)

def test_get_products_from_off_returns_a_dict_in_sequence():
    result = get_products_from_off("pizza")
    assert isinstance(result[0], dict)

def test_get_products_from_off_contains_products_with_product_name():
    result = get_products_from_off("pizza")
    assert result[0].get('product_name') is not None
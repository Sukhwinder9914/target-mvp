def validate_sku(sku):
    return sku.startswith("SKU-")

def test_valid_sku():
    assert validate_sku("SKU-123") == True

def test_invalid_sku():
    assert validate_sku("ABC-123") == False

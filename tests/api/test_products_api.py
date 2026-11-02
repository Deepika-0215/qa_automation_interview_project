import allure
import requests


BASE_URL = "https://dummyjson.com"


@allure.feature("Products API")
@allure.story("Retrieve products")
def test_get_products_returns_valid_response():
    """Verify the products endpoint returns a successful, structured response."""
    with allure.step("Send GET request to the products endpoint"):
        response = requests.get(f"{BASE_URL}/products", timeout=10)

    with allure.step("Validate HTTP status code"):
        assert response.status_code == 200, (
            f"Expected status 200 but received {response.status_code}"
        )

    with allure.step("Validate JSON response structure"):
        body = response.json()
        assert "products" in body
        assert isinstance(body["products"], list)
        assert len(body["products"]) > 0

    with allure.step("Validate fields in the first product"):
        first_product = body["products"][0]
        assert "id" in first_product
        assert "title" in first_product
        assert isinstance(first_product["id"], int)
        assert isinstance(first_product["title"], str)

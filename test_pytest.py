import requests


class TestSuppliers:
    url_base = 'http://127.0.0.1:8000/api/v1/suppliers/'

    def test_get_suppliers(self):
        response = requests.get(url=self.url_base)

        assert response.status_code == 200

    def test_get_supplier(self):
        response = requests.get(url=f'{self.url_base}5/')

        assert response.status_code == 200

    def test_post_supplier(self):

        new = {
            'name':'Pepsico'
        }

        response = requests.post(url=self.url_base, data=new)

        assert response.status_code == 201
        assert response.json()['name'] == new['name']

    def test_put_supplier(self):

        update = {
            'name':'Pepsico da Amazônia'
        }
        
        # Needs to find a way to put an int number on url PK
        response = requests.put(url=f'{self.url_base}8/', data=update)

        assert response.status_code == 200
        assert response.json()['name'] == update['name']

    def test_delete_supplier(self):
        response = requests.delete(url=f'{self.url_base}8/')

        assert response.status_code == 204 and len(response.text) == 0

class TestCategories:
    url_base = 'http://127.0.0.1:8000/api/v1/categories/'

    def test_get_categories(self):
        response = requests.get(url=self.url_base)

        assert response.status_code == 200

    def test_get_category(self):
        response = requests.get(url=f'{self.url_base}5/')

        assert response.status_code == 200

    def test_post_category(self):

        new = {
            'name':'Soda'
        }

        response = requests.post(url=self.url_base, data=new)

        assert response.status_code == 201
        assert response.json()['name'] == new['name']

    def test_put_category(self):

        update = {
            'name':'Sodas'
        }
        
        # Needs to find a way to put an int number on url PK
        response = requests.put(url=f'{self.url_base}6/', data=update)

        assert response.status_code == 200
        assert response.json()['name'] == update['name']

    def test_delete_category(self):
        response = requests.delete(url=f'{self.url_base}6/')

        assert response.status_code == 204 and len(response.text) == 0

class TestProducts:
    url_base = 'http://127.0.0.1:8000/api/v1/products/'

    def test_get_products(self):
        response = requests.get(url=self.url_base)

        assert response.status_code == 200

    def test_get_product(self):
        response = requests.get(url=f'{self.url_base}6/')

        assert response.status_code == 200

    def test_post_product(self):

        new = {
            
            'name': 'SSD M2 Fast',
            'SKU': 'SSDM2FT',
            'supplier': 'Samsung',
            'category': 'Hardwares',
            'price': 299.90,
            'description': 'SSD M2 Fast',

        }

        response = requests.post(url=self.url_base, data=new)

        assert response.status_code == 201
        assert response.json()['name'] == new['name']

    def test_put_product(self):

        update = {
            
            'name': 'SSD M2 Fast Gen 2',
            "SKU": 'SSDM2FTG2',
            "supplier": 'Samsung',
            "category": 'Hardwares',
            "price": 399.90,
            "description": 'SSD M2 Fast Gen 2',

        }
        
        # Needs to find a way to put an int number on url PK
        response = requests.put(url=f'{self.url_base}8/', data=update)

        assert response.status_code == 200
        assert response.json()['name'] == update['name']

    def test_delete_product(self):
        response = requests.delete(url=f'{self.url_base}8/')

        assert response.status_code == 204 and len(response.text) == 0

class TestReviews:
    url_base = 'http://127.0.0.1:8000/api/v1/reviews/'

    def test_get_reviews(self):
        response = requests.get(url=self.url_base)

        assert response.status_code == 200

    def test_get_review(self):
        response = requests.get(url=f'{self.url_base}5/')

        assert response.status_code == 200

    def test_post_review(self):

        new = {
            'product': 6,
            'user_name': 'avahe.l',
            'email': 'avahe.l@bol.com',
            'review': 'the worst',
            'rating': 1.0
        }

        response = requests.post(url=self.url_base, data=new)

        assert response.status_code == 201
        assert response.json()['product'] == new['product']

    def test_put_review(self):

        update = {
            'product': 6,
            'user_name': 'avahe.l',
            'email': 'avahe.l@bol.com',
            'review': 'ok',
            'rating': 3.0
        }
        
        # Needs to find a way to put an int number on url PK
        response = requests.put(url=f'{self.url_base}6/', data=update)

        assert response.status_code == 200
        assert response.json()['product'] == update['product']

    def test_delete_review(self):
        response = requests.delete(url=f'{self.url_base}6/')

        assert response.status_code == 204 and len(response.text) == 0
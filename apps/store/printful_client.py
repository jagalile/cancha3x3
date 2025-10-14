# store/printful_client.py

import requests
from django.conf import settings


class PrintfulAPIClient:
    """
    Un cliente para interactuar con la API REST de Printful.
    """

    def __init__(self):
        self.api_key = settings.PRINTFUL_API_KEY
        if not self.api_key:
            raise ValueError(
                "La clave de API de Printful no está configurada en los ajustes de Django."
            )
        self.base_url = "https://api.printful.com"

    def _get_headers(self):
        """Construye los encabezados de autorización requeridos."""
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def _request(self, method, endpoint, params=None, json=None):
        """Método genérico para realizar solicitudes a la API."""
        url = f"{self.base_url}/{endpoint}"
        headers = self._get_headers()

        try:
            response = requests.request(
                method, url, headers=headers, params=params, json=json
            )
            response.raise_for_status()  # Lanza una excepción para respuestas 4xx/5xx
            return response.json()
        except requests.exceptions.RequestException as e:
            # Aquí se podría añadir un logging más robusto
            print(f"Error en la solicitud a la API de Printful: {e}")
            return None

    def get_sync_products(self, offset=0, limit=20):
        """Recupera una lista de productos sincronizados de la tienda."""
        params = {"offset": offset, "limit": limit}
        # Nota: La documentación de la API v1 usa /sync/products. La v2 puede ser diferente.
        # Para este ejemplo, se usará el endpoint de la documentación de la v1/v2.
        # El endpoint correcto para productos de la tienda es /store/products
        return self._request("GET", "store/products", params=params)

    def get_sync_product_details(self, product_id):
        """Recupera los detalles completos de un único producto sincronizado, incluidas sus variantes."""
        return self._request("GET", f"store/products/{product_id}")

    def create_order(self, payload, confirm=True):
        """Crea un nuevo pedido en Printful."""
        params = {"confirm": 1 if confirm else 0}
        return self._request("POST", "orders", params=params, json=payload)

    def setup_webhook(self, url, event_types):
        """Configura la URL del webhook y los tipos de eventos."""
        payload = {"url": url, "types": event_types}
        return self._request("POST", "webhooks", json=payload)

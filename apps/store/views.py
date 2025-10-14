# store/views.py
from django.views.generic import ListView, DetailView
from .models import Product
from .printful_client import PrintfulAPIClient


class ProductListView(ListView):
    model = Product
    template_name = "store/product_list.html"
    context_object_name = "products"
    paginate_by = 12


class ProductDetailView(DetailView):
    model = Product
    template_name = "store/product_detail.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client = PrintfulAPIClient()
        # Usamos el external_id para obtener detalles, ya que es más robusto
        product_details = client.get_sync_product_details(self.object.external_id)

        if product_details and "result" in product_details:
            context["variants"] = product_details["result"]["sync_variants"]
        else:
            context["variants"] = ""
            context["api_error"] = "No se pudieron cargar las variantes del producto."

        return context

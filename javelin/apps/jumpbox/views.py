from django.views.generic import TemplateView

class Jumpbox(TemplateView):
    template_name = "jumpbox/jumpbox.html"
    first_page = None   #determine which page to show first
    
    def get_context_data(self, **kwargs):
        context = super(Jumpbox, self).get_context_data(**kwargs)
        context["first_page"] = self.first_page
        return context
        
class PortfolioItem(TemplateView):
    def get_template_names(self):
        """ template name depends on URL parameter item_name """
        return ["jumpbox/folio/{0}.html".format(self.kwargs["item_name"])]
        
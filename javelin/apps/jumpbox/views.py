from django.views.generic import TemplateView
from django.core.mail import EmailMessage
from django.conf import settings

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
        
class SendMessage(TemplateView):
    template_name = "jumpbox/send_message.html" #status message
    
    def post(self, request, *args, **kwargs):
        """prepare a message from POST data and send it, return status message"""
        email = EmailMessage(
            subject=request.POST["subject"], 
            body=request.POST["message"],
            to=map(lambda p: p[1], settings.ADMINS),
            headers={
                "From": request.POST["name"] + " <" + settings.DEFAULT_FROM_EMAIL + '>',
                "Reply-To": request.POST["email"],
            }
        )
        context = self.get_context_data(**kwargs)
        try:
            email.send()
        except:
            context["success"] = False
        else:
            context["success"] = True
        return self.render_to_response(context)
        
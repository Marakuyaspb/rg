import os
from django.shortcuts import render

from .tasks import order_created
from .models import OrderItem, Order

from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required

from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint
from weasyprint import HTML
import logging
from django.core.mail import send_mail, send_mass_mail
from django.template import loader



logging.basicConfig(filename='mail_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

#ПРОСТО ЗАКАЗ

def order_create(request):
	order = Order(request)
	if request.method == 'POST':
		form = OrderCreateForm(request.POST)
		if form.is_valid():
			order = form.save()
			OrderItem.objects.create(order=order, first_name='first_name',	phone='phone')


		# МАНАГЕРАМ ПИСЬМО

			context = {
			  'order': order,
			}
			try:
				send_mail('Новый заказ',
					'Здавствуйте, {order.first_name}!', 
					settings.EMAIL_HOST_USER,
					['aa@madfox.io'],
					fail_silently=True,
					html_message=loader.get_template('orders/order/mail_CallMe.html').render(context)
				)
				logging.info(f"Mail to manager send successfully")
			except Exception as e:
				logging.error(f"Error sending mail to: {str(e)}")


		#ПОКУПАТЕЛЮ ПИСЬМО

			# context_2 = {
			#   'order': order,
			# }
			# try:
			# 	send_mail('Новый заказ', 
			# 		'Здравствуйте, {order.first_name}!', 
			# 		settings.EMAIL_HOST_USER,
			# 		[order.email],
			# 		fail_silently=True,
			# 		html_message=loader.get_template('orders/order/mail_CallMe.html').render(context_2)
			# 	)
			# 	logging.info(f"Mail to client send successfully to {order.email}")
			# except Exception as e:
			# 	logging.error(f"Error sending mail to {order.email}")


			return render(request, 'orders/order/created.html', {'order': order})
	else:
		form = OrderCreateForm()
	return render(request, 'orders/order/create.html', {'form': form})



@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request,
                  'orders/order/detail.html',
                  {'order': order})

# @staff_member_required
# def admin_order_pdf(request, order_id):
# 	order = get_object_or_404(Order, id=order_id)
# 	html = render_to_string('orders/order/pdf.html', {'order': order})
# 	response = HttpResponse(content_type='application/pdf')
# 	response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
# 	stylesheet_path = os.path.join(settings.STATIC_ROOT, 'css/pdf.css')
# 	weasyprint.HTML(string=html).write_pdf(response, stylesheets=[weasyprint.CSS(filename=stylesheet_path)])
# 	return response
from export import export_data_to_dict
from datetime import datetime

import requests

result = export_data_to_dict("pedidos.xlsx", "sheet1")
if len(result) == 0:
	raise RuntimeError("Sem dados")

for output in result:
	subscription = output["subscription"]
	name_split = output["nome"].split(" ")
	full_price = float(output["valor"].replace("R$", "").replace(",", "."))
	phone_number = output["telefone"]
	dd_phone = phone_number[phone_number.find("(") + 1 : phone_number.find(")")]
	phone_number = phone_number.split(") ")[1]
	result = {
		"hottok": "xxx",
		"prod": "61c0d8f3ac99c37b9d8d25b2",
		"prod_name": output["produto"],
		"off": "xxx",
		"price": full_price,
		"aff": None,
		"aff_name": None,
		"email": output["email"],
		"name": output["nome"],
		"first_name": name_split[0],
		"last_name": name_split[0],
		"doc": output["cpf_cnpj"],
		"phone_local_code": dd_phone,
		"phone_number": phone_number,
		"phone_checkout_local_code": dd_phone,
		"phone_checkout_number": phone_number,
		"address": None,
		"address_number": None,
		"address_country": "Brasil",
		"address_district": None,
		"address_comp": None,
		"address_city": None,
		"address_state": None,
		"address_zip_code": None,
		"transaction": output["pay_do_pedido"],
		"xcod": None,
		"src": None,
		"utm_source": None,
		"utm_medium": None,
		"utm_campaign": None,
		"utm_term": None,
		"utm_content": None,
		"status": "approved" if subscription == "Ativo" else "cancelled",
		"payment_engine": "evermart",
		"payment_type": output["pagamento"],
		"hotkey": None,
		"name_subscription_plan": "Plano Mensal",
		"subscriber_code": "",
		"recurrency_period": "",
		"cms_marketplace": "",
		"cms_vendor": "",
		"cms_aff": "0.00",
		"coupon_code": None,
		"callback_type": "1",
		"subscription_status": "active",
		"transaction_ext": output["pay_do_pedido"],
		"sck": None,
		# "purchase_date": datetime.strptime(output["data"], "%d/%m/%Y %H:%M"),
		# "confirmation_purchase_date": datetime.strptime(output["data"], "%d/%m/%Y %H:%M"),
		"billet_url": None,
		"currency_code_from": "BRL",
		"currency_code_from_": "BRL",
		"original_offer_price": full_price,
		"currency": "BRL",
		"signature_status": "active",
		"billet_barcode": None,
		"refusal_reason": None,
		"doc_type": "CPF",
		"full_price": full_price,
		"cms_aff_currency": "BRL",
		"amount": "1",
		"aff_cms_rate_currency": "BRL",
		"aff_cms_rate_commission": "0.00",
		"aff_cms_rate_conversion": "0",
		"installments_number": "1",
		"has_co_production": "true",
		"receiver_type": "SELLER",
		"order_bump": "false",
		"order_bump_ids": None,
		"instagram": None,
	}

	response = requests.post("webhook_link", json=result)
	print(response.status_code)
	print(response.text)
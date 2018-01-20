
from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
	validate_filters(filters)

	columns = get_columns(filters)

	res = get_result(filters)

	return columns, res

def validate_filters(filters):
	if not filters.from_date or not filters.to_date:
		frappe.throw(_("Please insert Date"))

	if filters.from_date > filters.to_date:
		frappe.throw(_("From Date must be before To Date"))


def get_columns(filters):
	columns = [
		_("Arabic Name") + ":Data:300",
		_("Date") + ":Date:100", _("Tax ID") + ":Data:140",
		_("Tax File") + ":Data:100", _("Address") + ":Data:300",  _("Tax Value") + ":Data:100",
	]

	return columns


def get_result(filters):
	data = get_data(filters)
	result = get_result_as_list(data)
	return result

def get_data(filters):
	query = """
	select 
		 `tabGL Entry`.posting_date
		,`tabSupplier`.arabic_name
		,`tabSupplier`.tax_id
		,`tabSupplier`.tax_file_number
		,`tabAddress`.address_line1  
		,(`tabGL Entry`.credit-`tabGL Entry`.debit) as credit_debit
	from 
		 `tabGL Entry`
		,`tabDynamic Link`
		,`tabAddress`
		,`tabSupplier`
	where	
			`tabDynamic Link`.link_name = `tabGL Entry`.party and
			`tabAddress`.name = `tabDynamic Link`.parent	and
			`tabGL Entry`.party = `tabSupplier`.name and
			`tabGL Entry`.account = \"WITHHOLDING TAX PAYABLE - ECS\" and
			`tabGL Entry`.posting_date >= %(from_date)s and
			`tabGL Entry`.posting_date <= %(to_date)s
	"""

	data = frappe.db.sql(query, filters, as_dict=1)

	return data


def get_result_as_list(data):
	result = []
	for d in data:
		row = [
			d.get("arabic_name"), d.get("posting_date"), d.get("tax_id"),
			d.get("tax_file_number"), d.get("address_line1"), d.get("credit_debit")
		]
		result.append(row)

	return result


from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Taxes"),
			"items": [
				{
					"type": "report",
					"name": "Tax Witholding By Period Report",
					"doctype": "GL Entry",
					"is_query_report": True,
				}
			]
		}
	]

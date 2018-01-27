// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt
// CopyRight (2) 2017 FrontLine Solutions

frappe.query_reports["Tax Witholding By Period Report"] = {
        "filters": [
                {
                    "fieldname":"from_date",
                    "label": __("From Date"),
                    "fieldtype": "Date",
                    "default": get_today(),
                    "reqd": 1
                },
                {
                    "fieldname":"to_date",
                    "label": __("To Date"),
                    "fieldtype": "Date",
                    "default": get_today(),
                    "reqd": 1
                },
                {
                    "fieldname":"bank",
                    "label": __("Bank"),
                    "fieldtype": "Data",
                    "reqd": 0
                },
                {
                    "fieldname":"branch",
                    "label": __("Branch"),
                    "fieldtype": "Data",
                    "reqd": 0
                },
                {
                    "fieldname":"check",
                    "label": __("Check No"),
                    "fieldtype": "Data",
                    "reqd": 0
                },
                {
                    "fieldname":"namozag",
                    "label": __("Namozag No"),
                    "fieldtype": "Data",
                    "reqd": 0
                }
        ]
}


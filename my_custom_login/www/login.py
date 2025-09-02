
import frappe
from frappe import _

def get_context(context):
    # context variables to use in login.html
    context.title = "Custom Login"
    context.redirect_to = frappe.local.request.args.get("redirect-to") or "/app"

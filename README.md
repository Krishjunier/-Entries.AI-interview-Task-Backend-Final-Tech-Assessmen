# =====================================================
# FRAPPE EVENT MANAGEMENT SYSTEM - COMPLETE CODE
# =====================================================

# =====================================================
# 1. APP STRUCTURE
# =====================================================
"""
event_management/
├── event_management/
│   ├── __init__.py
│   ├── hooks.py
│   ├── modules.txt
│   ├── event_management/
│   │   ├── __init__.py
│   │   └── doctype/
│   │       ├── events/
│   │       │   ├── __init__.py
│   │       │   ├── events.py
│   │       │   ├── events.js
│   │       │   └── events.json
│   │       ├── ticket/
│   │       │   ├── __init__.py
│   │       │   ├── ticket.py
│   │       │   ├── ticket.js
│   │       │   └── ticket.json
│   │       ├── ticket_sales/
│   │       │   ├── __init__.py
│   │       │   ├── ticket_sales.py
│   │       │   ├── ticket_sales.js
│   │       │   └── ticket_sales.json
│   │       └── attendee/
│   │           ├── __init__.py
│   │           ├── attendee.py
│   │           ├── attendee.js
│   │           └── attendee.json
├── setup.py
├── requirements.txt
└── README.md
"""

# =====================================================
# 2. setup.py
# =====================================================
setup_py = '''
from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\\n")

setup(
    name="event_management",
    version="0.0.1",
    description="Event Management System for Frappe",
    author="Gokul Krishnan YN",
    author_email="your.email@example.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)
'''

# =====================================================
# 3. requirements.txt
# =====================================================
requirements = '''
frappe
'''

# =====================================================
# 4. hooks.py
# =====================================================
hooks_py = '''
from . import __version__ as app_version

app_name = "event_management"
app_title = "Event Management"
app_publisher = "Gokul Krishnan YN"
app_description = "Event Management System with Ticket Sales"
app_icon = "octicon octicon-calendar"
app_color = "blue"
app_email = "your.email@example.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/event_management/css/event_management.css"
# app_include_js = "/assets/event_management/js/event_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/event_management/css/event_management.css"
# web_include_js = "/assets/event_management/js/event_management.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "event_management/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "event_management.install.before_install"
# after_install = "event_management.install.after_install"

# Desk Notifications
# -------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "event_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"event_management.tasks.all"
# 	],
# 	"daily": [
# 		"event_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"event_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"event_management.tasks.weekly"
# 	]
# 	"monthly": [
# 		"event_management.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "event_management.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "event_management.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "event_management.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]
'''

# =====================================================
# 5. modules.txt
# =====================================================
modules_txt = '''
Event Management
'''

# =====================================================
# 6. EVENTS DOCTYPE
# =====================================================

# events.json
events_json = '''{
 "actions": [],
 "allow_rename": 1,
 "autoname": "field:event_name",
 "creation": "2024-01-20 10:00:00.000000",
 "doctype": "DocType",
 "editable_grid": 1,
 "engine": "InnoDB",
 "field_order": [
  "event_name",
  "event_date",
  "event_time",
  "venue",
  "description",
  "column_break_5",
  "total_capacity",
  "available_capacity",
  "status"
 ],
 "fields": [
  {
   "fieldname": "event_name",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Event Name",
   "reqd": 1,
   "unique": 1
  },
  {
   "fieldname": "event_date",
   "fieldtype": "Date",
   "in_list_view": 1,
   "label": "Event Date",
   "reqd": 1
  },
  {
   "fieldname": "event_time",
   "fieldtype": "Time",
   "label": "Event Time"
  },
  {
   "fieldname": "venue",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Venue",
   "reqd": 1
  },
  {
   "fieldname": "description",
   "fieldtype": "Text Editor",
   "label": "Description"
  },
  {
   "fieldname": "column_break_5",
   "fieldtype": "Column Break"
  },
  {
   "fieldname": "total_capacity",
   "fieldtype": "Int",
   "label": "Total Capacity",
   "reqd": 1
  },
  {
   "fieldname": "available_capacity",
   "fieldtype": "Int",
   "label": "Available Capacity",
   "read_only": 1
  },
  {
   "fieldname": "status",
   "fieldtype": "Select",
   "label": "Status",
   "options": "Upcoming\\nOngoing\\nCompleted\\nCancelled",
   "default": "Upcoming"
  }
 ],
 "index_web_pages_for_search": 1,
 "links": [],
 "modified": "2024-01-20 10:00:00.000000",
 "modified_by": "Administrator",
 "module": "Event Management",
 "name": "Events",
 "naming_rule": "By fieldname",
 "owner": "Administrator",
 "permissions": [
  {
   "create": 1,
   "delete": 1,
   "email": 1,
   "export": 1,
   "print": 1,
   "read": 1,
   "report": 1,
   "role": "System Manager",
   "share": 1,
   "write": 1
  }
 ],
 "sort_field": "modified",
 "sort_order": "DESC",
 "states": [],
 "track_changes": 1
}'''

# events.py
events_py = '''
import frappe
from frappe.model.document import Document

class Events(Document):
    def validate(self):
        if not self.available_capacity:
            self.available_capacity = self.total_capacity
    
    def before_save(self):
        # Update status based on event date
        from datetime import datetime
        if self.event_date:
            event_date = datetime.strptime(str(self.event_date), "%Y-%m-%d").date()
            today = datetime.now().date()
            
            if event_date < today and self.status != "Cancelled":
                self.status = "Completed"
            elif event_date == today and self.status == "Upcoming":
                self.status = "Ongoing"
'''

# events.js
events_js = '''
frappe.ui.form.on('Events', {
    refresh: function(frm) {
        // Add custom buttons or functionality
        if (!frm.is_new()) {
            frm.add_custom_button(__('View Tickets'), function() {
                frappe.route_options = {"event": frm.doc.name};
                frappe.set_route("List", "Ticket");
            });
            
            frm.add_custom_button(__('View Sales'), function() {
                frappe.route_options = {"event": frm.doc.name};
                frappe.set_route("List", "Ticket Sales");
            });
        }
    },
    
    total_capacity: function(frm) {
        if (!frm.doc.available_capacity) {
            frm.set_value('available_capacity', frm.doc.total_capacity);
        }
    }
});
'''

# =====================================================
# 7. TICKET DOCTYPE
# =====================================================

# ticket.json
ticket_json = '''{
 "actions": [],
 "allow_rename": 1,
 "autoname": "format:{event}-{ticket_type}-{####}",
 "creation": "2024-01-20 10:00:00.000000",
 "doctype": "DocType",
 "editable_grid": 1,
 "engine": "InnoDB",
 "field_order": [
  "event",
  "ticket_type",
  "price",
  "column_break_3",
  "total_tickets",
  "available_tickets",
  "sold_tickets"
 ],
 "fields": [
  {
   "fieldname": "event",
   "fieldtype": "Link",
   "in_list_view": 1,
   "label": "Event",
   "options": "Events",
   "reqd": 1
  },
  {
   "fieldname": "ticket_type",
   "fieldtype": "Select",
   "in_list_view": 1,
   "label": "Ticket Type",
   "options": "Prime\\nGeneral Pass\\nVIP\\nEarly Bird\\nStudent",
   "reqd": 1
  },
  {
   "fieldname": "price",
   "fieldtype": "Currency",
   "in_list_view": 1,
   "label": "Price",
   "reqd": 1
  },
  {
   "fieldname": "column_break_3",
   "fieldtype": "Column Break"
  },
  {
   "fieldname": "total_tickets",
   "fieldtype": "Int",
   "label": "Total Tickets",
   "reqd": 1
  },
  {
   "fieldname": "available_tickets",
   "fieldtype": "Int",
   "label": "Available Tickets",
   "read_only": 1
  },
  {
   "fieldname": "sold_tickets",
   "fieldtype": "Int",
   "label": "Sold Tickets",
   "read_only": 1,
   "default": "0"
  }
 ],
 "index_web_pages_for_search": 1,
 "links": [],
 "modified": "2024-01-20 10:00:00.000000",
 "modified_by": "Administrator",
 "module": "Event Management",
 "name": "Ticket",
 "naming_rule": "Expression",
 "owner": "Administrator",
 "permissions": [
  {
   "create": 1,
   "delete": 1,
   "email": 1,
   "export": 1,
   "print": 1,
   "read": 1,
   "report": 1,
   "role": "System Manager",
   "share": 1,
   "write": 1
  }
 ],
 "sort_field": "modified",
 "sort_order": "DESC",
 "states": [],
 "track_changes": 1
}'''

# ticket.py
ticket_py = '''
import frappe
from frappe.model.document import Document

class Ticket(Document):
    def validate(self):
        if not self.available_tickets:
            self.available_tickets = self.total_tickets
        if not self.sold_tickets:
            self.sold_tickets = 0
    
    def update_stock(self, quantity, operation="subtract"):
        """Update ticket stock"""
        if operation == "subtract":
            self.available_tickets -= quantity
            self.sold_tickets += quantity
        elif operation == "add":
            self.available_tickets += quantity
            self.sold_tickets -= quantity
        
        self.save(ignore_permissions=True)
'''

# ticket.js
ticket_js = '''
frappe.ui.form.on('Ticket', {
    refresh: function(frm) {
        if (!frm.is_new()) {
            frm.add_custom_button(__('View Sales'), function() {
                frappe.route_options = {"ticket": frm.doc.name};
                frappe.set_route("List", "Ticket Sales");
            });
        }
    },
    
    total_tickets: function(frm) {
        if (!frm.doc.available_tickets) {
            frm.set_value('available_tickets', frm.doc.total_tickets);
        }
    }
});
'''

# =====================================================
# 8. TICKET SALES DOCTYPE
# =====================================================

# ticket_sales.json
ticket_sales_json = '''{
 "actions": [],
 "allow_rename": 1,
 "autoname": "format:SALE-{#####}",
 "creation": "2024-01-20 10:00:00.000000",
 "doctype": "DocType",
 "editable_grid": 1,
 "engine": "InnoDB",
 "is_submittable": 1,
 "field_order": [
  "event",
  "ticket",
  "attendee",
  "column_break_3",
  "quantity",
  "unit_price",
  "total_amount",
  "section_break_7",
  "sale_date",
  "payment_status",
  "payment_method"
 ],
 "fields": [
  {
   "fieldname": "event",
   "fieldtype": "Link",
   "in_list_view": 1,
   "label": "Event",
   "options": "Events",
   "reqd": 1
  },
  {
   "fieldname": "ticket",
   "fieldtype": "Link",
   "in_list_view": 1,
   "label": "Ticket",
   "options": "Ticket",
   "reqd": 1
  },
  {
   "fieldname": "attendee",
   "fieldtype": "Link",
   "label": "Attendee",
   "options": "Attendee",
   "reqd": 1
  },
  {
   "fieldname": "column_break_3",
   "fieldtype": "Column Break"
  },
  {
   "fieldname": "quantity",
   "fieldtype": "Int",
   "in_list_view": 1,
   "label": "Quantity",
   "reqd": 1
  },
  {
   "fieldname": "unit_price",
   "fieldtype": "Currency",
   "label": "Unit Price",
   "read_only": 1
  },
  {
   "fieldname": "total_amount",
   "fieldtype": "Currency",
   "in_list_view": 1,
   "label": "Total Amount",
   "read_only": 1
  },
  {
   "fieldname": "section_break_7",
   "fieldtype": "Section Break"
  },
  {
   "fieldname": "sale_date",
   "fieldtype": "Datetime",
   "label": "Sale Date",
   "default": "Now"
  },
  {
   "fieldname": "payment_status",
   "fieldtype": "Select",
   "label": "Payment Status",
   "options": "Pending\\nPaid\\nRefunded",
   "default": "Pending"
  },
  {
   "fieldname": "payment_method",
   "fieldtype": "Select",
   "label": "Payment Method",
   "options": "Cash\\nCredit Card\\nDebit Card\\nUPI\\nNet Banking"
  }
 ],
 "index_web_pages_for_search": 1,
 "links": [],
 "modified": "2024-01-20 10:00:00.000000",
 "modified_by": "Administrator",
 "module": "Event Management",
 "name": "Ticket Sales",
 "naming_rule": "Expression",
 "owner": "Administrator",
 "permissions": [
  {
   "create": 1,
   "delete": 1,
   "email": 1,
   "export": 1,
   "print": 1,
   "read": 1,
   "report": 1,
   "role": "System Manager",
   "share": 1,
   "submit": 1,
   "write": 1,
   "cancel": 1
  }
 ],
 "sort_field": "modified",
 "sort_order": "DESC",
 "states": [],
 "track_changes": 1
}'''

# ticket_sales.py
ticket_sales_py = '''
import frappe
from frappe.model.document import Document
from frappe import _

class TicketSales(Document):
    def validate(self):
        self.validate_ticket_availability()
        self.calculate_total_amount()
    
    def validate_ticket_availability(self):
        """Prevent overselling"""
        ticket = frappe.get_doc("Ticket", self.ticket)
        
        if ticket.available_tickets < self.quantity:
            frappe.throw(_(f"Only {ticket.available_tickets} tickets available. Cannot sell {self.quantity} tickets."))
    
    def calculate_total_amount(self):
        """Calculate total amount based on quantity and unit price"""
        ticket = frappe.get_doc("Ticket", self.ticket)
        self.unit_price = ticket.price
        self.total_amount = self.quantity * self.unit_price
    
    def on_submit(self):
        """Update stock after ticket sale"""
        ticket = frappe.get_doc("Ticket", self.ticket)
        ticket.update_stock(self.quantity, operation="subtract")
        
        # Update event capacity
        event = frappe.get_doc("Events", self.event)
        event.available_capacity -= self.quantity
        event.save(ignore_permissions=True)
    
    def on_cancel(self):
        """Restore stock when sale is cancelled"""
        ticket = frappe.get_doc("Ticket", self.ticket)
        ticket.update_stock(self.quantity, operation="add")
        
        # Restore event capacity
        event = frappe.get_doc("Events", self.event)
        event.available_capacity += self.quantity
        event.save(ignore_permissions=True)
'''

# ticket_sales.js
ticket_sales_js = '''
frappe.ui.form.on('Ticket Sales', {
    ticket: function(frm) {
        if (frm.doc.ticket) {
            frappe.db.get_value('Ticket', frm.doc.ticket, ['price', 'event', 'available_tickets'], function(r) {
                if (r) {
                    frm.set_value('unit_price', r.price);
                    frm.set_value('event', r.event);
                    
                    // Show available tickets
                    frm.set_df_property('quantity', 'description', 
                        'Available Tickets: ' + r.available_tickets);
                }
            });
        }
    },
    
    quantity: function(frm) {
        calculate_total(frm);
    },
    
    unit_price: function(frm) {
        calculate_total(frm);
    }
});

function calculate_total(frm) {
    if (frm.doc.quantity && frm.doc.unit_price) {
        frm.set_value('total_amount', frm.doc.quantity * frm.doc.unit_price);
    }
}
'''

# =====================================================
# 9. ATTENDEE DOCTYPE
# =====================================================

# attendee.json
attendee_json = '''{
 "actions": [],
 "allow_rename": 1,
 "autoname": "format:ATD-{#####}",
 "creation": "2024-01-20 10:00:00.000000",
 "doctype": "DocType",
 "editable_grid": 1,
 "engine": "InnoDB",
 "field_order": [
  "full_name",
  "email",
  "phone",
  "column_break_3",
  "company",
  "designation",
  "section_break_6",
  "address"
 ],
 "fields": [
  {
   "fieldname": "full_name",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Full Name",
   "reqd": 1
  },
  {
   "fieldname": "email",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Email",
   "options": "Email",
   "reqd": 1
  },
  {
   "fieldname": "phone",
   "fieldtype": "Data",
   "in_list_view": 1,
   "label": "Phone",
   "options": "Phone"
  },
  {
   "fieldname": "column_break_3",
   "fieldtype": "Column Break"
  },
  {
   "fieldname": "company",
   "fieldtype": "Data",
   "label": "Company"
  },
  {
   "fieldname": "designation",
   "fieldtype": "Data",
   "label": "Designation"
  },
  {
   "fieldname": "section_break_6",
   "fieldtype": "Section Break"
  },
  {
   "fieldname": "address",
   "fieldtype": "Text",
   "label": "Address"
  }
 ],
 "index_web_pages_for_search": 1,
 "links": [],
 "modified": "2024-01-20 10:00:00.000000",
 "modified_by": "Administrator",
 "module": "Event Management",
 "name": "Attendee",
 "naming_rule": "Expression",
 "owner": "Administrator",
 "permissions": [
  {
   "create": 1,
   "delete": 1,
   "email": 1,
   "export": 1,
   "print": 1,
   "read": 1,
   "report": 1,
   "role": "System Manager",
   "share": 1,
   "write": 1
  }
 ],
 "sort_field": "modified",
 "sort_order": "DESC",
 "states": []
}'''

# attendee.py
attendee_py = '''
import frappe
from frappe.model.document import Document

class Attendee(Document):
    def validate(self):
        self.validate_email()
    
    def validate_email(self):
        """Validate email format"""
        import re
        if self.email:
            pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'
            if not re.match(pattern, self.email):
                frappe.throw("Invalid email format")
'''

# attendee.js
attendee_js = '''
frappe.ui.form.on('Attendee', {
    refresh: function(frm) {
        if (!frm.is_new()) {
            frm.add_custom_button(__('View Tickets'), function() {
                frappe.route_options = {"attendee": frm.doc.name};
                frappe.set_route("List", "Ticket Sales");
            });
        }
    }
});
'''

# =====================================================
# 10. SERVER SCRIPTS (To be created via UI or exported)
# =====================================================

server_scripts = """
# These server scripts should be created via Frappe UI:
# Go to: Desk > Server Script > New Server Script

# ============================================
# Script 1: Calculate Total Amount (Validate)
# ============================================
Name: Calculate Total Amount
DocType: Ticket Sales
Event: Validate

# Script:
if doc.ticket and doc.quantity:
    ticket_doc = frappe.get_doc("Ticket", doc.ticket)
    doc.unit_price = ticket_doc.price
    doc.total_amount = doc.quantity * doc.unit_price

# ============================================
# Script 2: Prevent Overselling (Validate)
# ============================================
Name: Prevent Overselling
DocType: Ticket Sales
Event: Validate

# Script:
if doc.ticket and doc.quantity:
    ticket_doc = frappe.get_doc("Ticket", doc.ticket)
    if ticket_doc.available_tickets < doc.quantity:
        frappe.throw(f"Only {ticket_doc.available_tickets} tickets available. Cannot sell {doc.quantity} tickets.")

# ============================================
# Script 3: Stock Update (After Insert)
# ============================================
Name: Stock Update
DocType: Ticket Sales
Event: On Submit

# Script:
if doc.ticket and doc.quantity:
    ticket_doc = frappe.get_doc("Ticket", doc.ticket)
    ticket_doc.available_tickets -= doc.quantity
    ticket_doc.sold_tickets += doc.quantity
    ticket_doc.save(ignore_permissions=True)
    
    # Update event capacity
    event_doc = frappe.get_doc("Events", doc.event)
    event_doc.available_capacity -= doc.quantity
    event_doc.save(ignore_permissions=True)

# ============================================
# Script 4: Restore Stock on Cancel
# ============================================
Name: Restore Stock on Cancel
DocType: Ticket Sales
Event: On Cancel

# Script:
if doc.ticket and doc.quantity:
    ticket_doc = frappe.get_doc("Ticket", doc.ticket)
    ticket_doc.available_tickets += doc.quantity
    ticket_doc.sold_tickets -= doc.quantity
    ticket_doc.save(ignore_permissions=True)
    
    # Restore event capacity
    event_doc = frappe.get_doc("Events", doc.event)
    event_doc.available_capacity += doc.quantity
    event_doc.save(ignore_permissions=True)
"""

# =====================================================
# 11. INSTALLATION INSTRUCTIONS
# =====================================================

installation_guide = """
# INSTALLATION STEPS:

1. Create the app structure:
   cd ~/frappe-bench/apps
   bench new-app event_management
   
2. Copy all the files to their respective locations as per the structure

3. Install the app:
   cd ~/frappe-bench
   bench --site [your-site-name] install-app event_management
   
4. Create DocTypes:
   - Create each DocType using the JSON files provided
   - Or import them using bench command
   
5. Create Server Scripts via UI:
   - Go to Frappe Desk
   - Navigate to Server Script
   - Create each of the 4 server scripts mentioned above
   
6. Set Permissions:
   - Configure role permissions for each DocType
   
7. Start the server:
   bench start

# USAGE:

1. Create an Event
2. Create Ticket types for the event
3. Create Attendees
4. Create Ticket Sales
5. System will automatically:
   - Calculate total amount
   - Validate stock availability
   - Update stock after sale
   - Restore stock on cancellation
"""

print("Event Management System - Complete Code Generated!")
print("=" * 60)
print("\\nFiles structure and content created above.")
print("\\nFollow the installation guide to set up the system.")
print("\\nServer Scripts need to be created via Frappe UI.")

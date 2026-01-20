import frappe
from frappe.model.document import Document


class TicketSales(Document):
    def validate(self):
        """
        Validate the ticket sale:
        - ticket must be selected
        - quantity must be > 0
        - ensure enough tickets available
        - compute total_amount from ticket price
        """
        if not self.ticket:
            frappe.throw("Please select a Ticket")

        if not self.quantity or self.quantity <= 0:
            frappe.throw("Quantity must be greater than 0")

        # Fetch price and compute total_amount
        price = frappe.db.get_value("Ticket", self.ticket, "price") or 0
        self.total_amount = price * self.quantity

        # Check availability
        ticket = frappe.get_doc("Ticket", self.ticket)
        total_qty = ticket.total_quantity or 0
        sold_qty = ticket.tickets_sold or 0
        available = total_qty - sold_qty

        if self.quantity > available:
            frappe.throw(f"Only {available} tickets available.")

    def on_submit(self):
        """
        When a sale is submitted, increment tickets_sold and update tickets_available.
        """
        ticket = frappe.get_doc("Ticket", self.ticket)

        sold = ticket.tickets_sold or 0
        qty = self.quantity or 0
        total = ticket.total_quantity or 0

        new_sold = sold + qty

        ticket.tickets_sold = new_sold
        ticket.tickets_available = max(total - new_sold, 0)

        # Save ignoring permissions so framework processes can update the ticket record
        ticket.save(ignore_permissions=True)

    def on_cancel(self):
        """
        When a sale is cancelled, decrement tickets_sold (not below 0) and update tickets_available.
        """
        ticket = frappe.get_doc("Ticket", self.ticket)

        sold = ticket.tickets_sold or 0
        qty = self.quantity or 0
        total = ticket.total_quantity or 0

        new_sold = sold - qty
        if new_sold < 0:
            new_sold = 0

        ticket.tickets_sold = new_sold
        ticket.tickets_available = max(total - new_sold, 0)

        ticket.save(ignore_permissions=True)
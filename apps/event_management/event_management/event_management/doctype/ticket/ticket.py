import frappe
from frappe.model.document import Document


class Ticket(Document):
    """
    Ticket doctype controller ensuring tickets_available stays consistent with
    total_quantity and tickets_sold, and preventing sold > total.
    """

    def validate(self):
        total = self.total_quantity or 0
        sold = self.tickets_sold or 0

        # Prevent negative or invalid values
        if sold < 0:
            frappe.throw("tickets_sold cannot be negative")

        if total < 0:
            frappe.throw("total_quantity cannot be negative")

        if sold > total:
            frappe.throw("Tickets sold cannot exceed total quantity")

        # Keep tickets_available up-to-date
        self.tickets_available = max(total - sold, 0)

    def before_save(self):
        """
        Ensure integer/zero defaults for counts to avoid None arithmetic issues.
        """
        if self.tickets_sold is None:
            self.tickets_sold = 0
        if self.total_quantity is None:
            self.total_quantity = 0
        # tickets_available will be computed in validate, but ensure it's at least zero
        if self.tickets_available is None:
            self.tickets_available = max(self.total_quantity - self.tickets_sold, 0)
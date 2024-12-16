from queue import Queue

class TicketBookingSystem:
    def __init__(self):
        self.queue = Queue()
        self.customers_served = 0

    def add_customers(self,customers):
        self.queue.put(customers)
        print(f"{customers} has joined the queue. ")
    
    def serve_customers(self):
     if not self.queue.empty(): 
        served_customers = self.queue.get()
        self.customers_served+=1
        print(f"Serving {served_customers}.")
     else:
        print("No (customers to serve")
    
    def total_customers_served(self):
       print(f"Total customers served: {self.customers_served}")


class CinemaBookingSystem:
    def __init__(self):
        self.vip_queue = []  # Queue for VIP customers
        self.regular_queue = []  # Queue for regular customers

    # Enqueue operation for regular customers
    def enqueue_regular(self, customer_name):
        self.regular_queue.append(customer_name)
        print(f"Regular customer '{customer_name}' added to the queue.")

    # Enqueue operation for VIP customers (they are added to the front)
    def enqueue_vip(self, customer_name):
        self.vip_queue.append(customer_name)
        print(f"VIP customer '{customer_name}' added to the front of the queue.")

    # Dequeue operation: Serve customers based on priority (VIP first)
    def dequeue(self):
        if self.vip_queue:
            # Serve VIP customer first
            vip_customer = self.vip_queue.pop(0)  # FIFO for VIP customers
            print(f"Serving VIP customer: {vip_customer}")
        elif self.regular_queue:
            # If no VIP customers, serve regular customers
            regular_customer = self.regular_queue.pop(0)  # FIFO for regular customers
            print(f"Serving regular customer: {regular_customer}")
        else:
            print("No customers in the queue.")

    # Peek operation: View the first customer in the queue without serving
    def peek(self):
        if self.vip_queue:
            return f"VIP customer '{self.vip_queue[0]}' is at the front of the queue."
        elif self.regular_queue:
            return f"Regular customer '{self.regular_queue[0]}' is at the front of the queue."
        else:
            return "The queue is empty."

    # Check if there are customers in the queue
    def is_empty(self):
        return len(self.vip_queue) == 0 and len(self.regular_queue) == 0

# Example usage:
cinema_system = CinemaBookingSystem()

# Enqueue regular customers
cinema_system.enqueue_regular("Alice")
cinema_system.enqueue_regular("Bob")
cinema_system.enqueue_regular("Charlie")

# Enqueue VIP customers
cinema_system.enqueue_vip("David (VIP)")
cinema_system.enqueue_vip("Eva (VIP)")

# Peek at the first customer to be served
print(cinema_system.peek())  # Should show that a VIP customer is at the front.

# Serve customers
cinema_system.dequeue()  # Should serve David (VIP) first.
cinema_system.dequeue()  # Should serve Eva (VIP) next.
cinema_system.dequeue()  # Should serve Alice (regular).

# Add more customers
cinema_system.enqueue_vip("Frank (VIP)")  # VIP customer
cinema_system.enqueue_regular("Grace")  # Regular customer

# Serve remaining customers
cinema_system.dequeue()  # Should serve Frank (VIP).


    

   
    
 
    

    





booking = TicketBookingSystem()
booking.add_customers("Alice")
booking.add_customers("Ben")
booking.add_customers("Alfredo")

booking.serve_customers()
booking.serve_customers()

booking.total_customers_served()
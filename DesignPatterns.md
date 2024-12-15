Design Patterns Implemented
1. Factory Pattern
   - Centralizes pizza creation logic.
   - Decouples pizza instantiation from business logic.
   - Provides a consistent interface for creating different pizza types.
   - Implementation Details:
     - PizzaFactory Class: A central class that handles pizza creation.
     - Supports Margherita and Pepperoni base pizzas.
     - Easily extensible for new pizza types in the future.
2. Decorator Pattern
- Enables dynamic addition of toppings.
- Maintains a consistent interface for pizza customization.
- Allows flexible modification of pizzas by adding different toppings.
- Implementation Details:
    -  Base ToppingDecorator Class: Defines the structure for adding toppings to pizzas.
    -  Supports the following toppings: Cheese, Olives, and Mushrooms.
    -  Each topping modifies the pizza's cost and description.
3. Singleton Pattern
-  Ensures there is only one instance of the inventory manager.
-  Maintains consistent tracking of ingredient quantities.
-  Provides a global access point for inventory management.
-  Implementation Details
     - InventoryManager: A single instance manages the inventory system.
     - Tracks ingredient quantities to ensure proper stock management.
     - Thread-safe implementation ensures reliable access in multi-threaded environments.
4. Strategy Pattern
   - Encapsulates payment processing logic.
   - Allows for runtime selection of payment methods.
   - Simplifies the addition of new payment methods in the future.
   - Implementation Details
   - PaymentStrategy Interface: An abstract interface that defines common methods for payment.
   - Supports two payment methods: PayPal and Credit Card.
   - Easily extensible to support other payment types.
5. Avoiding Overengineering
  Example :
                          
                class PizzaBuilder:
                    def __init__(self):
                        self.pizza = None
                        self.size = None
                        self.crust_type = None
                        self.sauce_type = None
                        self.cheese_amount = None
                        self.cooking_temperature = None
                        self.cooking_time = None
                        self.slicing_pattern = None
                        self.packaging_type = None
                        self.delivery_instructions = None
                
                    def set_size(self, size): pass
                    def set_crust(self, crust): pass
                    def set_sauce(self, sauce): pass
                    def set_cheese(self, amount): pass
                    def set_cooking_preferences(self, temp, time): pass
                    def set_slicing(self, pattern): pass
                    def set_packaging(self, type): pass
                    def set_delivery(self, instructions): pass
   - Common Pitfalls:
       - Excessive abstraction layers: Overcomplicating the design can confuse the system and reduce clarity.
       - Unnecessary configuration options: Adding configurations that are not essential can bloat the code and lead to complexity.
       - Over-complicated class hierarchies: A deep inheritance structure can be hard to maintain and understand.
       - Premature optimization: Focusing on performance optimizations before identifying real bottlenecks.
   - Best Practices
       - Start Simple: Begin with the simplest solution and iterate as requirements evolve.
       - Add Complexity Only When Needed: Introduce new features and design patterns only when the problem demands them.
       - Focus on Maintainability: Prioritize clean, readable, and maintainable code.
       - Follow YAGNI Principle: "You Ain't Gonna Need It." Avoid adding features that are not immediately required.

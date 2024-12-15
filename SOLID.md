# SOLID Principles 
Applied SOLID Principles:
1. Single Responsibility Principle (SRP)
   - Factory's sole responsibility is creating pizza objects
   - Separates object creation from business logic

2. Open/Closed Principle (OCP)
   - New pizza types can be added without modifying factory code
   - Example: 
        { class PizzaFactory:
             @staticmethod
             def create_pizza(pizza_type: str) -> Pizza:
                 if pizza_type.lower() == "margherita":
                     return MargheritaPizza()
                 elif pizza_type.lower() == "pepperoni":
                     return PepperoniPizza() }

3.Dependency Inversion Principle (DIP)
  - High-level modules depend on Pizza abstraction
  - Clients work with abstract Pizza interface   

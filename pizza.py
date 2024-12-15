from abc import ABC, abstractmethod

# Abstract Pizza Base
class Pizza(ABC):
    @abstractmethod
    def get_cost(self) -> float:
        pass
    
    @abstractmethod
    def get_description(self) -> str:
        pass

# Concrete Pizzas
class MargheritaPizza(Pizza):
    def get_cost(self) -> float:
        return 5.0
    
    def get_description(self) -> str:
        return "Margherita Pizza"

class PepperoniPizza(Pizza):
    def get_cost(self) -> float:
        return 6.0
    
    def get_description(self) -> str:
        return "Pepperoni Pizza"

# Pizza Factory
class PizzaFactory:
    @staticmethod
    def create_pizza(pizza_type: str, inventory_manager: InventoryManager) -> Pizza:
        if pizza_type == "1" and inventory_manager.check_and_decrement("Margherita"):
            return MargheritaPizza()
        elif pizza_type == "2" and inventory_manager.check_and_decrement("Pepperoni"):
            return PepperoniPizza()
        return None

# Topping Decorator
class ToppingDecorator(Pizza):
    def __init__(self, pizza: Pizza):
        self._pizza = pizza

class CheeseTopping(ToppingDecorator):
    def get_cost(self) -> float:
        return self._pizza.get_cost() + 1.0
    
    def get_description(self) -> str:
        return f"{self._pizza.get_description()}, Extra Cheese"

class OlivesTopping(ToppingDecorator):
    def get_cost(self) -> float:
        return self._pizza.get_cost() + 0.5
    
    def get_description(self) -> str:
        return f"{self._pizza.get_description()}, Olives"

class MushroomsTopping(ToppingDecorator):
    def get_cost(self) -> float:
        return self._pizza.get_cost() + 0.7
    
    def get_description(self) -> str:
        return f"{self._pizza.get_description()}, Mushrooms"


# Singleton Pattern for Inventory
class InventoryManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.ingredients = {
                "cheese": 100,
                "olives": 100,
                "mushrooms": 100
            }
        return cls._instance
    
    def check_ingredient(self, ingredient: str) -> bool:
        return self.ingredients.get(ingredient, 0) > 0
    
    def use_ingredient(self, ingredient: str) -> None:
        if self.check_ingredient(ingredient):
            self.ingredients[ingredient] -= 1

# Strategy Pattern for Payment
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> bool:
        pass

class PayPalPayment(PaymentStrategy):
    def pay(self, amount: float) -> bool:
        print(f"Paying ${amount:.2f} using PayPal")
        return True

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float) -> bool:
        print(f"Paying ${amount:.2f} using Credit Card")
        return True

# Order Class
class Order:
    def __init__(self, payment_strategy: PaymentStrategy):
        self.payment_strategy = payment_strategy
    
    def process_order(self, pizza: Pizza) -> bool:
        amount = pizza.get_cost()
        return self.payment_strategy.pay(amount)

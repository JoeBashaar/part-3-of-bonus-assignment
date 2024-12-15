from pizza import (
    PizzaFactory,
    CheeseTopping,
    OlivesTopping,
    MushroomsTopping,
    Order,
    PayPalPayment,
    CreditCardPayment,
    InventoryManager
)

def main(): #Example usage
    pizza_factory = PizzaFactory()
    pizza = pizza_factory.create_pizza("margherita")
    pizza = CheeseTopping(pizza)
    pizza = OlivesTopping(pizza)
    print(f"Pizza: {pizza.get_description()}")
    print(f"Total Cost: ${pizza.get_cost():.2f}")
    order = Order(PayPalPayment())
    if order.process_order(pizza):
        print("Payment successful!")

if __name__ == "__main__":
    main()

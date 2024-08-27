import random
def generate_customer_data(num_customers=100):
    customer_data = []
    for cust_id in range(1, num_customers + 1):
        product_views = random.randint(1, 10) 
        purchased = random.choice([True, False])
        customer_data.append((cust_id, product_views, purchased))
    return customer_data

# Calculate the conditional probability
def calculate_conditional_probability(customer_data):
    viewed_more_than_5 = 0
    purchased_given_viewed_more_than_5 = 0
    
    # Count the number of customers who viewed the product more than 5 times
    # and the number of those who also purchased the product
    for cust_id, views, purchased in customer_data:
        if views > 5:
            viewed_more_than_5 += 1
            if purchased:
                purchased_given_viewed_more_than_5 += 1
    
    # Calculate conditional probability P(Purchased | Viewed > 5)
    if viewed_more_than_5 == 0:
        return 0
    conditional_probability = purchased_given_viewed_more_than_5 / viewed_more_than_5
    return conditional_probability

customer_data = generate_customer_data()

conditional_prob = calculate_conditional_probability(customer_data)

print(f"The conditional probability that a customer purchases a product given that they viewed it more than 5 times is: {conditional_prob:.4f}")

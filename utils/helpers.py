# Utility functions
def take_screenshot(page, filename: str):
    page.screenshot(path=f"screenshots/{filename}.png")

def generate_random_email():
    import random
    return f"test{random.randint(1000,9999)}@example.com"
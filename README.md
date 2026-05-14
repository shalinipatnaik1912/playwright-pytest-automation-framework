# Playwright Python E-commerce Automation

> End-to-end test automation framework for e-commerce applications using Playwright, Python, and Page Object Model.

## 🚀 Quick Start

# Clone and setup
git clone https://github.com/shalinipatnaik1912/playwright-pytest-automation-framework.git
cd playwright-python-ecommerce-automation

# Create virtual environment
1. python -m venv .venv
2. .venv\Scripts\activate  # Windows
3. source .venv/bin/activate  # Mac/Linux

# Install dependencies
1. pip install -r requirements.txt
2. playwright install

# Run tests
python run_tests.py

## ✨ Features

- ✅ Page Object Model design pattern
- ✅ 24 automated test cases covering login, cart, and checkout
- ✅ Automated HTML reports with screenshots
- ✅ CI/CD with GitHub Actions

## 📁 Project Structure
- **tests/** - Test files organized by functionality
- **pages/** - Page Object Model classes  
- **utils/** - Test data and helper functions
- **reports/** - HTML test reports (auto-generated)
- **run_tests.py** - Automated test runner script

## 🧪 Running Tests

# Run all tests (auto-generates report)
python run_tests.py

# Run specific test file
pytest tests/test_login.py

# Run with browser UI visible
pytest --headed

# Run smoke tests only
pytest -m smoke

## 📊 Test Coverage

| Feature | Tests | Status |
|---------|-------|--------|
| Login | 6 | ✅ |
| Inventory | 5 | ✅ |
| Cart | 5 | ✅ |
| Checkout | 6 | ✅ |
| End-to-End | 2 | ✅ |

## 🛠️ Built With

- **Playwright** - Browser automation
- **Python 3.11** - Programming language
- **Pytest** - Testing framework
- **Page Object Model** - Design pattern

⭐ Star this repo if you find it helpful!
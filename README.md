# Android Testing Framework

> Professional Appium-based testing framework for Android applications using Python, PyTest, and Page Object Model design pattern.

![Tests](https://img.shields.io/badge/tests-7%20passed-brightgreen)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Appium](https://img.shields.io/badge/appium-3.1.1-orange)
![License](https://img.shields.io/badge/license-MIT-green)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running Tests](#running-tests)
- [Test Coverage](#test-coverage)
- [Page Object Model](#page-object-model)
- [Contributing](#contributing)
- [Author](#author)

## 🎯 Overview

This project demonstrates professional mobile test automation practices using Appium and Python. It tests the Wikipedia Android application with a focus on maintainability, scalability, and clean code principles.

The framework implements the **Page Object Model (POM)** design pattern, ensuring tests are easy to maintain and understand. All tests are organized using PyTest with proper fixtures and markers for flexible test execution.

## ✨ Features

- ✅ **Page Object Model** - Clean separation of test logic and page elements
- ✅ **Explicit Waits** - Robust element handling with WebDriverWait
- ✅ **PyTest Framework** - Modern testing with fixtures and markers
- ✅ **Modular Design** - Reusable components and base classes
- ✅ **Clear Reporting** - HTML reports with detailed test results
- ✅ **CI/CD Ready** - GitHub Actions integration for automated testing
- ✅ **Professional Structure** - Industry-standard project organization

## 🛠 Tech Stack

- **Python 3.13+** - Programming language
- **Appium 3.1.1** - Mobile automation framework
- **PyTest 7.4.3** - Testing framework
- **Selenium 4.16.0** - WebDriver protocol
- **UIAutomator2** - Android automation engine

## 📁 Project Structure

```
android-testing-framework/
├── .github/
│   └── workflows/
│       └── android-tests.yml      # CI/CD pipeline configuration
├── apps/
│   └── wikipedia.apk              # App under test
├── config/
│   ├── __init__.py
│   └── capabilities.py            # Appium configuration
├── pages/
│   ├── __init__.py
│   ├── base_page.py               # Base page with common methods
│   ├── home_page.py               # Home page object
│   └── search_page.py             # Search page object
├── tests/
│   ├── __init__.py
│   ├── conftest.py                # PyTest fixtures
│   ├── test_app_launch.py         # App launch tests
│   └── test_search.py             # Search functionality tests
├── utils/
│   ├── __init__.py
│   └── driver_factory.py          # Driver management
├── reports/                       # Generated test reports
├── .gitignore
├── pytest.ini                     # PyTest configuration
├── requirements.txt               # Python dependencies
└── README.md
```

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

### Required Software

1. **Python 3.8+**
   - Download: https://www.python.org/downloads/

2. **Node.js** (for Appium)
   - Download: https://nodejs.org/

3. **Android Studio** (for Android SDK and emulator)
   - Download: https://developer.android.com/studio

4. **Java JDK 8+**
   - Included with Android Studio or download separately

### Environment Variables

Set the following environment variables:

**Windows:**
```cmd
ANDROID_HOME=C:\Users\YourName\AppData\Local\Android\Sdk
JAVA_HOME=C:\Program Files\Java\jdk-11.x.x
```

**macOS/Linux:**
```bash
export ANDROID_HOME=$HOME/Library/Android/sdk
export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk-11.x.x/Contents/Home
```

Add to PATH:
```
%ANDROID_HOME%\platform-tools
%ANDROID_HOME%\tools
%JAVA_HOME%\bin
```

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/android-testing-framework.git
cd android-testing-framework
```

### 2. Install Appium

```bash
npm install -g appium
appium driver install uiautomator2
```

Verify installation:
```bash
appium --version
```

### 3. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate
```

### 4. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 5. Set Up Android Emulator

**Using Android Studio:**
1. Open Android Studio
2. Tools → AVD Manager
3. Create Virtual Device
4. Choose: Pixel 5
5. System Image: Android 12 (API 31) or Android 11 (API 30)
6. Finish and Launch

**Verify emulator:**
```bash
adb devices
```

Expected output:
```
List of devices attached
emulator-5554    device
```

### 6. Download Wikipedia APK

- Download from: https://apkpure.com/wikipedia/org.wikipedia
- Place in `apps/` folder as `wikipedia.apk`

## 🧪 Running Tests

### Start Prerequisites

**Terminal 1 - Start Appium Server:**
```bash
appium
```

**Terminal 2 - Start Emulator** (or use Android Studio Device Manager):
```bash
emulator -avd Pixel_5_API_31
```

**Verify Connection:**
```bash
adb devices
```

### Run All Tests

```bash
# Run all tests with verbose output
pytest tests/ -v

# Run with HTML report
pytest tests/ -v --html=reports/report.html

# Run with detailed output
pytest tests/ -v -s
```

### Run Specific Tests

```bash
# Run only smoke tests
pytest -m smoke -v

# Run only search tests
pytest -m search -v

# Run specific test file
pytest tests/test_search.py -v

# Run specific test
pytest tests/test_search.py::TestSearch::test_search_returns_results -v
```

### Test Execution Options

```bash
# Stop on first failure
pytest tests/ -v -x

# Run tests in parallel (requires pytest-xdist)
pytest tests/ -v -n 2

# Show print statements
pytest tests/ -v -s

# Quiet mode (less output)
pytest tests/ -v -q
```

## 📊 Test Coverage

### Test Scenarios

**App Launch Tests (3 tests):**
- ✅ App launches successfully
- ✅ Skip onboarding screens
- ✅ Verify app package and activity

**Search Functionality Tests (4 tests):**
- ✅ Search box is displayed on home page
- ✅ Clicking search opens search screen
- ✅ Search returns results
- ✅ Search results are relevant to search term

**Total: 7 automated tests**

### Test Markers

Tests are organized with markers for flexible execution:

- `@pytest.mark.smoke` - Quick smoke tests
- `@pytest.mark.search` - Search functionality tests
- `@pytest.mark.regression` - Full regression suite (future)

## 🏗 Page Object Model

The framework uses the Page Object Model design pattern for maintainability:

### Base Page

All page objects inherit from `BasePage`, which provides common methods:

```python
class BasePage:
    def find_element(self, locator)
    def click(self, locator)
    def send_keys(self, locator, text)
    def is_displayed(self, locator)
    def get_text(self, locator)
    def wait_for_element(self, locator)
```

### Page Objects

Each screen in the app has a corresponding page object:

**HomePage:**
- `skip_onboarding()` - Skip onboarding screens
- `is_search_displayed()` - Check if search is visible
- `click_search_box()` - Open search screen
- `search_for(text)` - Complete search action

**SearchPage:**
- `is_search_input_displayed()` - Check search input
- `enter_search_text(text)` - Type search query
- `is_results_displayed()` - Check if results shown
- `get_first_result_text()` - Get first result text
- `click_first_result()` - Click first result

### Example Test

```python
def test_search_returns_results(self, driver):
    """Test that searching displays results"""
    # Arrange
    home_page = HomePage(driver)
    home_page.skip_onboarding()
    
    # Act
    search_page = home_page.click_search_box()
    search_page.enter_search_text("Python programming")
    
    # Assert
    assert search_page.is_results_displayed(), \
        "Search results should be displayed"
```

## 🔧 Configuration

### Appium Capabilities

Configuration is centralized in `config/capabilities.py`:

```python
{
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "automationName": "UiAutomator2",
    "app": "/path/to/wikipedia.apk",
    "appPackage": "org.wikipedia",
    "appActivity": "org.wikipedia.main.MainActivity",
    "noReset": False,
    "autoGrantPermissions": True
}
```

### PyTest Configuration

Settings in `pytest.ini`:
- Test discovery patterns
- HTML report configuration
- Test markers
- Logging configuration

## 🐛 Troubleshooting

### Common Issues

**1. "Connection refused" error:**
```
Solution: Make sure Appium server is running (appium)
```

**2. "No devices found":**
```
Solution: Start emulator and verify with 'adb devices'
```

**3. "App not installed":**
```
Solution: Check wikipedia.apk is in apps/ folder
Verify path in config/capabilities.py
```

**4. Import errors:**
```
Solution: Make sure virtual environment is activated
Run: pip install -r requirements.txt
```

**5. Element not found:**
```
Solution: Increase timeout in base_page.py WebDriverWait
Check element locator hasn't changed
```

## 📈 Future Enhancements

Potential improvements and additions:

- [ ] Add Article page object and tests
- [ ] Implement test data management
- [ ] Add screenshot capture on test failure
- [ ] Implement parallel test execution
- [ ] Add performance metrics collection
- [ ] Create custom PyTest plugins
- [ ] Add API testing for backend validation
- [ ] Implement visual regression testing
- [ ] Add cross-platform support (iOS)
- [ ] Docker containerization


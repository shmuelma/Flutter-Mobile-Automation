# Platform Mobile Automation with Pytest Framework

This project is a **Appium-based testing framework** designed to automate mobile applications across platforms (Android, iOS), environments (QA, staging, production), and screen flows (Login, Welcome, Profile, etc.). It’s built using **Python, Pytest, and the Page Object Model (POM)**.

---

## Features

- Page Object Model (POM) for clean and modular code
- Support for both Android and iOS platforms
- Dynamic environment support via `config/`
- Built-in test hooks (e.g., auto-screenshot on failure)
- Mock-driven test flows
- Designed for CI/CD and future cloud execution (e.g., BrowserStack)

---

## Running the Appium Server
```shell
appium --use-drivers=flutter
```

## Running the Tests
💡Important to note
Currently, the tests will not run because the locators are not optimized for the flutter application

But the tests are there and take advantage of the capabilities of pytest
# Default run (Android)
pytest tests/


## 🧠 High-Level Design

project_root/
│
├── config/
│   ├── config_loader.py         # Technology responsible Central configuration from env or .env/YAML file
│   ├── capabilities.yaml        # Capabilities for different platforms (android/ios/web)
│   ├── device_profiles.yaml     # Description of various devices (emulators, real)
│
├── constants/
│   ├── enums.py                 # Global constants (timeouts, error markers, etc.)
│   ├── login_mocks.py           # Mock Data for Login
│   ├── welcome_mocks.py         # Mock Data for Welcome
    ├── messages_mocks.py         # Mock Data for Messages
    ├── profile_mocks.py         # Mock Data for Profile
│
├── drivers/
│   └── appium_driver.py         # Building a driver based on config/capabilities
│
├── pages/
│   └── ...                      # Page Objects
│
├── tests/
│   ├── test_login.py
│   ├── test_navigation.py
│   └── ...
│
├── utils/
│   ├── wait_utils.py
│   ├── screenshot_utils.py
│   └── ...
│                      
└── conftest.py  


## 🛠️ Steps to Make It a Scalable Multi-Platform Framework & Environments

- Use environment variables like `PLATFORM` and `ENV` to control configurations  
- Adding a pytest.init file to support e2e, sanity, etc. runtime types
- Create separate config files per platform (e.g., `android_capabilities.yaml`, `ios_capabilities.yaml`)  
- Split environment profiles (e.g., `qa.yaml`, `prod.yaml`) with relevant capabilities   
- Use CLI commands like `ENV=qa PLATFORM=ios pytest` to run targeted tests and jenkins in the future 
- Add support for BrowserStack/SauceLabs via env flags (`USE_BROWSERSTACK=true`)  
- Ensure CI/CD pipelines like jenkins pass env variables to support multi-platform testing   
- Future-proofing the framework by supporting both local and remote Appium servers
  And setting up the server as part of the CI/CD prep processes  

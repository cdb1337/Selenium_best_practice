This is a short piece of code showcasing two best practices while using Selenium.

1. To use the webdriver_manager.chrome module and import ChromeDriverManager. Then use the ChromeDriverManager().install() method in order to install the latest ChromeWebDriver.
   This will spare you from having the ChromeWebDriver file and locating its path, and thus it will assure that you have the latest version installed since the Driver is installed via the IDE.
2. Usage of explicit waits using the WebDriverWait module from selenium.webdriver.support.ui. The implicit waits using time module are not a best practice since it will always add the wait time even if your program function
   doesn't need it. 

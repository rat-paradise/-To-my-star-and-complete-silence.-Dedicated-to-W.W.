class BasePage():
    def __init__(self, browser, url):
        self.browser = browser  # <-- СВЯЗЫВАЕМ с браузером
        self.url = url          # <-- ЗАПОМИНАЕМ адрес
    
    def open(self):
        self.browser.get(self.url)  # --> КОМАНДА браузеру: "Иди на этот URL!"
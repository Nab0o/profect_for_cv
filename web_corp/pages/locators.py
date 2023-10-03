from selenium.webdriver.common.by import By

class BasePageLocators():
    sbertransport_icon = (By.CSS_SELECTOR, ".Layoutstyled__Header-sc-116pork-0>a>svg")
    USER_ICON = (By.CSS_SELECTOR, ".ant-avatar")
    personal_drop_menu_locator = (By.XPATH, "//span[text()='В. А. Ямсков']")  #Для конкретного пользователя
    personal_drop_menu_go_to_client_locator = (By.XPATH, "//span[text()='Перейти в клиентское приложение']") 
    personal_drop_menu_exit_locator = (By.XPATH, "//span[text()='Выйти']")


class MainPageLocators():
    oto_monitoring_section_locator = (By.XPATH, "//*[@href='/engineers']")
    reports_section_locator = (By.XPATH, "//*[@href='/reports']")

class MonitoringPageLocators():
    monitoring_taxi_search_bar_with_text_locator = (By.XPATH, "//*[@placeholder='Поиск']")
    monitoring_taxi_search_bar_search_button_locator = (By.CSS_SELECTOR, ".anticon.anticon-search")
    monitoring_taxi_first_result_locator = (By.CSS_SELECTOR, ".Engineer_link__Djsb-")

    monitoring_humanreadebleid_in_title_of_order_details_page_locator = (By.XPATH, "//*[@href='/engineers/OrdersExecution']")
    monitoring_humanreadebleid_in_order_details_page_locator = (By.XPATH, "//div[text()='ID заявки']//following-sibling::div")
    monitoring_price_in_order_details_page_locator = (By.XPATH, "//div[text()='Стоимость']//following-sibling::div")


class LoginPageLocators():
    login_field = (By.CSS_SELECTOR, "#login-form_login")
    password_field = (By.CSS_SELECTOR, "#login-form_password")
    login_button_locator = (By.CSS_SELECTOR, "button")
    alert_about_wrong_data_locator = (By.CSS_SELECTOR, ".ant-message-error")
    alert_about_wrong_data_text_locator = (By.CSS_SELECTOR, ".ant-message-error :nth-child(2)")
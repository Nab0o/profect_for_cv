from selenium.webdriver.common.by import By

class BasePageLocators():
    sbertransport_icon = (By.XPATH, "//div[text()='projectname']")
    USER_ICON = (By.CSS_SELECTOR, ".ant-avatar")
    personal_drop_menu_locator = (By.XPATH, "//span[text()='В. А. Ямсков']")  #Для конкретного пользователя 
    personal_drop_menu_profile_locator = (By.XPATH, "//span[text()='Профиль']") 
    personal_drop_menu_my_transport_locator = (By.XPATH, "//span[text()='Мой транспорт']")
    personal_drop_menu_corp_office_locator = (By.XPATH, "//a[text()='Переход в корпоративный кабинет']")
    personal_drop_menu_exit_locator = (By.XPATH, "//span[text()='Выйти']")


class MainPageLocators():
    make_order_locator = (By.XPATH, "//span[text()='Заказать поездку']")


class LoginPageLocators():
    login_field = (By.CSS_SELECTOR, "#login-form_login")
    password_field = (By.CSS_SELECTOR, "#login-form_password")
    login_button_locator = (By.CSS_SELECTOR, "button")
    alert_about_wrong_data_locator = (By.CSS_SELECTOR, ".ant-message-notice-content")
    alert_about_wrong_data_text_locator = (By.CSS_SELECTOR, ".ant-message-notice-content .ant-message-error")
    

class OrderPassengerLocators():
    adress_1_locator = (By.CSS_SELECTOR, "#createRequest_waypoints_0_waypoint")
    adress_2_locator = (By.CSS_SELECTOR, "#createRequest_waypoints_1_waypoint")
    adress_moscow_kutuzovski_prosp_57 = (By.XPATH, "//div[text()='Кутузовский проспект, 57, Москва']")
    adress_moscow_novaya_ploshad_3 = (By.XPATH, "//div[@id='createRequest_waypoints_1_waypoint_list']//div[text()='Новая площадь, 3/4, Москва']")
    adress_moscow_big_dmitrovka_street_5_6 = (By.XPATH, "//*[@class='ant-row']//*[@class='ant-select-item-option-content']//div[text()='улица Большая Дмитровка, 5/6 ст5, Москва']")

    go_now_button_locator = (By.XPATH, "//button[@type='submit']//span[text()='Поеду сейчас']")
    taxi_section_locator = (By.XPATH, "//*[@id='createRequest_taxiClass']//div[text()='Такси']")

    go_next_from_transport_selection_section_locator = (By.XPATH, "//span[text()='Далее']")  #all transport sections

    go_next_from_taxi_section_locator = (By.XPATH, "//span[text()='Далее']")
    go_from_together_ride_option_to_individual_locator = (By.XPATH, "//span[text()='Совместная']")
    go_next_from_taxi_individual_or_together_locator = (By.XPATH, "//span[text()='Далее']")  #//*[@class='ant-btn ant-btn-primary ant-btn-block sc-kHOZwM gnAHTo']

    taxi_econom_locator = (By.XPATH, "//div[text()='Эконом']")
    taxi_comfort_locator = (By.XPATH, "//div[text()='Комфорт']")
    taxi_comfort_plus_locator = (By.XPATH, "//div[text()='Комфорт+']")
    taxi_business_locator = (By.XPATH, "//div[text()='Бизнес']")
    make_passenger_order_locator = (By.XPATH, "(//button[@type='submit']//span[text()='Заказать'])[2]")
    route_not_done_warning_locator = (By.CSS_SELECTOR, ".create_noRouteWarning__siMvL")
    taxi_economy_go_to_order_details = (By.CSS_SELECTOR, ".ant-result-subtitle :nth-child(1)")
    taxi_economy_order_details_price_locator = (By.XPATH, "//span[text()='Предварительная cтоимость']//following-sibling::span")
    taxi_economy_order_details_humanreadebleid_locator = (By.CSS_SELECTOR, ".ant-page-header-heading-title")

    OT_section_locator = (By.XPATH, "//div[text()='Общественный']")
    OT_compensation_type_travel_in_city_name_locator = (By.XPATH, "//span[text()='Компенсация поездки по городу']")      #assert что название есть
    OT_compensation_type_travel_city_to_city_name_locator = (By.XPATH, "//span[text()='Компенсация поездки по городу']")
    OT_compensation_type_one_month_bypass_name_locator = (By.XPATH, "//span[text()='Компенсация проездного документа']")

    OT_type_travel_in_city_locator = (By.XPATH, "//input[@value = 'CITY_TRIP_COMPENSATION']")      #сами радиобаттoны
    OT_type_travel_city_to_city_locator = (By.XPATH, "//input[@value = 'SUBURB_TRIP_COMPENSATION']") #//*[@value="SUBURB_TRIP_COMPENSATION"]
    OT_type_one_month_bypass_locator = (By.XPATH, "//input[@value = 'TRAVEL_CARD_COMPENSATION']")

    OT_type_drop_menu_locator = (By.CSS_SELECTOR, '#create-request_tripsInfo_0_publicTransportType') #in city
    OT_type_autobus_from_drop_menu_locator = (By.XPATH, '//*[@title="Автобус"]//*[@class="ant-select-item-option-content"]')
    OT_type_trolleybus_from_drop_menu_locator = (By.XPATH, '//*[@title="Троллейбус"]//*[@class="ant-select-item-option-content"]')
    OT_type_trum_from_drop_menu_locator = (By.XPATH, '//*[@title="Трамвай"]//*[@class="ant-select-item-option-content"]')
    OT_type_metro_from_drop_menu_locator = (By.XPATH, '//*[@title="Метро"]//*[@class="ant-select-item-option-content"]')

    OT_type_travel_city_to_city_COST_field_locator = (By.CSS_SELECTOR, '#create-request_tripsInfo_0_cost')
    OT_type_travel_city_to_city_ADD_FILE_ticket_locator = (By.CSS_SELECTOR, '#create-request_tripsInfo_0_ticket')  

    OT_city_to_city_drop_menu_locator = (By.CSS_SELECTOR, '#create-request_tripsInfo_0_publicTransportType')
    OT_type_city_to_city_autobus_choose_from_drop_menu_locator = (By.XPATH, '//*[@title="Междугородный автобус"]')

    OT_make_an_order_button_locator = (By.CSS_SELECTOR, '.ant-modal-content .ant-btn-primary')
    OT_amount_of_tickets_increase_locator = (By.CSS_SELECTOR, '.ant-input-number-handler-up')
    OT_amount_of_tickets_increase_locator = (By.CSS_SELECTOR, '.ant-input-number-handler-down')

    order_done_locator = (By.XPATH, "//div[text()='Всё получилось']")

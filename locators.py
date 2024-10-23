from selenium.webdriver.common.by import By

class UrbanRoutesLocators:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    button_taxi = (By.CLASS_NAME, "button.round")
    locator_comfort = (By.CSS_SELECTOR, "div.tcard:nth-child(5) > div:nth-child(2) > img:nth-child(1)")
    click_phone_number = (By.CSS_SELECTOR, ".np-button")
    phone_input_locator = (By.CSS_SELECTOR, "#phone")
    button_next_phone = (By.CSS_SELECTOR, ".number-picker > div:nth-child(2) > div:nth-child(1) > form:nth-child(3) > div:nth-child(2) > button:nth-child(1)")
    phone_number_code = (By.ID, "code")
    confirm_code_phone = (By.CSS_SELECTOR, "div.active:nth-child(2) > form:nth-child(3) > div:nth-child(2) > button:nth-child(1)")
    payment_method = (By.CSS_SELECTOR, ".pp-button")
    add_card = (By.CSS_SELECTOR, ".pp-plus")
    field_number_card = (By.CSS_SELECTOR, "#number")
    field_code_card = (By.CSS_SELECTOR, ".card-code-input > input:nth-child(1)")
    button_add_card = (By.CSS_SELECTOR, ".pp-buttons > button:nth-child(1)")
    close_payment_button = (By.CSS_SELECTOR, ".payment-picker > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)")
    message_console = (By.XPATH, '//*[@id="comment"]')
    request_blankets_scarves = (By.CSS_SELECTOR, "div.r-type-switch:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(2)")
    request_helado = (By.CSS_SELECTOR, "div.sub:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3)")
    request_taxi = (By.CSS_SELECTOR, ".smart-button-main")
    name_driver = (By.XPATH, "//div[@class='order-button']/following-sibling::div[1]")
    time_of_waiting = (By.CSS_SELECTOR, '.order-header-title')
    number_of_trip = (By.CSS_SELECTOR, ".number")
    detail_button = (By.CSS_SELECTOR, '#root > div > div.order.shown > div.order-body > div.order-subbody > div.order-buttons > div:nth-child(3) > button > img')
    pickup_location = (By.CSS_SELECTOR, 'div.order-details-row:nth-child(1) > div:nth-child(2) > div:nth-child(1)')
    droppoff_location = (By.CSS_SELECTOR, 'div.order-details-row:nth-child(2) > div:nth-child(2) > div:nth-child(1)')
    payment_method_locator = (By.CSS_SELECTOR, 'div.order-details-row:nth-child(3) > div:nth-child(2) > div:nth-child(1)')
    get_info_trip = (By.CSS_SELECTOR, "div.order-details-row:nth-child(4) > div:nth-child(2) > div:nth-child(2)")
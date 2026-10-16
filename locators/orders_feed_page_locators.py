from selenium.webdriver.common.by import By

ORDER_BUTTON = [By.CLASS_NAME, "OrderHistory_link__1iNby"]
COMPOSITION_HEADER = [By.XPATH, ".//p[text()='Cостав']"]
ORDER_NAME = [By. CSS_SELECTOR, "div.Modal_orderBox__1xWdi h2"]
ORDER_DATE = [By.CSS_SELECTOR, "div.Modal_orderBox__1xWdi p.text_color_inactive"]
ORDER_ID = [By.CSS_SELECTOR, "div.Modal_orderBox__1xWdi p.mb-10"]
COUNT_COMPLETED_ALL_TIME = [By.CSS_SELECTOR, "div.mb-15 p.OrderFeed_number__2MbrQ"]
COUNT_COMPLETED_TODAY = [By.XPATH, ".//div[contains(@class, 'OrderFeed_ordersData__1L6Iv')]//div[last()]/p[contains(@class, 'OrderFeed_number__2MbrQ')]"]
LAST_ORDER_FROM_ORDERS_FEED_ID = [By.CSS_SELECTOR, "p.text_type_digits-default"]
LAST_ORDER_IS_READY_ID = [By.CSS_SELECTOR, "ul.OrderFeed_orderList__cBvyi li.text_type_digits-default"]
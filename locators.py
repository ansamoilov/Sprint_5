from selenium.webdriver.common.by import By


class Locators:
    # region MainPage
    SIGN_IN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']") # кнопка "Войти в аккаунт" на главной
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']") # кнопка "Оформить заказ" на главной
    PROFILE_BUTTON_MAIN = (By.XPATH, "//p[text()='Личный Кабинет']") # кнопка "Личный кабинет" на главной
    MAKE_BURGER_HEADER = (By.XPATH, "//h1[text()='Соберите бургер']") # заголовок конструктора
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo__2D0X2')]//a") # логотип
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']") # таб "Булки"
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']") # таб "Соусы"
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']") # таб "Начинки"
    SAUCES_HEADER = (By.XPATH, "//h2[contains(text(), 'Соусы')]") # заголовок "Соусы"
    FILLINGS_HEADER = (By.XPATH, "//h2[contains(text(), 'Начинки')]") # заголовок "Начинки"
    BUNS_HEADER = (By.XPATH, "//h2[contains(text(), 'Булки')]") # заголовок "Булки"
    # endregion MainPage

    # region LogInPage
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")  # ссылка "Зарегистрироваться" на странице входа
    REGISTER_BUTTON_LOGIN_PAGE = (By.XPATH, "//button[text()='Зарегистрироваться']") # кнопка "Зарегистрироваться" на странице входа
    EMAIL_INPUT_LOGIN_PAGE = (By.XPATH, '//label[text()="Email"]/parent::div/input') # инпут почты на странице входа
    PASSWORD_INPUT_LOGIN_PAGE = (By.XPATH, '//label[text()="Пароль"]/parent::div/input') # инпут пароля на странице входа
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']") # кнопка "Войти" на странице входа
    # endregion LogInPage

    # region RegistrationPage
    NAME_INPUT = (By.XPATH, '//label[text()="Имя"]/parent::div/input') # инпут имени на странице регистрации
    EMAIL_INPUT = (By.XPATH, '//label[text()="Email"]/parent::div/input') # инпут почты на странице регистрации
    PASSWORD_INPUT = (By.XPATH, '//label[text()="Пароль"]/parent::div/input') # инпут пароля на странице регистрации
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']") # кнопка регистрации на странице регистрации
    PASSWORD_ERROR = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]") # ошибка ввода пароля на странице регистрации
    REGISTRATION_LOGIN_BUTTON = (By.XPATH, "//a[text()='Войти']") # кнопка входа на странице регистрации
    FORGOT_PASSWORD_BUTTON = (By.XPATH, "//a[text()='Восстановить пароль']") # кнопка восстановления пароля
    # endregion RegistrationPage

    # region MyProfilePage
    PROFILE_BUTTON_MY_PROFILE_PAGE = (By.XPATH, "//a[text()='Профиль']") # кнопка "Профиль" в личном кабинете
    CONSTRUCTOR_BUTTON_MY_PROFILE_PAGE = (By.XPATH, "//p[text()='Конструктор']") # кнопка "Конструктор" в личном кабинете
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(@class, 'Account_button') and text()='Выход']") # Кнопка "Выход" в личном кабинете
    # endregion MyProfilePage

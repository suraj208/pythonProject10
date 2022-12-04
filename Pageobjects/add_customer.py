from selenium.webdriver.common.by import By


class Add_Customer:
    customer_tab_xpath=(By.XPATH,'//i[@class="nav-icon far fa-user"]/following-sibling::*')
    customers_subtab_xpath=(By.XPATH,'//*[text()=" Customers"]')
    add_button_xpath=(By.XPATH,'//a[@class="btn btn-primary"]')
    email_filed_id=(By.ID,'Email')
    password_filed_id=(By.ID,'Password')
    first_name_id=(By.ID,'FirstName')
    last_name_id=(By.ID,'LastName')
    gender_male_id=(By.ID,'Gender_Male')
    gender_female_id = (By.ID, 'Gender_Female')
    dateofBirth_filed_id=(By.ID,'DateOfBirth')
    company_name_id=(By.ID,"Company")
    istax_checkbox_id=(By.ID,'IsTaxExempt')
    newsletter_hower_xpath=(By.XPATH,'//input[@class="k-input k-readonly"]')
    hower_option_1=(By.XPATH,'//li[text()="Your store name"]')
    hower_option_2=(By.XPATH,'// li[text() = "Test store 2"]')
    Vendor_dropdown_id=(By.ID,'VendorId')
    active_checkbox_id=(By.ID,'Active')
    AdminComment_id=(By.ID,'AdminComment')


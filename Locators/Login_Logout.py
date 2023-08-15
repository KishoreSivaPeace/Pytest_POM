class Login_out_Locators():
    # URL's
    testing_source = "https://curtainmatrix.co.uk/testingsource/dashboard"
    final_testing = "https://curtainmatrix.co.uk/finaltesting/dashboard"
    live = "https://blindmatrix.software/login"

    # Login page ID's
    company_name_id = "//*[@id='companyname']"
    user_name_id = "#username"
    password_id = "#password"
    login_button_id = "/html/body/app-root/main/section/lib-login/div/div/div/div/div[2]/div/form/div[""4" \
                      "]/button[1]"
    company_name = "KISHORESIVADB"
    user_name = "Automation"
    password = "965577"

    # LogOut ID's
    profile_dropdown_id = "//*[@class='nav-head']/mat-toolbar-row/div/div[2]/a[3]/a"
    logout_id = "//*[text()='Log out ']"

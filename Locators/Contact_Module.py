class Contact_Locators():
    # Add New Contact
    contact_main = "//*[@class='nav-head']/mat-toolbar-row/div/div[1]/div/a[6]"
    contact_add_button = "//*[@class='header']/div[2]/div/div[4]/button"
    add_customer_button = "//*[@class='header']/div[2]/div/div[4]/div/a[1]"
    choose_contact_type = "//*[@id='contacttypemodel']/div/div/form/div/div/div[2]/mat-form-field"
    select_contact_type = "(//*[@id='contact_choose-panel']/div/mat-option)[3]"
    next_button = "//*[@id='contacttypemodel']/div/div/form/div[3]/button[1]"
    role_field = "//*[@placeholder='Role']"
    first_name_field = "//*[@id='First Name']"
    last_name_field = "//*[@id='Last Name']"
    phone_field = "(//*[text()='Phone'])[4]/following::input[1]"
    mobile_field = "//*[@placeholder='Mobile']"
    Email_field = "(//*[text()='Email'])[2]/following::input[1]"
    default_contact_checkbox = "(//*[text()='Default Contact']/following::input[1])[1]"
    acc_ref_field = "(//*[text()='Account Ref'])[2]/following::input[1]"
    company_name_field = "//*[text()='Company Name ']/following::input[1]"
    source_field = "(//*[text()='Source'])[2]/following::div[1]"
    source_option = "//*[@class='cdk-overlay-container']/div/div/div/div/div/mat-option[3]"
    address_type_dropdown = "//*[@id='custform']/div[1]/div/div[4]/div[2]/div[1]/div/div[2]/app-dynamic-field/select"
    zipcode_field = "//*[@id='contact_zipcodepostcode']"
    zipcode_search = "//*[@id='contactDynamicform']/span/i"
    address1_field = "//*[text()='Contact Info ']/following::textarea[1]"
    address2_field = "//*[text()='Contact Info ']/following::textarea[2]"
    town_city_field = "(//*[text()='Town / City']/following::input[1])[2]"
    country_field = "(//*[@id='contactDynamicform']/select)[3]"
    state_dropdown = "//*[@id='contactDynamicform']/div/mat-form-field/div/div[1]/div/mat-select/div/div/span"
    state_option = "//*[@class='cdk-overlay-container']/div/div/div/div/div/mat-option[42]"
    email_yes_radio_button = "(//*[@name='ismarketingemails'])[1]"
    received_document_yes_radio_button = "(//*[@name='isdocumentreceived'])[1]"
    received_document_setting_button = "//*[@id='yes1']/following::i"
    quotation_checkbox = "//*[@id='dynamic0']"
    invoiced_checkbox = "//*[@id='dynamic1']"
    order_checkbox = "//*[@id='dynamic2']"
    delivery_note_checkbox = "//*[@id='dynamic3']"
    credit_note_checkbox = "//*[@id='dynamic4']"
    daily_status_checkbox = "//*[@id='dynamic5']"
    online_portal_yes_radio_button = "(//*[@name='isonlineportal'])[1]"
    set_config_option = "//*[text()='Set Configure ']"
    user_name_field = "//*[@placeholder='Enter Your Name']"
    password_field = "//*[@placeholder='Enter Your Password']"
    password_confirm_field = "//*[@placeholder='Enter Your Confirm Password']"
    contact_save_button = "//*[@id='custform']/div[2]/button[1]"

    # Add Job from Conatct
    contact_3dot = "//*[@id='cont_contact']/div/div[2]/div[2]/div[3]/div[3]/div/div/div/span"
    add_job_option = "//*[@id='cont_contact']/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[1]/div/span/app-contactlisticon/div/div/div/div/button[2]"

    # Company Tab
    company_tab = "(//*[@class='mat-tab-labels'])[2]/div[1]"
    company_acc_ref_field = "//*[@id='customform']/div[1]/div[1]/div/div[3]/div/div/div/div/div[2]/div/div[2]/app-dynamic-field/input"
    company_source_field = "//*[text()='Source']/following::mat-select[1]/div/div/span"
    company_source_search = "//*[@aria-label='dropdown search']"
    company_source_option = "//*[@class='cdk-overlay-pane']/div/div/div/mat-option[3]"
    company_phone_field = "//*[@id='customform']/div[1]/div[1]/div/div[3]/div/div/div/div/div[5]/div/div[2]/app-dynamic-field/input"
    company_email_field = "//*[@id='customform']/div[1]/div[1]/div/div[3]/div/div/div/div/div[6]/div/div[2]/app-dynamic-field/input"
    company_website_field = "//*[@id='customform']/div[1]/div[1]/div/div[3]/div/div/div/div/div[7]/div/div[2]/app-dynamic-field/input"
    company_fax_field = "//*[@id='customform']/div[1]/div[1]/div/div[3]/div/div/div/div/div[8]/div/div[2]/app-dynamic-field/input"
    company_save_button = "//*[@id='customform']/div[2]/button[1]"

    # Pricing tab
    pricing_tab = "(//*[@class='mat-tab-labels'])[2]/div[3]"
    VAT_rate_field = "//*[text()='Customer-Specific VAT Rate']/following::input[1]"
    VAT_regis_no_field = "//*[text()='VAT Registration Number']/following::input[1]"
    surcharge_field = "//*[text()='Customer Surcharge(%)']/following::input[1]"
    default_delivery_cost_field = "//*[text()='Default Delivery Cost']/following::input[1]"
    default_appointment_type_dropdown = "//*[text()='Default Appointment Type']/following::mat-form-field[1]/div/div[1]/div/mat-select/div"
    appointment_type_search = "//*[@class='cdk-overlay-container']/div/div/div/div/input"
    appointment_type_option = "//*[@class='cdk-overlay-container']/div/div/div/div/div/mat-option[2]"
    default_staff = "(//*[@class='col-xl-8 col-lg-6 col-md-8']/following::mat-select[1]/div)[2]/div[1]"
    staff_option = "//*[@class='cdk-overlay-container']/div/div/div/div/div/mat-option[2]"

    # Payment Info
    payment_info_tab = "(//*[@class='mat-tab-labels'])[2]/div[4]"
    awaiting_payment_radio_button = "(//*[@class='radiomark'])[1]"
    payment_filter_dropdown = "(//*[@class='radiomark'])[2]/following::select[1]"
    awaiting_amount_field = "//*[@id='accountonfogrid']/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[8]"
    awaiting_amount_input = "//*[@id='accountonfogrid']/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[8]/editor-cell/input"
    payment_method_dropdown = "//*[@id='accountonfogrid']/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[9]"
    payment_type_dropdown = "//*[@id='accountonfogrid']/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[10]"
    paid_date_field = "(//*[@col-id='paiddate'])[2]"
    job_status_value = "//*[@id='accountonfogrid']/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[3]"
    paid_radio_button = "(//*[@class='radiomark'])[2]"
    bulk_payment_button = "//*[text()='Bulk Payments']"
    bulk_payment_method_dropdown = "//*[@id='payment_method']"
    bulk_payment_type_dropdown = "//*[@name='paymenttype']"
    bulk_job_status_filter_dropdown = "//*[@name='jobStatus']"
    bulk_job_checkbox = "//*[@id='BulkUpdateModal']/div/div/form/div[2]/div[3]/ag-grid-angular/div/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[2]/input"
    bulk_amount = "//*[@name='amount']"
    bulk_save_button = "//*[@id='BulkUpdateModal']/div/div/form/div[3]/button[1]"
    account_info_tab = "(//*[@class='mat-tab-labels'])[3]/div[2]/div"
    add_credit_field = "//*[text()='Add Credit']/following::input[1]"
    add_credit_plus = "//*[text()='Add Credit']/following::button[1]"
    payment_info_sub_tab = "(//*[@class='mat-tab-labels'])[3]/div[1]/div"

    # Commission Tab
    commission_tab = "(//*[@class='mat-tab-labels'])[2]/div[5]"
    add_commission_button = "//*[@class='Newaddbtn']"
    commission_field = "//*[@id='commission']"
    sales_consultant_dropdown = "(//*[text()='Sales Consultant'])[2]/following::mat-form-field[1]/div"
    sales_consultant_option1 = "//*[@class='cdk-overlay-container']/div/div/div/div/mat-option[3]"
    sales_consultant_option2 = "//*[@class='cdk-overlay-container']/div/div/div/div/mat-option[2]"
    commission_product_dropdown = "(//*[text()='Product'])[2]/following::mat-form-field[1]/div"
    commission_product_option1 = "//*[@id='selectProduct']/following::mat-option[2]"
    commission_product_option2 = "//*[@id='selectProduct']/following::mat-option[3]"
    commission_product_option3 = "//*[@id='selectProduct']/following::mat-option[4]"
    commission_save_button = "//*[@class='greenbtn ng-star-inserted Newsavebtn Newsavebtn_Onchange']"
    commission_checkbox = "//*[@id='commision']/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div/div[1]"
    commission_3dot = "//*[@id='commision']/div/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[5]/div[3]/span/i"
    commission_3dot_delete = "//*[@id='commision']/div/div[6]/div/div[2]/div/app-commissionheader/div/div[3]/span"
    commission_3dot_delete_ok = "//*[@id='deletecomomnotfication']/div/div/div/div/div/button[1]"
    commission_send_email_checkbox = "//*[text()=' Send Emails to The Consultant When Placed Orders Through Trade Online Portal ']/span"

    # Documents Tab
    document_tab = "(//*[@class='mat-tab-labels'])[2]/div[8]"
    add_document_button = "//*[@class='Newaddbtn']"
    document_description_field = "//*[@name='text']"
    document_attachment_button = "//*[@id='addnotesdocform']/div[2]/div/div[2]/div/div[2]/div/input"
    document_save_button = "//*[@id='addnotesdocform']/div[3]/button[1]"
    document_complete_dropdown = "//*[@id='addnotesdocform']/div[2]/div/div[3]/div/div[2]/mat-form-field/div/div[1]/div/mat-select/div/div[1]"
    document_complete_option = "//*[text()=' No']"
    document_checkbox = "//*[@id='note']/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div[2]/div/div/div"
    document_3dot_option = "//*[@id='note']/div/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[10]/div[3]/span"
    document_3dot_delete = "//*[@id='note']/div/div[6]/div/div[2]/div/app-noteheader/div/div[3]/span"
    document_3dot_delete_ok = "//*[@id='deletecomomnotfication']/div/div/div/div/div/button[1]"

    # Product Config - Product Enable/Disable
    product_config_tab = "(//*[@class='mat-tab-labels'])[2]/div[9]"
    product_enable_disable_tab = "//*[@id='headingOne']/h5/button"
    product_enable_all_desktop = "(//*[@name='enabledesktop'])[1]"
    product_enable_all_online = "(//*[@name='enabledesktop'])[2]"
    product_enable_desktop_option1 = "//*[@id='product-enable-disble-col1']/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div[2]/app-productdesktopcheckbox/label/span"
    product_enable_online_option1 = "//*[@id='product-enable-disble-col1']/div/div[2]/div[2]/div[3]/div[2]/div/div/div[4]/div[3]/app-productononlinecheckbox/label/span"
    product_enable_desktop_option2 = "//*[@id='product-enable-disble-col2']/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div[2]/app-productdesktopcheckbox/label/span"
    product_enable_online_option2 = "//*[@id='product-enable-disble-col2']/div/div[2]/div[2]/div[3]/div[2]/div/div/div[4]/div[3]/app-productononlinecheckbox/label/span"
    product_desktop_filter1 = "(//*[@name='sellist1'])[1]"
    product_online_filter1 = "(//*[@name='sellist1'])[2]"
    product_desktop_filter2 = "(//*[@name='sellist1'])[3]"
    product_online_filter2 = "(//*[@name='sellist1'])[4]"

    # Product Config - Price Group / Materials Discount
    price_group_disc_tab = "//*[@id='headingtwo']/h5/button[1]"
    price_group_disc_add_button = "//*[@id='headingtwo']/h5/button[2]"
    price_group_disc_field = "//*[@id='discount']"
    price_group_disc_supplier_field = "(//*[text()='Supplier'])[2]/following::mat-select[1]/div/div[1]"
    price_group_disc_supplier_option1 = "//*[@class='cdk-overlay-container']/div/div/div/div/div/mat-option[2]"
    price_group_disc_supplier_option2 = "//*[@class='cdk-overlay-container']/div/div/div/div/div/mat-option[1]"
    price_group_disc_product_field = "//*[@id='pricetabledis']/div[2]/div/div/div/div[6]/mat-form-field/div/div/div/mat-select/div/div/span"
    price_group_disc_product_option = "//*[@class='cdk-overlay-container']/div/div/div/div/div/mat-option[1]"
    price_group_disc_material_field = "(//*[text()='Select Material Group'])[1]"
    price_group_disc_material_all_checkbox = "(//*[@name='selectall'])[1]"
    price_group_disc_save_button = "//*[@id='pricetabledis']/div[3]/button[1]"
    price_group_disc_row1_checkbox = "//*[@id='contactdiscount']/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[1]/div/div/div/div[2]/input"
    price_group_disc_3dot = "//*[@id='contactdiscount']/div/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[7]/div[3]/span/i"
    price_group_disc_3dot_delete = "//*[@id='contactdiscount']/div/div[6]/div/div[2]/div/app-discountheader/div/div[3]/span"
    price_group_disc_3dot_delete_ok = "//*[@id='deletecomomnotfication']/div/div/div/div/div/button[1]"

    # Product Config - Option Discount
    option_disc_tab = "//*[@id='headingthree']/h5/button"
    option_disc_add_button = "//*[@id='headingthree']/h5/button[2]"
    option_disc_field = "//*[@id='common_discount']"
    option_disc_name_dropdown = "//*[@id='dropdownMenuButton']/div"
    option_disc_name_option1 = "//*[@id='componentdiscount']/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div[1]"
    option_disc_name_option2 = "//*[@id='componentdiscount']/div/div[2]/div[2]/div[3]/div[2]/div/div/div[2]/div[1]"
    option_disc_product_field = "(//*[text()='Products'])[2]/following::span[2]"
    option_disc_product_all_checkbox = "//*[text()=' All ']"
    option_disc_save_button = "//*[@id='adddiscountform']/div[3]/button[1]"
    option_disc_row1_checkbox = "//*[@id='componentdiscount']/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[2]/div/div/div"
    option_disc_3dot = "//*[@id='componentdiscount']/div/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[8]/div[3]/span"
    option_disc_3dot_delete = "//*[@id='componentdiscount']/div/div[6]/div/div[2]/div/app-discountmultidelete/div/div[3]/span"
    option_disc_3dot_delete_ok = "//*[@id='deletecomomnotfication']/div/div/div/div/div/button[1]"

    # Product Config - Product Gross Profit
    gross_profit_tab = "//*[@id='headingfour']/h5/button"
    gross_profit_add_button = "//*[@id='headingfour']/h5/button[2]"
    gross_profit_field = "(//*[text()='Gross Profit'])[2]/following::input"
    gross_profit_product_dropdown = "(//*[text()='Product'])[4]/following::span[2]"
    gross_profit_product_option1 = "//*[@class='cdk-overlay-pane']/div/div/div/mat-option[2]"
    gross_profit_product_option2 = "//*[@class='cdk-overlay-pane']/div/div/div/mat-option[3]"
    gross_profit_price_group_dropdown = "(//*[text()='Pricing Group'])[2]/following::span[2]"
    gross_profit_price_group_all_checkbox = "//*[@class='cdk-overlay-pane']/div/div/div/div/mat-checkbox"
    gross_profit_save_button = "//*[@id='grossprofitform']/div[3]/button[1]"
    gross_profit_row1_checkbox = "//*[@id='gross']/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div[2]/div/div/div"
    gross_profit_3dot = "//*[@id='gross']/div/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[7]/div[3]/span/i"
    gross_profit_3dot_delete = "//*[@id='gross']/div/div[6]/div/div[2]/div/lib-grossprofitheadercell/div/div[3]/span"
    gross_profit_3dot_delete_ok = "//*[@id='deletecomomnotfication']/div/div/div/div/div/button[1]"

    # Online Portal Tab
    online_portal_tab = "(//*[@class='mat-tab-labels'])[2]/div[10]"
    online_portal_all_job_dropdown = "//*[@id='alljobview']"
    online_portal_discount_field = "//*[@id='discountorder']"
    online_portal_language_dropdown = "//*[@id='orderlanguage']"
    online_portal_notification_dropdown = "//*[@id='Notification']"

    # FTP Tab
    ftp_tab = "(//*[@class='mat-tab-labels'])[2]/div[11]"
    add_ftp_button = "//*[@class='Newaddbtn']"
    ftp_format_dropdown = "//*[@id='for_mat']"
    ftp_status_dropdown = "//*[@id='status']"
    ftp_hostname_field = "//*[@id='hostname']"
    ftp_username_field = "//*[@id='username1']"
    ftp_password_field = "//*[@id='password1']"
    ftp_path_field = "//*[@id='path']"
    ftp_port_field = "//*[@id='port']"
    ftp_protocol_dropdown = "//*[@id='protocol']"
    ftp_save_button = "//*[@id='ftppopup']/div/div/form/div[3]/button[1]"
    ftp_delete_icon = "//*[@id='ftpdetails']/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[10]/app-ftpdelete"
    ftp_delete_ok = "//*[@id='deletecomomnotfication']/div/div/div/div/div/button[1]"

    # Add Task From 3Dots
    lead_customer_name = "html/body/app-root/main/section/app-customer/div[1]/ul/li[1]/span"
    contact_1st_row_3dot = "//*[@id='cont_contact']/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[1]/div/span/app-contactlisticon/div/div/div/button/i"
    contact_add_task_option = "//*[@id='cont_contact']/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[1]/div/span/app-contactlisticon/div/div/div/div/button[3]"
    contact_task_date_field = "(//*[text()='Add Task'])[2]/following::input[2]"
    contact_task_repeat_button = "(//*[@id='addtaskbody']/div[1]/div/div[4]/div[2]/div/div/label/div)[2]"
    contact_task_repeat_type = "//*[@id='RecurrenceEditor']/ejs-recurrenceeditor/div/div[1]/div"
    contact_task_repeat_every_field = "//*[@id='RecurrenceEditor']/ejs-recurrenceeditor/div/div[2]/table/tbody/tr/td[1]/div/input[1]"
    contact_task_repeat_end_field = "//*[@id='RecurrenceEditor']/ejs-recurrenceeditor/div/div[5]/div[2]/span"
    contact_task_repeat_save_button = "//*[@id='RecurrenceEditor']/div/button[1]"
    contact_task_description_field = "(//*[@id='taskdescription'])[2]"
    contact_task_save_button = "(//*[@id='addtaskform']/div[4]/input)[2]"

    # Add Appointment From 3Dots
    contact_add_appointment_option = "//*[@id='cont_contact']/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[1]/div/span/app-contactlisticon/div/div/div/div/button[4]"
    contact_appointment_allday_checkbox = "//*[@id='formID2']/div/div[2]/div[1]/div/div/label/div/label/span"
    contact_appointment_repeat_button = "//*[@id='repeatflag']/div/div/label/div"
    contact_appointment_repeat_option = "//*[@id='scheduleEditForm']/div[1]/div/div[1]/div/div[1]/div/input"
    contact_appointment_repeat_every_field = "//*[@id='scheduleEditForm']/div[1]/div/div[1]/div/div[2]/table/tbody/tr/td/div/input[1]"
    contact_appointment_repeat_save_button = "//*[@id='scheduleEditForm']/div[1]/div/div[2]/button[1]"
    contact_appointment_type = "//*[text()='Appointment type ']/following::mat-select[1]"
    contact_appointment_type_option = "//*[text()='Measurer']"
    contact_appointment_staff = "//*[@id='employee']/div/div[1]/span"
    contact_appointment_staff_option = "//*[@id='employee']/div/div[2]/ul[1]/li[1]/div"
    contact_appointment_traveltime = "//*[@id='formID2']/div/div[5]/div/div[1]/div/div[1]"
    contact_appointment_status = "//*[text()='Appointment Status ']/following::div[1]"
    contact_appointment_status_option = "//*[text()=' Confirmed ']"
    contact_appointment_description_field = "//*[@id='jobDescription']"
    contact_appointment_save_button = "//*[@id='schedule_dialog_wrapper']/div[3]/button[2]"

    # Add Task From Contact Tab
    contact_1st_row = "//*[@id='cont_contact']/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div[3]/div/span/span/a"
    contact_tab_cancel_button = "//*[@id='leadcustform']/div[2]/button[2]"
    contact_tab_add_task_icon = "//*[@id='myGridcontact']/div/div[2]/div[2]/div[3]/div[3]/div/div[3]"
    contact_tab_task_date_field = "(//*[text()='Add Task'])[2]/following::input[2]"
    contact_tab_task_repeat_button = "(//*[@id='addtaskbody']/div[1]/div/div[4]/div[2]/div/div/label/div)[2]"
    contact_tab_task_repeat_type = "//*[@id='RecurrenceEditor']/ejs-recurrenceeditor/div/div[1]/div"
    contact_tab_task_repeat_every_field = "//*[@id='RecurrenceEditor']/ejs-recurrenceeditor/div/div[2]/table/tbody/tr/td[1]/div/input[1]"
    contact_tab_task_repeat_end_field = "//*[@id='RecurrenceEditor']/ejs-recurrenceeditor/div/div[5]/div[2]/span"
    contact_tab_task_repeat_save_button = "//*[@id='RecurrenceEditor']/div/button[1]"
    contact_tab_task_description_field = "(//*[@id='taskdescription'])[2]"
    contact_tab_task_save_button = "(//*[@id='addtaskform']/div[4]/input)[2]"
    contact_tab_task_cancel_button = "(//*[@id='addtaskform']/div[4]/button)[2]"


    # Add Appointment From Contact Tab
    contact_tab_add_appointment_icon = "//*[@id='myGridcontact']/div/div[2]/div[2]/div[3]/div[3]/div/div[2]"
    contact_tab_appointment_allday_checkbox = "//*[@id='formID2']/div/div[2]/div[1]/div/div/label/div/label/span"
    contact_tab_appointment_repeat_button = "//*[@id='repeatflag']/div/div/label/div"
    contact_tab_appointment_repeat_option = "//*[@id='scheduleEditForm']/div[1]/div/div[1]/div/div[1]/div/input"
    contact_tab_appointment_repeat_every_field = "//*[@id='scheduleEditForm']/div[1]/div/div[1]/div/div[2]/table/tbody/tr/td/div/input[1]"
    contact_tab_appointment_repeat_save_button = "//*[@id='scheduleEditForm']/div[1]/div/div[2]/button[1]"
    contact_tab_appointment_type = "//*[text()='Appointment type ']/following::mat-select[1]"
    contact_tab_appointment_type_option = "//*[text()='Measurer']"
    contact_tab_appointment_staff = "//*[@id='employee']/div/div[1]/span"
    contact_tab_appointment_staff_option = "//*[@id='employee']/div/div[2]/ul[1]/li[1]/div"
    contact_tab_appointment_traveltime = "//*[@id='formID2']/div/div[5]/div/div[1]/div/div[1]"
    contact_tab_appointment_status = "//*[text()='Appointment Status ']/following::div[1]"
    contact_tab_appointment_status_option = "//*[text()=' Confirmed ']"
    contact_tab_appointment_description_field = "//*[@id='jobDescription']"
    contact_tab_appointment_save_button = "//*[@id='schedule_dialog_wrapper']/div[3]/button[2]"

    # Add Contact from Contact Tab
    contact_tab_add_contact_button = "//*[text()='Add New Contact']"
    contact_tab_role_field = "//*[@placeholder='Role']"
    contact_tab_first_name_field = "(//*[@id='First Name'])"
    contact_tab_last_name_field = "(//*[@id='Last Name'])"
    contact_tab_phone_field = "(//*[text()='Phone'])[4]/following::input[1]"
    contact_tab_mobile_field = "(//*[@placeholder='Mobile'])"
    contact_tab_Email_field = "(//*[text()='Email'])[2]/following::input[1]"
    contact_tab_default_contact_checkbox = "(//*[text()='Default Contact']/following::input[1])[2]"
    contact_tab_acc_ref_field = "(//*[text()='Account Ref'])[2]/following::input[1]"
    contact_tab_address_type_dropdown = "//*[@id='custform']/div[1]/div/div[4]/div/div[1]/div/div[2]/app-dynamic-field/select"
    contact_tab_zipcode_field = "//*[@id='contact_zipcodepostcode']"
    contact_tab_zipcode_search = "//*[@id='contactDynamicform']/span/i"
    contact_tab_address1_field = "//*[text()='Contact Info ']/following::textarea[1]"
    contact_tab_address2_field = "//*[text()='Contact Info ']/following::textarea[2]"
    contact_tab_town_city_field = "(//*[text()='Town / City']/following::input[1])[2]"
    # contact_tab_country_field = "(//*[@id='contactDynamicform']/select)[3]"
    contact_tab_state_dropdown = "//*[@id='custform']/div[1]/div/div[4]/div/div[5]/div/div[2]/app-dynamic-field/div/input"
    # contact_tab_state_option = "//*[@class='cdk-overlay-container']/div/div/div/div/div/mat-option[42]"
    contact_tab_email_yes_radio_button = "(//*[@name='ismarketingemails'])[1]"
    contact_tab_received_document_yes_radio_button = "(//*[@name='isdocumentreceived'])[1]"
    contact_tab_received_document_setting_button = "//*[@id='yes1']/following::i"
    contact_tab_quotation_checkbox = "//*[@id='dynamic0']"
    contact_tab_invoiced_checkbox = "//*[@id='dynamic1']"
    contact_tab_order_checkbox = "//*[@id='dynamic2']"
    contact_tab_delivery_note_checkbox = "//*[@id='dynamic3']"
    contact_tab_credit_note_checkbox = "//*[@id='dynamic4']"
    contact_tab_daily_status_checkbox = "//*[@id='dynamic5']"
    # contact_tab_online_portal_yes_radio_button = "(//*[@name='isonlineportal'])[1]"
    # contact_tab_set_config_option = "//*[text()='Set Configure ']"
    # contact_tab_user_name_field = "//*[@placeholder='Enter Your Name']"
    # contact_tab_password_field = "//*[@placeholder='Enter Your Password']"
    # contact_tab_password_confirm_field = "//*[@placeholder='Enter Your Confirm Password']"
    contact_tab_contact_save_button = "//*[@id='custform']/div[2]/button[1]"

    # Delete Contacts
    # From Contact Tab
    contact_tab_delete_icon = "//*[@id='myGridcontact']/div/div[2]/div[2]/div[3]/div[3]/div/div[1]"
    contact_tab_delete_ok_button = "//*[@id='deletecomomnotfication']/div/div/div/div/div/button[1]"
    # From 3dots
    contact_tab_leads_customers_name = "html/body/app-root/main/section/app-customer/div[1]/ul/li[1]/span"
    contact_1st_row_3dot_icon = "//*[@id='cont_contact']/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[1]/div/span/app-contactlisticon/div/div/div/button/i"
    contact_1st_row_3dot_delete_option = "//*[@id='cont_contact']/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[1]/div/span/app-contactlisticon/div/div/div/div/button[5]"
    contact_1st_row_3dot_delete_ok_button = "//*[@id='deletecomomnotfication']/div/div/div/div/div/button[1]"

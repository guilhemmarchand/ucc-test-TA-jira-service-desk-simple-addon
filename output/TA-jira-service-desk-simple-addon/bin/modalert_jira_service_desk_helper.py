
# encoding = utf-8

def process_event(helper, *args, **kwargs):
    """
    # IMPORTANT
    # Do not remove the anchor macro:start and macro:end lines.
    # These lines are used to generate sample code. If they are
    # removed, the sample code will not be updated when configurations
    # are updated.

    [sample_code_macro:start]

    # The following example gets the alert action parameters and prints them to the log
    name = helper.get_param("name")
    helper.log_info("name={}".format(name))

    account = helper.get_param("account")
    helper.log_info("account={}".format(account))


    # The following example adds two sample events ("hello", "world")
    # and writes them to Splunk
    # NOTE: Call helper.writeevents() only once after all events
    # have been added
    helper.addevent("hello", sourcetype="jira:service_desk_alert_action")
    helper.addevent("world", sourcetype="jira:service_desk_alert_action")
    helper.writeevents(index="summary", host="localhost", source="localhost")

    # The following example gets the events that trigger the alert
    events = helper.get_events()
    for event in events:
        helper.log_info("event={}".format(event))

    # helper.settings is a dict that includes environment configuration
    # Example usage: helper.settings["server_uri"]
    helper.log_info("server_uri={}".format(helper.settings["server_uri"]))
    [sample_code_macro:end]
    """

    helper.log_info("Alert action jira_service_desk started.")

    # TODO: Implement your alert action logic here

    name = helper.get_param("name")
    helper.log_info("name={}".format(name))

    account = helper.get_param("account")
    helper.log_info("account={}".format(account))

    # Retrieve the session_key
    helper.log_debug("Get session_key.")
    session_key = helper.session_key

    import solnlib

    app = 'TA-jira-service-desk-simple-addon'
    account_cfm = solnlib.conf_manager.ConfManager(
        session_key,
        app,
        realm="__REST_CREDENTIAL__#{}#configs/conf-ta_service_desk_simple_addon_account".format(app))
    splunk_ta_account_conf = account_cfm.get_conf("ta_service_desk_simple_addon_account").get_all()
    helper.log_info("account={}".format(splunk_ta_account_conf))

    # account details
    account_details = splunk_ta_account_conf[account]

    # Get authentication type
    auth_type = account_details.get("auth_type", 0)
    helper.log_info("auth_type={}".format(auth_type))

    # Get username
    username = account_details.get("username", 0)
    helper.log_info("username={}".format(username))

    # Get passowrd
    password = account_details.get("password", 0)
    helper.log_info("password={}".format(password))

    # Get jira_url
    jira_url = account_details.get("jira_url", 0)
    helper.log_info("jira_url={}".format(jira_url))

    # Get jira_ssl_certificate_validation
    jira_ssl_certificate_validation = account_details.get("jira_ssl_certificate_validation", 0)
    helper.log_info("jira_ssl_certificate_validation={}".format(jira_ssl_certificate_validation))

    # Get jira_ssl_certificate_path
    jira_ssl_certificate_path = account_details.get("jira_ssl_certificate_path", 0)
    helper.log_info("jira_ssl_certificate_path={}".format(jira_ssl_certificate_path))

    # Get Passthrough mode
    jira_passthrough_mode = helper.get_global_setting("jira_passthrough_mode")
    helper.log_info("jira_passthrough_mode={}".format(jira_passthrough_mode))


    return 0

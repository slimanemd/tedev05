#
def ejsonnify(mymodel, myclass):
    from tedev.data.data_general import model01s
    entity = {}
    for attribute in model01s[mymodel]['fields'][myclass.entity_name]: #entity_fields[myclass.entity_name]:
        entity[attribute] = getattr(myclass, attribute)
    return entity


#
def edejsonnify(myclass, entity=None):
    if entity is not None:
        for key in entity.keys():
            if hasattr(myclass, key):
                setattr(myclass, key, entity[key])


#"slimanemd@hotmail.com"  send_email("slimanemd@hotmail.com")
def send_email(receiver_email):
    import smtplib, ssl

    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "slimanemd01@gmail.com"
    password = "Security93" #input("Type your password and press enter: ")

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        # TO DO: Send email here

        message = """\
        Subject: Inscription

        Nous avons recu votre demande d'inscription, Merci."""

        server.sendmail(sender_email, receiver_email, message)

    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()



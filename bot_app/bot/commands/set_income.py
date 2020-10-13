
def set_income(argument, command_function, update, handler_messages, context):
    if argument == None:
        print('Error: El argumento introducido por el usuario no fue válido')
    else:
        # Send the value to the DB function:
        command_function(
            user_data=update.message['chat'],
            field="relationship_income_id",
            type_data="income",
            value=argument
        )

        # Send a message informing the user:
        handler_messages.standard_message(
            update=update,
            context=context,
            message='Has añadido un ingreso por valor de',
        )
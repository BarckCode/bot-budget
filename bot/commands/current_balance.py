
def current_balance(argument, command_function, update, handler_messages, context):
    if argument == None:
        print('El argumento introducido por el usuario no fue válido')
    else:
        # Send the value to the DB function:
        command_function(data=update.message['chat'], initial_budget=argument)

        # Send a message informing the user:
        handler_messages.standard_message(
            update=update,
            context=context,
            message='Has configurado tu saldo actual en',
        )

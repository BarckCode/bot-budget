
def show_current_balance(validation, command_function, update, handler_messages, context):
    if validation == 1:
        print('Error: El usuario introdujo argumentos con el comando')
    else:
        # Obtain the current balance of the user
        current_balance = command_function(user_data=update.message['chat'])

        # Generate message for user
        message = f'Tu saldo actual es de: {current_balance}'

        # Send a message informing the user:
        handler_messages.standard_message(
            update=update,
            context=context,
            message=message,
            args=False
        )


def filter_need_args(context, handler_messages, update):
    if len(context.args) == 0:
        # Error message: Not receiving arguments
        handler_messages.get_message(
            update=update,
            message='./messages/error/no_arguments.md'
        )
    else:
        try:
            # Transform the argument into a float
            argument = float(context.args[0])

            return argument

        except ValueError:
            # Error message: Argument data type error
            handler_messages.get_message(
                update=update,
                message='./messages/error/data_type_error_messages.md'
            )

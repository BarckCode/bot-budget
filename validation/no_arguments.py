def filter_no_need_args(context, handler_messages, update):
    if len(context.args) > 0:
        # Error message: Command contains arguments
        handler_messages.get_message(
            update=update,
            message='./messages/error/no_need_arguments.md'
        )

        return 1
    else:
        return 0

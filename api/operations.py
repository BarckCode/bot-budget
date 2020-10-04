def find_value_and_replace_it(document, updater, field, value, updated_value):
    budget_object = document['budget']

    updater(
        field_to_search='_id',
        value_to_search=document['_id'],
        field_to_replace=field,
        value_to_replace=-budget_object[value]
    )

    updater(
        field_to_search='_id',
        value_to_search=document['_id'],
        field_to_replace=field,
        value_to_replace=float(updated_value)
    )


def calculate_current_balance(data, search_function, user_document):
        user_id = data.id

        income_document = search_function(
            field="relationship_income_id",
            value=user_id
        )


        expenses_document = search_function(
            field="relationship_expense_id",
            value=user_id
        )


        initial_budget_object = user_document['budget']
        initial_budget = initial_budget_object['initial_budget']
        income_list = income_document['income']
        expense_list = expenses_document['expenses']

        income = 0
        for i in income_list:
            income += float(i)


        expense = 0
        for i in expense_list:
            expense += float(i)

        balance = initial_budget + income - expense

        return balance
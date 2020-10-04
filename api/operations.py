def find_value_and_replace_it(document, updater, updated_value):
    actual_initial_budget = document['budget']

    updater(
        field_to_search='_id',
        value_to_search=document['_id'],
        field_to_replace='budget.initial_budget',
        value_to_replace=-actual_initial_budget['initial_budget']
    )

    updater(
        field_to_search='_id',
        value_to_search=document['_id'],
        field_to_replace='budget.initial_budget',
        value_to_replace=float(updated_value)
    )
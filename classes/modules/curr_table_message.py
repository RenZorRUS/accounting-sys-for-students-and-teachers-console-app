from api.screen_clear import screen_clear

def curr_table_message(table_name: str) -> None:
    """Clear screen and shows message about adding row to the table"""

    screen_clear()
    print(f'You are adding a row to the {table_name} table\n')

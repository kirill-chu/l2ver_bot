from prettytable import PrettyTable


def pretty_output(results):
    table = PrettyTable()
    table.field_names = results[0]
    table.align = 'c'
    table.add_rows(results[1:])
    return table

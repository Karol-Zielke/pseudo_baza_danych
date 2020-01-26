COMMANDS = {
    'create': {
        'regex': 'CREATE DOCUMENTS (.*) \((.*)\)',
        'order': ['documents', 'columns'],
    },
    'add': {
        'regex': 'ADD \((.*)\) TO (.*)',
        'order': ['data', 'columns']
    },
    'select': {
        'regex': 'SELECT \((.*)\) FROM (.*)',
        'order': ["columns", "document"]
    }

}

COMMANDS = {
    'create': {
        'regex': 'CREATE DOCUMENT (.*) \((.*)\)',
        'order': ['document', 'columns'],
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

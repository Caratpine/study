
routes = []


def call_baz():
    return 'Call baz'


routes.append(dict(
    rule='/call-baz/',
    view_func=call_baz
))


def delete_baz():
    return 'Delete baz'


routes.append(dict(
    rule='/delete-baz/',
    view_func=delete_baz,
    options=dict(methods=['GET', 'POST'])
))

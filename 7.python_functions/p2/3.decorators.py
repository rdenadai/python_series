"""
Controlling transactions explicitly
https://docs.djangoproject.com/en/5.0/topics/db/transactions/#controlling-transactions-explicitly
"""

from functools import wraps


def db_execute(query, *args):
    print("==>", query.format(*args))
    return [{"id": 1, "name": "Rodolfo"}]


def transaction(fn):
    @wraps(fn)
    def execute(*args, **kwargs):
        print("==> Start transaction ...")
        result = fn(*args, **kwargs)
        print("==> Close transaction")
        return result

    return execute


@transaction
def select(id_, name):
    select_query = "SELECT * FROM users WHERE id = {} and name = '{}'"
    return db_execute(select_query, id_, name)


@transaction
def insert():
    ...


print(select(1, "Rodolfo"))

print(insert())

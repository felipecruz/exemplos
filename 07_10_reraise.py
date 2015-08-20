class InvalidDataTypeException(Exception):
    pass


def validate_kind(kind):
    if not kind in ('bigint', 'numeric', 'varchar'):
        raise InvalidDataTypeException

try:
    validate_kind('invalid type')
except Exception as e:
    print("Peguei o erro mas vou repassa-lo")
    raise e


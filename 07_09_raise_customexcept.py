class InvalidDataTypeException(Exception):
    pass

def validate_kind(kind):
    if not kind in ('bigint', 'numeric', 'varchar'):
        raise InvalidDataTypeException


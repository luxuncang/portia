from portia_orm.exceptions import ImproperlyConfigured


__all__ = [
    'schema',
]

schemas = {}


def get_schema(schema_type):
    try:
        return schemas[schema_type]
    except KeyError:
        raise ImproperlyConfigured(f"No schema for type '{schema_type}' exists")

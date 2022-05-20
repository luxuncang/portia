from six import itervalues

from .exceptions import ImproperlyConfigured


__all__ = [
    'get_model',
    'get_polymorphic_model',
]

models = {}


def get_model(model_name):
    try:
        return models[model_name]
    except KeyError:
        raise ImproperlyConfigured(f"No model named '{model_name}' exists")


def get_polymorphic_model(data):
    for model in itervalues(models):
        if polymorphic := model.opts.polymorphic:
            polymorphic_key = polymorphic
            if isinstance(polymorphic_key, bool):
                polymorphic_key = 'type'
            if data.get(polymorphic_key) == model.__name__:
                return model
    raise ImproperlyConfigured(
        u"No model found for data: {!r}".format(data))

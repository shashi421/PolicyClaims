import random
import string


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_order_id_generator(instance):
    claim_id= random_string_generator()

    Klass= instance.__class__

    qs_exists= Klass.objects.filter(claim_id= claim_id).exists()
    if qs_exists:
        return unique_order_id_generator(instance)
    return claim_id


from yoconfig.util import get_config

from authtkt.encrypted import EncryptedAuthTkt
from authtkt.ticket import validate


def get_ticket_data(ticket):
    """We store user information in our session hashes. You can retreive that
    data with this function."""
    ticket = validate(ticket, get_config('SECRET'))
    if not ticket:
        return None

    ticket = EncryptedAuthTkt(ticket, get_config('CRYPTO_SECRET'))
    data = ticket.data
    data.update({
        'id': ticket.uid,
        'tokens': ticket.authticket.tokens
    })
    return data

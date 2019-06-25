from typing import Dict, Optional
import json

from indy import crypto, error
from .error import errorcode_to_exception

async def pack_message(wallet_handle: int,
                       message: str,
                       recipient_verkeys: list,
                       sender_verkey: Optional[str]) -> bytes:
    try:
        return await crypto.pack_message(
            wallet_handle,
            message,
            recipient_verkeys,
            sender_verkey
        )
    except error.IndyError as err:
        raise errorcode_to_exception(err.error_code) from err


async def unpack_message(wallet_handle: int,
                         jwe: bytes) -> bytes:
    try:
        return await crypto.unpack_message(wallet_handle, jwe)
    except error.IndyError as err:
        raise errorcode_to_exception(err.error_code) from err

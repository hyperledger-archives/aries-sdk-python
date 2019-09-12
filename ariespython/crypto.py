import json
from typing import Optional

from indy import crypto

from .error import IndyErrorHandler


@IndyErrorHandler()
async def pack_message(
    wallet_handle: int,
    message: str,
    recipient_verkeys: list,
    sender_verkey: Optional[str] = None,
) -> bytes:
    return await crypto.pack_message(
        wallet_handle, message, recipient_verkeys, sender_verkey
    )


@IndyErrorHandler()
async def unpack_message(wallet_handle: int, jwe: bytes) -> (str, str, str):
    unpacked = json.loads(await crypto.unpack_message(wallet_handle, jwe))
    return (
        unpacked["message"],
        unpacked["recipient_verkey"],
        unpacked.get("sender_verkey", None),
    )


@IndyErrorHandler()
async def crypto_sign(wallet_handle: int, signer_vk: str, msg: bytes) -> bytes:
    return await crypto.crypto_sign(wallet_handle, signer_vk, msg)


@IndyErrorHandler()
async def crypto_verify(signer_vk: str, msg: bytes, signature: bytes) -> bool:
    return await crypto.crypto_verify(signer_vk, msg, signature)

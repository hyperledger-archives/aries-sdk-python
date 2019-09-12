import json
from typing import Any, Dict, Union

from indy import did

from .error import IndyErrorHandler, WalletItemNotFound


@IndyErrorHandler()
async def create_and_store_my_did(
    wallet_handle: int, did_dict: Dict[str, Any] = {}
) -> (str, str):
    return await did.create_and_store_my_did(wallet_handle, json.dumps(did_dict))


@IndyErrorHandler()
async def create_key(wallet_handle: int, key_dict: Dict[str, Any]) -> str:
    return await did.create_key(wallet_handle, json.dumps(key_dict))


@IndyErrorHandler()
async def store_their_did(wallet_handle: int, identity_dict: Dict[str, Any]) -> None:
    await did.store_their_did(wallet_handle, json.dumps(identity_dict))


@IndyErrorHandler()
async def set_key_metadata(
    wallet_handle: int, verkey: str, metadata: Union[Dict, str]
) -> None:
    if isinstance(metadata, dict):
        metadata = json.dumps(metadata)
    await did.set_key_metadata(wallet_handle, verkey, metadata)


@IndyErrorHandler()
async def get_key_metadata(wallet_handle: int, verkey: str) -> str:
    metadata = await did.get_key_metadata(wallet_handle, verkey)

    try:
        metadata = json.loads(metadata)
    except json.decoder.JSONDecodeError:
        pass

    return metadata


@IndyErrorHandler()
async def get_did_metadata(wallet_handle: int, did_subject: str) -> str:
    metadata = await did.get_did_metadata(wallet_handle, did_subject)

    try:
        metadata = json.loads(metadata)
    except json.decoder.JSONDecodeError:
        pass

    return metadata


@IndyErrorHandler()
async def set_did_metadata(
    wallet_handle: int, did_subject: str, metadata: Union[Dict, str]
) -> None:
    if isinstance(metadata, dict):
        metadata = json.dumps(metadata)

    return await did.set_did_metadata(wallet_handle, did_subject, metadata)


@IndyErrorHandler()
async def key_for_local_did(wallet_handle: int, did: str) -> str:
    return await did.key_for_local_did(wallet_handle, did)


async def did_for_key(wallet_handle: int, verkey: str) -> str:
    try:
        with IndyErrorHandler():
            key_meta = await get_key_metadata(wallet_handle, verkey)
            if "did" not in key_meta:
                return None
            return key_meta["did"]
    except WalletItemNotFound:
        return None


@IndyErrorHandler()
async def map_key_to_did(wallet_handle: int, verkey: str, did: str):
    await set_key_metadata(wallet_handle, verkey, {"did": did})

from typing import Dict, Optional, Any, Union
import json

from indy import did, non_secrets, error
from .error import errorcode_to_exception

async def create_and_store_my_did(wallet_handle: int,
                                  did_dict: Dict[str, Any]) -> (str, str):
    try:
        (my_did, my_vk) = await did.create_and_store_my_did(
            wallet_handle,
            json.dumps(did_dict)
        )

        await non_secrets.add_wallet_record(
            wallet_handle,
            'key-to-did',
            my_vk,
            my_did,
            '{}'
        )

        return my_did, my_vk
    except error.IndyError as err:
        raise errorcode_to_exception(err.error_code) from err


async def store_their_did(wallet_handle: int,
                          identity_dict: Dict[str, Any]) -> None:
    try:
        await did.store_their_did(
            wallet_handle,
            json.dumps(identity_dict)
        )
        await non_secrets.add_wallet_record(
            wallet_handle,
            'key-to-did',
            identity_dict['verkey'],
            identity_dict['did'],
            '{}'
        )
    except error.IndyError as err:
        raise errorcode_to_exception(err.error_code) from err


async def set_key_metadata(wallet_handle: int,
                           verkey: str,
                           metadata: Union[Dict, str]) -> None:
    if isinstance(metadata, dict):
        metadata = json.dumps(metadata)

    try:
        await did.set_key_metadata(wallet_handle, verkey, metadata)
    except error.IndyError as err:
        raise errorcode_to_exception(err.error_code) from err



async def get_key_metadata(wallet_handle: int,
                           verkey: str) -> str:
    try:
        metadata = await did.get_key_metadata(wallet_handle, verkey)

        try:
            metadata = json.loads(metadata)
        except json.decoder.JSONDecodeError:
            pass

        return metadata
    except error.IndyError as err:
        raise errorcode_to_exception(err.error_code) from err


async def get_did_metadata(wallet_handle: int,
                           did_subject: str) -> str:
    try:
        metadata = await did.get_did_metadata(wallet_handle, did_subject)

        try:
            metadata = json.loads(metadata)
        except json.decoder.JSONDecodeError:
            pass

        return metadata
    except error.IndyError as err:
        raise errorcode_to_exception(err.error_code) from err


async def set_did_metadata(wallet_handle: int,
                           did_subject: str,
                           metadata: Union[Dict, str]) -> None:
    if isinstance(metadata, dict):
        metadata = json.dumps(metadata)

    try:
        await did.set_did_metadata(wallet_handle, did_subject, metadata)
    except error.IndyError as err:
        raise errorcode_to_exception(err.error_code) from err



async def did_for_key(wallet_handle: int,
                      verkey: str) -> str:
    try:
        found_did = json.loads(
            await non_secrets.get_wallet_record(
                wallet_handle,
                'key-to-did',
                verkey,
                '{}'
            )
        )['value']

        return found_did
    except error.IndyError as err:
        raise errorcode_to_exception(err.error_code) from err

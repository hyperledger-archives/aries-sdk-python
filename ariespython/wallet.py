from typing import Dict, Optional
import json

from indy import wallet, error
from .error import errorcode_to_exception


async def create_wallet(config: Dict,
                        credentials: Dict) -> None:
    try:
        return await wallet.create_wallet(
            json.dumps(config),
            json.dumps(credentials)
        )
    except error.IndyError as err:
        raise errorcode_to_exception(err.error_code) from err


async def open_wallet(config: Dict,
                      credentials: Dict) -> int:
    try:
        return await wallet.open_wallet(
            json.dumps(config),
            json.dumps(credentials)
        )
    except error.IndyError as err:
        raise errorcode_to_exception(err.error_code) from err


async def close_wallet(handle: int) -> None:
    try:
        return await wallet.close_wallet(handle)
    except error.IndyError as err:
        raise errorcode_to_exception(err.error_code) from err


async def delete_wallet(config: Dict,
                        credentials: Dict) -> None:
    try:
        return await wallet.delete_wallet(
            json.dumps(config),
            json.dumps(credentials)
        )
    except error.IndyError as err:
        raise errorcode_to_exception(err.error_code) from err


async def export_wallet(handle: int,
                        export_config: Dict) -> None:
    try:
        return await wallet.export_wallet(
            handle,
            json.dumps(export_config)
        )
    except error.IndyError as err:
        raise errorcode_to_exception(err.error_code) from err


async def import_wallet(config: Dict,
                        credentials: Dict,
                        import_config: Dict) -> None:
    try:
        return await wallet.import_wallet(
            json.dumps(config),
            json.dumps(credentials),
            json.dumps(import_config)
        )
    except error.IndyError as err:
        raise errorcode_to_exception(err.error_code) from err


async def generate_wallet_key(config: Optional[Dict]) -> Dict:
    try:
        return json.loads(await wallet.generate_wallet_key(json.dumps(config)))
    except error.IndyError as err:
        raise errorcode_to_exception(err.error_code) from err

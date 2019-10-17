from typing import Dict, Optional
import json

from indy import wallet
from .error import IndyErrorHandler


@IndyErrorHandler()
async def create_wallet(config: Dict, credentials: Dict) -> None:
    return await wallet.create_wallet(json.dumps(config), json.dumps(credentials))


@IndyErrorHandler()
async def open_wallet(config: Dict, credentials: Dict) -> int:
    return await wallet.open_wallet(json.dumps(config), json.dumps(credentials))


@IndyErrorHandler()
async def close_wallet(handle: int) -> None:
    return await wallet.close_wallet(handle)


@IndyErrorHandler()
async def delete_wallet(config: Dict, credentials: Dict) -> None:
    return await wallet.delete_wallet(json.dumps(config), json.dumps(credentials))


@IndyErrorHandler()
async def export_wallet(handle: int, export_config: Dict) -> None:
    return await wallet.export_wallet(handle, json.dumps(export_config))


@IndyErrorHandler()
async def import_wallet(config: Dict, credentials: Dict, import_config: Dict) -> None:
    return await wallet.import_wallet(
        json.dumps(config), json.dumps(credentials), json.dumps(import_config)
    )


@IndyErrorHandler()
async def generate_wallet_key(config: Optional[Dict]) -> Dict:
    return json.loads(await wallet.generate_wallet_key(json.dumps(config)))

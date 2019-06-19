from indy import wallet
from typing import Dict, Optional
import json


async def test_method(arg1, arg2):
    return None


async def create_wallet(config: Dict,
                        credentials: Dict) -> None:
    return await wallet.create_wallet(json.dumps(config), json.dumps(credentials))


async def open_wallet(config: Dict,
                      credentials: Dict) -> int:
    return await wallet.open_wallet(json.dumps(config), json.dumps(credentials))


async def close_wallet(handle: int) -> None:
    return await wallet.close_wallet(handle)


async def delete_wallet(config: Dict,
                        credentials: Dict) -> None:
    return await wallet.delete_wallet(json.dumps(config), json.dumps(credentials))


async def export_wallet(handle: int,
                        export_config: Dict) -> None:
    return await wallet.export_wallet(handle, json.dumps(export_config))


async def import_wallet(config: Dict,
                        credentials: Dict,
                        import_config: Dict) -> None:
    return await wallet.import_wallet(json.dumps(config), json.dumps(credentials), json.dumps(import_config))


async def generate_wallet_key(config: Optional[Dict]) -> Dict:
    return json.loads(await wallet.generate_wallet_key(json.dumps(config)))

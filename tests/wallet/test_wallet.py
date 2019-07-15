from unittest import mock
import pytest

from tests import AsyncMock
from ariespython import wallet


@pytest.mark.asyncio
async def test_create_wallet():
    with mock.patch('indy.wallet.create_wallet', new_callable=AsyncMock) as m:
        await wallet.create_wallet({'a': 1}, {'b': 2})
        m.assert_called_once_with('{"a": 1}', '{"b": 2}')

@pytest.mark.asyncio
async def test_open_wallet():
    with mock.patch('indy.wallet.open_wallet', new_callable=AsyncMock) as m:
        await wallet.open_wallet({'a': 1}, {'b': 2})
        m.assert_called_once_with('{"a": 1}', '{"b": 2}')

@pytest.mark.asyncio
async def test_close_wallet():
    with mock.patch('indy.wallet.close_wallet', new_callable=AsyncMock) as m:
        await wallet.close_wallet(7)
        m.assert_called_once_with(7)

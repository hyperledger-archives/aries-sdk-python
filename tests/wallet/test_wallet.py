from unittest import mock
import pytest

from tests import async_mock
from ariespython import wallet


@pytest.mark.asyncio
async def test_create_wallet():
    with async_mock('indy.wallet.create_wallet') as m:
        await wallet.create_wallet({'a': 1}, {'b': 2})
        m.assert_called_once_with('{"a": 1}', '{"b": 2}')

@pytest.mark.asyncio
async def test_open_wallet():
    with async_mock('indy.wallet.open_wallet') as m:
        await wallet.open_wallet({'a': 1}, {'b': 2})
        m.assert_called_once_with('{"a": 1}', '{"b": 2}')

@pytest.mark.asyncio
async def test_close_wallet():
    with async_mock('indy.wallet.close_wallet') as m:
        await wallet.close_wallet(7)
        m.assert_called_once_with(7)

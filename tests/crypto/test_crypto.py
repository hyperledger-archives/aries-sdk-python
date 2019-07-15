from unittest import mock
import json

import pytest

from tests import AsyncMock
from ariespython import crypto


@pytest.mark.asyncio
async def test_pack_message():
    with mock.patch(
            'indy.crypto.pack_message',
            new_callable=AsyncMock
    ) as method:
        await crypto.pack_message(1, 'test', [])
        method.assert_called_once_with(1, 'test', [], None)


@pytest.mark.asyncio
async def test_unpack_message():
    with mock.patch(
            'indy.crypto.unpack_message',
            new_callable=AsyncMock
    ) as method:
        method.return_value = json.dumps({
            'message': 'message',
            'recipient_verkey': 'recipient_verkey',
            'sender_verkey': 'sender_verkey'
        })

        message, recip_vk, sender_vk = \
            await crypto.unpack_message(1, b'mock_jwe_bytes')

        method.assert_called_once_with(1, b'mock_jwe_bytes')
        assert message == 'message'
        assert recip_vk == 'recipient_verkey'
        assert sender_vk == 'sender_verkey'

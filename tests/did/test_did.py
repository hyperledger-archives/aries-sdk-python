import json

import pytest

from tests import async_mock
from ariespython import did


@pytest.mark.parametrize(
    'mocked_method, method_to_test, before_dict, after_dict',
    [
        ('indy.did.create_and_store_my_did', did.create_and_store_my_did, [], []),
        ('indy.did.create_key', did.create_key, [], []),
        ('indy.did.store_their_did', did.store_their_did, [], []),
        ('indy.did.set_key_metadata', did.set_key_metadata, ['vk'], []),
        ('indy.did.set_did_metadata', did.set_did_metadata, ['did'], [])
    ]
)
@pytest.mark.asyncio
async def test_dumping_dict(mocked_method, method_to_test, before_dict, after_dict):
    with async_mock(
            mocked_method,
    ) as method:
        did_dict = {
            'blah': 'blah'
        }
        await method_to_test(1, *before_dict, did_dict, *after_dict)
        method.assert_called_once_with(1, *before_dict, json.dumps(did_dict), *after_dict)


@pytest.mark.parametrize(
    'mocked_method, method_to_test, params',
    [
        ('indy.did.get_did_metadata', did.get_did_metadata, [1, 'did']),
        ('indy.did.get_key_metadata', did.get_key_metadata, [1, 'vk'])
    ]
)
@pytest.mark.asyncio
async def test_loading_dict(mocked_method, method_to_test, params):
    with async_mock(mocked_method) as method:
        method.return_value = json.dumps({'testing': 'test'})
        loaded_dict = await method_to_test(*params)
        assert isinstance(loaded_dict, dict)
        assert 'testing' in loaded_dict
        assert loaded_dict['testing'] == 'test'

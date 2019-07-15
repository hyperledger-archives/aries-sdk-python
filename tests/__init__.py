from unittest import mock

class AsyncMock(mock.MagicMock):
    async def __call__(self, *args, **kwargs):
        return super(AsyncMock, self).__call__(*args, **kwargs)


def async_mock(method_to_mock, **kwargs):
    return mock.patch(method_to_mock, new_callable=AsyncMock, **kwargs)

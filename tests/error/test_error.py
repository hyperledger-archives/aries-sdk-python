import pytest

import indy.error

from ariespython import error


def test_error_context():
    with pytest.raises(error.WalletItemNotFound):
        with error.IndyErrorHandler():
            raise indy.error.IndyError(212)


@pytest.mark.asyncio
async def test_error_decorator():
    @error.IndyErrorHandler()
    async def fail():
        raise indy.error.IndyError(212)

    with pytest.raises(error.WalletItemNotFound):
        await fail()

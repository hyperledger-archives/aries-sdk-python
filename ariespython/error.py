""" Aries Errors """

from functools import wraps

from indy.error import IndyError


def errorcode_to_exception(errorcode: int, message: str = None):
    """ Map error code to an Exception """
    if message:
        args = (message,)
    else:
        args = ()
    return {
        100: CommonInvalidParam1,
        101: CommonInvalidParam2,
        102: CommonInvalidParam3,
        103: CommonInvalidParam4,
        104: CommonInvalidParam5,
        105: CommonInvalidParam6,
        106: CommonInvalidParam7,
        107: CommonInvalidParam8,
        108: CommonInvalidParam9,
        109: CommonInvalidParam10,
        110: CommonInvalidParam11,
        111: CommonInvalidParam12,
        112: CommonInvalidState,
        113: CommonInvalidStructure,
        114: CommonIOError,
        200: WalletInvalidHandle,
        201: WalletUnknownTypeError,
        202: WalletTypeAlreadyRegisteredError,
        203: WalletAlreadyExistsError,
        204: WalletNotFoundError,
        205: WalletIncompatiblePoolError,
        206: WalletAlreadyOpenedError,
        207: WalletAccessFailed,
        208: WalletInputError,
        209: WalletDecodingError,
        210: WalletStorageError,
        211: WalletEncryptionError,
        212: WalletItemNotFound,
        213: WalletItemAlreadyExists,
        214: WalletQueryError,
        400: AnoncredsRevocationRegistryFullError,
        401: AnoncredsInvalidUserRevocId,
        404: AnoncredsMasterSecretDuplicateNameError,
        405: AnoncredsProofRejected,
        406: AnoncredsCredentialRevoked,
        407: AnoncredsCredDefAlreadyExistsError,
        500: UnknownCryptoTypeError,
        600: DidAlreadyExistsError,
        700: PaymentUnknownMethodError,
        701: PaymentIncompatibleMethodsError,
        702: PaymentInsufficientFundsError,
        703: PaymentSourceDoesNotExistError,
        704: PaymentOperationNotSupportedError,
        705: PaymentExtraFundsError,
    }[errorcode](*args)


class IndyErrorHandler:
    """Error handler for mapping Indy errors."""

    def __enter__(self):
        """Enter the context manager."""
        return self

    def __exit__(self, err_type, err_value, err_traceback):
        """Exit the context manager."""
        if err_type is IndyError:
            msg = hasattr(err_value, "message") and err_value.message or None
            raise errorcode_to_exception(err_value.error_code, msg)

    def __call__(self, coro):
        """Perform as a decorator."""

        @wraps(coro)
        async def wrapped(*args, **kwargs):
            with self:
                return await coro(*args, **kwargs)

        return wrapped


class AriesError(Exception):
    """Base class for Aries exceptions."""


class CommonInvalidParam1(AriesError):
    """Caller passed invalid value as param 1 (null, invalid json and etc..)
    """


class CommonInvalidParam2(AriesError):
    """Caller passed invalid value as param 2 (null, invalid json and etc..)
    """


class CommonInvalidParam3(AriesError):
    """ Caller passed invalid value as param 3 (null, invalid json and etc..)
    """


class CommonInvalidParam4(AriesError):
    """ Caller passed invalid value as param 4 (null, invalid json and etc..)
    """


class CommonInvalidParam5(AriesError):
    """ Caller passed invalid value as param 5 (null, invalid json and etc..)
    """


class CommonInvalidParam6(AriesError):
    """ Caller passed invalid value as param 6 (null, invalid json and etc..)
    """


class CommonInvalidParam7(AriesError):
    """ Caller passed invalid value as param 7 (null, invalid json and etc..)
    """


class CommonInvalidParam8(AriesError):
    """ Caller passed invalid value as param 8 (null, invalid json and etc..)
    """


class CommonInvalidParam9(AriesError):
    """ Caller passed invalid value as param 9 (null, invalid json and etc..)
    """


class CommonInvalidParam10(AriesError):
    """ Caller passed invalid value as param 10 (null, invalid json and etc..)
    """


class CommonInvalidParam11(AriesError):
    """ Caller passed invalid value as param 11 (null, invalid json and etc..)
    """


class CommonInvalidParam12(AriesError):
    """ Caller passed invalid value as param 12 (null, invalid json and etc..)
    """


class CommonInvalidState(AriesError):
    """ Invalid library state was detected in runtime. It signals library bug.
    """


class CommonInvalidStructure(AriesError):
    """ Object (json, config, key, credential and etc...) passed by library
        caller has invalid structure
    """


class CommonIOError(AriesError):
    """ IO Error """


# Wallet errors


class WalletInvalidHandle(AriesError):
    """ Caller passed invalid wallet handle """


class WalletUnknownTypeError(AriesError):
    """ Unknown type of wallet was passed on create_wallet """


class WalletTypeAlreadyRegisteredError(AriesError):
    """ Attempt to register already existing wallet type """


class WalletAlreadyExistsError(AriesError):
    """ Attempt to create wallet with name used for another exists wallet """


class WalletNotFoundError(AriesError):
    """ Requested entity id isn't present in wallet """


class WalletIncompatiblePoolError(AriesError):
    """ Trying to use wallet with pool that has different name """


class WalletAlreadyOpenedError(AriesError):
    """ Trying to open wallet that was opened already """


class WalletAccessFailed(AriesError):
    """ Input provided to wallet operations is considered not valid """


class WalletInputError(AriesError):
    """ Attempt to open encrypted wallet with invalid credentials """


class WalletDecodingError(AriesError):
    """ Decoding of wallet data during input/output failed """


class WalletStorageError(AriesError):
    """ Storage error occurred during wallet operation """


class WalletEncryptionError(AriesError):
    """ Error during encryption-related operations """


class WalletItemNotFound(AriesError):
    """ Requested wallet item not found """


class WalletItemAlreadyExists(AriesError):
    """ Returned if wallet's add_record operation is used with record name
        that already exists
    """


class WalletQueryError(AriesError):
    """ Returned if provided wallet query is invalid """


class AnoncredsRevocationRegistryFullError(AriesError):
    """ Revocation registry is full and creation of new registry is necessary
    """


class AnoncredsInvalidUserRevocId(AriesError):
    """ Invalid User Revocaction ID """


class AnoncredsMasterSecretDuplicateNameError(AriesError):
    """ Attempt to generate master secret with duplicated name """


class AnoncredsProofRejected(AriesError):
    pass


class AnoncredsCredentialRevoked(AriesError):
    pass


class AnoncredsCredDefAlreadyExistsError(AriesError):
    """ Attempt to create credential definition with duplicated did schema
        pair
    """


# Crypto errors
class UnknownCryptoTypeError(AriesError):
    """ Unknown format of DID entity keys """


class DidAlreadyExistsError(AriesError):
    """ Attempt to create duplicate did """


class PaymentUnknownMethodError(AriesError):
    """ Unknown payment method was given """


class PaymentIncompatibleMethodsError(AriesError):
    """ No methods were scraped from inputs/outputs or more than one was
        scraped
    """


class PaymentInsufficientFundsError(AriesError):
    """ Insufficient funds on inputs """


class PaymentSourceDoesNotExistError(AriesError):
    """ No such source on a ledger """


class PaymentOperationNotSupportedError(AriesError):
    """ Operation is not supported for payment method """


class PaymentExtraFundsError(AriesError):
    """ Extra funds on inputs """

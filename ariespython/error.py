""" Aries Errors """


def errorcode_to_exception(errorcode):
    """ Map error code to an Exception """
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
        705: PaymentExtraFundsError
    }[errorcode]()


class CommonInvalidParam1(Exception):
    """Caller passed invalid value as param 1 (null, invalid json and etc..)
    """


class CommonInvalidParam2(Exception):
    """Caller passed invalid value as param 2 (null, invalid json and etc..)
    """


class CommonInvalidParam3(Exception):
    """ Caller passed invalid value as param 3 (null, invalid json and etc..)
    """


class CommonInvalidParam4(Exception):
    """ Caller passed invalid value as param 4 (null, invalid json and etc..)
    """


class CommonInvalidParam5(Exception):
    """ Caller passed invalid value as param 5 (null, invalid json and etc..)
    """


class CommonInvalidParam6(Exception):
    """ Caller passed invalid value as param 6 (null, invalid json and etc..)
    """


class CommonInvalidParam7(Exception):
    """ Caller passed invalid value as param 7 (null, invalid json and etc..)
    """


class CommonInvalidParam8(Exception):
    """ Caller passed invalid value as param 8 (null, invalid json and etc..)
    """


class CommonInvalidParam9(Exception):
    """ Caller passed invalid value as param 9 (null, invalid json and etc..)
    """


class CommonInvalidParam10(Exception):
    """ Caller passed invalid value as param 10 (null, invalid json and etc..)
    """


class CommonInvalidParam11(Exception):
    """ Caller passed invalid value as param 11 (null, invalid json and etc..)
    """


class CommonInvalidParam12(Exception):
    """ Caller passed invalid value as param 12 (null, invalid json and etc..)
    """


class CommonInvalidState(Exception):
    """ Invalid library state was detected in runtime. It signals library bug.
    """


class CommonInvalidStructure(Exception):
    """ Object (json, config, key, credential and etc...) passed by library
        caller has invalid structure
    """


class CommonIOError(Exception):
    """ IO Error """


# Wallet errors

class WalletInvalidHandle(Exception):
    """ Caller passed invalid wallet handle """


class WalletUnknownTypeError(Exception):
    """ Unknown type of wallet was passed on create_wallet """


class WalletTypeAlreadyRegisteredError(Exception):
    """ Attempt to register already existing wallet type """


class WalletAlreadyExistsError(Exception):
    """ Attempt to create wallet with name used for another exists wallet """


class WalletNotFoundError(Exception):
    """ Requested entity id isn't present in wallet """


class WalletIncompatiblePoolError(Exception):
    """ Trying to use wallet with pool that has different name """


class WalletAlreadyOpenedError(Exception):
    """ Trying to open wallet that was opened already """


class WalletAccessFailed(Exception):
    """ Input provided to wallet operations is considered not valid """


class WalletInputError(Exception):
    """ Attempt to open encrypted wallet with invalid credentials """


class WalletDecodingError(Exception):
    """ Decoding of wallet data during input/output failed """


class WalletStorageError(Exception):
    """ Storage error occurred during wallet operation """


class WalletEncryptionError(Exception):
    """ Error during encryption-related operations """


class WalletItemNotFound(Exception):
    """ Requested wallet item not found """


class WalletItemAlreadyExists(Exception):
    """ Returned if wallet's add_record operation is used with record name
        that already exists 
    """


class WalletQueryError(Exception):
    """ Returned if provided wallet query is invalid """


class AnoncredsRevocationRegistryFullError(Exception):
    """ Revocation registry is full and creation of new registry is necessary
    """


class AnoncredsInvalidUserRevocId(Exception):
    """ Invalid User Revocaction ID """


class AnoncredsMasterSecretDuplicateNameError(Exception):
    """ Attempt to generate master secret with duplicated name """


class AnoncredsProofRejected(Exception):
    pass


class AnoncredsCredentialRevoked(Exception):
    pass


class AnoncredsCredDefAlreadyExistsError(Exception):
    """ Attempt to create credential definition with duplicated did schema
        pair
    """


# Crypto errors
class UnknownCryptoTypeError(Exception):
    """ Unknown format of DID entity keys """


class DidAlreadyExistsError(Exception):
    """ Attempt to create duplicate did """


class PaymentUnknownMethodError(Exception):
    """ Unknown payment method was given """


class PaymentIncompatibleMethodsError(Exception):
    """ No methods were scraped from inputs/outputs or more than one was
        scraped
    """


class PaymentInsufficientFundsError(Exception):
    """ Insufficient funds on inputs """


class PaymentSourceDoesNotExistError(Exception):
    """ No such source on a ledger """


class PaymentOperationNotSupportedError(Exception):
    """ Operation is not supported for payment method """


class PaymentExtraFundsError(Exception):
    """ Extra funds on inputs """

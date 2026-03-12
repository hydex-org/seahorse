from typing import *
from complexTypes import *
from num import *

class Pubkey:
    """32-byte account identifier."""

    def find_program_address(seeds: List[Any], program_id: 'Pubkey' = None) -> Tuple['Pubkey', u8]:
        """
        Find a valid program derived address and its corresponding bump seed. Calls the same function from Solana's Pubkey struct - read more [here](https://docs.rs/solana-program/latest/solana_program/pubkey/struct.Pubkey.html#method.find_program_address).
        
        @param seeds: A list of parameters to uniquely identify this account among all accounts created by your program. These may be string literals, other accounts, integers, or lists of bytes.
        @param program_id: The pubkey of the program that the PDA belongs to. Defaults to the current program's key.
        @returns: The canonical pubkey and bump seed.
        """

class AccountWithKey:
    """Generic Solana account."""

    def key(self) -> Pubkey:
        """Get this account's key."""

class Account(AccountWithKey):
    """User-defined Solana account."""

    def transfer_lamports(self, to: AccountWithKey, amount: u64):
        """
        Transfer some SOL directly to another account. Since this account is program-owned, this transfer does not require a CPI.

        @param to: The recipient Solana account.
        @param amount: The amount (in lamports, not SOL) to transfer.
        """

class Event:
    """Anchor event that clients can listen for"""

    def emit(self):
        """
        Emit the event to the blockchain
        """

class Signer(AccountWithKey):
    """Instruction signer."""

    def transfer_lamports(self, to: AccountWithKey, amount: u64):
        """
        Transfer some SOL directly to another account. Unlike using transfer_lamports from a program account, this transfer will require a CPI.

        @param to: The recipient Solana account.
        @param amount: The amount (in lamports, not SOL) to transfer.
        """

class Empty(Generic[T]):
    """An account that needs to be initialized."""

    def init(self, payer: Signer, seeds: List[Any] = None, mint: 'TokenMint' = None, decimals: u8 = None, authority: AccountWithKey = None, associated: bool = False, space: u64 = None, padding: u64 = None)  -> T:
        """
        Initialize the account.
        
        @param payer: The account that will pay for the rent cost of the initialized account. Must be an instruction signer.
        @param seeds: A list of parameters to uniquely identify this account among all accounts created by your program. These may be string literals, other accounts, integers, or lists of bytes.
        @param mint: If initializing a TokenAccount, this is the mint that the account belongs to.
        @param decimals: If initializing a TokenMint, this is the number of decimals the new token has.
        @param authority: If initializing a TokenAccount/TokenMint, this is the account that has authority over the account.
        @param associated: If initializing an associated token account, must be set to true.
        @param space: If initializing a program account, you can use this to overwrite Seahorse's calculation of the account size.
        @param padding: If initializing a program account, you can use this to add extra space to Seahorse's calculation of the account size.
        @returns: The new, initialized account. All of the data in this account will be set to 0, bytewise.
        """

    def bump(self) -> u8:
        """
        Get this account's bump, needed if you want to use this account to sign CPI calls.
        
        If you've initialized an account without seeds, then a bump will not have been calculated. This will result in a runtime error when you try to access it.
        """

    def key(self) -> Pubkey:
        """Get this account's key."""

class CpiAccount:
    """Account and metadata used for making arbitrary CPIs (via `Program.invoke`)."""

    def __init__(account: AccountWithKey, mut: bool = False, signer: bool = False, seeds: List[Any] = None) -> 'CpiAccount':
        """
        Create the CpiAccount.

        @param account: The account being passed to the CPI.
        @param mut: Whether this account needs to be mutable for the CPI - defaults to false.
        @param signer: Whether this account needs to be an instruction signer - defaults to false. Mutually exclusive with seeds, and should only really be true if account is a Signer.
        @param seeds: PDA signer seeds, if this account needs to sign the CPI. Mutually exclusive with signer.
        """

class Program(AccountWithKey):
    """Arbitrary program."""

    def invoke(self, accounts: List[CpiAccount], data: List[u8]):
        """
        Call this program in a cross-program invocation. Make sure you know what you're doing before you try using this - a poorly crafted data list could cost you real money.

        @param accounts: List of accounts being passed to the CPI - the program itself does not need to be in here.
        @param data: "Raw" list of bytes used to tell the program what to do, pass args, etc.
        """

class UncheckedAccount(AccountWithKey):
    """
    Raw account that has had no safety checks performed on it.
    
    The underlying Anchor code cannot guarantee anything about the account unless you check it in your instruction - not the type, not the data, not the program it came from. Use carefully.
    """

class Clock:
    """
    Solana's Clock sysvar.
    
    Consult Solana's reference to learn more. Information copied from https://docs.rs/solana-program/1.14.3/solana_program/clock/struct.Clock.html.
    """

    def slot(self) -> u64:
        """Get the current network/bank Slot."""

    def epoch_start_timestamp(self) -> i64:
        """Get the timestamp of the first Slot in this Epoch."""

    def epoch(self) -> u64:
        """Get the bank Epoch."""

    def leader_schedule_epoch(self) -> u64:
        """Get the future Epoch for which the leader schedule has most recently been calculated."""

    def unix_timestamp(self) -> i64:
        """
        Get the estimated current UNIX timestamp.
        
        Originally computed from genesis creation time and network time in slots (drifty); corrected using validator timestamp oracle as of timestamp_correction and timestamp_bounding features.
        """

class TokenAccount(AccountWithKey):
    """SPL token account."""

    def authority(self) -> Pubkey:
        """Get the owner of this token account."""

    def amount(self) -> u64:
        """Get the amount of token stored in this account."""

    def mint(self) -> Pubkey:
        """Get the mint that this token account corresponds to."""

    def transfer(self, authority: AccountWithKey, to: 'TokenAccount', amount: u64, signer: List[Any] = None):
        """
        Transfer funds from this SPL token account to another.
        
        @param authority: The account that owns this TokenAccount. Must be an instruction signer or the account given by the `signer` param.
        @param to: The recipient TokenAccount.
        @param amount: How much (in *native* token units) to transfer.
        @param signer: (Optional) seeds for the signature of a PDA.
        """

class TokenMint(AccountWithKey):
    """SPL token mint."""

    def authority(self) -> Pubkey:
        """Get the owner of this token mint."""

    def freeze_authority(self) -> Pubkey:
        """Get the freeze authority of this token mint."""

    def decimals(self) -> u8:
        """Get the number of decimals for this token."""

    def supply(self) -> u64:
        """Get the amount of this token that exists."""

    def mint(self, authority: AccountWithKey, to: TokenAccount, amount: u64, signer: List[Any] = None):
        """
        Mint new tokens to a token account.

        @param authority: The account that owns this TokenMint. Must be an instruction signer or the account given by the `signer` param.
        @param to: The recipient TokenAccount.
        @param amount: How much (in *native* token units) to mint.
        @param signer: (Optional) seeds for the signature of a PDA.
        """

    def burn(self, authority: AccountWithKey, holder: TokenAccount, amount: u64, signer: List[Any] = None):
        """
        Burn tokens from a token account.

        @param authority: The account that owns the `holder` TokenAccount. Must be an instruction signer or the account given by the `signer` param.
        @param holder: The TokenAccount to burn from.
        @param amount: How much (in *native* token units) to burn.
        @param signer: (Optional) seeds for the signature of a PDA.
        """

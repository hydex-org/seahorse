from typing import *

T = TypeVar('T')
N = TypeVar('N')

class Array(Generic[T, N]):
    """
    A fixed-length array: contains type T and has size N.

    N must be known at compile-time, and may not be anything other than a non-negative integer literal. Example:

    ```
    # Good
    a: Array[u8, 4]

    # Bad
    N = 4
    a: Array[u8, N]
    ```
    """

    def __init__(iterable: Iterable[T], len: N) -> 'Array[T, N]':
        """
        Construct an array from an iterable and a length.

        The parameter len must be known at compile-time, and may not be anything other than a non-negative integer literal. Example:

        ```
        a = [0, 1, 2, 3]

        # Good
        Array(a, 4)
        # Compiles, but will definitely error at runtime
        Array(a, 5)

        # Bad (will not compile)
        a = [0, 1, 2, 3]
        Array(a, len(a))
        ```
        """

    def __getitem__(self, index: Any) -> T:
        """
        Index into this array.
        
        Like Python's native list type, performs wrapping indexing - if you pass in -1, you'll get the last element of the array.
        """

def array(*elements: T) -> Array[T, N]:
    """
    Create an array from a variadic list of elements. Example:

    ```
    # Array[u64, 3]
    array(u64(0), 1, 2)

    # Array[str, 4]
    array('seahorse', 'is', 'the', 'best!')
    ```
    """

class Enum:
    """
    A type that can have one of multiple named values.

    Note that unlike Rust enums, these cannot contain any data (other than the variant itself). Example:

    ```
    class MyEnum(Enum):
        ONE = 1
        TWO = 2
        THREE = 3

    @instruction
    def use_enum(code: MyEnum):
        if code == MyEnum.ONE:
            print(1)
        # ...
    ```
    """

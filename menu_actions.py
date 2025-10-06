from enum import IntEnum, auto

class Action(IntEnum):
    SAVE_NEW_ENTRY      = auto()
    SEARCH_BY_ID        = auto()
    PRINT_AGES_AVG      = auto()
    PRINT_ALL_NAMES     = auto()
    PRINT_ALL_IDS       = auto()
    PRINT_ALL_ENTRIES   = auto()
    PRINT_ENTRY_BY_INDEX  = auto()
    SAVE_ALL_DATA       = auto()
    EXIT                = auto()
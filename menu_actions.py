from enum import IntEnum

class Action(IntEnum):
    SAVE_NEW_ENTRY      = 1
    SEARCH_BY_ID        = 2
    PRINT_AGES_AVG      = 3
    PRINT_ALL_NAMES     = 4
    PRINT_ALL_IDS       = 5
    PRINT_ALL_ENTRIES   = 6
    PRINT_ENTRY_BY_IDX  = 7
    SAVE_ALL_DATA       = 8
    EXIT                = 9
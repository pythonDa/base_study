from enum import unique, Enum


@unique
class AppStatus(Enum):
    """
    枚举App的状态信息
    """
    Success = 'success'
    Failed = 'failed'

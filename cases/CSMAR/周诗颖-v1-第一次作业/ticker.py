"""
简单的ticker模块，提供格式化功能
"""

class FormatStrFormatter:
    """
    格式化字符串的格式化器
    """
    def __init__(self, fmt):
        self.fmt = fmt
    
    def __call__(self, x, pos=None):
        """Return the formatted label string."""
        return self.fmt % x 
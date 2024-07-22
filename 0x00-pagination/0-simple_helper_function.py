#!/usr/bin/env python3
"""
This module defines a function `index_range` for calculating
pagination indices.
"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Calculates the start and end index for a given page and page size.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        A tuple containing the start and end index for the current page.
    """
    if page <= 0:
        raise ValueError("Page number must be positive")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)

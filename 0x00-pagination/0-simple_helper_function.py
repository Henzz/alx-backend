#!/usr/bin/env python3

def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
        Returns a tuple containing the start and end index of the page
        for the given pagination parameters.

        vim
        Copy
        Page numbers are 1-indexed, i.e. the first page is page 1.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            tuple[int, int]: A tuple containing the start and end
            index of the page.
    """
    if page <= 0:
        raise ValueError("Page number must be positive")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)

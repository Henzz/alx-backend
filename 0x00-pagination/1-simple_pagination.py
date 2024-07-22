#!/usr/bin/env python3

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Returns a tuple containing the start and end index of the page
    for the given pagination parameters.

    Page numbers are 1-indexed, i.e. the first page is page 1.

    Args:
    page (int): The page number (1-indexed).
    page_size (int): The number of items per page.

    Returns:
    tuple[int, int]: A tuple containing the start and end index of the page.
    """
    # Calculate the start index of the current page
    start_index = (page - 1) * page_size

    # Calculate the end index of the current page
    end_index = start_index + page_size

    return (start_index, end_index)


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        # Initialize the dataset to None, it will be loaded when needed
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Returns the cached dataset.

        If the dataset has not been loaded yet, it will be loaded
        from the CSV file. The first row (header) of the CSV file is
        skipped, and the rest of the rows are returned.

        Returns:
        List[List]: The dataset as a list of rows.
        """
        if self.__dataset is None:
            # Load the dataset from the CSV file
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]

            # Skip the first row (header) and store the rest of the rows
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns the appropriate page of the dataset.

        Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

        Returns:
        List[List]: The appropriate page of the dataset.
        """
        # Ensure that the input arguments are valid
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # Get the full dataset
        dataset = self.dataset()

        # Calculate the start and end index of the current page
        start_index, end_index = index_range(page, page_size)

        # If the start index is out of range for the dataset,
        # return an empty list
        if start_index >= len(dataset):
            return []

        # Return the appropriate page of the dataset
        return dataset[start_index:end_index]

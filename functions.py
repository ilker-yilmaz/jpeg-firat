from __future__ import annotations

import os
import numpy as np

def create_directories(base_directory, folder_name):
    plt_save_directory = os.path.join(base_directory, folder_name, f"compressed-{folder_name}-plt")
    compressed_image_directory = os.path.join(base_directory, folder_name, f"compressed-{folder_name}-images")
    excel_file_directory = os.path.join(base_directory, folder_name, f"compressed-{folder_name}")

    os.makedirs(plt_save_directory, exist_ok=True)
    os.makedirs(compressed_image_directory, exist_ok=True)

    return plt_save_directory, compressed_image_directory, excel_file_directory


def calculate_psnr(img1: np.ndarray[np.uint8], img2: np.ndarray[np.uint8]) -> float:
                """Calculate PSNR using formula: PSNR = 20 * log10(MAX_I) - 10 * log10(MSE)"""
                mse = np.mean((img1 - img2) ** 2)
                psnr = 20 * np.log10(255 / np.sqrt(mse))
                return psnr

def number_of_elements(blocks: list[np.ndarray[np.int32]]) -> int:
                """Calculates the total number of elements in the grayscale JPEG encoded array"""
                total_elements = 0
                for block in blocks:
                    # Trim the trailing zeros from the 1D array
                    total_elements += np.trim_zeros(block, "b").size
                return total_elements

def total_number_of_elements(
                    blocks: list[np.ndarray[np.int32]]
                            | tuple[
                                list[np.ndarray[np.int32]],
                                list[np.ndarray[np.int32]],
                                list[np.ndarray[np.int32]],
                            ],
                    color: bool,
            ) -> int:
                """
                Calculates the total number of elements for both color and grayscale JPEG encoded arrays
                This is a utility function that will be used to calculate the compression ratio
                """
                total_elements = 0
                if color:
                    # Add the number of elements for each color channel
                    total_elements = (
                            number_of_elements(blocks[0])
                            + number_of_elements(blocks[1])
                            + number_of_elements(blocks[2])
                    )
                else:
                    total_elements = number_of_elements(blocks)
                return total_elements


def zigzag_scan(block: np.ndarray[np.int32]) -> np.ndarray[np.int32]:
                """
                Scans a block in zigzag order and return a 1D array
                Each block is assumed to be a square matrix
                """
                block_size = block.shape[0]
                zigzag_arr = np.concatenate(
                    [
                        np.diagonal(block[::-1, :], i)[:: (2 * (i % 2) - 1)]
                        for i in range(1 - block_size, block_size)
                    ]
                )
                return zigzag_arr


def zigzag_unscan(
                    zigzag_arr: np.ndarray[np.int32], block_size: int
            ) -> np.ndarray[np.float32]:
                """Unscans a 1D array in zigzag order and return a 2D array"""
                # Create an empty 2D array to store the unscanned values
                block = np.zeros((block_size, block_size), dtype=np.float32)
                x, y = 0, 0
                for num in zigzag_arr:
                    # Set the current value in the corresponding coordinate of the 2D array
                    block[x, y] = num

                    # Determine the direction to move based on the current position
                    # if the sum of the coordinates is even
                    if (x + y) % 2 == 0:
                        # if at the last column, move down one row
                        if y == block_size - 1:
                            x += 1
                        # if at the first row, move right one column
                        elif x == 0:
                            y += 1
                        # otherwise move up one row and right one column
                        else:
                            x -= 1
                            y += 1
                    # if the sum of the coordinates is odd
                    else:
                        # if at the last row, move right one column
                        if x == block_size - 1:
                            y += 1
                        # if at the first column, move down one row
                        elif y == 0:
                            x += 1
                        # otherwise move down one row and left one column
                        else:
                            x += 1
                            y -= 1

                # return the 2D array with the unscanned values
                return block

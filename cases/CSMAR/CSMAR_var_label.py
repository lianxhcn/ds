# Author: Yujun Lian
# Date: 2025/04/16
# Version: 1.0
# Description: This script processes the 'FileName[DES][xlsx].txt' file from CSMAR to extract variable labels and descriptions.
# encoding: utf-8

import os
def CSMAR_var_label(file_path):
    """
    Process the [DES][xlsx].txt file from CSMAR to extract variable labels and descriptions.

    Args:
        file_path (str): The file path of the [DES][xlsx].txt file.

    Returns:
        tuple: Two dictionaries:
            - dic_var_label: A dictionary mapping variable names to their Chinese labels.
            - dic_var_notes: A dictionary mapping variable names to their descriptions.
    """
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Initialize lists to store the split fields
    var_names = []
    var_labels = []
    var_descriptions = []

    # Process each line in the file
    for line in lines:
        if ' [' in line and '] - ' in line:
            # Extract the fields using the delimiters
            var_name = line.split(' [')[0].strip()
            var_label = line.split(' [')[1].split('] - ')[0].strip()
            var_description = line.split('] - ')[1].strip()
            # Append the extracted fields to their respective lists
            var_names.append(var_name)
            var_labels.append(var_label)
            var_descriptions.append(var_description)

    # Create dictionaries
    dic_var_label = dict(zip(var_names, var_labels))
    dic_var_notes = dict(zip(var_names, var_descriptions))

    return dic_var_label, dic_var_notes
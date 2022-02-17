import numpy as np
import pandas as pd

class FileParser:

    def __init__(self, path_to_file, file_name):
        self.path_to_file = path_to_file
        self.file_name = file_name



    # Reads instance file and initializes flows, distances and number of nodes
    def parse_file(self):
        distances = np.array([])
        flows = np.array([])
        lists_for_matrix = []
        flag = "num_nodes"

        with open(self.path_to_file + self.file_name) as data_file:

            for line in data_file:
                if line.strip():
                    strip = list(map(int, line.split()))
                    if len(strip) == 1 and flag == "num_nodes":
                        num_nodes = int(strip[0])
                        flag = "flows"
                    else:
                        lists_for_matrix.append(strip)
                        if len(lists_for_matrix) == num_nodes and flag == "flows":
                            flows = np.array(lists_for_matrix)
                            lists_for_matrix = []
                            flag = "distances"
                        elif len(lists_for_matrix) == num_nodes and flag == "distances":
                            distances = np.array(lists_for_matrix)

            return flows, distances, num_nodes

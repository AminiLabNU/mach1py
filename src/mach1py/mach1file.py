import pandas as pd
from typing import Optional, Union
import csv
from io import StringIO


class mach1file:

    def __init__(self, file_path: str) -> None:

        with open(file_path, "r") as f:
            content = f.read()
            f.close()

        val = mach1filevalidator(file_path, content)

        lines = content.splitlines()

        # load info

        info_idx_start = lines.index("<INFO>")

        info_idx_end = lines.index("<END INFO>")

        self.info = {}

        if info_idx_start >= 0 and info_idx_end < 0:
            raise ValueError("Info block not terminated")

        for line in lines[info_idx_start + 1 : info_idx_end]:

            # separate and clean key value pairs
            if ":" in line:
                key, value = line.split(":", 1)

                if "\t" in value:
                    value = value.lstrip("\t")

                self.info[key] = value

        # load action
        action = lines[info_idx_end + 1].strip("<").strip(">")
        self.info["Action"] = action

        data_idx_start = lines.index("<DATA>")

        for line in lines[info_idx_end + 2 : data_idx_start]:

            # separate and clean key value pairs
            if ":" in line:
                key, value = line.split(":", 1)

                if "\t" in value:
                    value = value.lstrip("\t")

                self.info[key] = value

        # load data

        data_idx_end = lines.index("<END DATA>")

        data_io = StringIO("\n".join(lines[data_idx_start + 1 : data_idx_end]))

        self.data = pd.read_csv(data_io, sep="\t")


class mach1filevalidator:

    def __init__(self, file_path: str, fdata: str) -> None:

        # check inputs
        if type(file_path) != str:
            raise TypeError("File path must be a string!")

        if type(fdata) != str:
            raise TypeError("File data not a string")

        # check if mach 1 file
        if fdata.find("<Mach-1 File>") < 0:
            raise ValueError("Mach-1 header not found, file is not Mach-1 data")

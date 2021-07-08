import csv
import glob
import os
from typing import List, Type

from .serializers.base_serializer import BaseSerializer
from .serializers.bank1_serializer import Bank1Serializer
from .serializers.bank2_serializer import Bank2Serializer
from .serializers.bank3_serializer import Bank3Serializer


class CSVApplication:

    def __init__(self, input_path_folder: str, result_folder: str, result_file_name: str):
        self.registered_serializers = [
            Bank1Serializer,
            Bank2Serializer,
            Bank3Serializer
        ]
        self.result_header = ["date", "transaction_type", "amount", "from", "to"]
        self.input_path_folder = input_path_folder
        self.result_folder = result_folder
        self.result_file_name = result_file_name

    def run(self) -> str:
        # scanning all csv files
        csv_files = glob.glob(f"{self.input_path_folder}/*.csv")
        result_message_buffer = ','.join(self.result_header) + '\n'
        print(f"Found files: {', '.join(csv_files) if csv_files else '-'}")

        if not os.path.exists(self.result_folder):
            os.makedirs(self.result_folder)

        # opening a new stream to write data into new .csv file
        with open(f"{self.result_folder}/{self.result_file_name}.csv", mode="w+", encoding="UTF-8") as banks_file:
            writer = csv.writer(banks_file)
            # adding csv header
            writer.writerow(self.result_header)
            # opening found files
            for file_name in csv_files:
                result_message_buffer += self.parse_file(writer, file_name)

        print(f"Processing completed!")
        return result_message_buffer

    def find_serializer(self, header: List) -> Type[BaseSerializer]:
        for cls in self.registered_serializers:
            if cls.header == header:
                return cls
        raise Exception(f"Serializer implementation not found! File header: {', '.join(header)}")

    def parse_file(self, writer, file_name: str):
        with open(file_name, mode="r", encoding="UTF-8") as csv_file:
            csv_reader = csv.reader(csv_file)
            result_message = ''
            try:
                # passing header in each file and getting serializer
                serializer_cls = self.find_serializer(next(csv_reader, None))
                for row in csv_reader:
                    line = serializer_cls.create_row(row)
                    writer.writerow(line)
                    result_message += ','.join(str(val) for val in line)+'\n'
            except Exception as ex:
                result_message = f"Error: {ex} (File: {os.path.basename(file_name)})"
                print(result_message)
            return result_message

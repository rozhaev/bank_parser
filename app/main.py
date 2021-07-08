from core.csv_application import CSVApplication
import sys

if __name__ == "__main__":
    app = CSVApplication(input_path_folder=sys.argv[1], result_folder=sys.argv[2], result_file_name=sys.argv[3])
    result = app.run()
    print(result)

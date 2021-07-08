# CSV Application for bank transactions
The project is written using only the python standard library (no third party dependencies).

## Project Structure
• app - Application folder

• csv - example files

• tests - test cases

### Launch

In the project folder run the script:
python app/main.py <'input folder with csv files'> <'output folder'> <'output file name'>

For example:
python app/main.py 'csv' 'result' 'banks'

### Tests

python -m unittest -v tests/test_parser.py

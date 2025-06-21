from abc import ABC, abstractmethod
import os

class DataSource(ABC):
    @abstractmethod
    def read_data(self):
        pass

class FileDataSource(DataSource):
    def __init__(self, file_path):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(script_dir, file_path)

    def read_data(self):
        try:
            print("Файл ищется по пути:", self.file_path)
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            return "Файл не найден."

class DatabaseDataSource:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def fetch_data(self):
        return f"Данные из базы по подключению: {self.connection_string}"

class DatabaseAdapter(DataSource):
    def __init__(self, database_source: DatabaseDataSource):
        self.database_source = database_source

    def read_data(self):
        return self.database_source.fetch_data()

file_source = FileDataSource("data.txt")
print(file_source.read_data())

database_source = DatabaseDataSource("database_connection_string")
database_adapter = DatabaseAdapter(database_source)
print(database_adapter.read_data())

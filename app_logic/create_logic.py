from app_files.files_handling import FileHandling


class CreateLogic:
    def create(self, data):
        fh = FileHandling()
        fh.create_and_save(data['document'] + '.ddb', data['columns'])

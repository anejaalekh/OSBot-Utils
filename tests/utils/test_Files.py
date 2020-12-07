from unittest                import TestCase
from osbot_utils.utils.Files import Files, path_combine, parent_folder, path_current


#todo add tests for other methods in Files class

class test_Files(TestCase):

    def test_folder_create(self):
        tmp_folder = '_tmp_folder'
        assert Files.folder_exists(tmp_folder) is False
        assert Files.folder_create(tmp_folder) == tmp_folder
        assert Files.folder_create(tmp_folder) == tmp_folder
        assert Files.folder_exists(tmp_folder) is True
        assert Files.folder_delete_all(tmp_folder) is True

    def test_file_extension(self):
        assert Files.file_extension('/path/to/somefile.ext') == '.ext'
        assert Files.file_extension('/path/to/somefile.'   ) == '.'
        assert Files.file_extension('/path/to/somefile..'  ) == '.'
        assert Files.file_extension('/path/to/somefile'    ) == ''
        assert Files.file_extension('/a/b.c/d'             ) == ''
        assert Files.file_extension('/a/b.c/.git'          ) == ''
        assert Files.file_extension('/a/b.c/a.git'         ) == '.git'
        assert Files.file_extension('/a/b.c/a.git.abc'     ) == '.abc'
        assert Files.file_extension(None)                    == ''

    def test_path_combine(self):
        assert path_combine('a', 'b') == f"{path_current()}/a/b"       # todo: add more use cases

    def test_temp_folder(self):
        assert Files.exists(Files.temp_folder())
        assert 'aa_'  in Files.temp_folder('_bb','aa_','/tmp')
from collections.abc import Mapping
import os


class Folder(Mapping):

    def __init__(self, path):
        #превратить в абсолютный путь
        if not os.path.isdir(path):
            raise FileNotFoundError(f'Such directory {path} not found')
        self.path = path
        self._content = {i: os.path.isdir(path + os.sep + i) for i in os.listdir(self.path)}

    def __getitem__(self, key):
        ipath = os.path.join(self.path, key)
        # проверить в словаре
        if not os.path.exists(ipath):
            raise FileNotFoundError(f'file or dir {ipath} not found')
        if self._content[key]:
            return type(self)(ipath)
        # pathlib pathobject
        with open(ipath) as f:
            return f.read()

    def __iter__(self):
        yield from self._content

    def __len__(self):
        return len(self._content)

    def __repr__(self):
        files = ', '.join(k for k, dir_ in self._content.items() if not dir_)
        dirs = ', '.join(k for k, dir_ in self._content.items() if dir_)
        return f'Files:\n {files} \n\nDirs:\n {dirs}'


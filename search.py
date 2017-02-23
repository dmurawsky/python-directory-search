import mmap
import os
from os import walk
import re

class SearchDir():
    def __init__(self, args):
        if 'directory' in args:
            if args['directory'] != '.':
                args['directory'] = os.getcwd()+'/'+args['directory']
            else:
                args['directory'] = os.getcwd()+'/'
        self._args = args
        if self.valid_args():
            self._firstlen = len(args['first'])
            self._secondlen = len(args['second'])
            self._cwdlen = len(os.getcwd())

    def get_files_in_dir(self):
        f = []
        for (dirpath, dirnames, filenames) in walk(self._args['directory']):
            f.append({'dir':dirpath, 'files':filenames})
        return f

    def get_search_text(self, path, indexes):
        f = open(path)
        s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        first = min(indexes)
        second = max(indexes) + max(self._firstlen, self._secondlen)
        return '... '+s[first:second].replace('\n', ' ')+' ...'

    def print_results(self):
        files = self.search_all_files()
        for f in files:
            if len(f['results']) > 0:
                print '\n\n'+f['file']+' :'
                for r in f['results']:
                    print '\t'+r
        print '\n'

    def search_all_files(self):
        files = []
        for fldr in self.get_files_in_dir():
            for f in fldr['files']:
                if f[-4:] == '.txt':
                    results = []
                    path = fldr['dir']+'/'+f
                    d = self.distances_between_strings(path)
                    for i in d:
                        results.append(self.get_search_text(path,i))
                    files.append({'file':path[self._cwdlen:], 'results':results})
        return files

    def search_file_for_string(self, path, str):
        f = open(path)
        s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        return [m.start() for m in re.finditer(self._args[str], s)]

    def distances_between_strings(self, file):
        first = self.search_file_for_string(file, 'first')
        second = self.search_file_for_string(file, 'second')
        return self.distances(first, second)

    def distances(self, first, second):
        dists = []
        for f in first:
            for s in second:
                d = abs(f-s)
                if d<=int(self._args['context']):
                    dists.append([f,s])
        return dists

    def valid_args(self):
        if 'directory' not in self._args:
            return False
        if 'context' not in self._args:
            return False
        if 'first' not in self._args:
            return False
        if 'second' not in self._args:
            return False
        return True

    def print_args(self):
        print self._args
        return
if __name__ == "__main__":
    import sys

    def get_input():
        directory = raw_input('Directory to search: ')
        first = raw_input('First search phrase: ')
        second = raw_input('Second search phrase: ')
        context = raw_input('Max distance between phrases: ')
        return {'directory':directory, 'context':context, 'first':first, 'second':second}

    def get_args():
        return {'directory':sys.argv[1], 'first':sys.argv[2], 'second':sys.argv[3], 'context':sys.argv[4]}

    def init(args):
        search = SearchDir(args)
        # search.print_args()
        search.print_results()

    if len(sys.argv)==1:
        init(get_input())
    elif len(sys.argv)==5:
        init(get_args())
    else:
        print 'Invalid syntax:\nInline Usage: python search.py <directory> <first_phrase> <second_phrase> <context>\nInput Usage: python search.py'

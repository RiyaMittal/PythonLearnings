class FileOwners:
    dict={}
    list_dir=list()
    @staticmethod
    def group_by_owners(files):
        list_dir = list ()
        for key in files:
            val=files[key]
            dict[val]=list_dir.append(key)
            for key1 in files:
                val1=files[key1]
                if key==key1:
                    pass
                else:
                    if val==val1:
                        dict[val]=list_dir.append(key1)
        return dict




files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(FileOwners.group_by_owners(files))

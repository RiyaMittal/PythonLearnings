class Path:
    @staticmethod
    def change_dir(orig_path,new_path):
         current_path_hie = []
         current_path_hie = orig_path.split ( '/' )
         print current_path_hie
         dir=list()
         dir=new_path.split('/')
         for item in dir:
            if item=='..':
                current_path_hie.pop(-1)
            else:
                current_path_hie.append(item)
         print current_path_hie
         print "/".join(i for i in current_path_hie )


path=Path.change_dir('/a/b/c/d','../x')





files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}

print files.get('Input.txt')

value_list=[]
new_dict=dict()
value_list=files.values()

print value_list
for each_value in value_list:
    for new_each_value in value_list:
        if (each_value==new_each_value)& (value_list.index('new_each_value')<>value_list.index(each_value):
            new_dict[]



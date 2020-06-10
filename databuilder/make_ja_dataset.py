import os
import yaml

class MakeJaDataset:
    def __init__(self):
        self.POS = 5
        self.NEG = 1
        params = self.load_params()
        self.DATA_DIR = params['TMP_DATA_DIR']
        self.DOMAIN_A = params['DATA_DOMAIN_A']
        self.DOMAIN_B = params['DATA_DOMAIN_B']
        self.OUTPUT = params['TMP_DATA']

    def load_params(self):
        with open('./databuilder/params.yml', 'r') as f:
            params = yaml.safe_load(f)
        return params


    def make_dataset(self, filepath: str, label: int):
        '''{"star": label, "text": "text"}'''
        data = []
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                data.append('{{"score": {label}, "review": "{text}"}}'.format(label=label, text=line.rstrip('\n').replace('"', '')))

        return data

    def build_ja_data(self):
        data = self.make_dataset(filepath=os.path.join(self.DATA_DIR, self.DOMAIN_A), label=5.0)
        data += self.make_dataset(filepath=os.path.join(self.DATA_DIR, self.DOMAIN_B), label=1.0)
        with open(os.path.join(self.DATA_DIR, self.OUTPUT), 'w', encoding='utf-8') as f:
            f.write('\n'.join(data))
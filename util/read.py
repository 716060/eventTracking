import csv
import yaml
import json
import pandas as pd
import numpy as np

class Read:

    def readCsv(self, path):
        csv_result = []
        with open(path, 'r') as f:
            csv_reader = csv.DictReader(f, delimiter='\t')
            for row in csv_reader:
                csv_result.append(row)
        return csv_result

    def readYaml(self, path):
        with open(path, 'r') as f:
            return yaml.safe_load(f)

    def readExcel(self, path):
        df = pd.read_excel(path)
        if "fields" in df.columns and not df["fields"].isnull().all():
            df['fields'] = df['fields'].apply(lambda x: json.loads(x) if isinstance(x, str) else x)
        return df.to_dict('records')


if __name__ == '__main__':
    # print(Read().readYaml('../resources/applicationContext.yaml'))
    print(Read().readExcel("../file/testCase.xlsx"))
    # print(Read().readCsv("../file/EventTracking.csv"))




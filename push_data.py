import os
import json
import sys


from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL=os.getenv("MonGO_DB_URL")

print(MONGO_DB_URL)


# For trusted certificate authorities

import certifi
ca=certifi.where()

import pandas as pd
import numpy as np
import pymongo


class NetworkDataExtract():

    def __init__(self) :
        try :

            pass

        except Exception as e :

            raise RuntimeError
    
    def csv_tojson_convertor(self, file_path) :

        try:
            data=pd.read_csv(file_path)
            print(data)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records

        except Exception as e :

            raise RuntimeError

    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records

            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]
            
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            return(len(self.records))
        

        except Exception as e :

            raise RuntimeError
        

if __name__ == "__main__":

    FILE_PATH = r"D:\MLops_e2e\networksecurity\Network_Data\phisingData.csv"

    print(FILE_PATH)
    
    DATABASE="SABYAAI"

    Collection ="NetworkData"

    networkobj = NetworkDataExtract()

    records= networkobj.csv_tojson_convertor(file_path=FILE_PATH)

    print(records)

    no_of_records =networkobj.insert_data_mongodb(records,DATABASE,Collection)
    
    print(no_of_records)






            
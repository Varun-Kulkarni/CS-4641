import os
import pandas


def load_HAM10000_metadata(data_path):
    metadata_fname = "HAM10000_metadata.csv"
    metadata_fpath = os.path.join(data_path, metadata_fname)
    if os.path.exists(metadata_fpath):
        print("Found HAM10000 metadata file, loading into pandas df")

        df = pandas.read_csv(metadata_fpath)
        print(df)
        return df

    else:
        raise FileNotFoundError(f"Could not find HAM100000 metadata at \"{metadata_fpath}\"")

def load_HAM10000_L(data_path, size_8=True, size_64=False):
    hmnist8_8_L = None
    hmnist64_64_L = None 

    if size_8:
        file_name = "hmnist_8_8_L.csv"
        file_path = os.path.join(data_path, file_name)

        if os.path.exists(file_path):
            print("Found HAM10000 luminescence images in size 8x8")

            hmnist8_8_L = pandas.read_csv(file_path)
            print(hmnist8_8_L)
        else:
            raise FileNotFoundError(f"Could not find luminescence image csv at \"{file_path}\"")

    return hmnist8_8_L, hmnist64_64_L


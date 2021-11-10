import os
import pandas


def load_HAM10000_metadata(data_path, verbose=False):
    metadata_fname = "HAM10000_metadata.csv"
    metadata_fpath = os.path.join(data_path, metadata_fname)
    if os.path.exists(metadata_fpath):
        print("Found HAM10000 metadata file, loading into pandas df")

        df = pandas.read_csv(metadata_fpath)
        print("Done")
        return df

    else:
        raise FileNotFoundError(f"Could not find HAM100000 metadata at \"{metadata_fpath}\"")

def load_HAM10000_L(data_path, size_8=True, size_28=False):
    hmnist8_8_L = None
    hmnist28_28_L = None 

    if size_8:
        file_name = "hmnist_8_8_L.csv"
        file_path = os.path.join(data_path, file_name)

        if os.path.exists(file_path):
            print("Found HAM10000 luminescence images in size 8x8")

            hmnist8_8_L = pandas.read_csv(file_path)
            # print(hmnist8_8_L.head(3))
            print("Done")
        else:
            raise FileNotFoundError(f"Could not find luminescence image csv at \"{file_path}\"")

    return hmnist8_8_L, hmnist28_28_L

def load_HAM10000_RGB(data_path, prints, size_28=True, size_8=False):
    hmnist_28_28_RGB = None 

    if size_28:
        file_name="hmnist_28_28_RGB.csv"
        file_path = os.path.join(data_path, file_name)

        if os.path.exists(file_path):
            print("Found HAM10000 RGB images in size 28x28, reading into df")
            hmnist_28_28_RGB = pandas.read_csv(file_path)
            print("Done")
            if prints:
                print(hmnist_28_28_RGB.head())
        else:
            raise FileNotFoundError(f"Could not RGB images \"{file_path}\"")
    return hmnist_28_28_RGB
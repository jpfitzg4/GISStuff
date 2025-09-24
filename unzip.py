import zipfile, os, glob

zip_dir = r"C:\DEM"                 # folder with your zip files
out_dir = r"C:\DEMEx"               # single output folder

os.makedirs(out_dir, exist_ok=True)

for zfile in glob.glob(os.path.join(zip_dir, "*.zip")):
    with zipfile.ZipFile(zfile, 'r') as zip_ref:
        zip_ref.extractall(out_dir)

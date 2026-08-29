import pandas as pd
import tableauserverclient as TSC

import pantab 
import zipfile

from pathlib import Path 

def download_tdsx(server: TSC.Server, ds_id: str, file_path: Path | None = None) -> Path :
    try:
        ds = server.datasources
        res = ds.download(ds_id, file_path)
        download_path = Path(res)
        
        if not download_path.exists():
            raise Exception(f"Failed to download datasource {ds_id}: File does not exist after download.")
        
        return download_path
    except Exception as e:
        raise Exception(f"Failed to download datasource {ds_id}: {e}")

def get_hyper_from_tdsx(download_path: Path, ds_id: str) -> Path:

    if not download_path.exists():
        raise Exception(f"Failed to download datasource {ds_id}: File does not exist after download.")
    # prenet + tdsx_path.stem_extraido
    extract_dir = download_path.parent / f"{download_path.stem}_extracted"
    extract_dir.mkdir(parents=True, exist_ok=True)
    
    with zipfile.ZipFile(download_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    
    hyper_file = extract_dir / "Data" / "Extracts" / "hyper_0.hyper"

    if not hyper_file.exists():
        raise FileNotFoundError(
            f"No .hyper file found in datasource {ds_id}."
        )
    return hyper_file

def read_hyper(hyper_file: Path, ds_id: str) -> pd.DataFrame:
    tables = pantab.frames_from_hyper(hyper_file) 
    if not tables:
        raise Exception(f"No tables found in the .hyper file of datasource {ds_id}.")
    
    # tables é um dicionario de tablelas, mas precisamos o de uma 
    extract = tables.get(('Extract', 'Extract'))
    if isinstance(extract, pd.DataFrame):
        return extract
    else: 
        raise Exception(f"Extract table not found in the .hyper file of datasource {ds_id}.")


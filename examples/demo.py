"""Demo for Finance Quant Compression Tool."""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import finance_quant_compressor

print("Finance Quant Compression Tool", "v" + finance_quant_compressor.__version__)
print("modules:", [m for m in dir(finance_quant_compressor) if not m.startswith('_')])

import pandas as pd
import sys 
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("Olá mundo Python!")
print("Data: 23/08/2024")
print("Horário: 22:26")
# Elimina todo rastro del keylogger y archivos generados

echo "===== Cleanup: eliminando archivos del keylogger ====="

# Archivos de código
rm -f keylogger.py
rm -f keylogger_core.py
rm -f file_manager.py
rm -f email_handler.py

# Archivos de registro generados
rm -f output.txt
rm -f output_temporal.txt

# Caché de Python
rm -f __pycache__/*.*
rm -f *.pyc

echo "Archivos eliminados."

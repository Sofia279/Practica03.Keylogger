## Práctica 03: Keylogger Remoto en Python


### 1. Integrantes:
- 319062359
- 318229687
- 318309877
- 316031536

### 2. Herramientas y librerías:
- **Python 3.8+**  
- **bash** (para `cleanup.sh`)  
- **pyxhook** (captura global de teclado en Linux/Unix)  
- **pyperclip** (acceso al portapapeles para detectar pegado con Ctrl+V)  
- **yagmail** (envío de correos vía SMTP/Gmail)  
- **(Opcional)** `keybinder` o `keyboard` si se quisiera portar a otras plataformas, pero en esta práctica usamos `pyxhook`.  
- **smtplib** (podría usarse como alternativa, aunque aquí empleamos `yagmail`).  

Para instalar dependencias en tu sistema (Linux/Unix):

```bash
pip install pyxhook pyperclip yagmail
```

### 3. Ejecución:

- Para iniciar el keylogger:
```bash
python3 keylogger.py

```
- Primero permisos de ejecución:
```bash
chmod +x cleanup.sh

```
- Para eliminar el keylogger y todos sus archivos generados:
```bash
./cleanup.sh
```
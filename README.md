# Setup

## Entorno virtual

- Descargar el entorno virtual virtual env
    
    ```bash
    pip install virtualenv
    ```
    
- Inicia el entorno virtual en la carpeta actual
    
    ```bash
    virtualenv .
    ```
    
    - Posibles errores:
        
        ![error1.jpeg](Setup%20103f1794d57c4a4b91c5c68e9e20108e/error1.jpeg)
        
        Puedes intentar con: 
        
        ```bash
        python -m venv
        ```
        
- Abre tu entorno virtual
    
    ```bash
    source Scripts/activate
    ```
    

## Instalar librerías

- Textblob
    
    ```bash
    pip install -U textblob
    python -m textblob.download_corpora
    ```
    
- seaborn
    
    ```bash
    pip install seaborn 
    ```
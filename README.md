**RGB to Json LIST**

Una herramienta simple para generar listados de colores en formato JSON, perfectos para crear librerías personalizadas para proyectos de Python. 🎨

--------------------------------------------------

🚀 **Descripción**

RGB to Json LIST es una utilidad diseñada para quienes necesitan un listado estructurado de colores RGB con nombres personalizados. Con esta herramienta, puedes generar fácilmente tu propia librería de colores en formato JSON, ideal para proyectos de diseño, desarrollo web o cualquier aplicación que requiera una amplia gama de colores.

    Creé este programa porque necesitaba un listado grande de colores RGB para un proyecto reciente. Aunque originalmente intenté usarlo como una librería personalizada, 
    descubrí que al incluir la lista completa directamente en el código, el proyecto funcionaba perfectamente. Este programa simplifica esa tarea y puede ser útil para muchos otros.

--------------------------------------------------

✨ **Características**

  - Genera listados de colores RGB con nombres personalizados.
  - Exporta los listados en formato JSON, fácil de integrar en otros proyectos.
  - Útil para diseñadores, desarrolladores y quienes buscan librerías de colores personalizadas.
  - Compatible con Python 3.10 en adelante.
    
💡 Ejemplo de Uso
¡Es súper fácil de usar! Simplemente ingresa los códigos RGB y asigna nombres personalizados. Aquí tienes un ejemplo de cómo se vería el JSON generado:

    [
      { "name": "Sky Blue", "rgb": [135, 206, 235] },
      { "name": "Crimson Red", "rgb": [220, 20, 60] },
      { "name": "Forest Green", "rgb": [34, 139, 34] }
    ]
    
Así puedes usarlo en un proyecto de Python:

    import json
    
    # Cargar la librería de colores
    with open('colors.json', 'r') as file:
        colors = json.load(file)
    
    # Usar un color específico
    sky_blue = colors[0]['rgb']
    print(f"El color Sky Blue es: {sky_blue}")

--------------------------------------------------
  
📦 **Instalación**

  1. Asegúrate de tener Python 3.10 o superior instalado.

  2. Clona este repositorio:
     
    git clone https://github.com/micropixelstudiocl/RGB-to-Json-LIST.git
    cd RGB-to-Json-LIST

  4. Ejecuta el script para generar tu lista de colores.

--------------------------------------------------

🛠 **Próximos Pasos**

Actualmente, la herramienta requiere que el script sea ejecutado manualmente. En futuras versiones, planeo:

  - Convertirlo en un ejecutable para facilitar su uso.
  - Mejorar la interfaz para hacerlo más interactivo.
  - Incluir opciones de categorización de colores.

--------------------------------------------------
  
🤝 **Contribuciones**

¡Contribuciones son bienvenidas! Si tienes ideas o mejoras, no dudes en abrir un issue o enviar un pull request.

--------------------------------------------------

📄 Licencia

Este proyecto está bajo la licencia MIT. Siéntete libre de usarlo, modificarlo y compartirlo.

--------------------------------------------------

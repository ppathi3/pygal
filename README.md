# Pygal Customization Guide
## Installation steps
1. Clone the repository: 
```bash
git clone https://github.com/ppathi3/pygal.git
```
2. Go to the project directory: 
```bash
cd path/to/pygal
```
3. Ensure you have setup tools and wheel installed:
```bash
pip install setuptools wheel
```
4. Create the distribution package:
```bash
python setup.py bdist_wheel
```
NOTE: If you run into any issues regarding missing packages, please install the missing libraries as specified. This command will generate the distribution files (.whl file) in the dist directory.
Now you can install the library using the .whl file by navigating to the dist directory: cd dist
5. Install the .whl file using pip:
```bash
pip install pygal-3.0.4-py3-none-any.whl
```
6. Install all the required libraries present inside the docs folder by navigating to the docs using:
```bash
cd docs
pip install -r requirements.txt
```
7. Test if the installation works fine
8. You can find sample.ipynb file in the project, restart the kernel and run this file to check if the bar chart is rendered without any issues and your changes are reflected.


## File structure
1. The pygal repo consists of a pygal/graph folder in which you can find all the files consisting of the code responsible for rendering multiple visualisations.
2. All the major changes were made in the bar.py file and xy.py file for the bar chart and the scatter plot customization implementations.
## Walking through the examples
1. I’ve implemented two main features:
    a. Custom spacing
    b. Texture
2. The custom spacing feature lets the user provide an array of values where the user can provide the spacing that he/she wants to provide between the graph bars.
3. The texture feature lets the user provide an array of image URLs for each bar to which he/she wants to add a texture to.
4. There's another feature that allows the user to provide a shape data and it builds the bar chart accordingly.
   ## How to use the feature?
   Examples:
   ![image](https://github.com/user-attachments/assets/2473bd7b-5db8-48f8-a999-1028a6545ff5)

    ### Specifying bar spacing values
    ```bash
    bar_spacing = [0.1, 0.15, 0.1, 0.15, 0.2, 0.15, 0.1, 0.15, 0.2, 0.15, 0.1, 0.15]  # Adjust spacing values for each bar as needed

    bar_chart = pygal.Bar(bar_spacing=bar_spacing)
    ```
   ![image](https://github.com/user-attachments/assets/85d6fcb4-c0a1-4fd8-bb7a-07533643fef8)

    ### Specifying bar spacing values
    ```bash
    bar_spacing = [0.1, 0.15, 0.1, 0.15, 0.2, 0.15, 0.1, 0.15, 0.2, 0.15, 0.1, 0.15]  # Adjust spacing values for each bar as needed

    bar_chart = pygal.Bar(bar_spacing=bar_spacing, bar_images=['https://docs.tibco.com/pub/sfire-cloud/12.4.0/doc/html/en-US/TIB_sfire_client/client/images/stacked_100__bar_chart_intro.png', 'https://img.freepik.com/free-vector/abstract-colorful-soft-watercolor-texture-background_1035-18958.jpg', 'https://t4.ftcdn.net/jpg/06/06/89/91/360_F_606899189_2snQer28Ka7oAUQp65vraexOsaBnNWXb.jpg', 'https://images.hdqwalls.com/wallpapers/colorful-abstract-texture-g6.jpg', 'https://cdn.pixabay.com/photo/2017/06/10/09/43/colorful-background-2389472_960_720.jpg', 'https://p4.wallpaperbetter.com/wallpaper/1021/131/727/colors-texture-pattern-artwork-wallpaper-preview.jpg', 'https://docs.tibco.com/pub/sfire-cloud/12.4.0/doc/html/en-US/TIB_sfire_client/client/images/stacked_100__bar_chart_intro.png', 'https://img.freepik.com/free-vector/abstract-colorful-soft-watercolor-texture-background_1035-18958.jpg', 'https://t4.ftcdn.net/jpg/06/06/89/91/360_F_606899189_2snQer28Ka7oAUQp65vraexOsaBnNWXb.jpg', 'https://images.hdqwalls.com/wallpapers/colorful-abstract-texture-g6.jpg', 'https://cdn.pixabay.com/photo/2017/06/10/09/43/colorful-background-2389472_960_720.jpg', 'https://p4.wallpaperbetter.com/wallpaper/1021/131/727/colors-texture-pattern-artwork-wallpaper-preview.jpg'])
    ```

   ![image](https://github.com/user-attachments/assets/2cf56e85-b4c9-45b6-a580-5a68fcf987a8)

    ```bash
    bar_chart = pygal.Bar(bar_images=['https://docs.tibco.com/pub/sfire-cloud/12.4.0/doc/html/en-US/TIB_sfire_client/client/images/stacked_100__bar_chart_intro.png', 'https://img.freepik.com/free-vector/abstract-colorful-soft-watercolor-texture-background_1035-18958.jpg', 'https://t4.ftcdn.net/jpg/06/06/89/91/360_F_606899189_2snQer28Ka7oAUQp65vraexOsaBnNWXb.jpg', 'https://images.hdqwalls.com/wallpapers/colorful-abstract-texture-g6.jpg', 'https://cdn.pixabay.com/photo/2017/06/10/09/43/colorful-background-2389472_960_720.jpg', 'https://p4.wallpaperbetter.com/wallpaper/1021/131/727/colors-texture-pattern-artwork-wallpaper-preview.jpg', 'https://docs.tibco.com/pub/sfire-cloud/12.4.0/doc/html/en-US/TIB_sfire_client/client/images/stacked_100__bar_chart_intro.png', 'https://img.freepik.com/free-vector/abstract-colorful-soft-watercolor-texture-background_1035-18958.jpg', 'https://t4.ftcdn.net/jpg/06/06/89/91/360_F_606899189_2snQer28Ka7oAUQp65vraexOsaBnNWXb.jpg', 'https://images.hdqwalls.com/wallpapers/colorful-abstract-texture-g6.jpg', 'https://cdn.pixabay.com/photo/2017/06/10/09/43/colorful-background-2389472_960_720.jpg', 'https://p4.wallpaperbetter.com/wallpaper/1021/131/727/colors-texture-pattern-artwork-wallpaper-preview.jpg'], custom_shape=None)

    ```
   ![image](https://github.com/user-attachments/assets/f3ae4e99-97aa-4349-92c0-74d932f536cc)

    ```bash
    # Specifying file path for reading shape data from CSV
    file_path = 'shape_data.csv'
    coordinates = read_shape_data_from_csv(file_path)
    print(coordinates)

    # Specifying custom shape object
    custom_shape = {            
    'tag': 'polygon',
    'attrib': {
        'points': coordinates,
        'class': 'custom-shape'
        }
    }
    bar_chart = pygal.Bar(custom_shape=custom_shape)
    ```
   ![image](https://github.com/user-attachments/assets/e04ad966-2eb6-4ad6-a585-18d2823b3ed8)

    ```bash
    # Specify a shape among rect/polygon/circle to render the scatter chart
    xy_chart = pygal.XY(stroke=False, shape='rect')
    ```
   
   
## Recompiling the updated version and testing the new changes
1. Every time we make a change to the repo, ensure to create a new distribution package using:
```bash
python setup.py bdist_wheel
```
2. Now you can install the library using the .whl file by navigating to the dist directory:
```bash
cd dist
```
3. Install the .whl file using pip:
```bash
pip install pygal-3.0.4-py3-none-any.whl
```
Restart the kernel and run your file to check if your changes are reflected.

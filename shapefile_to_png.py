import geopandas as gpd
import matplotlib.pyplot as plt
import os

input_shapefile = input("Enter the path to the shapefile: ")
output_directory = input("Enter the directory path where you want to save the PNG files: ")
column_name = input("Enter the column name based on which you want to name the output files: ")

gdf = gpd.read_file(input_shapefile)


# CLEAN THE FILE NAMES
def clean_filename(name):
    # Replacing problematic characters with underscores
    return name.replace('/', '_').replace('\\', '_').replace(':', '_').replace('*', '_').replace('?', '_').replace('"', '_').replace('<', '_').replace('>', '_').replace('|', '_')

# Iterating over each row in the GeoDataFrame
i = 1
for index, row in gdf.iterrows():
    print(f"Progress: {i} of {len(gdf)}")
    print(f"Making PNG of: {row[column_name]}")

    geometry = row.geometry
    
    # Extracting the value from the user-input column for the filename
    filename = clean_filename(row[column_name]) + '.png'
    
    # Creating a temporary GeoDataFrame for plotting the geometry
    gdf_temp = gpd.GeoDataFrame({'geometry': [geometry]})
    
    # Creating a new figure and axis
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Ploting the geometry on the axis
    gdf_temp.plot(ax=ax)
    
    # Setting title if necessary
    ax.set_title(row[column_name])
    ax.axis('off')
    
    # Saving the figure as PNG in the specified directory
    filepath = os.path.join(output_directory, filename)
    plt.savefig(filepath, dpi=300, bbox_inches='tight')
    
    # Releasing some memory.
    plt.close()

    i = i + 1

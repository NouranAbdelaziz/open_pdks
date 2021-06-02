# Device Generation in Klayout using PCells

The aim of this project is to automatically generate Sky130A devices in Klayout just like in magic. This is achieved through using PCells property in klayout in which you can write a python script for a cell, and then you will be able to get an instance from it automatically using the Pcell menu. Also, the height and width of the device are adjustable and are given as parameters to the PCell.

# Generated devices and links to python script:
| Device Name                    | Link to File                          |
| ------------------------------ | --------------------------------------|
| sky130_fd_pr__res_high_po_0p35 | [sky130_fd_pr__res_high_po_0p35.lym]()|
| sky130_fd_pr__res_generic_nd   | [sky130_fd_pr__res_generic_nd.lym]()  |


# Device generation steps:

1. Download the devices files as well as “Create_Library.py” file  
2. Place all the files in the path : /Klayout/pymacros/ 
3. Open Klayout in editor mode
4. From “Macros” select “Macro Development”
![image](https://user-images.githubusercontent.com/79912650/120478572-489ded00-c3ad-11eb-9e38-13a3f5c7aa48.png)
5. From “Local” open “Create_Library” file and run it using “Run current script” button
6. Select C instance icon
7. From the “Library” drop down box select “Sky130 - sky130_fd_pr__”
8. From “Cell” choose the device you want to generate
9. From “PCell” tab you can adjust the width and height of the cell (make sure to enter them in database units)
10. Then press “OK” and now you can place the cell wherever you want. 


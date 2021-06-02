# Device Generation in Klayout using PCells

The aim of this project is to automatically generate Sky130A devices in Klayout just like in magic. This is achieved through using PCells property in klayout in which you can write a python script for a cell, and then you will be able to get an instance from it automatically using the Pcell menu. Also, the length and width of the device are adjustable and are given as parameters to the PCell.

**Generated devices and links to python script:**
| Device Name                    | Link to File                          |
| ------------------------------ | --------------------------------------|
| sky130_fd_pr__res_high_po_0p35 | [sky130_fd_pr__res_high_po_0p35.lym]()|
| sky130_fd_pr__res_generic_nd   | [sky130_fd_pr__res_generic_nd.lym]()  |


**Device generation steps:**

1. Download the devices files as well as “Create_Library.py” file  
2. Place all the files in the path : /Klayout/pymacros/ 
3. Open Klayout in editor mode
4. Select “Macros” from the menu bar then select “Macro Development”
    ![image](https://user-images.githubusercontent.com/79912650/120478572-489ded00-c3ad-11eb-9e38-13a3f5c7aa48.png)
    
5. From “Local” open “Create_Library” file and run it using “Run current script” button
    ![image](https://user-images.githubusercontent.com/79912650/120478859-97e41d80-c3ad-11eb-9b9e-0a8e83672d7b.png)
    
6. Select C instance icon from the toolbar 
    ![image](https://user-images.githubusercontent.com/79912650/120478951-afbba180-c3ad-11eb-9482-c2e3ad261db2.png)
    
7. From the “Library” drop down box select “Sky130 - sky130_fd_pr__”
    ![image](https://user-images.githubusercontent.com/79912650/120479062-ccf07000-c3ad-11eb-8983-40f17f3076f7.png)
    
8. From “Cell” choose the device you want to generate
    ![image](https://user-images.githubusercontent.com/79912650/120479232-fe693b80-c3ad-11eb-817d-c84b54e3fecc.png)
    
9. From “PCell” tab you can adjust the length and width of the cell (make sure to enter them in database units)
    ![image](https://user-images.githubusercontent.com/79912650/120479390-32446100-c3ae-11eb-8d23-872fbace0c0d.png)
    
10. Then press “OK” and now you can place the cell wherever you want. 
    ![image](https://user-images.githubusercontent.com/79912650/120479699-894a3600-c3ae-11eb-920a-4737bec7ec73.png)




# Enter your Python code here
import math

extra_width = 1000-420
if(extra_width==0):
  licons_num = 1
else:
  licons_num = math.floor(extra_width/170)
x_left = -85 - ((licons_num-1)*170)
x_right = x_left + 170
print(licons_num)

for i in range(licons_num):
  print(x_left)
  print(x_right)
  x_left = x_right + 170
  x_right = x_left + 170

class MyLib(pya.Library):
  """
  The library where we will put the PCell into 
  """

  def __init__(self):
  
    # Set the description
    self.description = "sky130_fd_pr__"
    
    # Create the PCell declarations
    self.layout().register_pcell("sky130_fd_pr__res_generic_nd", sky130_fd_pr__res_generic_nd())
    self.layout().register_pcell("sky130_fd_pr__res_high_po_0p35", sky130_fd_pr__res_high_po_0p35())
    self.layout().register_pcell("sky130_fd_pr__res_generic_m1", sky130_fd_pr__res_generic_m1())
    self.layout().register_pcell("sky130_fd_pr__nfet01v8", sky130_fd_pr__nfet01v8())
    # That would be the place to put in more PCells ...
    
    # Register us with the name "MyLib".
    # If a library with that name already existed, it will be replaced then.
    self.register("Sky 130")


# Instantiate and register the library
MyLib()
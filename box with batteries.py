import Part
from FreeCAD import Base;

# ������� ��������� � ������
document = App.newDocument('FreeCAD filler test')

batteryWidth = float(300.0)                             # ������ ���� (x)
batteryDepth = float(300.0)                             # ������� ���� (y)
batteryHeight = float(300.0)                            # ������ ���� (z)
row_betweenBattery = float(50.0)                        # ���������� ����� ���������
boxThickness = float(20.0)                              # ������� ������ ������
additionalHeight = float(50.0)                          # + � ������ ������ ������ �� ������������ 

# ����� ������ ������ (x, y, z)
wallLeftWidth = float(boxThickness)                     # ������ (x)
wallLeftDepth = float((5*(batteryDepth)+
                row_betweenBattery*6)
                )                                       # ������� (y)
wallLeftHeight = float(batteryHeight+additionalHeight)  # ������ (z)

# ���������� ����� ������ ������  (x,y,z)
LeftWall_X = float((-batteryWidth - 
             2*row_betweenBattery-
             boxThickness)
             )
LeftWall_Y = float(-row_betweenBattery)
LeftWall_Z = float(0.0)

# ����� ����� ������ ������
boxShape = Part.makeBox(wallLeftWidth, wallLeftDepth, 
           wallLeftHeight, Base.Vector(LeftWall_X, 
           LeftWall_Y, LeftWall_Z)
           )
# ������ ��� ����������� ����� 
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape


# ������ ������ ������ (x, y, z)
wallRightWidth = float(boxThickness)                    # ������ (x)
wallRightDepth = float((5*(batteryDepth)+ 
                 row_betweenBattery*6)
                 )                                      # ������� (y)
wallRightHeight = float((batteryHeight+
                  additionalHeight)
                  )                                     # ������ (z)

# ���������� ������ ������ ������ (x,y,z)
RightWall_X = float(batteryWidth+row_betweenBattery)
RightWall_Y = float(-row_betweenBattery)
RightWall_Z = float(0.0)

# ����� ������ ������ ������
boxShape = Part.makeBox(wallRightWidth, wallRightDepth, 
           wallRightHeight, Base.Vector
           (RightWall_X, RightWall_Y, RightWall_Z)
           )
# ������ ��� ����������� ����� 
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape


# �������� ������� ������ (x, y, z)
wallAnteriortWidth = float((2*batteryWidth+
                     row_betweenBattery*
                     3 + 2*boxThickness)
                     )                                  # ������ (x)
wallAnteriortDepth = float(boxThickness)                # ������� (y)
wallAnteriortHeight = float((batteryHeight+
                      additionalHeight)
                      )                                 # ������ (z)

# ���������� �������� ������ ������  (x,y,z)
AnteriortWall_X = float((-batteryWidth - 
                  2*row_betweenBattery-
                  boxThickness)
                  )
AnteriortWall_Y = float((-row_betweenBattery-
                  boxThickness)
                  )
AnteriortWall_Z = float(0.0)

# ����� �������� ������ ������
boxShape = Part.makeBox(wallAnteriortWidth, 
           wallAnteriortDepth, wallAnteriortHeight, 
           Base.Vector(AnteriortWall_X, 
           AnteriortWall_Y, 
           AnteriortWall_Z)
           )
# ������ ��� ����������� ����� 
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape


# ������ ������� ������ (x, y, z)
wallPosteriorWidth = float((2*batteryWidth+
                     row_betweenBattery*3 +
                     2*boxThickness)
                     )                                   # ������ (x)
wallPosteriorDepth = float(boxThickness)                 # ������� (y)
wallPosteriorHeight = float((batteryHeight+
                      additionalHeight)
                      )                                  # ������ (z)

# ���������� ������ ������ ������  (x,y,z)
PosteriorWall_X = float((-batteryWidth - 
                  2*row_betweenBattery-
                  boxThickness)
                  )
PosteriorWall_Y = float((5*row_betweenBattery + 
                  5*batteryDepth)
                  )
PosteriorWall_Z = float(0.0)

# ����� ������ ������ ������
boxShape = Part.makeBox(wallPosteriorWidth, 
           wallPosteriorDepth, wallPosteriorHeight, 
           Base.Vector(PosteriorWall_X, 
           PosteriorWall_Y, PosteriorWall_Z)
           )
# ������ ��� ����������� ����� 
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape


# ������ ������� ������ (x, y, z)
wallLowerWidth = float((2*batteryWidth+
                 row_betweenBattery*3 +
                 2*boxThickness)
                 )                                         # ������ (x)
wallLowerDepth = float(6*row_betweenBattery + 
                 + 5*batteryDepth + 2*boxThickness
                 )                                         # ������� (y)
wallLowerHeight = float(boxThickness)                      # ������ (z)

# ���������� ������ ������ ������  (x,y,z)
LowerWall_X = float((-batteryWidth - 
              2*row_betweenBattery-
              boxThickness)
              )
LowerWall_Y = float((-row_betweenBattery-
              boxThickness)
              )
LowerWall_Z = float(-boxThickness) 

# ����� ������ ������ ������
boxShape = Part.makeBox(wallLowerWidth, 
           wallLowerDepth, wallLowerHeight, 
           Base.Vector(LowerWall_X, 
           LowerWall_Y, LowerWall_Z)
)
# ������ ��� ����������� ����� 
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape

# ������������ ���� ��� 1-�� ����  (x,y,z)
row1_cubeLocation_X = float(0.0)                           # ������ (x)
row1_cubeLocation_Y = float(batteryDepth)                  # ������� (y)
row1_cubeLocation_Z = float(0.0)                           # ������ (z)

# ������������ ���� ��� 2-�� ����  (x,y,z)
row2_cubeLocation_X = float((-batteryWidth-
                      row_betweenBattery)  
                      )                                    # ������ (x)
row2_cubeLocation_Y = float(batteryDepth)                  # ������� (y)
row2_cubeLocation_Z = float(0.0)                           # ������ (z)
 

# ����� ���� 1-�� ���� (1)
boxShape = Part.makeBox(batteryWidth,
           batteryDepth, batteryHeight, 
           Base.Vector(0, 0, 0)
           )
# ������ ��� ����������� ����� 
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape

# ����� ���� 1-�� ���� (2)
boxShape = Part.makeBox(batteryWidth, batteryDepth, 
           batteryHeight, Base.Vector
           (row1_cubeLocation_X, row1_cubeLocation_Y+
           row_betweenBattery, row1_cubeLocation_Z)
           )
# ������ ��� ����������� ����� 
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape

# ����� ���� 1-�� ���� (3)
boxShape = Part.makeBox(batteryWidth, batteryDepth, 
           batteryHeight, Base.Vector(row1_cubeLocation_X, 
           2*(row1_cubeLocation_Y)+row_betweenBattery*2, 
           row1_cubeLocation_Z)
           )
# ������ ��� ����������� ����� 
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape

# ����� ���� 1-�� ���� (4)
boxShape = Part.makeBox(batteryWidth, batteryDepth, 
           batteryHeight, Base.Vector(row1_cubeLocation_X, 
           3*(row1_cubeLocation_Y)+row_betweenBattery*3, 
           row1_cubeLocation_Z)
           )
# ������ ��� ����������� ����� 
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape

# ����� ���� 1-�� ���� (5)
boxShape = Part.makeBox(batteryWidth, batteryDepth, 
           batteryHeight, Base.Vector(row1_cubeLocation_X, 
           4*(row1_cubeLocation_Y)+row_betweenBattery*4, 
           row1_cubeLocation_Z)
           )
# ������ ��� ����������� ����� 
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape

# ����� ���� 2-�� ���� (1)
boxShape = Part.makeBox(batteryWidth, batteryDepth, 
           batteryHeight, Base.Vector(row2_cubeLocation_X, 0, 0)
           )
# ������ ��� ����������� ����� 
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape

# ����� ���� 2-�� ���� (2)
boxShape = Part.makeBox(batteryWidth, batteryDepth, 
           batteryHeight, Base.Vector(row2_cubeLocation_X, 
           row1_cubeLocation_Y+row_betweenBattery, 
           row1_cubeLocation_Z)
           )
# ������ ��� ����������� ����� 
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape

# ����� ���� 2-�� ���� (3)
boxShape = Part.makeBox(batteryWidth, batteryDepth, 
           batteryHeight, Base.Vector(row2_cubeLocation_X, 
           2*(row1_cubeLocation_Y)+row_betweenBattery*2, 
           row1_cubeLocation_Z)
           )
# ������ ��� ����������� ����� 
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape

# ����� ���� 2-�� ���� (4)
boxShape = Part.makeBox(batteryWidth, batteryDepth, 
           batteryHeight, Base.Vector(row2_cubeLocation_X, 
           3*(row1_cubeLocation_Y)+row_betweenBattery*3, 
           row1_cubeLocation_Z)
           )
# ������ ��� ����������� ����� 
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape

# ����� ���� 2-�� ���� (5)
boxShape = Part.makeBox(batteryWidth, batteryDepth, 
           batteryHeight, Base.Vector(row2_cubeLocation_X, 
           4*(row1_cubeLocation_Y)+row_betweenBattery*4, 
           row1_cubeLocation_Z)
           )
# ������ ��� ����������� ����� 
box = document.addObject('Part::Feature', 'Box')
box.Shape = boxShape

# ����������� �� �������� ������� ���
Gui.SendMsgToActiveView("ViewFit")
Gui.activeDocument().activeView().viewAxonometric()

# �������� ���������� ��������
document.recompute()
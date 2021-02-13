def cordinates_to_angles(*cords, lengths):
  import numpy as np
  # Doc strings
  """
  This module is specifically developed for robotic arms, it calculates the 3axis robotic arm angles from 3d space cordinates given by user,\n
  it will only works for 3axis arms, it is developed to learn principles of kinematics in real life, and it is developed by two AI students for their 2021 SCARA project,\n
  for questions on working of this module, contact to the module creator AdilJK@gmail.com\n
  All mathematics part is created and developed by Mr.Adil,\n
  Module is developed by Syed.M.Erdum Adnan
  """
  
  if len(cords) > 3 or (len(cords) < 3 and len(cords) > 0) or len(cords) <= 0:
    raise ValueError('Only three cordinate values are acceptable')
    
  if len(lengths) > 3 or (len(lengths) < 3 and len(lengths) > 0) or len(lengths) <= 0:
    raise ValueError('Only three link length values are acceptable')

  for i in lengths:
    if i < 1:
      raise ValueError('Lenght values must not be negative and greater then or equal to 1')
      break
    
  x = cords[0]
  y = cords[1]
  z = cords[2]

  a1 = lengths[0]
  a2 = lengths[1]
  a3 = lengths[2]

  # For Theta 1 (T1)
  if x==0 and y==0:
    T1=0
  else:
    T1 = np.arctan(y/x)
    T1 = (T1*180.0)/np.pi

  # For Theta 2 (T2)
  r1 = np.sqrt(x**2 + y**2)
  r2 = z - a1
  phi2 = np.arctan(r2/r1)

  # phi2 in degrees
  phi2 = (phi2*180.0)/np.pi
  r3 = np.sqrt(r1**2 + r2**2)

  # For phi1, using law of cosines
  phi1 = np.arccos((a2**2+r3**2-a3**2)/(2*a2*r3))

  # phi1 in degrees
  phi1 = (phi1*180.0)/np.pi
  T2 = phi2 - phi1


  # For Theta 3
  # From law of cosines
  phi3 = np.arccos((a2**2+a3**2-r3**2)/(2*a2*a3))

  # phi3 in degrees
  phi3 = (phi3*180.0)/np.pi
  T3 = 180.0 - phi3

  return (T1, T2, T3)
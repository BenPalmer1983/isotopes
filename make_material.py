from isotopes import isotopes








iso = ['Fe','C','Cr','Ni','Co55']
masses = [70,1,18,11,5]


mat = isotopes.make_material(iso, masses)

for m in mat:
  print(mat[m])


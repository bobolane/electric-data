from nec_tables import NECTables


conductor_gauge = input("AWG#: ")
conductor_type = input("Insulation type: ")
num_conductors = int(input("No. of Conductors: "))
conduit_type = input("Conduit Type: ")

thhn_alt_names = ['thhn', 'thwn', 'thwn-2']
rhh_alt_names = ['rhh', 'rhw', 'rhw-2', 'pv', 'pv wire', 'pv-wire']


def thhn_value(x):
  if conductor_type in thhn_alt_names:
    for key in NECTables.thhn_awg_to_area:
      if x == key:
        return NECTables.thhn_awg_to_area[key]
      
def rhh_value(x):
  if conductor_type in rhh_alt_names:
    for key in NECTables.rhh_awg_to_area:
      if x == key:
        return NECTables.rhh_awg_to_area[key]

thhn = thhn_value(conductor_gauge)
rhh = rhh_value(conductor_gauge)

if conductor_type in rhh_alt_names:
  area = rhh * num_conductors
elif conductor_type in thhn_alt_names:
  area = thhn * num_conductors


emt_lst = [.0, .304, .533, .864, 1.496, 2.036, 3.356,
5.858, 8.846, 11.545, 14.753]


emt_dict_two = {
.304: '1/2"',
.533: '3/4"',
.864: '1"',
1.496: '1-1/4"',
2.036: '1-1/2"',
3.356: '2"',
5.858: '2-1/2"',
8.846: '3"',
11.545: '3-1/2"',
14.753: '4"'}


for x in emt_lst:	
	if (area / .4) > x:
		continue
	elif (area / .4) < x:
		cross_sect = area / x
		print(cross_sect)
		print(emt_dict_two[x])
		break

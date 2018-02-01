import re
all_vlans = []
all_vlans_lists = []
common_vlans = []
unique_vlans = []
output = []

with open('comands.txt', 'r') as f:
    for line in f:
        if line.startswith('switchport trunk allowed vlan'):
            temp = re.findall(r'\b\d+\b', line)
            all_vlans_lists.append(temp)
            output = map(int, temp)
            all_vlans.extend(output)

    unique_vlans = list(set(all_vlans))
    my_sets = map(set, all_vlans_lists)
    common_vlans = list(set.intersection(*my_sets))

print ('All vlans: ',all_vlans)
print ('Unique vlans: ', unique_vlans)
print ('Common vlans: ', common_vlans)
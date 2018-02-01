mode = raw_input('Enter interface mode (access/trunk): ')
interface = raw_input('Enter interface type and number: ')
vlan = int(raw_input('Enter VLAN number: '))

access_template = ['switchport mode access',
                   'switchport access vlan %d',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk allowed vlan %d']

if mode == 'access':
    print '\n' + '-' * 30
    print 'interface %s' % interface
    print '\n'.join(access_template) % vlan
elif mode == 'trunk':
    print '\n' + '-' * 30
    print 'interface %s' % interface
    print '\n'.join(trunk_template) % vlan
else:
    print 'Wrong intrface mode'

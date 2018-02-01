# -*- coding: utf-8 -*-
"""
Задание 4.1b

Преобразовать скрипт из задания 4.1a таким образом, чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.
"""
ip_add = raw_input("Type IP address: ")


ip_add=ip_add.replace('.',' ')
ip_add=ip_add.replace('/',' ')
ip_add=ip_add.split()


ip_add_sts=""
mask_add_sts=""
dec_str=""
bin_str=''

if len(ip_add)<5:
    ip_add_sts="The ip address format should be '10.1.1.0/24' try agan!"
    print ip_add_sts
else:
    for i in range(len(ip_add)-1):
        if int(ip_add[i])>=0 and int(ip_add[i])<=256:
            ip_add_sts="IP is GOOD!"

            if int(ip_add[-1])>=1 and int(ip_add[-1])<=32:
                mask_add_sts="Mask is GOOD!"

                bin_str = bin_str + format(int(ip_add[i], 10), '08b') + "  "
                if int(ip_add[i]) > 99:     dec_str = dec_str + ip_add[i] + "       "
                elif int(ip_add[i]) > 9:    dec_str = dec_str + ip_add[i] + "        "
                else:                       dec_str = dec_str + ip_add[i] + "         "

                mask_bits = int(ip_add[-1])
                bin_mask = '1' * mask_bits + '0' * (32 - mask_bits)
                str_bin_mask = ''
                for j in range(0, len(bin_mask)):
                    if j == 8 or j == 16 or j == 24:
                        str_bin_mask += "  "
                        str_bin_mask += bin_mask[j]
                    else:
                        str_bin_mask += bin_mask[j]

                dec_mask = '       '.join([str(int(bin_mask[l:l + 8], 2)) for l in [0, 8, 16, 24]])

                if i==3:
                    print "Network:"
                    print dec_str
                    print bin_str
                    print "\nMask:"
                    print "/" + ip_add[-1]
                    print dec_mask
                    print str_bin_mask

        else:
            mask_add_sts="IP has imposible value"
            print mask_add_sts
            break
    else:
        '''ip_add_sts="Mask has imposible value"'''
        print ip_add_sts
'''
Input Harga: 370000
Input Diskon: 15
Output: harga yang harus dibayar adalah Rp. 314.500
'''

# input
diskon_str = input('berapa diskonnya= ')
diskon= int(diskon_str)
harga_str = input('berapa harganya= ')
harga= int(harga_str)

#code

harga_diskon = (diskon / 100) * harga

harga_akhir = harga - harga_diskon

print("harga yang harus dibayar adalah Rp.", harga_akhir)
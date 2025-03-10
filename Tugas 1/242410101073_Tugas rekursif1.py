pilihan = int(input("Soal nomor : "))

#Soal nomor 1
if pilihan == 1:
    def print_menu(isi_menu, parent_id=0, level=0):
        for menu_id, (parent, nama) in sorted(isi_menu.items()):
            if parent == parent_id:
                print("..." * level + nama)
                print_menu(isi_menu, menu_id, level + 1)

    n = int(input())
    isi_menu = {}

    for _ in range(n):
        menu_id, parent_id, nama = input().split()
        isi_menu[int(menu_id)] = (int(parent_id), nama)

    print_menu(isi_menu)

#Soal nomor 2
elif pilihan == 2:
    import re

    def palindrome(string):
        if len(string) <= 1:
            return True 
        if string[0] != string[-1]:
            return False
        return palindrome(string[1:-1])

    str_tes = input()

    str_bersih = re.sub(r'[^a-zA-Z]', '', str_tes).lower()

    print(palindrome(str_bersih))

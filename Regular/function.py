class NewMember:
    total = 0
    def __init__(self, name, grade_class):
        # your code here
        self.Nama = name
        self.Kelas = grade_class
        NewMember.total += 1
    
    def __del__(self):
        print(self.Nama, 'telah keluar')

    def info(self):
        print(self.__dict__)

    @classmethod
    def new_member_total(cls):
        print('total anggota baru : ', NewMember.total)





member1 = NewMember('Muhammad Aris', "Informatics student")
member1.info()
NewMember.new_member_total()


member2 = NewMember('Ucup kasep', "Sundanese culture")
member2.info()
NewMember.new_member_total()

del member1
NewMember.new_member_total()

# FOR LEARN GIT
learnGit = NewMember('Git Handsome', 'Version Control Management')
learnGit.total

gitHandsome = NewMember('Git two chances', 'The Best VCS')
gitHandsome.info()

print('Does Git make us easier to management our source code\nCertainly')
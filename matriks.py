class Matriks:
    def __init__(self, baris, kolom):
        self.baris = baris
        self.kolom = kolom
        self.matriksBaris = []
        self.matriksOperasi = []
        
    def membuatMatriks(self):
        self.matriksBaris = []
        for b in range (self.baris):
            matriksKolom = []
            for k in range (self.kolom):
                nKolom = int(input(f"Masukkan data M{b+1}{k+1}: "))
                matriksKolom.append(nKolom)
            self.matriksBaris.append(matriksKolom)
        return self.matriksBaris
    
    def menampilkanMatriks(self):
        for x in self.matriksBaris:
            print("|", end=" ")
            for y in x:
                print(y, end=" ")
            print("|")
        
    def penjumlahanMatriks(self):
        kondisi = True
        while kondisi:
            kondisi2 = True
            self.matriksOperasi.append(self.membuatMatriks())
            self.menampilkanMatriks()
            while kondisi2:
                print("Tambahkan dengan: ")
                self.matriksOperasi.append(self.membuatMatriks())
                self.menampilkanMatriks()
                
                opsi = str(input("Lanjut menambahkan? (y/n)")).lower()
                if opsi == "y":
                        kondisi2 = True
                else:
                        x = 0
                        kondisi2 = False
                        kondisi = False
        
        matriksFinal = []                  
        for x in range (len(self.matriksOperasi[0])):
            jumlahMatriks = []
            for y in range (len(self.matriksOperasi[0][0])):
                jumlahMatriks.append(0)
            matriksFinal.append(jumlahMatriks)

        for x in range (len(self.matriksOperasi)):
            for y in range (len(self.matriksOperasi[x])):
                for z in range (len(self.matriksOperasi[x][y])):
                     matriksFinal[y][z] += self.matriksOperasi[x][y][z]
        
        for x in matriksFinal:
            print("|", end=" ")
            for y in x:
                print(y, end=" ")
            print("|")
        
    def penguranganMatriks(self):
        kondisi = True
        while kondisi:
            kondisi2 = True
            self.matriksOperasi.append(self.membuatMatriks())
            self.menampilkanMatriks()
            while kondisi2:
                print("Kurangkan dengan: ")
                self.matriksOperasi.append(self.membuatMatriks())
                self.menampilkanMatriks()
                
                opsi = str(input("Lanjut mengurangkan? (y/n)")).lower()
                if opsi == "y":
                        kondisi2 = True
                else:
                        x = 0
                        kondisi2 = False
                        kondisi = False
        
        matriksFinal = []                  
        for x in range (len(self.matriksOperasi[0])):
            jumlahMatriks = []
            for y in range (len(self.matriksOperasi[0][0])):
                jumlahMatriks.append(0)
            matriksFinal.append(jumlahMatriks)

        for x in range (len(self.matriksOperasi)):
            for y in range (len(self.matriksOperasi[x])):
                for z in range (len(self.matriksOperasi[x][y])):
                        if x == 0:
                            matriksFinal[y][z] += self.matriksOperasi[x][y][z]
                        else:
                            matriksFinal[y][z] -= self.matriksOperasi[x][y][z]
        
        for x in matriksFinal:
            print("|", end=" ")
            for y in x:
                print(y, end=" ")
            print("|")
    
print("OPERASI MATRIKS\n1. Penjumlahan\n2. Pengurangan")
opsi = int(input("Pilih opsi: "))
if opsi == 1 :       
    baris = int(input("Masukkan ordo matriks (mxn), m : "))
    kolom = int(input("Masukkan ordo matriks (mxn), n : "))
    Matriks(baris, kolom).penjumlahanMatriks()
elif opsi == 2 :
    baris = int(input("Masukkan ordo matriks (mxn), m : "))
    kolom = int(input("Masukkan ordo matriks (mxn), n : "))
    Matriks(baris, kolom).penguranganMatriks()
        


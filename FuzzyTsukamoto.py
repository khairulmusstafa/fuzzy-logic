# deklarasi class FuzzyTsukamoto untuk dipanggil di fungsi main nanti
class FuzzyTsukamoto:
    # deklarasi seluruh variabel-variabel yang akan digunakan nantinya
    kecepatanLambat = 0.0
    kecepatanCepat = 0.0
    suhuRendah = 0.0
    suhuTinggi = 0.0
    a_predikat1 = 0.0
    a_predikat2 = 0.0
    a_predikat3 = 0.0
    a_predikat4 = 0.0
    z1 = 0.0
    z2 = 0.0
    z3 = 0.0
    z4 = 0.0
    zTotal = 0.0
    z = 0.0
    a_pred_z = 0.0

    def fuzzifikasiKecepatan(self, kecepatan):
        # Variabel kecepatan terdiri atas 2 himpunan fuzzy, yaitu LAMBAT dan CEPAT.
        if (kecepatan <= 1000):
            self.kecepatanLambat = 1
            self.kecepatanCepat = 0
        elif(kecepatan >= 1000 and kecepatan <= 5000):
            self.kecepatanLambat = (5000 - kecepatan) / (5000 - 1000)
            self.kecepatanCepat = (kecepatan - 1000) / (5000 - 1000)
        else:
            self.kecepatanLambat = 0
            self.kecepatanCepat = 1
        print("derajat keanggotaan kecepatan cepat : " + str(self.kecepatanCepat))
        print("derajat keanggotaan kecepatan lambat : " +
              str(self.kecepatanLambat))

    def fuzzifikasiSuhu(self, suhu):
        # Variabel suhu terdiri atas 2 himpunan fuzzy, yaitu RENDAH dan TINGGI.
        if (suhu <= 100):
            self.suhuRendah = 1
            self.suhuTinggi = 0
        elif(suhu >= 100 and suhu <= 600):
            self.suhuRendah = (600 - suhu) / (600 - 100)
            self.suhuTinggi = (suhu - 100) / (600 - 100)
        else:
            self.suhuRendah = 0
            self.suhuTinggi = 1
        print("derajat keanggotaan suhu rendah : " + str(self.suhuRendah))
        print("derajat keanggotaan suhu tinggi : " + str(self.suhuTinggi))

    def mesinInferensiTsukamoto(self):
        # Variabel frekuensi terdiri atas dua himpunan, yaitu KECIL dan BESAR

        # IF kecepatan LAMBAT dan suhu TINGGI then Frekuensi   KECIL
        self.a_predikat1 = min(self.kecepatanLambat, self.suhuTinggi)
        self.z1 = 7000 - self.a_predikat1 * (7000 - 2000)
        print("a predikat 1 : " + str(self.a_predikat1) +
              " | " + "z1 : " + str(self.z1))
        # IF kecepatan LAMBAT dan suhu RENDAH then Frekuensi KECIL
        self.a_predikat2 = min(self.kecepatanLambat, self.suhuRendah)
        self.z2 = 7000 - self.a_predikat2 * (7000 - 2000)
        print("a predikat 2 : " + str(self.a_predikat2) +
              " | " + "z2 : " + str(self.z2))
        # IF kecepatan CEPAT dan suhu TINGGI then Frekuensi BESAR
        self.a_predikat3 = min(self.kecepatanCepat, self.suhuTinggi)
        self.z3 = 2000 - self.a_predikat3 * (2000 - 7000)
        print("a predikat 3 : " + str(self.a_predikat3) +
              " | " + "z3 : " + str(self.z3))
        # IF kecepatan CEPAT dan suhu RENDAH then Frekuensi BESAR
        self.a_predikat4 = min(self.kecepatanCepat, self.suhuRendah)
        self.z4 = 2000 - self.a_predikat4 * (2000 - 7000)
        print("a predikat 4 : " + str(self.a_predikat4) +
              " | " + "z4 : " + str(self.z4))

    def defuzzifikasi(self):
        # Disini nilai tegas dari z akan dicari menggunakan rata-rata terbobot
        self.a_pred_z = (self.a_predikat1 * self.z1) + (self.a_predikat2 *
                                                        self.z2) + (self.a_predikat3 * self.z3) + (self.a_predikat4 * self.z4)
        self.z = self.a_predikat1 + self.a_predikat2 + \
            self.a_predikat3 + self.a_predikat4
        self.zTotal = self.a_pred_z / self.z
        print("Output Fuzzy berupa Frekuensi Kipas : " + str(self.zTotal) + " Hz")

    @staticmethod
    def main(args):
        fs = FuzzyTsukamoto()
        # input kecepatan dan suhu terlebih dahulu disini, untuk dipakai di proses fuzzyfikasi nantinya
        kec = 4000
        suhu = 300
        print("========== NILAI INPUTAN FUZZY ==========")
        print("Kecepatan : " + str(kec) + " rpm")
        print("Suhu      : " + str(suhu) + " kelvin")
        print("========== FUZZIFIKASI KECEPATAN ==========")
        fs.fuzzifikasiKecepatan(kec)
        print("========== FUZZIFIKASI SUHU ==========")
        fs.fuzzifikasiSuhu(suhu)
        print("========== INFERENSI TSUKAMOTO ==========")
        fs.mesinInferensiTsukamoto()
        print("========== HASIL DEFUZZIFIKASI TSUKAMOTO ==========")
        fs.defuzzifikasi()


if __name__ == "__main__":
    FuzzyTsukamoto.main([])

class Siswa:
    def __init__(self, NIS: int, nama, kelas, alamat, ipa, ips, mtk, inggris, indonesia, sunda, pkn):
        self.NIS = NIS
        self.nama = nama
        self.kelas = kelas
        self.alamat = alamat
        self.ipa = ipa
        self.ips = ips
        self.mtk = mtk
        self.inggris = inggris
        self.indonesia = indonesia
        self.sunda = sunda
        self.pkn = pkn

    def print_data(self):
        print("===== data siswa =====")
        print("nama\t\t:", self.nama)
        print("NIS\t\t:", self.NIS)
        print("kelas\t\t:", self.kelas)
        print("alamat\t\t:", self.alamat)
        print("====== nilai ======")
        print("ipa\t\t:", self.ipa)
        print("ips\t\t:", self.ips)
        print("mtk\t\t:", self.mtk)
        print("inggris\t\t:", self.inggris)
        print("indonesia\t:", self.indonesia)
        print("sunda\t\t:", self.sunda)
        print("pkn\t\t:", self.pkn)
        print("======================")

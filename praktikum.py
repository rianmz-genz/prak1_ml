import pandas as pd
from helper import data_to_excel, read_csv

def exercise_one(db):
    #exercise 1
    #Tampilkan informasi nim, nama mahasiswa, nama prodi, dan nama dosen pada console dan export hasilnya ke Microsoft Excel.
    column_mahasiswa = ['nim', 'nama_mahasiswa', 'id_prodi', 'id_dosen_pa']
    query = "SELECT * FROM mahasiswa"
    data_mahasiswa = db.select(query)
    df = pd.DataFrame(data_mahasiswa, columns=column_mahasiswa)

    data_to_excel(df, column_mahasiswa, data_mahasiswa, 'output/data_siswa.xlsx')
    
    
    
def exercise_two(db):
    #exercise 2
    # Tampilkan ID dosen dan nama dosen yang tidak memiliki mahasiswa bimbingan pada console dan export hasilnya ke Microsoft Excel.
    column_dosen = ["id_dosen_pa", "nama_dosen"]
    query = """
        SELECT dosen_pa.id_dosen_pa, dosen_pa.nama_dosen
        FROM dosen_pa
        LEFT JOIN mahasiswa ON dosen_pa.id_dosen_pa = mahasiswa.id_dosen_pa
        WHERE mahasiswa.id_dosen_pa IS NULL;
    """
    data_dosen = db.select(query)
    df = pd.DataFrame(data_dosen, columns=column_dosen)
    
    data_to_excel(df, column_dosen, data_dosen, 'output/data_dosen.xlsx')

def exercise_three():
    # limit 10 data
    read_csv('src/housing.csv')
    
    # menampilkan semua data
    # read_csv('src/housing.csv', limit=99999)
import os
from crewai import Agent, Task, Crew, Process

# =====================================================================
# 1. SETUP API KEY (Ganti dengan API Key milikmu sendiri)
# =====================================================================
os.environ["OPENAI_API_KEY"] = "AIzaSyB1RHPwyt0PClMrIDhkeBx-z780BgVaAiw"

# =====================================================================
# 2. DEFINISI AGEN-AGEN KRU SEKOLAH (SCHOOL CREW)
# =====================================================================

# Agen 1: Pencari & Penggali Materi (Kurikulum Terupdate)
materi_researcher = Agent(
    role='Pakar Kurikulum Nasional & Internasional',
    goal='Menggali secara dalam materi pembelajaran sekolah (SMP sampai SMK Jurusan Teknologi) sesuai standar dinas pendidikan nasional dan internasional terbaru yang terus update.',
    backstory='Kamu adalah peneliti akademis jenius yang memiliki akses ke kurikulum sekolah menengah awal (SMP) hingga sekolah menengah kejuruan (SMK) bidang teknologi seperti Elektronika, Informatika, Otomotif, Mekatronika, dan lainnya.',
    verbose=True
)

# Agen 2: Pembaca & Perangkum Materi
materi_summarizer = Agent(
    role='Spesialis Perangkum Akademik',
    goal='Membaca secara detail materi hasil riset lalu membuat rangkuman yang padat, rapi, dan mudah dipahami.',
    backstory='Kamu adalah pembaca super cepat yang mampu menyaring ribuan halaman materi pelajaran menjadi poin-poin rangkuman yang sangat rapi.',
    verbose=True
)

# Agen 3: Peringkas Materi (Membuat Kesimpulan Singkat)
materi_condenser = Agent(
    role='Spesialis Pembuat Kesimpulan Singkat',
    goal='Mengubah rangkuman panjang menjadi satu kesimpulan akhir yang super singkat, padat, dan jelas (tidak bertele-tele).',
    backstory='Kamu adalah penulis cerdas yang ahli menyederhanakan materi sulit menjadi satu kesimpulan singkat berkelas yang sangat mudah dipahami.',
    verbose=True
)

# Agen 4: Pembuat Kuis / Flashcard & Contoh Soal
quiz_creator = Agent(
    role='Desainer Pembelajaran Interaktif',
    goal='Membuat quiz, flashcard menarik, dan contoh soal beserta pembahasannya berdasarkan materi yang dipelajari.',
    backstory='Kamu adalah guru kreatif yang tahu cara membuat belajar menjadi seru lewat metode kuis interaktif, flashcard kreatif, dan soal-soal latihan yang menantang.',
    verbose=True
)


# =====================================================================
# 3. DEFINISI AGEN-AGEN KRU KEUANGAN (FINANCE CREW)
# =====================================================================

# Agen 1: Periset Pasar & Harga Produk
market_researcher = Agent(
    role='Analis Pasar Finansial & Teknologi',
    goal='Melakukan riset mendalam terkait harga saham, emas, kripto, hingga harga produk fisik (transportasi, komunikasi, dan berbagai teknologi lainnya).',
    backstory='Kamu adalah analis pasar handal yang selalu tahu pergerakan harga emas, kripto, saham, serta perkembangan harga gadget dan teknologi terbaru.',
    verbose=True
)

# Agen 2: Penggali Pola & Penyimpul Waktu Jual-Beli (Strategi Transaksi)
trend_analyst = Agent(
    role='Pakar Strategi Investasi & Transaksi',
    goal='Menggali pola kenaikan atau penurunan harga barang/aset, lalu menyimpulkan kapan waktu yang paling tepat untuk membeli atau menjual.',
    backstory='Kamu adalah trader dan analis teknikal profesional yang sangat jeli melihat pola chart dan tren pasar untuk memberikan keputusan beli/jual terbaik.',
    verbose=True
)

# Agen 3: Pengelola & Pengatur Pengeluaran (Budgeting)
finance_manager = Agent(
    role='Manajer Keuangan Pribadi',
    goal='Mengelola pengeluaran harian serta mengatur anggaran pengeluaran bulanan dan tahunan secara bijak.',
    backstory='Kamu adalah akuntan handal yang sangat disiplin. Tugasmu memastikan uang keluar terencana dengan rapi, mencegah pemborosan, dan menyusun anggaran tahunan yang stabil.',
    verbose=True
)


# =====================================================================
# 4. CONTOH CARA JALANKAN TUGASNYA (INPUT DARI USER)
# =====================================================================

# INPUT DARI LU (Nanti tinggal lu ganti bagian ini setiap kali mau minta tolong)
MATERI_SEKOLAH_HARI_INI = "Materi Sistem Komputer dan Dasar Informatika Kelas 10 SMK"
PRODUK_KEUANGAN_HARI_INI = "Investasi Emas Batangan vs Kripto Bitcoin serta kisaran harga HP gaming mid-range saat ini"

# --- Tasks untuk Kru Sekolah ---
task_sekolah_1 = Task(
    description=f'Gali secara mendalam materi berikut ini sesuai kurikulum nasional & internasional terupdate: "{MATERI_SEKOLAH_HARI_INI}". Fokuskan pada pemahaman konsep dasar.',
    expected_output='Dokumen hasil riset materi yang mendalam.',
    agent=materi_researcher
)

task_sekolah_2 = Task(
    description='Baca hasil riset materi dan buatlah rangkuman yang rapi, terstruktur, serta mudah dipahami oleh anak sekolah.',
    expected_output='Rangkuman materi berpoin-poin rapi.',
    agent=materi_summarizer
)

task_sekolah_3 = Task(
    description='Persingkat rangkuman tersebut menjadi satu paragraf kesimpulan akhir yang sangat singkat, padat, dan jelas.',
    expected_output='Teks kesimpulan singkat (maksimal 1 paragraf).',
    agent=materi_condenser
)

task_sekolah_4 = Task(
    description='Berdasarkan materi di atas, buatlah 3 buah Flashcard/Kuis interaktif menarik dan 2 contoh soal latihan lengkap dengan kunci jawabannya.',
    expected_output='Kuis/Flashcard menarik dan contoh soal latihan beserta jawabannya.',
    agent=quiz_creator
)


# --- Tasks untuk Kru Keuangan ---
task_keuangan_1 = Task(
    description=f'Lakukan riset harga pasar saat ini, tren pergerakan, dan detail dari: "{PRODUK_KEUANGAN_HARI_INI}".',
    expected_output='Laporan riset harga dan kondisi pasar terkini.',
    agent=market_researcher
)

task_keuangan_2 = Task(
    description='Analisis pola kenaikan atau penurunan dari hasil riset, lalu berikan kesimpulan waktu terbaik kapan harus membeli atau menjual aset/produk tersebut.',
    expected_output='Analisis pola tren dan rekomendasi keputusan beli/jual yang tepat.',
    agent=trend_analyst
)

task_keuangan_3 = Task(
    description='Buatkan rencana pengelolaan pengeluaran serta draf anggaran bulanan dan tahunan agar keuangan tetap sehat dan bisa membeli produk/aset tersebut tanpa mengganggu tabungan utama.',
    expected_output='Skema pengelolaan keuangan bulanan & tahunan.',
    agent=finance_manager
)


# =====================================================================
# 5. PEMBUATAN TIM KREATOR (CREWS)
# =====================================================================

# Menggabungkan semua agen sekolah ke dalam satu Kru
school_crew = Crew(
    agents=[materi_researcher, materi_summarizer, materi_condenser, quiz_creator],
    tasks=[task_sekolah_1, task_sekolah_2, task_sekolah_3, task_sekolah_4],
    process=Process.sequential
)

# Menggabungkan semua agen keuangan ke dalam satu Kru
finance_crew = Crew(
    agents=[market_researcher, trend_analyst, finance_manager],
    tasks=[task_keuangan_1, task_keuangan_2, task_keuangan_3],
    process=Process.sequential
)

# =====================================================================
# 6. RUNNING (JALANKAN PROGRAM)
# =====================================================================
if __name__ == "__main__":
    print("\n=========================================")
    print(" JALANKAN KRU SEKOLAH (AUTOMATION START) ")
    print("=========================================")
    hasil_sekolah = school_crew.kickoff()
    print("\n=== HASIL KRU SEKOLAH ===")
    print(hasil_sekolah)

    print("\n=========================================")
    print(" JALANKAN KRU KEUANGAN (AUTOMATION START) ")
    print("=========================================")
    hasil_keuangan = finance_crew.kickoff()
    print("\n=== HASIL KRU KEUANGAN ===")
    print(hasil_keuangan)

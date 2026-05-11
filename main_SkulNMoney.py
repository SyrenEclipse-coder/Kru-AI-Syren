import os
from crewai import Agent, Task, Crew, Process, LLM

# =====================================================================
# 1. SETUP API KEY (Mengambil aman dari Environment Variable di Render)
# =====================================================================
api_key = os.environ.get("GEMINI_API_KEY")

# Inisialisasi Model Gemini 1.5 Flash (Sangat stabil untuk CrewAI)
gemini_llm = LLM(
    model="gemini/gemini-1.5-flash",
    api_key=api_key
)

# =====================================================================
# 2. DEFINISI AGEN-AGEN KRU SEKOLAH (SCHOOL CREW)
# =====================================================================

materi_researcher = Agent(
    role='Pakar Kurikulum Nasional & Internasional Dinamis',
    goal='Menggali materi SMP lengkap dan SMK teknologi yang dinamis dengan melakukan pencarian mandiri secara dinamis untuk melacak perubahan kebijakan kurikulum terbaru di lapangan (seperti transisi K13, Kurikulum Merdeka, Cambridge IGCSE, IB, maupun jika di masa depan kurikulum nasional berubah lagi).',
    backstory='Kamu adalah peneliti kurikulum akademis super update yang dibekali kemampuan melacak perubahan kebijakan pendidikan secara dinamis melalui penjelajahan informasi terbaru di internet.',
    verbose=True,
    llm=gemini_llm
)

materi_summarizer = Agent(
    role='Spesialis Perangkum Akademik Komprehensif',
    goal='Membaca hasil riset kurikulum terbaru lalu menyusun rangkuman yang sangat terstruktur, rapi, padat, dan mudah dipahami oleh siswa sekolah dengan membedakan secara jelas fokus Teori Dasar (SMP) dan Aplikasi Praktis (SMK).',
    backstory='Kamu adalah edukator dan penulis akademis handal yang mampu menyederhanakan materi rumit (seperti pemrograman, PLC, sistem kendali, rangkaian elektronika, IoT, CNC, hingga SolidWorks) menjadi poin-poin penjelasan yang ramah otak siswa.',
    verbose=True,
    llm=gemini_llm
)

materi_condenser = Agent(
    role='Spesialis Pembuat Kesimpulan Singkat',
    goal='Mengubah dokumen rangkuman kurikulum yang panjang menjadi satu paragraf kesimpulan akhir yang super padat, jelas, langsung ke inti, dan tidak bertele-tele.',
    backstory='Kamu adalah editor jurnal pendidikan yang ahli memadatkan informasi besar menjadi satu paragraf kesimpulan berbobot tinggi.',
    verbose=True,
    llm=gemini_llm
)

quiz_creator = Agent(
    role='Desainer Pembelajaran & Evaluasi Interaktif',
    goal='Membuat kuis, flashcard interaktif, dan contoh soal latihan berkualitas tinggi lengkap dengan pembahasannya berdasarkan materi kurikulum terbaru.',
    backstory='Kamu adalah guru kreatif yang ahli membuat instrumen ujian interaktif yang menantang namun seru, guna menguji pemahaman siswa secara mendalam.',
    verbose=True,
    llm=gemini_llm
)


# =====================================================================
# 3. DEFINISI AGEN-AGEN KRU KEUANGAN (FINANCE CREW)
# =====================================================================

market_researcher = Agent(
    role='Analis Pasar Finansial, Properti & Teknologi Ekstrem',
    goal='Melakukan riset mendalam terkait instrumen investasi (Emas vs Bitcoin), spesifikasi gadget gaming tangguh standar militer (tahan rendaman air, debu, sertifikasi IP tinggi IP68/IP69K, MIL-STD-810), harga motor sport (khususnya Kawasaki ZX-25R), serta kriteria rumah strategis aman banjir.',
    backstory='Kamu adalah analis pasar serba bisa yang memiliki mata tajam dalam memantau harga emas, pergerakan kripto, spesifikasi ketahanan hardware (IP rating/militer), pasar otomotif sport, hingga peta kerawanan banjir untuk properti.',
    verbose=True,
    llm=gemini_llm
)

trend_analyst = Agent(
    role='Pakar Strategi Investasi & Transaksi',
    goal='Menganalisis pola tren pasar (naik/turun) untuk emas dan kripto, serta menilai kelayakan investasi jangka panjang pada motor sport, HP tangguh, dan rumah strategis untuk menyimpulkan keputusan beli/jual terbaik.',
    backstory='Kamu adalah penasihat keuangan dan analis teknikal berpengalaman yang ahli membaca momentum pasar untuk memaksimalkan keuntungan dan menghindari kerugian.',
    verbose=True,
    llm=gemini_llm
)

finance_manager = Agent(
    role='Manajer Keuangan & Perencana Anggaran Pribadi',
    goal='Menyusun skema budgeting, pengelolaan pengeluaran, serta draf anggaran bulanan dan tahunan secara realistis agar user bisa memiliki aset impian tersebut tanpa mengganggu dana darurat utama.',
    backstory='Kamu adalah perencana keuangan bersertifikat (CFP) yang sangat disiplin, detail, dan realistis dalam menyusun target pencapaian finansial jangka menengah dan panjang.',
    verbose=True,
    llm=gemini_llm
)


# =====================================================================
# 4. INPUT DETAIL MATERI & KEUANGAN (INPUT DARI USER)
# =====================================================================

MATERI_SEKOLAH_HARI_INI = """
1. Jenjang Sekolah Menengah Pertama (SMP):
- Kurikulum Nasional (Kurikulum Merdeka): Pendidikan Agama & Budi Pekerti (Fiqih/Teologi, Sejarah, Akhlak), Pendidikan Pancasila (Sejarah Pancasila, UUD 1945, NKRI, Bhinneka), Bahasa Indonesia (LHO, Iklan, Slogan, Artikel Ilmiah, Fiksi), Matematika (Bilangan, Aljabar, Geometri, Statistika, Peluang), IPA (Sains, Sel, Sistem Tubuh, Gerak & Gaya, Gelombang, Cahaya, Unsur & Senyawa), IPS (Geografi, Sosial Budaya, Ekonomi Kebutuhan, Sejarah Nasional), Bahasa Inggris (Greeting, Descriptive, Narrative, Recount, Report, Procedure), Informatika (Berpikir Komputasional, HW/SW, Internet, Analisis Data, Algoritma), PJOK, Seni & Prakarya.
- Kurikulum Internasional (Cambridge IGCSE / IB MYP): Mathematics (Core & Extended), Biology (Organisms, Cells, Nutrition, Transport, Inheritance), Chemistry (States of matter, Atoms, Reactions, Organic), Physics (Motion, Energy, Waves, Electricity, Space), English, Humanities (History & Geography), Global Perspectives (Climate Change, Human Rights, Sustainable Living).

2. Jenjang SMK (Jurusan Teknologi - Mekatronika, Elektronika, Teknik Mesin & Manufaktur):
- A. Teknik Mekatronika: Sistem Kontrol (PLC), Pneumatik & Hidrolik, Robotika Industri, Sensor & Aktuator, Mikrokontroler (Arduino, Raspberry Pi). Kurikulum Industri: Festo Pedagogy (Jerman), Siemens Automation.
- B. Teknik Elektronika: Dasar Listrik & Elektronika (Ohm, Kirchhoff), Elektronika Digital (Gerbang Logika, Biner, Flip-flop), Penerapan Rangkaian (Audio-Video, Catu Daya), Internet of Things (IoT). Kurikulum Industri: Schneider Electric, Microchip Technology.
- C. Teknik Mesin & Manufaktur: Gambar Teknik Manufaktur (CAD/AutoCAD), Teknik Pemesinan (Bubut, Frais, Gerinda), NC/CNC, Teknologi Bahan (Sifat Logam, Heat Treatment, Korosi). Kurikulum Industri: Autodesk Certification, SolidWorks.

*Perbandingan Fokus Utama:*
- SMP: Teori Dasar (Mengapa fenomena terjadi?).
- SMK: Aplikasi Praktis (Bagaimana cara membuat, memperbaiki, dan mengoperasikan teknologi?).

*PENTING: Lakukan pencarian mandiri secara dinamis untuk melacak dan mencocokkan materi di atas dengan perubahan kurikulum nasional/internasional terbaru yang aktif atau baru dirilis saat ini di lapangan!*
"""

PRODUK_KEUANGAN_HARI_INI = """
1. Investasi: Emas Batangan vs Kripto Bitcoin (analisis keuntungan, risiko, dan tren harga).
2. Gadget: Handphone Gaming Tahan Banting (Wajib memiliki sertifikasi IP tinggi seperti IP68/IP69K, tahan rendaman air, tahan debu, dan bersertifikasi standar militer MIL-STD-810).
3. Otomotif: Motor Sport Kawasaki ZX-25R (kisaran harga saat ini, performa, dan biaya perawatan).
4. Properti: Rumah dengan lokasi strategis (akses transportasi mudah, fasilitas publik dekat) dan WAJIB aman dari banjir.
"""

# --- Tasks untuk Kru Sekolah ---
task_sekolah_1 = Task(
    description=f'Gali secara mendalam materi berikut ini dan pastikan untuk menyelaraskannya secara dinamis dengan kurikulum nasional maupun internasional paling update/terbaru yang berlaku saat ini: "{MATERI_SEKOLAH_HARI_INI}". Cari secara aktif jika ada perubahan regulasi kurikulum terbaru di internet.',
    expected_output='Dokumen hasil riset materi kurikulum SMP & SMK Teknologi yang mendalam dan up-to-date.',
    agent=materi_researcher
)

task_sekolah_2 = Task(
    description='Baca hasil riset materi kurikulum terbaru dan buatlah rangkuman yang sangat rapi, terstruktur dengan poin-poin, serta membedakan secara jelas antara fokus teori (SMP) dan aplikasi praktis kejuruan (SMK) agar mudah dipahami oleh siswa.',
    expected_output='Rangkuman materi pelajaran berpoin-poin rapi sesuai standar kurikulum terbaru.',
    agent=materi_summarizer
)

task_sekolah_3 = Task(
    description='Persingkat seluruh rangkuman materi tersebut menjadi satu paragraf kesimpulan akhir yang sangat padat, jelas, dan menggambarkan esensi utama kurikulum.',
    expected_output='Teks kesimpulan kurikulum singkat (maksimal 1 paragraf).',
    agent=materi_condenser
)

task_sekolah_4 = Task(
    description='Berdasarkan materi kurikulum di atas, buatlah 3 buah Flashcard/Kuis interaktif menarik dan 2 contoh soal latihan lengkap dengan kunci jawabannya.',
    expected_output='Kuis/Flashcard menarik dan 2 contoh soal latihan beserta pembahasannya.',
    agent=quiz_creator
)


# --- Tasks untuk Kru Keuangan ---
task_keuangan_1 = Task(
    description=f'Lakukan riset pasar mendalam mengenai detail harga, spesifikasi, keuntungan, dan risiko dari: "{PRODUK_KEUANGAN_HARI_INI}". Cari rekomendasi HP militer spesifik, harga riil ZX-25R saat ini, perbandingan investasi emas vs bitcoin, dan kriteria daerah rumah strategis bebas banjir.',
    expected_output='Laporan riset pasar komprehensif mengenai instrumen investasi, HP tangguh militer, ZX-25R, dan properti bebas banjir.',
    agent=market_researcher
)

task_keuangan_2 = Task(
    description='Analisis tren harga dari laporan riset tersebut. Berikan rekomendasi keputusan beli/jual untuk emas & kripto, kelayakan beli untuk ZX-25R, HP tangguh, dan rumah strategis berdasarkan nilai jangka panjangnya.',
    expected_output='Analisis pola tren dan rekomendasi keputusan investasi/pembelian yang matang.',
    agent=trend_analyst
)

task_keuangan_3 = Task(
    description='Susun rencana keuangan pribadi, skema alokasi pengeluaran bulanan, serta strategi menabung/investasi yang realistis agar user bisa mengamankan rumah bebas banjir, membeli HP militer, motor ZX-25R, dan berinvestasi emas/kripto secara sehat.',
    expected_output='Skema perencanaan keuangan komprehensif bulanan & tahunan.',
    agent=finance_manager
)


# =====================================================================
# 5. PEMBUATAN TIM KREATOR (CREWS)
# =====================================================================

school_crew = Crew(
    agents=[materi_researcher, materi_summarizer, materi_condenser, quiz_creator],
    tasks=[task_sekolah_1, task_sekolah_2, task_sekolah_3, task_sekolah_4],
    process=Process.sequential
)

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

# ---------- Fungsi Feedback Berdasarkan Keypoints ----------
def feedback_kaki_ke_belakang(keypoints):
    if keypoints is None:
        return "Belum Terdeteksi"
    
    ankle_idx = 16  # Pergelangan kaki kanan
    knee_idx = 14   # Lutut kanan
    
    diff = keypoints[knee_idx * 2] - keypoints[ankle_idx * 2]  # Selisih X
    if diff < 0:
        return "Ayo gerakkan!"
    elif diff < 0.05:
        return "Ayo tarik kaki lebih ke belakang!"
    else:
        return "Gerakan kamu sempurna!"


def feedback_lutut_turun(keypoints):
    if keypoints is None:
        return "Belum Terdeteksi"

    knee_idx = 14  # Lutut kanan
    hip_idx = 12   # Pinggul kanan
    
    diff = keypoints[knee_idx * 2 + 1] - keypoints[hip_idx * 2 + 1]  # Selisih Y
    if diff < 0:
        return "Ayo gerakkan!"
    elif diff < 0.1:
        return "Turunkan lutut lagi!"
    else:
        return "Gerakan kamu sempurna!"


def feedback_naikan_kepalan_kedepan(keypoints):
    if keypoints is None:
        return "Belum Terdeteksi"

    wrist_idx = 10    # Pergelangan tangan kanan
    shoulder_idx = 6  # Bahu kanan
    
    diff = keypoints[shoulder_idx * 2 + 1] - keypoints[wrist_idx * 2 + 1]  # Selisih Y
    if diff < 0:
        return "Ayo gerakkan!"
    elif diff < 0.05:
        return "Ayo naikkan kepalan lagi!"
    else:
        return "Gerakan kamu sempurna!"


def feedback_pinggul_naik(keypoints):
    if keypoints is None:
        return "Belum Terdeteksi"

    hip_idx = 12  # Pinggul kanan
    knee_idx = 14  # Lutut kanan
    
    diff = keypoints[knee_idx * 2 + 1] - keypoints[hip_idx * 2 + 1]  # Selisih Y
    if diff < 0:
        return "Ayo gerakkan!"
    elif diff < 0.1:
        return "Naikkan pinggul lagi!"
    else:
        return "Gerakan kamu sempurna!"


def feedback_rentangkan(keypoints):
    if keypoints is None:
        return "Belum Terdeteksi"

    lwrist_idx = 9   # Pergelangan tangan kiri
    rwrist_idx = 10  # Pergelangan tangan kanan
    
    diff = abs(keypoints[lwrist_idx * 2] - keypoints[rwrist_idx * 2])  # Selisih X
    if diff < 0.3:
        return "Ayo gerakkan!"
    elif diff < 0.5:
        return "Rentangkan lebih lebar!"
    else:
        return "Gerakan kamu sempurna!"

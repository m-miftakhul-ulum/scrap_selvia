from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import gspread
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv
import os
load_dotenv()

# Konfigurasi Google Sheets API
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]
SERVICE_ACCOUNT_FILE = os.getenv('SERVICE_ACCOUNT_FILE')  # Ubah sesuai path file JSON Anda
SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')  # Ganti dengan ID Spreadsheet Anda

# Autentikasi dengan Google Sheets API
credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPE)
gc = gspread.authorize(credentials)
sheet = gc.open_by_key(SPREADSHEET_ID).sheet1

# Inisialisasi WebDriver
driver = webdriver.Chrome()
driver.get("https://www.linkedin.com")

# Memuat cookies dari file
with open("cookies.json", "r") as file:
    cookies = json.load(file)

for cookie in cookies:
    if "sameSite" in cookie:
        del cookie["sameSite"]
    driver.add_cookie(cookie)

driver.refresh()
driver.get("https://www.linkedin.com")

# Data LinkedIn URLs
data = [
    "https://www.linkedin.com/in/michael-strauss-57096969",
    "https://www.linkedin.com/in/meganlieu/",
]

# Loop untuk setiap URL LinkedIn
for i in data:
    driver.get(i)
    time.sleep(10)

    try:
        section = driver.find_element(
            By.XPATH,
            "//section[contains(@class, 'artdeco-card') and contains(@class, 'pv-profile-card') and contains(@class, 'break-words') and .//div[@id='education' and contains(@class, 'pv-profile-card__anchor')]]",
        )

        # Mengambil data universitas
        try:
            univ = section.find_element(
                By.XPATH,
                ".//div[contains(@class, 'display-flex flex-wrap align-items-center full-height') and not(contains(text(), 'Education')) ]",
            )
            data_univ = univ.find_element(
                By.XPATH, ".//span[@class='visually-hidden' or @aria-hidden='true']"
            ).text
        except Exception:
            data_univ = "kosong"

        # Mengambil data jurusan
        try:
            jurusan = section.find_element(
                By.XPATH, ".//span[contains(@class, 't-14 t-normal') ]"
            )
            data_jurusan = jurusan.find_element(
                By.XPATH, ".//span[@class='visually-hidden' or @aria-hidden='true']"
            ).text
        except Exception:
            data_jurusan = "kosong"

        # Mengambil data tahun
        try:
            data_year = section.find_element(
                By.XPATH, ".//span[contains(@class, 'pvs-entity__caption-wrapper') ]"
            ).text
        except Exception:
            data_year = "kosong"

        # Masukkan data ke Google Sheets
        sheet.append_row([i, data_univ, data_jurusan, data_year])
        print(f"Data berhasil disimpan untuk {i}")

    except Exception as e:
        print(f"Gagal memproses {i}: {e}")

input("Tekan Enter untuk menutup browser...")
driver.quit()

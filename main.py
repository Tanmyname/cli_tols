from colorama import Fore as x
import requests
import platform
import shutil
import psutil
import time 
import sys
import threading
import yt_dlp
from pytubefix import Search
from pytubefix import YouTube
from pytubefix.cli import on_progress
import os

#Intetface tampilan awal 
def osinfo():
# Mendapatkan informasi OS
  os_name = platform.system()
  os_version = platform.release()

  os_name = platform.system()
  os_version = platform.release()

# Mendapatkan informasi penyimpanan
  disk_info = psutil.disk_usage('/')
  total_storage = disk_info.total / (1024 ** 3)  # Konversi ke GB
  used_storage = disk_info.used / (1024 ** 3)    # Konversi ke GB
  free_storage = disk_info.free / (1024 ** 3)    # Konversi ke GB
# Menampilkan informasi
  print(f"\n{x.YELLOW}==============SYSTEM==============\n{x.YELLOW}{os_name} {os_version}")
  print(f"STORAGE \t: {total_storage:.2f} GB")
  print(f"USED STORAGE \t: {used_storage:.2f} GB")
  print(f"FREE STORAGE \t: {free_storage:.2f} GB\n==================================")
  print("\n====================\nDOWNLOADER \n1:YOUTUBE = YT\n2.TIKTOK = TT\n3.INSTAGRAM = IG\n4.FACEBOOK = FB \n5.PINTEREST = PIN\n====================\nAI\n1.OPENAI = AI\n2.MIYU-AI = MAI\n====================")


def head():
  icon = [
  (f"{x.GREEN}  _______   ____  __________  __   ____"),
  (" / ___/ /  /  _/ /_  __/ __ \/ /  / __/"),
  ("/ /__/ /___/ /    / / / /_/ / /___\ \  "),
  ("\___/____/___/   /_/  \____/____/___/ ")
  ]
  for huruf in icon :
    print(huruf)

#Loading 
def Loading():
  load = [
    (f"\n\n{x.YELLOW}Loading......\n",1),
    (f"{x.YELLOW}Mengirim info video....\n",1)
    ]
  for baris, jeda in load:
    for huruf in baris :
      print(huruf, end='',flush=True)
      time.sleep(jeda / len(baris))
    print()
    time.sleep(2)

def pini():
  pinicon = [
    ("\t\t    ____  _____   ______  __ ",1),
    ("\t\t   / __ \/  _/ | / / __ \/ /   ",1),
    ("\t\t  / /_/ // //  |/ / / / / /     ",1),
    ("\t\t / ____// // /|  / /_/ / /___",1),
    ("\t \t/_/   /___/_/ |_/_____/_____/\n\n",1)
    ]
  for baris, jeda in pinicon:
    for huruf in baris :
      print(huruf, end='',flush=True)
      time.sleep(jeda / len(baris))
    print()

def fbi():
  fbicon = [
    ("\t\t    ________    ____  __ ",1),
    ("\t\t   / ____/ /_  / __ \/ /   ",1),
    ("\t\t  / /_  / __ \/ / / / /     ",1),
    ("\t\t / __/ / /_/ / /_/ / /___",1),
    ("\t \t/_/   /_.___/_____/_____/\n\n",1)
    ]
  for baris, jeda in fbicon:
    for huruf in baris :
      print(huruf, end='',flush=True)
      time.sleep(jeda / len(baris))
    print()
def igi():
  igicon = [
    ("\t\t       ____      ____  __ ",1),
    ("\t\t      /  _/___ _/ __ \/ /  ",1),
    ("\t\t     / // __ `/ / / / /   ",1),
    ("\t\t   _/ // /_/ / /_/ / /___",1),
    ("\t \t  /___/\__, /_____/_____",1),
    ("\t\t      /____/  \n\n",1)
    ]
  for baris, jeda in igicon:
    for huruf in baris :
      print(huruf, end='',flush=True)
      time.sleep(jeda / len(baris))
    print()
def tti():
  tticon = [
    ("\t\t   ________________  __ ",1),
    ("\t\t  /_  __/_  __/ __ \/ / ",1),
    ("\t\t   / /   / / / / / / /  ",1),
    ("\t\t  / /   / / / /_/ / /___",1),
    ("\t \t /_/   /_/ /_____/_____/\n\n",1)
    ]
  for baris, jeda in tticon:
    for huruf in baris :
      print(huruf, end='',flush=True)
      time.sleep(jeda / len(baris))
    print()
def yti():
  wlm = [
      ("\t\t__  ____________  __",1),
      ("\t\t\ \/ /_  __/ __ \/ /   ",1),
      ("\t\t \  / / / / / / / /  ",1),
      ("\t\t / / / / / /_/ / /___",1),
      ("\t\t/_/ /_/ /_____/_____/  \n\n",1)
      ]
  for baris, jeda in wlm:
    for huruf in baris :
      print(huruf, end='',flush=True)
      time.sleep(jeda / len(baris))
    print()
def miyu():
  icon = [
    ("",0),
    ("",0),
    ("__  __ _____   ___   _      _    ___  ",1),
    (" |  \/  |_ _\ \ / / | | |    / \  |_ _| ",1),
    (" | |\/| || | \ V /| | | |   / _ \  | |  ",1),
    (" | |  | || |  | | | |_| |  / ___ \ | |  ",1),
    (" |_|  |_|___| |_|  \___/  /_/   \_\___| ",1)
    ]
  for baris,jeda in icon:
    for huruf in baris :
      print(huruf, end='',flush=True)
      time.sleep(jeda / len(baris))
    print()
    

#Spiner Text
#class spiner dev
class devspiner:
    def __init__(self, message):
        self.message = message
        self.spinner_characters = [f'{x.GREEN}@TAN', f'{x.YELLOW}@TAN', f'{x.YELLOW}@TAN', f'{x.RED}@TAN',f'{x.WHITE}@TAN']
        self.stop_event = threading.Event()
        self.thread = threading.Thread(target=self.run_spinner)

    def run_spinner(self):
        """Menjalankan spinner di latar belakang."""
        while not self.stop_event.is_set():
            for character in self.spinner_characters:
                sys.stdout.write(f'\r{self.message} {character}')
                sys.stdout.flush()
                time.sleep(0.1)

    def start(self):
        """Memulai spinner."""
        self.thread.start()

    def stop(self):
        """Menghentikan spinner."""
        self.stop_event.set()
        self.thread.join()  # Tunggu sampai thread spinner selesai
        sys.stdout.write('\r')  # Menghapus spinner dari terminal
        sys.stdout.flush()

class aireq:
    def __init__(self, message):
        self.message = message
        self.spinner_characters = [f'{x.GREEN}AI', f'{x.YELLOW}AI', f'{x.YELLOW}AI', f'{x.RED}AI',f'{x.WHITE}AI']
        self.stop_event = threading.Event()
        self.thread = threading.Thread(target=self.run_spinner)

    def run_spinner(self):
        """Menjalankan spinner di latar belakang."""
        while not self.stop_event.is_set():
            for character in self.spinner_characters:
                sys.stdout.write(f'\r{self.message} {character}')
                sys.stdout.flush()
                time.sleep(0.1)

    def start(self):
        """Memulai spinner."""
        self.thread.start()

    def stop(self):
        """Menghentikan spinner."""
        self.stop_event.set()
        self.thread.join()  # Tunggu sampai thread spinner selesai
        sys.stdout.write('\r')  # Menghapus spinner dari terminal
        sys.stdout.flush()
class load:
    def __init__(self, message):
        self.message = message
        self.spinner_characters = [f'{x.GREEN}.', f'{x.YELLOW}..', f'{x.YELLOW}...', f'{x.RED}....',f'{x.WHITE}.....']
        self.stop_event = threading.Event()
        self.thread = threading.Thread(target=self.run_spinner)

    def run_spinner(self):
        """Menjalankan spinner di latar belakang."""
        while not self.stop_event.is_set():
            for character in self.spinner_characters:
                sys.stdout.write(f'\r{self.message} {character}')
                sys.stdout.flush()
                time.sleep(0.1)

    def start(self):
        """Memulai spinner."""
        self.thread.start()

    def stop(self):
        """Menghentikan spinner."""
        self.stop_event.set()
        self.thread.join()  # Tunggu sampai thread spinner selesai
        sys.stdout.write('\r')  # Menghapus spinner dari terminal
        sys.stdout.flush()

#spiner Loading
class TextSpinner:
    def __init__(self, message):
        self.message = message
        self.spinner_characters = [f'{x.GREEN}Loading.',f'{x.YELLOW}Loading..',f'{x.YELLOW}Loading...',f'{x.RED}Loading....',f'{x.WHITE}Loading.....']
        self.stop_event = threading.Event()
        self.thread = threading.Thread(target=self.run_spinner)

    def run_spinner(self):
        """Menjalankan spinner di latar belakang."""
        while not self.stop_event.is_set():
            for character in self.spinner_characters:
                sys.stdout.write(f'\r{self.message} {character}')
                sys.stdout.flush()
                time.sleep(0.5)

    def start(self):
        """Memulai spinner."""
        self.thread.start()

    def stop(self):
        """Menghentikan spinner."""
        self.stop_event.set()
        self.thread.join()  # Tunggu sampai thread spinner selesai
        sys.stdout.write('\r')  # Menghapus spinner dari terminal
        sys.stdout.flush()
#run and stop spinner
def dev():
  spinner = devspiner("====> Creator")
  spinner.start() #Mulai spinner 
    # Simulasi pekerjaan yang memakan waktu
  time.sleep(2)  # Ganti dengan kode yang Anda ingin jalankan
    # Hentikan spinner
  spinner.stop()

def resai():
  spinner = aireq("LOADING ")
  spinner.start() #Mulai spinner 
    # Simulasi pekerjaan yang memakan waktu
  time.sleep(2)  # Ganti dengan kode yang Anda ingin jalankan
    # Hentikan spinner
  spinner.stop()
def loading():
  spinner = load("LOADING")
  spinner.start() #Mulai spinner 
    # Simulasi pekerjaan yang memakan waktu
  time.sleep(2)  # Ganti dengan kode yang Anda ingin jalankan
    # Hentikan spinner
  spinner.stop()
#DOWNLOADER
#ytdl
def ytdl():
  os.system("clear")
  yti()
  search = input(f"{x.WHITE}\n\nMasukkan judul Youtube ")
  os.system("clear")
  result = Search(f"{search}")
  for video in result.videos:
    Loading()
    print(f'{x.CYAN}Title: {video.title}\n')
    print(f'{x.CYAN}URL: {video.watch_url}\n')
    print(f'{x.CYAN}Duration: {video.length} seg\n')
    print(f'{x.GREEN}Done✓\n')
    y = input("Next? [y/n] ")
    if y == "y" or y == "Y":
      pass
    else:
      break
  url = input("\ninput Link : ")
  yt = YouTube(url, on_progress_callback = on_progress)
  print(yt.title)
  while True:
    tipe = input(f"\n\n{x.BLUE}Mau download mp3 atau mp4 ?\n [mp3/mp4] : ")
    print()
    print()
    if tipe == "mp4" or tipe == "Mp4":
      ys = yt.streams.get_highest_resolution()
      ys.download()
      print(f"{x.GREEN}\n\nSukses✓")
      print()
      print()
      break
  #mp3 download
    elif tipe == "mp3" or tipe == "Mp3":
      ys = yt.streams.get_audio_only()
      ys.download(mp3=True)
      print(f"{x.GREEN}\n\nSukses✓")
      print()
      print()
      break
    else:
      print(f"{color.RED}invalid input!!!")
#fbdl
def fbdl(url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',  # Menentukan nama file output
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
def linkfb():
  url = input("Enter link Facebook : ")
  fbdl(url)
  
#Igdl
def igdl(url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
def linkig():
  url = input("Enter link INSTAGRAM : ")
  igdl(url)
##ttdl
def ttdl(url):
  os.system("clear")
  ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',  # Mengatur nama file output
        'noplaylist': True,  # Hanya unduh video, bukan playlist
    }

  try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
      ydl.download([url])
      print("Video berhasil diunduh.")
  except Exception as e:
    print(f"Gagal mengunduh video: {e}")
def linktt():
  url = input("Enter link TIKTOK : ")
  ttdl(url)
#pinterest
def fetch_pinterest_images(url):
    # Mengirim permintaan GET ke URL Pinterest
    response = requests.get(url)

    # Memeriksa apakah permintaan berhasil (status code 200)
    if response.status_code == 200:
        data = response.json()

        # Menyiapkan list untuk menyimpan URL gambar
        image_urls = []

        # Ekstraksi data dari respons JSON
        try:
            pins = data['resource_response']['data']['results']
            for pin in pins:
                # Mencari URL gambar dari struktur JSON
                image_url = pin['images']['orig']['url']
                image_urls.append(image_url)
        except KeyError:
            print("Data JSON tidak memiliki format yang diharapkan.")
            return []

        return image_urls
    else:
        print(f"Gagal mengambil data, status code: {response.status_code}")
        return []

def download_image(image_url, output_dir):
    # Membuat nama file berdasarkan URL gambar
    filename = os.path.join(output_dir, image_url.split('/')[-1])

    # Mendownload gambar
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"Gambar berhasil didownload: {filename}")
    else:
        print(f"Gagal mendownload gambar dari {image_url}, status code: {response.status_code}")
    return filename

def move_to_sdcard(filename, sdcard_dir):
    # Memastikan direktori SD card ada atau membuatnya
    os.makedirs(sdcard_dir, exist_ok=True)

    # Nama file baru di SD card
    new_path = os.path.join(sdcard_dir, os.path.basename(filename))

    # Memindahkan file ke SD card
    shutil.move(filename, new_path)
    print(f"Gambar dipindahkan ke: {new_path}")

def download_images_from_pinterest(pinterest_url, output_dir, sdcard_dir):
    # Membuat direktori output jika belum ada
    os.makedirs(output_dir, exist_ok=True)

    # Mengambil URL gambar dari Pinterest
    image_urls = fetch_pinterest_images(pinterest_url)

    # Mendownload setiap gambar dari URL yang ditemukan dan memindahkannya ke SD card
    for image_url in image_urls:
        downloaded_file = download_image(image_url, output_dir)
        move_to_sdcard(downloaded_file, sdcard_dir)
def linkpin():
  query = input("What photos do you want to download? ")
  os.system("clear")
  loading()
  pinterest_url = f"https://id.pinterest.com/resource/BaseSearchResource/get/?_=1619980301559&data=%7B%22options%22%3A%7B%22isPrefetch%22%3Afalse%2C%22query%22%3A%22${query}%22%2C%22scope%22%3A%22pins%22%2C%22no_fetch_context_on_resource%22%3Afalse%7D%2C%22context%22%3A%7B%7D%7D&source_url=%2Fsearch%2Fpins%2F%3Fq%3D{query}"
    # Direktori output untuk menyimpan gambar yang diunduh
  sdcard_dir = '/storage/emulated/0/Download'
  output_dir = f'{query}'
  download_images_from_pinterest(pinterest_url, output_dir, sdcard_dir)
  print(f"\nThe photo has been successfully saved on  {query}")

#ai
def ai():
  i = 1
  while i > 0:
    i +=1
    text = input("\nAnda : ")
    print()
    print()
    resai()
    url =(f"https://widipe.com/openai?text={text}")
    response = requests.get(url)
    text = response.json()
    if "result" in text :
      ai = text['result']
      x = [
      (f"AI : {ai}",1)
      ]
    for baris, jeda in x:
      for huruf in baris :
        print(huruf, end='',flush=True)
        time.sleep(jeda / len(baris))
      print()
      time.sleep(2)
    if i > 10 :
      x = input("NEXT [y/n] : ")
      def go():
        if x == "y" or x == "Y":
          pass
        elif x == "n" or x == "N":
          def back():
            b = input("Back to main? [y/n]")
            if b == "Y" or b == "y":
              import call 
            elif b == "n" or b == "N":
              pass
            else:
              print("Invalid keyword plis input y or no \n")
              back()
          back() 
        else:
          print("Invalid Keyword input y or n ")
          go()
      go()
      
#Runner all fuction
#Program Downloader and Ai interaction
#Creator @Tan 
#Enjoy The program You are free to modify and add features as you like. Don't forget to give the sc creator 
def main():
  os.system("clear")
  loading() #from modul reqai
  os.system("clear")
  #print("")
  #print("")
  dev()#from modul dev  
  head() #from modul interface 
  osinfo() #from modul interface 
  tipe = input("\n\n ENTER THE FAIRY CODE \n ENTER COMMAND CODE  :  ")
  if tipe == "TT" or tipe == "Tt":
    linktt()
    def go():
      next = input("\nBack to Main [y/n] ")
      if next == "Y" or next == "y":
        os.system('clear')
        dev()
        main()
      elif next == "n" or next == "N":
        os.system('clear')
        dev()
        os.system("clear")
        print (f"{x.GREEN}STOP THE PROGRAM ✓ ")
      else:
        os.system('clear')
        print("EROR keyword !! ")
        dev()
        go()
    go()
  elif tipe == "Tiktok" or tipe == "tiktok":
    linktt()
    def go():
      next = input("\nBack to Main [y/n] ")
      if next == "Y" or next == "y":
        os.system('clear')
        dev()
        main()
      elif next == "n" or next == "N":
        os.system('clear')
        dev()
        os.system("clear")
        print (f"{x.GREEN}STOP THE PROGRAM ✓ ")
      else:
        os.system('clear')
        print("EROR keyword !! ")
        dev()
        go()
    go()
  elif tipe == "TIKTOK" or tipe == "tt":
    linktt()
    def go():
      next = input("\nBack to Main [y/n] ")
      if next == "Y" or next == "y":
        os.system('clear')
        dev()
        main()
      elif next == "n" or next == "N":
        os.system('clear')
        dev()
        os.system("clear")
        print (f"{x.GREEN}STOP THE PROGRAM ✓ ")
      else:
        os.system('clear')
        print("EROR keyword !! ")
        dev()
        go()
    go()
  elif tipe == "yt" or tipe == "YT":
    os.system('clear')
    loading()
    ytdl()
    def go():
      next = input("\nBack to Main [y/n] ")
      if next == "Y" or next == "y":
        os.system('clear')
        dev()
        main()
      elif next == "n" or next == "N":
        os.system('clear')
        dev()
        os.system("clear")
        print (f"{x.GREEN}STOP THE PROGRAM ✓ ")
      else:
        os.system('clear')
        print("EROR keyword !! ")
        dev()
        go()
    go()
  elif tipe == "Youtube" or tipe == "youtube":
    os.system("clear")
    loading()
    ytdl()
    def go():
      next = input("\nBack to Main [y/n] ")
      if next == "Y" or next == "y":
        os.system('clear')
        dev()
        main()
      elif next == "n" or next == "N":
        os.system('clear')
        dev()
        os.system("clear")
        print (f"{x.GREEN}STOP THE PROGRAM ✓ ")
      else:
        os.system('clear')
        print("EROR keyword !! ")
        dev()
        go()
    go()
  elif tipe == "ig" or tipe == "IG":
    os.system("clear")
    igi()
    linkig()
    def go():
      next = input("\nBack to Main [y/n] ")
      if next == "Y" or next == "y":
        os.system('clear')
        dev()
        main()
      elif next == "n" or next == "N":
        os.system('clear')
        dev()
        os.system("clear")
        print (f"{x.GREEN}STOP THE PROGRAM ✓ ")
      else:
        os.system('clear')
        print("EROR keyword !! ")
        dev()
        go()
    go()
  elif tipe == "instagram" or tipe == "Instagram":
    os.system("clear")
    igi()
    linkig()
    def go():
      next = input("\nBack to Main [y/n] ")
      if next == "Y" or next == "y":
        os.system('clear')
        dev()
        main()
      elif next == "n" or next == "N":
        os.system('clear')
        dev()
        os.system("clear")
        print (f"{x.GREEN}STOP THE PROGRAM ✓ ")
      else:
        os.system('clear')
        print("EROR keyword !! ")
        dev()
        go()
    go()
  elif tipe == "fb" or tipe == "Fb":
    os.system('clear')
    fbi()
    linkfb()
    def go():
      next = input("\nBack to Main [y/n] ")
      if next == "Y" or next == "y":
        os.system('clear')
        dev()
        main()
      elif next == "n" or next == "N":
        os.system('clear')
        dev()
        os.system("clear")
        print (f"{x.GREEN}STOP THE PROGRAM ✓ ")
      else:
        os.system('clear')
        print("EROR keyword !! ")
        dev()
        go()
    go()
    
  elif tipe == "Fb":
    os.system('clear')
    fbi()
    linkfb()
    def go():
      next = input("\nBack to Main [y/n] ")
      if next == "Y" or next == "y":
        os.system('clear')
        dev()
        main()
      elif next == "n" or next == "N":
        os.system('clear')
        dev()
        os.system("clear")
        print (f"{x.GREEN}STOP THE PROGRAM ✓ ")
      else:
        os.system('clear')
        print("EROR keyword !! ")
        dev()
        go()
    go()
  elif tipe == "Pinterest" or tipe == "pinterest":
    os.system('clear')
    pini()
    linkpin()
    def go():
      next = input("\nBack to Main [y/n] ")
      if next == "Y" or next == "y":
        os.system('clear')
        dev()
        main()
      elif next == "n" or next == "N":
        os.system('clear')
        dev()
        os.system("clear")
        print (f"{x.GREEN}STOP THE PROGRAM ✓ ")
      else:
        os.system('clear')
        print("EROR keyword !! ")
        dev()
        go()
    go()
  elif tipe == "Pin" or tipe == "pin":
    os.system('clear')
    pini()
    linkpin()
    def go():
      next = input("\nBack to Main [y/n] ")
      if next == "Y" or next == "y":
        os.system('clear')
        dev()
        main()
      elif next == "n" or next == "N":
        os.system('clear')
        dev()
        os.system("clear")
        print (f"{x.GREEN}STOP THE PROGRAM ✓ ")
      else:
        os.system('clear')
        print("EROR keyword !! ")
        dev()
        go()
    go()
  elif tipe == "Openai" or tipe == "openai":
    ai()
  elif tipe == "Ai" or tipe == "ai":
    os.system("clear")
    ai()
  elif tipe == "AI":
    os.system("clear")
    ai()
  elif tipe == "mai" or tipe == "Mai":
    os.system('clear')
    miyuai()
  elif tipe == "MAI" or tipe == "Miyu-ai":
    os.system('clear')
    miyuai()
  else:
    print("Invalid Input!! ")
    main()

main()

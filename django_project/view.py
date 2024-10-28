from django.http import HttpResponse
from django.shortcuts import render


def index(request):
  context = {
      'title':
      'Daftar Buku',
      'all_buku': [
          {
              "no" :1,
              "judul": "Belajar Pemrograman Python",
              "tahun": 2015,
              "author": "Alfian"
          },
          {
              "no" :2,

              "judul": "HTML untuk pemula",
              "tahun": 2014,
              "author": "Firzy"
          },
          {
              "no" :3,

              "judul":
              "Membuat aplikasi sederhana menggunakan Framework Django",
              "tahun": 2020,
              "author": "Yusuf"
          },
      ]
  }

  return render(request, 'index.html', context)

from moviepy.editor import *

import os

from pytubefix import YouTube
from pytubefix.cli import on_progress

import sys

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox

def widgets() -> None:
   linkLabel = tk.Label(
      root,
      text='Link: ',
      font='System 22',
      bg='DarkSlateBlue',
      padx=5,
      pady=5
   )
   linkLabel.grid(
      row=0,
      column=0,
      padx=5,
      pady=5
   )
   linkText = tk.Entry(
      root,
      textvariable=link,
      width=25,
      font='System 22'
   )
   linkText.grid(
      row=0,
      column=1,
      padx=5,
      pady=5,
      columnspan=6
   )

   pathLabel = tk.Label(
      root,
      text='Path: ',
      font='System 22',
      bg='DarkSlateBlue',
      padx=5,
      pady=5
   )
   pathLabel.grid(
      row=1,
      column=0,
      padx=5,
      pady=5
   )
   pathText = tk.Entry(
      root,
      textvariable=path,
      font='System 22'
   )
   pathText.grid(
      row=1,
      column=1,
      padx=5,
      pady=5,
   )
   browseButton = tk.Button(
      root,
      text='Browse',
      font='System 11',
      bg='SlateGrey',
      command=browse
   )
   browseButton.grid(
      row=1,
      column=5,
      padx=0,
      pady=0,
   )

   typeLabel = tk.Label(
      root,
      text='Type: ',
      font='System 22',
      bg='DarkSlateBlue',
      padx=5,
      pady=5
   )
   typeLabel.grid(
      row=2,
      column=0,
      padx=5,
      pady=5,
   )
   typeSelect = ttk.Combobox(
      root,
      state="readonly",
      values=['mp3', 'mp4'],
      textvariable=mediaType,
      font='System 22',
   )
   typeSelect.grid(
      row=2,
      column=1,
      padx=5,
      pady=5,
      columnspan=7
   )

   downloadBut = tk.Button(
      root,
      text='Download',
      font='System 22',
      bg='SlateGrey',
      command=download
   )
   downloadBut.grid(
      row=3,
      column=0,
      padx=5,
      pady=5,
      columnspan=7
   )

def browse() -> None:
   downloadPath = filedialog.askdirectory(
      title='Save as'
   )
   path.set( downloadPath )

def download() -> None:
   inputLink = link.get()
   downloadPath = path.get()
   downloadType = mediaType.get()

   getVideo = YouTube( inputLink )

   videoStream = getVideo.streams.get_highest_resolution()
   outFile = videoStream.download( downloadPath )

   if downloadType == 'mp3':
      video = AudioFileClip( outFile )

      base, _ = os.path.splitext( outFile )
      newOutFile = base + '.mp3'

      video.write_audiofile( newOutFile )
      video.close()

      os.remove( outFile )

   messagebox.showinfo( 'Success', 'Downloaded into "' + downloadPath + '"' )

if __name__ == '__main__':
   root = tk.Tk()

   root.geometry( '528x297' )
   root.resizable( False, False )
   root.title( 'pangGetVideo' )
   root.config( background='DarkSlateBlue' )

   link = tk.StringVar()
   path = tk.StringVar()
   mediaType = tk.StringVar()

   widgets()

   sys.exit( root.mainloop() )
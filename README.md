# YouTube Video Downloader

A simple, user-friendly GUI application for downloading YouTube videos in the highest available resolution using Python and Tkinter.

## Features

- 🎥 Download YouTube videos in highest resolution
- 📁 Choose custom download location
- 📊 Real-time download progress
- 🔍 Find your latest downloaded file
- 🖥️ Clean and intuitive GUI interface
- ⚡ Fast and reliable downloads

## Screenshots

![YouTube Downloader Interface](screenshot.png)
*Simple and clean interface for easy video downloading*

## Requirements

- Python 3.6 or higher
- tkinter (usually comes with Python)
- pytubefix

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/youtube-downloader.git
   cd youtube-downloader
   ```

2. **Install required dependencies:**
   ```bash
   pip install pytubefix
   ```

3. **Run the application:**
   ```bash
   python Project1.py
   ```

## Usage

1. **Launch the application** by running the Python script
2. **Enter a YouTube video URL** in the text field
3. **Click "Download Video"** - you'll be prompted to select a download folder
4. **Wait for the download to complete** - a success message will appear
5. **Use "Show Latest File"** to see your most recently downloaded video

## How It Works

The application uses the `pytubefix` library (a maintained fork of pytube) to:
- Extract video information from YouTube URLs
- Download the highest resolution stream available
- Provide download progress feedback
- Handle errors gracefully with user-friendly messages

## File Structure

```
youtube-downloader/
│
├── Project1.py          # Main application file
├── README.md           # This file
└── requirements.txt    # Python dependencies
```

## Dependencies

- **pytubefix**: For YouTube video downloading functionality
- **tkinter**: For the graphical user interface (built into Python)
- **glob**: For file system operations (built into Python)
- **os**: For operating system interface (built into Python)

## Troubleshooting

### Common Issues

**"Failed to download video" error:**
- Check your internet connection
- Verify the YouTube URL is correct and accessible
- Some videos may be restricted or unavailable in your region

**"No video files found" when checking latest file:**
- Make sure you've downloaded at least one video
- Ensure you're checking the same folder where videos were saved

**Application won't start:**
- Verify Python 3.6+ is installed
- Install pytubefix: `pip install pytubefix`
- Check that tkinter is available (try `python -m tkinter`)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Future Enhancements

- [ ] Support for downloading audio-only files
- [ ] Batch download multiple videos
- [ ] Download quality selection
- [ ] Playlist support
- [ ] Download history
- [ ] Custom file naming
- [ ] Progress bar in the GUI

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is for educational purposes only. Please respect YouTube's Terms of Service and only download videos you have permission to download. The developers are not responsible for any misuse of this software.

## Acknowledgments

- [pytubefix](https://github.com/JuanBindez/pytubefix) - The library that makes this downloader possible
- Original pytube library developers
- Python tkinter documentation and community

## Support

If you encounter any issues or have questions, please [open an issue](https://github.com/yourusername/youtube-downloader/issues) on GitHub.

---

**⭐ If you found this project helpful, please give it a star!**
# Safe Data Handling Utilities

Small Python helpers that treat all external input strictly as **data** — never as code or instructions.

## Features

- Size limits on input (both character length and UTF-8 byte size)
- Safe processing of untrusted text
- HTML escaping before display
- Phone-number validation that accepts **digits only**

## Requirements

- Python 3.6 or newer  
  (No external packages needed)

## How to run the example

```bash
python safe_data.py
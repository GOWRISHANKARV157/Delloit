# Deloitte Assessment - Telemetry Conversion

## 📌 Project Overview

This repository contains a Python-based solution for converting telemetry data from multiple input formats into a unified structure.

The project demonstrates data transformation, timestamp normalization, and structured JSON processing.

---

## 📂 Project Structure

```
delloit/
└── telemetry-conversion/
    ├── main.py
    ├── data-1.json
    ├── data-2.json
    ├── data-result.json
```

---

## ⚙️ Features

* Supports multiple telemetry input formats
* Converts ISO 8601 timestamps to milliseconds since epoch
* Normalizes nested and flat JSON structures
* Ensures consistent output schema
* Includes unit tests validation

---

## 🔄 Conversion Logic

### Format 1

* Extracts location from a single string
* Maps fields directly into unified schema

### Format 2

* Parses ISO timestamp → converts to epoch milliseconds
* Extracts nested device information
* Aligns structure with unified output format

---

## 🚀 How to Run

```bash
cd telemetry-conversion
python main.py
```

---

## ✅ Expected Output

```
Ran 3 tests in X.XXXs
OK
```

---

## 🛠️ Technologies Used

* Python 3
* JSON Processing
* Datetime module

---

## 👨‍💻 Author

Gowri Shankar

---

## 📌 Notes

* UTF-8 encoding used to handle file reading
* Assumes valid input JSON structure
* Designed to pass all provided unit tests

---

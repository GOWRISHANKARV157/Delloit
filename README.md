# Telemetry Data Conversion — Technical Project Report

**Author:** Gowri Shankar V
**Programme:** Deloitte Job Simulation — Technical Assessment
**Language:** Python 3
**Document Type:** Technical Project Report

---

## 1. Abstract

This report presents a Python-based software solution developed as part of the Deloitte Technical Job Simulation. The project addresses the practical challenge of ingesting telemetry data from heterogeneous input sources and converting it into a unified, schema-consistent output format. The solution demonstrates proficiency in JSON processing, timestamp normalisation, and structured data transformation — core competencies expected of a data engineering analyst at Deloitte.

---

## 2. Introduction

In modern enterprise environments, telemetry systems collect operational data from a wide variety of devices and sensors. These systems frequently produce data in differing formats, schemas, and timestamp conventions, making downstream analytics and monitoring unreliable without a robust normalisation layer.

This project simulates such a real-world scenario. Given two distinct telemetry data sources — each with its own structural conventions — the objective is to develop a deterministic Python pipeline that transforms both formats into a single, consistent output schema. The result is a reusable, testable module that can serve as the data ingestion layer in a larger analytics or monitoring platform.

---

## 3. Project Structure

The repository follows a simple, flat directory layout appropriate for a focused data conversion task:

```
delloit/
└── telemetry-conversion/
    ├── main.py           # Core conversion logic and unit tests
    ├── data-1.json       # Input — Format 1 telemetry records
    ├── data-2.json       # Input — Format 2 telemetry records
    ├── data-result.json  # Expected unified output
    └── Deloitte Job Simulation — Technical Assessment # Assessment Desc
```

The consolidation of logic within `main.py` is intentional: it promotes transparency and makes the submission self-contained for assessment purposes. In a production context, this would be modularised into separate parser, transformer, and validator components.

---

## 4. System Design and Conversion Logic

### 4.1 Format 1 — Flat Structure Mapping

The first input format adheres to a flat JSON structure, where geospatial information is embedded within a single location string. The conversion pipeline performs the following operations:

- Reads each record from `data-1.json` using UTF-8 encoding to support internationalised device names and locations.
- Parses the `location` field from a concatenated string into its constituent latitude and longitude components.
- Maps remaining fields directly to the target schema using defined key aliases, preserving data integrity throughout.

### 4.2 Format 2 — Nested Structure with Timestamp Normalisation

The second input format introduces additional structural complexity through nested device metadata and ISO 8601 formatted timestamps. The conversion pipeline handles these as follows:

- Parses the ISO 8601 timestamp string and converts it to the number of milliseconds elapsed since the Unix epoch (1 January 1970, 00:00:00 UTC), using Python's `datetime` module.
- Traverses the nested device object to extract device identifier, type, and firmware version, flattening these into the top-level output schema.
- Aligns all extracted fields with the unified output format, ensuring structural consistency with Format 1 output records.

---

## 5. Unified Output Schema

Both input formats are transformed into a common schema, which is validated against the reference output file `data-result.json`. The schema enforces the following field conventions:

| Field | Type | Description |
|---|---|---|
| `deviceId` | String | Unique identifier of the reporting device |
| `timestamp` | Integer (ms) | Epoch time in milliseconds since 1 Jan 1970 |
| `location.lat` | Float | Latitude of the device in decimal degrees |
| `location.lng` | Float | Longitude of the device in decimal degrees |
| `temperature` | Float | Recorded temperature reading from the sensor |
| `deviceType` | String | Category or model classification of the device |

---

## 6. Technologies and Dependencies

The solution relies exclusively on Python's standard library, ensuring portability and ease of execution in any standard Python 3 environment without the need for third-party package installation.

| Module / Tool | Purpose |
|---|---|
| `Python 3` | Core runtime environment for executing the conversion pipeline |
| `json` | Parsing input JSON files and serialising the unified output |
| `datetime` | Converting ISO 8601 timestamp strings to epoch milliseconds |
| `unittest` | Validating conversion correctness through automated test cases |

---

## 7. Execution Instructions

To execute the conversion pipeline and run the unit test suite, navigate to the project directory and invoke the main module as follows:

```bash
cd delloit/telemetry-conversion
python main.py
```

Upon successful execution, the test runner will report the outcome of three unit tests. A passing run produces the following output:

```
Ran 3 tests in 0.002s
OK
```

The UTF-8 encoding flag is applied during file I/O operations to accommodate any special characters present in location names or device identifiers within the input datasets.

---

## 8. Testing and Validation

The project includes a suite of three automated unit tests implemented using Python's built-in `unittest` framework. These tests verify the correctness of the conversion logic against the provided reference output file (`data-result.json`), covering the following scenarios:

- Correct transformation of Format 1 records, including accurate location string parsing and field mapping.
- Correct transformation of Format 2 records, including ISO 8601 timestamp conversion to epoch milliseconds and nested field extraction.
- Schema consistency validation, confirming that all output records conform to the unified output structure regardless of their source format.

The use of automated testing ensures the solution is deterministic and reproducible — a critical quality in data pipeline development where downstream consumers depend on consistent data shapes.

---

## 9. Design Considerations and Assumptions

Several deliberate design decisions were made during development to ensure robustness and alignment with the assessment requirements:

- The solution assumes all input JSON files are well-formed and structurally valid. No defensive error handling for malformed input has been included, as the assessment scope defines valid data as a precondition.
- UTF-8 encoding is explicitly specified for all file read operations to ensure cross-platform compatibility, particularly on Windows environments where the default encoding may differ.
- The `datetime` module's timezone-aware parsing is used for Format 2 timestamps to ensure accurate epoch conversion irrespective of the system's local timezone configuration.
- Field naming in the unified schema follows camelCase conventions consistent with JSON best practices and Deloitte's typical API design standards.

---

## 10. Conclusion

This project demonstrates a clear and methodical approach to a common data engineering challenge: the harmonisation of disparate telemetry data formats into a reliable, schema-consistent output. The solution is lightweight, dependency-free, and fully validated through automated testing.

The techniques applied — JSON processing, timestamp normalisation, schema flattening, and unit testing — reflect the analytical rigour and attention to detail expected of an entry-level analyst at Deloitte. The codebase is structured to be readable, maintainable, and extensible for integration into larger data pipeline architectures.

---

*Gowri Shankar · Deloitte Job Simulation · Telemetry Conversion Assessment*

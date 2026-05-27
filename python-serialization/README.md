# README - Python Serialization Module

## Description
This module teaches serialization and deserialization techniques in Python. It covers different data storage formats: JSON, Pickle, CSV, and XML.

## Learning Objectives
- Understand serialization and deserialization
- Master different data formats (JSON, Pickle, CSV, XML)
- Save and load complex data
- Handle file manipulation errors
- Convert between data formats

## Module Content

| Task | File | Description |
|------|------|-------------|
| 0 | `task_00_basic_serialization.py` | Basic JSON serialization with dictionaries |
| 1 | `task_01_pickle.py` | Pickling custom Python objects |
| 2 | `task_02_csv.py` | Convert CSV to JSON |
| 3 | `task_03_xml.py` | XML serialization |

## Skills Learned

### Task 0 - JSON
- `json.dump()` and `json.load()`
- Serialize Python dictionaries
- Read and write JSON files

### Task 1 - Pickle
- `pickle` module for custom objects
- Create classes with serialization methods
- `@classmethod` and class methods
- Exception handling

### Task 2 - CSV to JSON
- `csv.DictReader`
- Convert CSV to dictionary list
- Format JSON with indentation
- Error handling

### Task 3 - XML
- `xml.etree.ElementTree`
- Create XML structure from dictionary
- Parse and extract XML data
- Type conversion

## Format Comparison

| Format | Readable | Universal | Types | Use Case |
|--------|----------|-----------|-------|----------|
| **JSON** | ✅ | ✅ | Limited | APIs, config |
| **Pickle** | ❌ | ❌ | All | Python only |
| **CSV** | ✅ | ✅ | Strings | Tabular data |
| **XML** | ✅ | ✅ | Strings | Web, SOAP |

## Usage Examples

```python
# JSON
from task_00_basic_serialization import serialize_and_save_to_file
serialize_and_save_to_file({"name": "John"}, 'data.json')

# Pickle
from task_01_pickle import CustomObject
obj = CustomObject("John", 25, True)
obj.serialize('object.pkl')

# CSV to JSON
from task_02_csv import convert_csv_to_json
convert_csv_to_json('data.csv')

# XML
from task_03_xml import serialize_to_xml
serialize_to_xml({"name": "John"}, 'data.xml')
```

## Author
Holberton School - Python Advanced Curriculum
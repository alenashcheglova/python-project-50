### Hexlet tests and linter status:
[![Actions Status](https://github.com/alenashcheglova/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/alenashcheglova/python-project-50/actions)
[![Python CI](https://github.com/alenashcheglova/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/alenashcheglova/python-project-50/actions/workflows/pyci.yml)
[![Quality gate status](https://sonarcloud.io/api/project_badges/measure?project=alenashcheglova_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=alenashcheglova_python-project-50)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=alenashcheglova_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=alenashcheglova_python-project-50)

### Installation

```bash
uv tool install .
```

### Usage

```bash
gendiff file1.json file2.json
```

### JSON comparison

```bash
gendiff tests/test_data/file1.json tests/test_data/file2.json
```

```text
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
```

### YAML comparison

```bash
gendiff tests/test_data/file1.yml tests/test_data/file2.yml
```

```text
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
```

### Plain format

```bash
gendiff --format plain tests/test_data/nested_file1.json tests/test_data/nested_file2.json
```

```text
Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]
```

### JSON format

```bash
gendiff --format json tests/test_data/nested_file1.json tests/test_data/nested_file2.json
```

```json
[
    {
        "key": "common",
        "type": "nested",
        "children": [
            {
                "key": "follow",
                "type": "added",
                "value": false
            },
            {
                "key": "setting1",
                "type": "unchanged",
                "value": "Value 1"
            },
            {
                "key": "setting2",
                "type": "removed",
                "value": 200
            },
            {
                "key": "setting3",
                "type": "changed",
                "old_value": true,
                "new_value": null
            },
            {
                "key": "setting4",
                "type": "added",
                "value": "blah blah"
            },
            {
                "key": "setting5",
                "type": "added",
                "value": {
                    "key5": "value5"
                }
            },
            {
                "key": "setting6",
                "type": "nested",
                "children": [
                    {
                        "key": "doge",
                        "type": "nested",
                        "children": [
                            {
                                "key": "wow",
                                "type": "changed",
                                "old_value": "",
                                "new_value": "so much"
                            }
                        ]
                    },
                    {
                        "key": "key",
                        "type": "unchanged",
                        "value": "value"
                    },
                    {
                        "key": "ops",
                        "type": "added",
                        "value": "vops"
                    }
                ]
            }
        ]
    },
    {
        "key": "group1",
        "type": "nested",
        "children": [
            {
                "key": "baz",
                "type": "changed",
                "old_value": "bas",
                "new_value": "bars"
            },
            {
                "key": "foo",
                "type": "unchanged",
                "value": "bar"
            },
            {
                "key": "nest",
                "type": "changed",
                "old_value": {
                    "key": "value"
                },
                "new_value": "str"
            }
        ]
    },
    {
        "key": "group2",
        "type": "removed",
        "value": {
            "abc": 12345,
            "deep": {
                "id": 45
            }
        }
    },
    {
        "key": "group3",
        "type": "added",
        "value": {
            "deep": {
                "id": {
                    "number": 45
                }
            },
            "fee": 100500
        }
    }
]
```

#### Аскинема работы пакета на 5м шаге
https://asciinema.org/a/kXpZkLRChIsxU9rj

#### Аскинема работы пакета на 7м шаге
https://asciinema.org/a/kMEIQRYQc7k4SqGg

#### Аскинема работы пакета на 8м шаге
https://asciinema.org/a/bvrvC9JY9pGUtxM2

#### Аскинема работы пакета на 9м шаге
https://asciinema.org/a/kDFuZY9SHcdlwUSx

#### Аскинема работы пакета на 10м шаге
https://asciinema.org/a/iZk2IpGZwTwnckoE
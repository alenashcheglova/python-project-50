from gendiff.formatters.json import format_json
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish


def format_diff(diff_tree, format_name):
    if format_name == "stylish":
        return stylish(diff_tree)
    if format_name == "plain":
        return plain(diff_tree)
    if format_name == "json":
        return format_json(diff_tree)
    
    raise ValueError(f"Unknown format: {format_name}")
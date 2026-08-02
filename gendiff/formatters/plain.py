def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)


def plain(diff_tree, path=''):
    lines = []

    for node in diff_tree:
        key = node['key']
        node_type = node['type']
        current_path = f'{path}{key}'

        if node_type == 'added':
            value = format_value(node['value'])
            lines.append(f"Property '{current_path}' "
                         f"was added with value: {value}")
            
        elif node_type == 'removed':
            lines.append(f"Property '{current_path}' was removed")
            
        elif node_type == 'changed':
            old_value = format_value(node['old_value'])
            new_value = format_value(node['new_value'])
            lines.append(f"Property '{current_path}' was updated. "
                         f"From {old_value} to {new_value}")
            
        elif node_type == "nested":
            nested_lines = plain(node['children'], f'{current_path}.')
            if nested_lines:
                lines.append(nested_lines)
                
    return '\n'.join(lines)
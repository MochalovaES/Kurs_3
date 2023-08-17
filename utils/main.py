from utils.functions import load_operations, load_is_executed, load_sorted_operations, print_operations
filename = 'operations.json'
if __name__ == '__main__':
    operations = load_operations(filename)
    executed_operations = load_is_executed(operations)
    sorted_operations = load_sorted_operations(executed_operations)
    print(print_operations(sorted_operations))



import sys
from Trees import TreeNode, ArrayToBST, ArrayToAVL, PrintAll, Delete, Export, Balance

def main():
    tree_type = None
    input_values = []
    command_lines = [] #lista poleceń

    if len(sys.argv) > 1 and sys.argv[1] == '--tree':  
        if len(sys.argv) > 2:
            tree_type = sys.argv[2].upper()
    
    try:
        if tree_type.upper() not in {'AVL', 'BST'}:
            print("Invalid tree type. Use --tree AVL or --tree BST")
            return
    except AttributeError:
        print("Invalid argument. Use --tree AVL or --tree BST")
        return

    # jeśli nie terminal, a plik/heredoc 
    if not sys.stdin.isatty():
        all_input = sys.stdin.read().splitlines() #read() sczytuje cały input .splitlines() dzieli go liniami
        if len(all_input) > 0:
            # Jeśli wgl dali jakąś ilość wierzchołków
            if len(all_input) > 1:
                input_values = all_input[1].strip().split() #wierzchołki
            if len(all_input) > 2:
                command_lines = all_input[2:]  #Lista poleceń z pliczku/heredocu
        numbers = [int(i) for i in input_values]
    else:
        #tryb terminala ciąg dalszy~
        while True:
            print("\tnodes> ", end='', flush=True) #flush zapewnia, że się sprintuje przed wprowadzeniem inputa czy coś w tym stylu~
            try:
                node_count = input().strip()
                try:
                    node_count = int(node_count)
                    if node_count<1:
                        print("Node count must exceed 0")
                    else:
                        break
                except ValueError:                  #try+except sprawia że python niewywala jeśli ktoś wpisał string zamiast inta~
                    print("Invalid node count")
            except EOFError:
                print("\nExit unavailable - enter node count")
        
        while True:
            print("\tinsert> ", end='', flush=True)
            try:
                input_values = input().strip().split()
                try:
                    numbers = [int(x) for x in input_values]
                    if len(numbers)!=node_count:
                        print(f"Node count and Input count do not match - please enter {node_count} number{'s' if node_count > 1 else ''}")
                    else:
                        break
                except ValueError:
                    print("Invalid input values - must be integers f.e.:\tinsert> 2 8 4 3") #jeśli użytkownik wpisał coś co nie jest liczbą za wierzchołek
            except EOFError:
                print(f"\nExit unavailable -  please enter {node_count} number{'s' if node_count > 1 else ''}")

    
    root = None
    if tree_type == 'AVL':
        print("Sorted:", ", ".join(map(str, sorted(numbers))))
        mid = len(numbers) // 2
        print(f"Median: {sorted(numbers)[mid]}")
        root = ArrayToAVL(numbers)
    elif tree_type == 'BST':
        print("Inserting:", ", ".join(map(str, numbers)))
        root = ArrayToBST(numbers)
    else:
        print("Invalid tree type. Use --tree AVL or --tree BST")
        return
    
    def exist_root(cmd):
        if not root:
            print(f"Cannot {cmd} - tree is empty\nExiting the program is recommended. Enter 'exit' or press Ctrl+D.")
            return False
        return True

    def process_command(cmd):   #przesyłamy pojedynczą komendę
        nonlocal root           #zamiast tworzyć roota bierze istniejacego roota z funkcji up
        parts = cmd.split()
        if not parts:           #jeśli parts nie ma elementów- zwróć True (pusta linia, zabezpiecza parts[0] niżej)
            return True         
        
        command = parts[0].lower() #bierze pierwsze słowo z parts czyli np. *Remove* 12 3 5
        
        if command == 'help':
            print_help() 
        elif command == 'print':
            if exist_root(command):
                PrintAll(root)
        elif command == 'remove':
            if exist_root(command):
                if len(parts) < 2:
                    print("Usage: Remove <value1> <value2> ...")
                else:
                    for val in parts[1:]:
                        try:
                            val = int(val)
                            root = root.remove(val)
                        except ValueError:
                            print(f"Invalid value: {val}")
        elif command == 'delete':
            if exist_root(command):
                Delete(root)
                root = None
        elif command == 'export':
            if exist_root(command):
                print(Export(root))
        elif command == 'rebalance':
            if exist_root(command):
                root = Balance(root)
                print("Tree rebalanced")
        elif command == 'findmin':
            if exist_root(command):
                print("Min value:", root.findMin().value)
        elif command == 'findmax':
            if exist_root(command):
                print("Max value:", root.findMax().value) 
        elif command == 'exit':
            print("Program exited with status: 0")
            return False    
        else:
            print(f"Unknown command: {command}")
            print_help()
        return True 
    
    #jesli jest wiecej poleceń
    if command_lines:
        for cmd in command_lines:
            cmd = cmd.strip() 
            if cmd:  # pomija puste linie
                print("\taction>", cmd)  
                if not process_command(cmd):   #gdy zfalsuje (exit) kończymy sielaneczke
                    break
    else:
        #dopóki ctrl+d lub exit lecimy w kółeczko z >action
        while True:
            print("\taction> ", end='', flush=True)
            try:
                command = input().strip()
            except EOFError:
                print("\nProgram exited with status: 0")
                break
            if not process_command(command):
                break

def print_help():
    help_text = """
\tHelp\t\tShow this message
\tPrint\t\tPrint the tree with In-order, Pre-order, Post-order
\tRemove\t\tRemove elements from the tree
\tDelete\t\tDelete whole tree
\tExport\t\tExport the tree to tikzpicture
\tRebalance\tRebalance the tree
\tFindMin\t\tFind minimum value in the tree
\tFindMax\t\tFind maximum value in the tree
\tExit\t\tExit the program (same as ctrl+D)
    """
    print(help_text)

if __name__ == "__main__":
    main()

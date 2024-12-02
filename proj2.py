import socket
from random import randint

def roll_dice(die):
    """
    Helper function to roll a die based on its type (e.g., 'd4', 'd6').
    """
    if not die.startswith('d') or not die[1:].isdigit():
        return None, "Invalid dice format. Use 'd4', 'd6', etc."
    
    sides = int(die[1:])
    if sides < 1:
        return None, "Dice must have at least 1 side."
    
    return randint(1, sides), None

def send_to_server(host, port, message):
    """
    Sends a message to another server.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))
            client_socket.sendall(message.encode('utf-8'))
            response = client_socket.recv(1024).decode('utf-8')
        return response
    except Exception as e:
        return f"Error sending to server: {e}"

# Configuration
NEXT_SERVER_HOST = '127.0.0.1'  # Replace with the IP of the next server
NEXT_SERVER_PORT = 6790  # Replace with the port of the next server

# Main Program
print("Type 'roll dX' to roll a die (e.g., 'roll d20') or 'quit' to exit.")

while True:
    user_input = input("> ").strip()
    
    if user_input.lower() == 'quit':
        print("Exiting the program. Goodbye!")
        break
    
    # Parse command
    if user_input.lower().startswith("roll "):
        die = user_input[5:].strip()  # Extract the dice type (e.g., 'd20')
        result, error = roll_dice(die)
        
        if error:
            print(error)
        else:
            print(f"You rolled a {die}: {result}")
            
            # Send result to the next server
            response = send_to_server(NEXT_SERVER_HOST, NEXT_SERVER_PORT, f"Rolled {die}: {result}")
            print(f"Response from server: {response}")
    else:
        print("Invalid command. Use 'roll dX' or 'quit'.")

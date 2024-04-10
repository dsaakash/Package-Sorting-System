def sort_package(width, height, length, mass):
    """
    Sorts a package into STANDARD, SPECIAL, or REJECTED stack based on its dimensions and mass.
    
    Parameters:
    - width (int): Width of the package in cm.
    - height (int): Height of the package in cm.
    - length (int): Length of the package in cm.
    - mass (int): Mass of the package in kg.
    
    Returns:
    - str: The stack where the package should go ("STANDARD", "SPECIAL", "REJECTED").
    """
    # Calculate the volume of the package
    volume = width * height * length
    
    # Check if the package is bulky
    is_bulky = volume >= 1000000 or width >= 150 or height >= 150 or length >= 150
    
    # Check if the package is heavy
    is_heavy = mass >= 20
    
    # Determine the stack based on the package's properties
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

# Example
if __name__ == "__main__":
    # Test cases
    print(sort_package(10, 10, 10, 5))  # Should return "STANDARD"
    print(sort_package(150, 10, 10, 5))  # Should return "SPECIAL"
    print(sort_package(50, 50, 50, 20))  # Should return "SPECIAL"
    print(sort_package(150, 150, 150, 25))  # Should return "REJECTED"

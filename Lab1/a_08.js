const equivalent = (type, val) => {
    let result = "Dec"; // Default result

    try {
        if (type === "Bin") {
            result = val.toString(2); // Convert to binary
        } else if (type === "Hex") {
            result = val.toString(16).toUpperCase(); // Convert to hexadecimal
        } else if (type === "Oct") {
            result = val.toString(8); // Convert to octal
        } else if (type === "Dec") {
            result = val; // Decimal
        } else if (type === "Char") {
            result = String.fromCharCode(val); // Convert to character
        } else {
            console.log("Invalid type. Use 'Bin', 'Hex', 'Dec', 'Oct', or 'Char'.");
        }
    } catch (error) {
        console.log("An unexpected error occurred:", error);
    }

    return result;
};

// Example Usage
console.log(equivalent("Bin", 93)); // This will print "5D"

const equivalence = (type, val) => {
    let result = "";

    try {
        switch (type) {
            case "Bin":
                result = "0b" + val.toString(2); // Binary with '0b' prefix
                break;
            case "Hex":
                result = "0x" + val.toString(16).toUpperCase(); // Hex with '0x' prefix and uppercase
                break;
            case "Oct":
                result = "0o" + val.toString(8); // Octal with '0o' prefix
                break;
            case "Dec":
                result = val.toString(); // Decimal, no prefix needed
                break;
            case "Char":
                result = String.fromCharCode(val); // Character conversion
                break;
            default:
                console.log("Invalid type. Use 'Bin', 'Hex', 'Dec', 'Oct', or 'Char'.");
        }
    } catch (error) {
        console.log("An unexpected error occurred", error);
    }

    return result;
};

// Example usage:
const val1 = 93;  // equivalence to 0x5D in hex

console.log("Dec:\t", equivalence("Dec", val1));   // Decimal
console.log("Bin:\t", equivalence("Bin", val1));   // Binary with '0b' prefix
console.log("Hex:\t", equivalence("Hex", val1));   // Hex with '0x' prefix
console.log("Oct:\t", equivalence("Oct", val1));   // Octal with '0o' prefix
console.log("Char:\t", equivalence("Char", val1)); // Character


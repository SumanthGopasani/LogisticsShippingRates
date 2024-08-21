#!/bin/bash

# Function to calculate simple interest
calculate_simple_interest() {
    local principal=$1
    local rate=$2
    local time=$3

    # Simple interest formula: SI = (P * R * T) / 100
    local interest=$(echo "scale=2; ($principal * $rate * $time) / 100" | bc)
    echo "$interest"
}

# Main script
echo "Simple Interest Calculator"

# Read inputs from user
read -p "Enter the principal amount: " principal
read -p "Enter the rate of interest (in %): " rate
read -p "Enter the time period (in years): " time

# Validate inputs (ensure they are numbers and non-negative)
if [[ ! $principal =~ ^[0-9]+(\.[0-9]+)?$ ]] || [[ ! $rate =~ ^[0-9]+(\.[0-9]+)?$ ]] || [[ ! $time =~ ^[0-9]+(\.[0-9]+)?$ ]]; then
    echo "Error: Please enter valid numeric values."
    exit 1
fi

if (( $(echo "$principal < 0" | bc -l) )) || (( $(echo "$rate < 0" | bc -l) )) || (( $(echo "$time < 0" | bc -l) )); then
    echo "Error: Values should be non-negative."
    exit 1
fi

# Calculate interest
interest=$(calculate_simple_interest $principal $rate $time)

# Display the result
echo "The simple interest is: $interest"


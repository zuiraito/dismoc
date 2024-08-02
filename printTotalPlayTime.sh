#!/bin/bash

# Navigate to the world/stats directory
cd world/stats

# Initialize a variable to hold the total play time
total_play_time=0

# Loop through each JSON file in the directory
for file in *.json; do
  # Extract the play time from the JSON file
  play_time=$(jq '.["stats"]["minecraft:custom"]["minecraft:play_time"]' "$file")

  # Convert play time from ticks to hours (assuming 1 tick = 1/20 seconds)
  play_time_hours=$(echo "$play_time / 20 / 3600" | bc)

  # Add the play time in hours to the total play time
  total_play_time=$(echo "$total_play_time + $play_time_hours" | bc)
done

# Output the total play time in hours
echo "Total play time: ${total_play_time}h"

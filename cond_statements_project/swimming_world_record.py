world_record = float(input()) # seconds
distance = float(input())# meters
time = float(input()) # seconds for one meter
# water resistance slows him down
# 12.5 sec for every 15 meters
result = distance * time # seconds
actual_result = result + (distance // 15) * 12.5
if actual_result < world_record:
    print(f'Yes, he succeeded! The new world record is {actual_result:.2f} seconds.')
else:
    difference = actual_result - world_record
    print(f'No, he failed! He was {difference:.2f} seconds slower.')
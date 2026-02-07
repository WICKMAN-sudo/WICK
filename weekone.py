print("*"*10 , "Welcome to Eduvos Storage Management window","*"*10 )

laptop = float(input("Enter the total storage application of your laptop (in GB):"))
windows_percentage = float(input("Enter the percentage of storage allocated for windows (%):"))
ubuntu = float(input("Enter the percentage of storage allocated for Ubuntu (%):"))
windows_backup = float(input (" Enter the space reseved for Windows Backup (in GB):"))
ubuntu_backup = float(input ("Enter the space reserved for Ubuntu backup (in GB):"))



print("-"*5, "Storage allocation Summary", "-"*5)


windows_allocation = (windows_percentage/100) * laptop
ubuntu_allocation = (ubuntu/100) * laptop

print(f"'WINDOWS ALLOCATION:' {windows_allocation}")
print(f"'UBUNTU ALLOCATION:' {ubuntu_allocation}")

total_used = (windows_allocation + ubuntu_allocation + windows_backup + ubuntu_backup)
space_left = (laptop - total_used)

print(f" 'Total Storage used (including backups):' {total_used} GB ")

print (f" ' Free space remaining: {space_left} GB")






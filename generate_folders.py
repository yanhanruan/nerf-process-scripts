import os

def create_folders(date, number):
  """Creates a folder structure based on given date and number.

  Args:
    date: A string representing the date in the format 'mm-dd'.
    number: An integer representing the number of subfolders to create.
  """

  base_path = f"data/{date}"
  if os.path.exists(base_path):
    overwrite = input(f"Folder '{base_path}' already exists. Overwrite? (y/n): ")
    if overwrite.lower() != 'y':
      return

  os.makedirs(base_path, exist_ok=True)

  for i in range(1, number + 1):
    subfolder_path = os.path.join(base_path, str(i))
    os.makedirs(subfolder_path, exist_ok=True)

if __name__ == "__main__":
  date = input("Enter date (m-dd): ")
  number = int(input("Enter number of subfolders: "))
  
  create_folders(date, number)

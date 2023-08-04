import os
from datetime import datetime


def main():
    current_month_capitalized = datetime.now().strftime('%B')
    current_month = current_month_capitalized.lower()
    current_year = datetime.now().strftime('%Y')
    filename = f"updates-{current_month}-{current_year}.md"
    
    if not os.path.isfile(filename):
        f = open(filename, 'w')
        f.write("Title: Updates - ")
        f.write(f"{current_month_capitalized} {current_year}\n")
        f.write(f"Date: {current_month_capitalized} {current_year}\n")
        f.write("Category: \n")
        f.write("Authors: \n")
        f.write("Templates: resources/update-post\n")
        f.write(f"url: /resources/updates/{filename[:-3]}\n")
        f.write(f"save_as: resources/updates/{filename[:-3]}/index.html\n")

if __name__ == "__main__":
    main()
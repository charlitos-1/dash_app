import time
from database import get_table_as_list

DATABASE_REFRESH_INTERVAL = 5

def new_row(row):
    print("new row")
    print(row)


def running_row(row):
    print("running row")
    print(row)
    

def unknown_row(row):
    print("unknown row")
    print(row)


def main():
    row_functions = {
        "new": new_row,
        "running": running_row,
    }

    while True:
        database_cache = get_table_as_list()
        for row in database_cache:
            status = row.get("Status", "unknown")
            try:
                status = status.lower()
            except:
                status = "unknown"
                
            row_function = row_functions.get(status, unknown_row)
            row_function(row)
        time.sleep(DATABASE_REFRESH_INTERVAL)
        

if __name__ == "__main__":
    main()
import sqlite3
 

con = sqlite3.connect('ytman.db')
cur = con.cursor()

cur.execute(''' CREATE TABLE IF NOT EXISTS videos(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
            )
            ''')

def list_videos():
    cur.execute("SELECT * FROM videos")
    for row in cur.fetchall():
        print(row)

def add_videos(name,time):
    cur.execute("INSERT INTO videos (name,time) VALUES (?,?)", (name,time))
    con.commit()
    
def update_videos(vid_id,new_name, new_time):
    cur.execute("UPDATE videos SET name=?, time=? WHERE id=?", (new_name,new_time,vid_id))
    con.commit()
    
def delete_videos(vid_id):
    cur.execute('DELETE FROM videos where id=?', (vid_id,))
    con.commit()
    
def main():
    while True:
        print("\n YT MAN with DB")
        print('1. List videos')
        print('2. Add videos')
        print('3. Update videos')
        print('4. Delete videos')
        print("5. Exit App")
        choice = input(("enter your choice: "))

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("enter name:")
            time = input("enter time:")
            add_videos(name,time)
        elif choice == '3':
            vid_id = input("enter vid id:")
            name = input("enter name:")
            time = input("enter time:")
            update_videos(vid_id,name,time)
        elif choice == '4':
            vid_id = input("enter vid id:")
            delete_videos(vid_id)
        elif choice == '5':
            break
        else:
            print("invalid choice")

    con.close()





if __name__ == "__main__":
    main()
import sqlite3
conn =sqlite3.connect("Youtube Database.db")
cur = conn.cursor()

cur.execute('''
        CREATE TABLE IF NOT EXISTS  datayoutube(
            video_id INTEGER PRIMARY KEY AUTOINCREMENT,
            video_name TEXT NOT NULL,
            video_time TEXT NOT NULL 
        )            
''')

def list_all_the_videos():
    cur.execute("SELECT  * FROM datayoutube")
    rows = cur.fetchall()
    if rows:
        print("*" * 25 , "List of all videos start here", "*"*25)
        for row in rows:
            print(row)
            
    else:
        print("⚠️ No videos found in the database.")
    print("*" * 25 , "List of all videos ends here", "*"*25)  

def add_video(video_name, video_time):
    cur.execute("INSERT INTO datayoutube (video_name,video_time) VALUES (?,?)", (video_name,video_time))
    conn.commit()
    print(" video added suceessfully")

def update_video(video_id,new_name, new_time ):
    cur.execute("UPDATE datayoutube SET video_name = ? , video_time = ? WHERE video_id = ?",(new_name, new_time, int(video_id)))
    conn.commit()
    print(" video updated suceessfully")

def delete_video(video_id):
    cur.execute("DELETE FROM datayoutube where video_id = ?",(int(video_id), ))
    conn.commit()
    print(" video deleted suceessfully")

def search_video(video_name):
    cur.execute("SELECT * FROM datayoutube WHERE video_name LIKE ?", ("%"+ video_name + "%", ))
    results = cur.fetchall()
    if results:
        print("*" * 25, f"Search results for {video_name}", "*" * 25)
        for row in results:
            print(row)
            print("Video founded Sucessfully")
    else:
        print("no such video found in database")

def count_total_videos():
    cur.execute("SELECT COUNT(*) FROM  datayoutube")
    total_videos = cur.fetchone()[0]
    print(f"the total video in database is: {total_videos}")
    


def main():
    while True:
        print("\n" + "*" * 70)
        print(' Welcome to Youtube manager with db')
        print(' 1. list all the videos')
        print(' 2. add a new  video')
        print(' 3. Update from the  added videos')
        print(' 4. Delete a  video')
        print(' 5. Search video by name')
        print(' 6. Count total videos')
        print(' 7. Exit the App')
        print("*" * 70)
        
        choice = input('\n enter from the above option: ')
        
        
        if choice == '1':
            list_all_the_videos()
        elif  choice == '2':
            video_name = input("eneter the video name : ")
            video_time = input("eneter the video time : ")
            add_video(video_name , video_time)
        elif  choice == '3':
            video_id = input("enter the video ID to update: ")
            new_name = input("enter the update video name: ")
            new_time = input("enter the update video time: ")
            update_video(int(video_id), new_name, new_time)
        elif  choice == '4':
            video_id = input("enter the video id to delete the video: ")
            delete_video(video_id )
        elif choice == '5':
            video_name=input("Enter the video nname to Search:  ")
            search_video(video_name)
            
        elif choice == '6':
            count_total_videos()
        elif choice =='7':
            print("👋 Exiting the app. Goodbye!")
            break
        else:
            print("select option from the Given choice")
    conn.close()        
            

if __name__  == '__main__':
    main()
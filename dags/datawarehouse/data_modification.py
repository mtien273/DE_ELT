import logging

logger = logging.getLogger(__name__)
table = "yt_api"

def insert_rows(cur,conn,schema,row):
    try:
        if schema == 'staging':
            video_id = 'video_id'
            cur.execute(
                f"""INSERT INTO {schema}.{table}("Video_ID","Videp_Title","Upload_Date","Duration","Video_Views","Likes_Count", "Comments_Count")
                VALUES (%(video_id)s,%(title)s,%(publishedAt)s,%(duration)s,%(viewCounts)s,%(likeCount)s,%(commentCount)s);
                """, row
            )
        else:
            video_id = 'Video_ID'
            cur.execute(
                f"""INSERT INTO {schema}.{table}("Video_ID","Videp_Title","Upload_Date","Duration","Video_Type","Video_Views","Likes_Count", "Comments_Count")
                VALUES (%(Video_ID)s,%(Video_Title)s,%(Upload_Date)s,%(Duration)s,%(Video_Type)s,%(Video_Views)s,%(Likes_Count)s,%(Comments_Count)s)
                """, row
                        )
        conn.commit()
        logger.info(f"Inserted row with Video_ID:{row[video_id]}")
    except Exception as e:
        logger.error(f"Error Inserting row with Video_ID:{row[video_id]}")
        raise e
    
def update_rows(cur,conn,schema,row):
    try:
        #staging
        if schema == 'staging':
            video_id = 'video_id'
            upload_date = 'PublishedAt'
            video_title = 'title'
            video_views = 'viewCount'
            likes_count = 'likeCount'
            comments_count = 'commentCount'
        #core
        else: 
            video_id = 'Video_ID'
            upload_date = 'Upload_Data'
            video_title = 'Video_Title'
            video_views = 'Video_View'
            likes_count = 'Likes_Count'
            comments_count = 'Comments_Count'

        cur.execute(

            f"""UPDATE {schema}.{table}
            SET "Video_Title" = %({video_title})s,
                "Video_Views" = %({video_views})s,
                "Likes_Count" = %({likes_count})s,
                "Comments_Count" = %({comments_count})s
            WHERE "Video_ID" = %%({video_id})s 
            AND    "Upload_Date" = %({upload_date})s;
            """, row
        )
        conn.commit()
        logger.info(f"Updated row with Video_ID:{row[video_id]}")           
    except Exception as e:
            logger.error(f"Error Updating row with Video_ID:{row[video_id]}")
            raise e
            
def delete_rows(cur,conn,schema,ids_to_delete):
    try:
        # Chuyển danh sách ID ['id1', 'id2'] thành chuỗi SQL dạng ('id1', 'id2')
        ids_to_delete = f"""({', '.join(f"'{id}'" for  id in ids_to_delete)})"""
        cur.execute(

            f"""DELETE {schema}.{table}
            WHERE "Video_ID" = IN {ids_to_delete};
            """
        )
        conn.commit()
        logger.info(f"Deleted row with Video_ID:{ids_to_delete}")           
    except Exception as e:
            logger.error(f"Error deleting row with ideo_ID:{ids_to_delete}")
            raise e
            




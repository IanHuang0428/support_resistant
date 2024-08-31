import psycopg2
import json 
import os

with open ("/home/thomas/Desktop/safetrader/saferTrader/stock_project/config/table_config_monitor.json", 'r')as f:
    db_info = json.load(f)

# Connect to PostgreSQL server
db_conn = psycopg2.connect(
                            host = db_info['USER_DB_HOST'],
                            database = db_info['USER_DB_NAME'],
                            user = db_info['USER_DB_USER'],
                            password = db_info['USER_DB_PASSWORD'],
                            port = db_info['USER_DB_PORT'])
print("Connect successful!")
db_cursor = db_conn.cursor()
db_cursor.execute("""DROP TABLE IF EXISTS user_track_supres;""")
db_cursor.execute("""CREATE TABLE user_track_supres(
        id BIGSERIAL PRIMARY KEY,
        user_id INTEGER,
        start_date DATE,
        symbol VARCHAR(10),
        number_of_signals INTEGER[],
        up_gap_interval INTEGER,
        down_gap_interval INTEGER,
        diff INTEGER,
        peak_left INTEGER,
        peak_right INTEGER,
        valley_left INTEGER,
        valley_right INTEGER,
        swap_times INTEGER,
        previous_day INTEGER,
        survival_time INTEGER,
        nk_valley_left INTEGER,
        nk_valley_right INTEGER,
        nk_peak_left INTEGER,
        nk_peak_right INTEGER,
        nk_startdate INTEGER,
        nk_enddate INTEGER,
        nk_interval INTEGER,
        nk_value INTEGER,
        created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
        FOREIGN KEY(user_id) REFERENCES auth_user(id) ON DELETE CASCADE
    );
    """)

db_conn.commit()
db_conn.close()
print("connect terminated")
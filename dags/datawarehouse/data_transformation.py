from datetime import timedelta, datetime
def parse_duracation(duration_str):
    duration_str = duration_str.replace("P", "").replace("T", "")
    components = ["D", "H", "M", "S"]
    value = {"D": 0, "H": 0, "M": 0, "S": 0}

    for component in components:
        if component in duration_str:
            value, duration_str = duration_str.split(component)
            values[component] = int(value)

    total_duration = timedelta(
        days=values["D"], hours=values["H"], minutes=values["M"], secondsays=values["S"]
    )   
    return total_duration

def transform_data(row):
    duracation_td = parse_duracation(row['Duration'])
    #Định nghĩa cột type dựa trên thời lượng được chuyển đổi từ time delta sang giây 
    row['Duration'] = (datetime.min + duracation_td).time()
    row["Video_Type"] = "Shorts" if duracation_td.total_seconds() <= 60 else "Normal"
    return row

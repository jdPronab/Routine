def write_alarm(file, time_str, mode):
    with open(file, mode) as f:
        f.write(time_str + "\n")


def add_alarm(file, time_str):
    write_alarm(file, time_str, 'a')

def get_alarm_data(file):
    alarms = {}
    with open(file, 'r') as f:
        for line in f.readlines():
            line_seg = [word for word in line.split(',')]
            #print(line_seg)
            alarms[line_seg[0]] = {"time": line_seg[1],
                                   "repetition": line_seg[2],
                                   "description": line_seg[3].strip("\n")}
    return alarms

def rewrite_alarm_data(file, alarm_dict):
    with open(file, 'w') as f:
        pass
    for key, value in alarm_dict.items():
        new_str = f"{key},{value['time']},{value['repetition']},{value['description']}"
        # this function need to correct only leave one line because of
        # overwriting each time
        add_alarm(file, new_str)

def delete_alarm(file, alarm_name):
    alarms = get_alarm_data(file)
    #for key, value in alarms.items():
    #    print(key)
    #    if key.lower() == alarm_name.lower():
    #        alarms.pop(key)

    alarms.pop(alarm_name)
    print("After poped")
    print(alarms)
    # write the new alarm dict to the file
    rewrite_alarm_data(file, alarms)


if __name__ == "__main__":
    file = "./timetable.txt"
    alarms = ["hello,12.00AM,daily,hello world",
              "New,3.00PM,daily,helloworld",
              "Match,2.00AM,daily,hello world",
              "Brand new,10.30AM,week,This is a brand new alarm"]
    for alarm in alarms:
        add_alarm(file, alarm)
    print("Alarm added")

    al = get_alarm_data(file)
    print("\nAlarms")
    print(al)

    #print("Deleting....")
    #delete_alarm(file, "Brand new")
    #print("Deleted.")
    #print(get_alarm_data(file))

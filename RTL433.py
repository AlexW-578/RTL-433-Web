import PySimpleGUIWeb as sg
import time as sleep

def Read(window):
    end = 0
    while True:
        time = ""
        model = ""
        station_id = ""
        temperature = ""
        humidity = ""
        wind_degrees = ""
        wind_avg_speed = ""
        wind_gust = ""
        total_rainfall = ""
        with open('rtl433.txt', 'r+') as file:
            for line in file:
                with open("log.txt","a") as log:
                    log.writelines(line)
                for word in line.split():
                    split_line = line.split(":")
                    if word == "_":
                        end = end + 1
                    if end == 40:
                        print("Wipe")
                        file.truncate(0)
                        end=0
                        sleep.sleep(1)
                    if word == "time":
                        time = split_line[1] + ":" + split_line[2] + ":" + split_line[3]
                        # print(line)
                    elif word == "model":
                        model = split_line[1]
                        # print(line)
                    elif word == "Station":
                        station_id = split_line[1]
                        # print(line)
                    elif word == "Temperature:":
                        temperature = split_line[1]
                        # print(line)
                    elif word == "Humidity":
                        humidity = split_line[1]
                        # print(line)
                    elif word == "degrees":
                        wind_degrees = split_line[1]
                        # print(line)
                    elif word == "avg":
                        wind_avg_speed = split_line[1]
                        # print(line)
                    elif word == "gust":
                        wind_gust = split_line[1]
                        # print(line)
                    elif word == "rainfall:":
                        total_rainfall = split_line[1]
                        # print(line)
                    elif word == "House":
                        station_id = split_line[1]
                    else:
                        with open('Other.txt', 'a') as other:
                            other.write(line)
                window.Finalize()
                window["Time"].Update(time)
                window["Model"].Update(model)
                window["Station"].Update(station_id)
                window["Temp"].Update(temperature)
                window["Humid"].Update(humidity)
                window["w_deg"].Update(wind_degrees)
                window["w_avg"].Update(wind_avg_speed)
                window["w_gust"].Update(wind_gust)
                window["Rain"].Update(total_rainfall)
                print(time, "\n", model, "\n", station_id, "\n", temperature, "\n", humidity, "\n", wind_degrees, "\n",
                      wind_avg_speed, "\n", wind_gust, "\n", total_rainfall)



def Wipe():
    file = open("rtl433.txt", "r+")
    file.truncate(0)
    file.close()


def main():
    # run = 1
    # while run == 1:
    layout = [[sg.Text('', key="Time")],
              [sg.Text("Model: "), sg.Text('', key="Model")],
              [sg.Text("Station ID: "), sg.Text('            ', key="Station")],
              [sg.Text("Temperature: "), sg.Text('            ', key="Temp")],
              [sg.Text("Humidity: "), sg.Text('            ', key="Humid")],
              [sg.Text("Wind Degrees: "), sg.Text('            ', key="w_deg")],
              [sg.Text("Average Wind Speed: "), sg.Text('            ', key="w_avg")],
              [sg.Text("Wind Gust Speed: "), sg.Text('            ', key="w_gust")],
              [sg.Text("Total Rainfall: "), sg.Text('            ', key="Rain")]]
    window = sg.Window("RTL-433", layout, web_ip="192.168.1.125", web_port=8888, web_start_browser=False)
    Read(window)


main()

import network
import urequests
import ujson

def do_connect(SSID, PASSWORD):
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect(SSID, PASSWORD)
        print("Conectando a la red", SSID + "...")
        while not sta_if.isconnected():
            pass
    print("Conectado! IP:", sta_if.ifconfig()[0])


def obtener_clima(ciudad):
    url_geo = "https://geocoding-api.open-meteo.com/v1/search?name=" + ciudad
    res = urequests.get(url_geo)
    data_geo = ujson.loads(res.text)
    res.close()

    if "results" not in data_geo:
        return "Ciudad no encontrada"

    lat = data_geo["results"][0]["latitude"]
    lon = data_geo["results"][0]["longitude"]

    url_weather = "https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&current=temperature_2m,wind_speed_10m".format(lat, lon)
    res = urequests.get(url_weather)
    data_weather = ujson.loads(res.text)
    res.close()

    temp = data_weather["current"]["temperature_2m"]
    viento = data_weather["current"]["wind_speed_10m"]

    return {
        "ciudad": ciudad,
        "lat": lat,
        "lon": lon,
        "temperatura": temp,
        "viento": viento
    }


do_connect("robotica", "12345678")

info = obtener_clima("Bogota")
print("Ciudad:", info["ciudad"])
print("Temperatura actual:", info["temperatura"], "°C")
print("Viento:", info["viento"], "m/s")

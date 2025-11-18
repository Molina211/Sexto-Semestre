from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from datetime import datetime

from fastapi.middleware.cors import CORSMiddleware
import uvicorn

import models
from database import engine, SessionLocal

app = FastAPI()

# CORS: permitir frontend local/LAN (ajusta según necesites)
origins = [
    "http://localhost:4200",
    "http://127.0.0.1:4200",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://192.168.1.15:4200",
    "http://192.168.1.15:5173",
    "http://192.168.1.15"
    # agrega más orígenes si necesitas
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crear tablas
models.Base.metadata.create_all(engine)

# Dependencia BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Modelo de entrada JSON
class SensorPayload(BaseModel):
    claveDinamica: str | None = None
    temperatura: float | None = None
    alarmaBuzzer: bool | None = None

# Endpoint único: guardar datos provenientes del ESP32
@app.post("/esp32/sensores", status_code=status.HTTP_201_CREATED)
async def recibir_sensores(payload: SensorPayload, db: Session = Depends(get_db)):
    try:
        nuevo = models.Informacion(
            claveDinamica=payload.claveDinamica,
            temperatura=payload.temperatura,
            alarmaBuzzer=payload.alarmaBuzzer,
            fecha_hora=datetime.now()
        )
        db.add(nuevo)
        db.commit()
        db.refresh(nuevo)
        return {"msg": "Datos guardados", "id": nuevo.IDInfo}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al guardar datos: {e}")

# ----- Nuevos endpoints GET -----
def _serialize_informacion(obj):
    return {
        "id": getattr(obj, "IDInfo", None),
        "claveDinamica": getattr(obj, "claveDinamica", None),
        "temperatura": getattr(obj, "temperatura", None),
        "alarmaBuzzer": getattr(obj, "alarmaBuzzer", None),
        "fecha_hora": getattr(obj, "fecha_hora", None),
    }

@app.get("/esp32/registros", status_code=status.HTTP_200_OK)
def obtener_todos(db: Session = Depends(get_db)):
    registros = db.query(models.Informacion).all()
    return [ _serialize_informacion(r) for r in registros ]

@app.get("/esp32/registro/{registro_id}", status_code=status.HTTP_200_OK)
def obtener_por_id(registro_id: int, db: Session = Depends(get_db)):
    registro = db.query(models.Informacion).filter(models.Informacion.IDInfo == registro_id).first()
    if not registro:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return _serialize_informacion(registro)

# Estado en memoria del buzzer (True = encendido, False = apagado)
buzzer_state = False

@app.post("/esp32/buzzer/on", status_code=status.HTTP_200_OK)
def activar_buzzer(db: Session = Depends(get_db)):
    global buzzer_state
    buzzer_state = True
    return {"msg": "Buzzer activado", "buzzer": buzzer_state}

@app.post("/esp32/buzzer/off", status_code=status.HTTP_200_OK)
def desactivar_buzzer(db: Session = Depends(get_db)):
    global buzzer_state
    buzzer_state = False
    return {"msg": "Buzzer desactivado", "buzzer": buzzer_state}

@app.get("/esp32/buzzer", status_code=status.HTTP_200_OK)
def estado_buzzer(db: Session = Depends(get_db)):
    return {"buzzer": buzzer_state}

# endpoint de salud
@app.get("/", status_code=200)
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    # Ejecutar en 0.0.0.0 para que sea accesible desde la LAN
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)

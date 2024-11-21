from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import json
from typing import Dict, List

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 방별로 접속한 클라이언트들을 저장
rooms: Dict[str, Dict[str, dict]] = {}


@app.websocket("/ws/{room_id}/{client_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: str, client_id: str):
    await websocket.accept()

    if room_id not in rooms:
        rooms[room_id] = {}

    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)

            if message.get("type") == "init":
                # 새 플레이어 정보 저장
                rooms[room_id][client_id] = {
                    "websocket": websocket,
                    "data": {
                        "client_id": client_id,
                        "x": message["x"],
                        "y": message["y"],
                        "direction": message["direction"],
                        "characterType": message["characterType"],
                        "name": message["name"],
                    },
                }

                # 새 플레이어에게 현재 방의 모든 플레이어 정보 전송
                current_players = [
                    player["data"]
                    for player in rooms[room_id].values()
                    if player["data"]["client_id"] != client_id
                ]
                await websocket.send_text(
                    json.dumps({"type": "init", "players": current_players})
                )

                # 다른 플레이어들에게 새 플레이어 정보 전송
                for cid, player in rooms[room_id].items():
                    if cid != client_id:
                        await player["websocket"].send_text(
                            json.dumps(
                                {
                                    "client_id": client_id,
                                    "x": message["x"],
                                    "y": message["y"],
                                    "direction": message["direction"],
                                    "characterType": message["characterType"],
                                    "name": message["name"],
                                }
                            )
                        )
            else:
                # 위치 업데이트 처리 시에도 모든 필요한 정보 포함
                for cid, player in rooms[room_id].items():
                    if cid != client_id:
                        await player["websocket"].send_text(
                            json.dumps(
                                {
                                    "client_id": client_id,
                                    "x": message["x"],
                                    "y": message["y"],
                                    "direction": message["direction"],
                                    "characterType": message["characterType"],
                                    "name": message["name"],
                                }
                            )
                        )

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if room_id in rooms and client_id in rooms[room_id]:
            del rooms[room_id][client_id]
            if not rooms[room_id]:
                del rooms[room_id]

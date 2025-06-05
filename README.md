# Streamlit WebSocket Chat

🟢 실시간 채팅을 위한 Streamlit 클라이언트입니다.  
백엔드 서버는 FastAPI + WebSocket 기반이며 별도로 배포됩니다.

## ▶️ 사용법
1. 이 레포를 [Streamlit Cloud](https://streamlit.io/cloud)에 연결하거나 로컬에서 다음 명령으로 실행:

```bash
streamlit run streamlit_app.py
```

2. `streamlit_app.py` 안의 `WEBSOCKET_URL`을 여러분의 FastAPI 웹소켓 서버 주소로 바꿔주세요.

## 📡 예시 WebSocket 주소
```
wss://your-railway-name.up.railway.app/ws
```

import streamlit as st
import streamlit.components.v1 as components

st.title("실시간 웹소켓 채팅앱 (Streamlit 클라이언트)")

# Railway에서 배포한 주소로 바꾸세요 (wss://...)
WEBSOCKET_URL = "web-production-cf377.up.railway.app"

html_code = f"""
<!DOCTYPE html>
<html>
<head>
<style>
  #chatbox {{
    width: 100%;
    height: 300px;
    border: 1px solid #ccc;
    overflow-y: scroll;
    padding: 5px;
    font-family: Arial, sans-serif;
  }}
  #msgInput {{
    width: 80%;
    padding: 5px;
    font-size: 16px;
  }}
  #sendBtn {{
    width: 18%;
    padding: 5px;
    font-size: 16px;
  }}
</style>
</head>
<body>
<div id="chatbox"></div>
<input type="text" id="msgInput" placeholder="메시지를 입력하세요" autocomplete="off" />
<button id="sendBtn">전송</button>

<script>
  const chatbox = document.getElementById("chatbox");
  const msgInput = document.getElementById("msgInput");
  const sendBtn = document.getElementById("sendBtn");

  const ws = new WebSocket("{WEBSOCKET_URL}");

  ws.onopen = () => {{
    console.log("웹소켓 연결 성공");
  }};

  ws.onmessage = (event) => {{
    const msg = event.data;
    const div = document.createElement("div");
    div.textContent = msg;
    chatbox.appendChild(div);
    chatbox.scrollTop = chatbox.scrollHeight;
  }};

  ws.onclose = () => {{
    console.log("웹소켓 연결 종료");
    const div = document.createElement("div");
    div.textContent = "[서버 연결 끊김]";
    div.style.color = "red";
    chatbox.appendChild(div);
  }};

  function sendMessage() {{
    const msg = msgInput.value.trim();
    if (msg) {{
      ws.send(msg);
      msgInput.value = "";
    }}
  }}

  sendBtn.addEventListener("click", sendMessage);

  msgInput.addEventListener("keypress", (e) => {{
    if (e.key === "Enter") {{
      sendMessage();
    }}
  }});
</script>
</body>
</html>
"""

components.html(html_code, height=400)

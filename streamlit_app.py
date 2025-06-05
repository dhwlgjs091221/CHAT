import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="실시간 채팅", layout="centered")
st.title("💬 실시간 웹소켓 채팅")

# 아래 주소를 당신의 Railway 도메인 주소로 교체하세요
WEBSOCKET_URL = "wss://your-railway-name.up.railway.app/ws"

html_code = f"""
<!DOCTYPE html>
<html>
<head>
<style>
  #chatbox {{
    width: 100%;
    height: 300px;
    border: 1px solid #ccc;
    overflow-y: auto;
    padding: 5px;
    font-family: sans-serif;
  }}
  #msgInput {{
    width: 75%;
    padding: 8px;
    font-size: 14px;
  }}
  #sendBtn {{
    width: 20%;
    padding: 8px;
    font-size: 14px;
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
    console.log("웹소켓 연결됨");
  }};

  ws.onmessage = (event) => {{
    const msg = event.data;
    const div = document.createElement("div");
    div.textContent = msg;
    chatbox.appendChild(div);
    chatbox.scrollTop = chatbox.scrollHeight;
  }};

  ws.onclose = () => {{
    const div = document.createElement("div");
    div.textContent = "[서버와 연결이 끊어졌습니다]";
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

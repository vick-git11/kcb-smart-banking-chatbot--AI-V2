import React, { useState } from "react";
import { sendMessage } from "../api";

export default function ChatBot() {
  const [messages, setMessages] = useState([
    {
      sender: "bot",
      text: "Welcome to KCB Smart Assistant. How can I help you today?",
      time: new Date().toISOString()
    }
  ]);

  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const send = async () => {
    if (!input.trim()) return;

    const userTime = new Date().toISOString();

    setMessages(prev => [
      ...prev,
      { sender: "user", text: input, time: userTime }
    ]);

    setInput("");
    setLoading(true);

    const res = await sendMessage(input);

    let botText = res.reply;

    // Render live branch results
    if (res.live_data && Array.isArray(res.live_data)) {
      botText += "\n\nNearby branches:\n";
      res.live_data.forEach((b, i) => {
        botText += `${i + 1}. ${b.name}\n   (${b.latitude}, ${b.longitude})\n`;
      });
    }

    setMessages(prev => [
      ...prev,
      { sender: "bot", text: botText, time: res.time }
    ]);

    setLoading(false);
  };

  return (
    <div className="chat-container">
      <div className="chat-header">KCB Smart Assistant</div>

      <div className="chat-body">
        {messages.map((m, i) => (
          <div key={i} style={{ marginBottom: "14px" }}>
            <div className={`msg ${m.sender}`}>
              {m.text.split("\n").map((line, idx) => (
                <div key={idx}>{line}</div>
              ))}
            </div>
            <div
              style={{
                fontSize: "0.75rem",
                marginTop: "4px",
                textAlign: m.sender === "user" ? "right" : "left",
                color: "#64748b"
              }}
            >
              {new Date(m.time).toLocaleTimeString([], {
                hour: "2-digit",
                minute: "2-digit"
              })}
            </div>
          </div>
        ))}
        {loading && <div className="msg bot">Typing…</div>}
      </div>

      <div className="chat-footer">
        <input
          placeholder="Type your question..."
          value={input}
          onChange={e => setInput(e.target.value)}
          onKeyDown={e => e.key === "Enter" && send()}
        />
        <button onClick={send}>Send</button>
      </div>
    </div>
  );
}

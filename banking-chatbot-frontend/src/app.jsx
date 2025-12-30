import React, { useState } from "react";
import ChatBot from "./components/ChatBot";

export default function App() {
  const [open, setOpen] = useState(false);

  return (
    <>
      {/* Floating Toggle Button */}
      <div className="chat-widget">
        <button
          className="chat-toggle"
          onClick={() => setOpen(!open)}
        >
          💬
        </button>
      </div>

      {/* Floating Chat Panel */}
      <div className={`chat-panel ${open ? "open" : ""}`}>
        <ChatBot />
      </div>
    </>
  );
}

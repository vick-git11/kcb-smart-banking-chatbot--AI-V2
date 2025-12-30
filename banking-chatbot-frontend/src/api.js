import axios from "axios";

export const sendMessage = async (message) => {
  const res = await axios.post("http://127.0.0.1:8000/api/chat/", {
    message,
    authenticated: false
  });

  return {
    reply: res.data.reply,
    time: res.data.created_at,
    live_data: res.data.live_data || null
  };
};

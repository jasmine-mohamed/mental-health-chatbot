const API_BASE = localStorage.getItem("serverUrl") || "http://127.0.0.1:8000";

// Session management
function getOrCreateSessionId() {
    let sessionId = localStorage.getItem("mhc_session_id");
    if (!sessionId) {
        sessionId = "session_" + Date.now() + "_" + Math.random().toString(36).substr(2, 9);
        localStorage.setItem("mhc_session_id", sessionId);
    }
    return sessionId;
}

let SESSION_ID = getOrCreateSessionId();

// DOM elements
const chatWindow = document.getElementById("chatWindow");
const chatForm = document.getElementById("chatForm");
const messageInput = document.getElementById("messageInput");
const sendBtn = document.getElementById("sendBtn");
const docToggle = document.getElementById("docToggle");
const resetBtn = document.getElementById("resetBtn");
const serverUrl = document.getElementById("serverUrl");

// Update server URL display
serverUrl.textContent = API_BASE;

function appendMessage(type, text) {
    const wrapper = document.createElement("div");
    wrapper.className = `message message--${type}`;
    
    const avatar = document.createElement("div");
    avatar.className = "message__avatar";
    avatar.textContent = type === "user" ? "U" : "B";
    
    const bubble = document.createElement("div");
    bubble.className = "message__bubble";
    bubble.textContent = text;
    
    wrapper.appendChild(avatar);
    wrapper.appendChild(bubble);
    
    chatWindow.appendChild(wrapper);
    chatWindow.scrollTop = chatWindow.scrollHeight;
}

function setLoading(loading) {
    sendBtn.disabled = loading;
    messageInput.disabled = loading;
}

async function sendMessage(query) {
    const useDocs = !!docToggle?.checked;
    const endpoint = useDocs ? "/doc-chat" : "/chat";
    const url = `${API_BASE}${endpoint}`;

    const payload = useDocs
        ? { session_id: SESSION_ID, query }
        : { session_id: SESSION_ID, query };

    const res = await fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
    });

    if (!res.ok) {
        const text = await res.text();
        throw new Error(`Request failed (${res.status}): ${text}`);
    }
    
    const data = await res.json();
    // Backend returns { response: string }
    return data.response ?? "(No response)";
}

// Initial greeting
appendMessage("bot", "Hi! I'm here to listen. You can chat with me or toggle 'Use documents' to ask questions about the knowledge base.");

chatForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const text = messageInput.value.trim();
    if (!text) return;

    appendMessage("user", text);
    messageInput.value = "";
    setLoading(true);

    try {
        const reply = await sendMessage(text);
        appendMessage("bot", reply);
    } catch (err) {
        console.error(err);
        appendMessage("bot", `⚠️ Error: ${err.message}\nMake sure your FastAPI server is running at ${API_BASE}.`);
    } finally {
        setLoading(false);
        messageInput.focus();
    }
});

messageInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        sendBtn.click();
    }
});

resetBtn?.addEventListener("click", () => {
    localStorage.removeItem("mhc_session_id");
    SESSION_ID = getOrCreateSessionId();
    chatWindow.innerHTML = "";
    appendMessage("bot", "Session reset. How are you feeling now?");
});

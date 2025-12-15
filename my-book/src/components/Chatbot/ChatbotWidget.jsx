import React, { useState, useEffect, useRef } from "react";
import "./ChatbotWidget.css";

// Define the backend API base URL
const API_BASE_URL = "https://palwasha-49-hackathon-1.hf.space";

// Simple markdown parser function
const parseMarkdown = (text) => {
  if (!text) return text;

  // Convert headers
  let result = text.replace(/^### (.*$)/gim, "<h3>$1</h3>");
  result = result.replace(/^## (.*$)/gim, "<h2>$1</h2>");
  result = result.replace(/^# (.*$)/gim, "<h1>$1</h1>");

  // Convert bold
  result = result.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");
  result = result.replace(/__(.*?)__/g, "<strong>$1</strong>");

  // Convert italic
  result = result.replace(/\*(.*?)\*/g, "<em>$1</em>");
  result = result.replace(/_(.*?)_/g, "<em>$1</em>");

  // Convert code blocks
  result = result.replace(/```([\s\S]*?)```/g, "<pre><code>$1</code></pre>");
  result = result.replace(/`(.*?)`/g, "<code>$1</code>");

  // Convert links
  result = result.replace(
    /\[([^\]]+)\]\(([^)]+)\)/g,
    '<a href="$2" target="_blank" rel="noopener noreferrer">$1</a>'
  );

  // Convert lists
  result = result.replace(/^\s*\*\s(.*)$/gm, "<li>$1</li>");
  result = result.replace(/^\s*\d+\.\s(.*)$/gm, "<li>$1</li>");

  // Wrap lists
  result = result.replace(/(<li>.*<\/li>)/gs, "<ul>$1</ul>");

  // Convert line breaks
  result = result.replace(/\n/g, "<br>");

  return result;
};

const ChatbotWidget = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [sessionId, setSessionId] = useState(null);
  const [selectedText, setSelectedText] = useState("");
  const [shouldAutoSend, setShouldAutoSend] = useState(false);

  const messagesEndRef = useRef(null);

  // Function to get selected text from the page with smart workflow
  useEffect(() => {
    const handleTextSelection = () => {
      const selectedText = window.getSelection().toString().trim();
      if (selectedText && selectedText.length > 5) {
        setIsOpen(true);
        setSelectedText(selectedText);
        setShouldAutoSend(true);
      }
    };

    document.addEventListener("mouseup", handleTextSelection);
    return () => {
      document.removeEventListener("mouseup", handleTextSelection);
    };
  }, []);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const sendMessage = async (textOverride = null, isAutoSend = false) => {
    // If auto-sending, we use the override. Otherwise use input value.
    const textToSend = textOverride || inputValue;

    console.log(
      "[Chatbot] sendMessage called. textToSend:",
      textToSend,
      "isAutoSend:",
      isAutoSend
    );

    // Validation:
    // 1. If auto-sending, we just need textOverride (which will be the question)
    // 2. If manual, we need either inputValue OR selectedText context
    if (!isAutoSend && !textToSend.trim() && !selectedText) {
      console.log("[Chatbot] Validation failed: No text to send.");
      return;
    }
    if (isLoading) {
      console.log("[Chatbot] Blocked: Already loading.");
      return;
    }

    // Use the override or construct default question
    let question = textToSend.trim();
    if (!question && selectedText) {
      question = "Explain this selected text";
    }

    // Add detailed explanation instructions if not already present
    // (For auto-send, we'll pass the full formatted string, so skip this)
    let detailedQuestion = question;
    if (!isAutoSend) {
      detailedQuestion = `${question} Please provide a detailed explanation.`;
    }

    console.log("[Chatbot] Prepared Question:", detailedQuestion);
    console.log("[Chatbot] Selected Text Context:", selectedText);

    const userMessage = { role: "user", content: question };
    const newMessages = [...messages, userMessage];
    setMessages(newMessages);
    setInputValue("");
    setIsLoading(true);

    try {
      let response;
      // Determine if we should use selection context
      // For auto-send, the selection is embedded in the question prompt usuallly,
      // OR we can pass the selection explicitly.
      // Let's assume for auto-send "Explain... [Quote]", we rely on RAG + Selection

      const selectionContext = isAutoSend ? selectedText : selectedText;

      console.log("[Chatbot] Sending request to backend...");

      if (selectionContext) {
        console.log("[Chatbot] Ending point: /api/ask-selection");
        response = await fetch(`${API_BASE_URL}/api/ask-selection`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            question: detailedQuestion,
            selection: selectionContext,
          }),
        });
      } else {
        console.log("[Chatbot] Endpoint: /api/ask");
        response = await fetch(`${API_BASE_URL}/api/ask`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            question: detailedQuestion,
          }),
        });
      }

      console.log("[Chatbot] Response status:", response.status);
      const data = await response.json();
      console.log("[Chatbot] Response data:", data);

      if (response.ok) {
        const botMessage = {
          role: "assistant",
          content: data.answer || data.response || data.message,
          sources: data.sources || [],
        };
        setMessages([...newMessages, botMessage]);
        if (!isAutoSend) setSelectedText(""); // Clear selection only if manual (keep context for auto?) or clear it? User wanted "Explain this" so task is done.
        if (isAutoSend) setSelectedText("");
      } else {
        console.error(
          "[Chatbot] API returned error:",
          data.detail || data.error
        );
        setMessages([
          ...newMessages,
          { role: "assistant", content: `Error: ${data.detail || data.error}` },
        ]);
      }
    } catch (error) {
      console.error("[Chatbot] Fetch error:", error);
      setMessages([
        ...newMessages,
        { role: "assistant", content: `Error: ${error.message}` },
      ]);
    } finally {
      setIsLoading(false);
      console.log("[Chatbot] Loading state set to false.");
    }
  };

  // Auto-send effect
  useEffect(() => {
    if (shouldAutoSend && selectedText) {
      // Trigger send message with the selected text context
      const question = `Explain this section in detail: "${selectedText}"`;
      sendMessage(question, true);
      setShouldAutoSend(false);
    }
  }, [shouldAutoSend, selectedText]);

  const [showMenu, setShowMenu] = useState(false);
  const inputRef = useRef(null);

  // Auto-resize input
  const handleInput = (e) => {
    setInputValue(e.target.value);
    e.target.style.height = "auto";
    e.target.style.height = `${e.target.scrollHeight}px`;
  };

  // Reset height on send
  const handleSend = async () => {
    if (inputRef.current) {
      inputRef.current.style.height = "auto";
    }
    await sendMessage();
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  const toggleChat = () => {
    setIsOpen(!isOpen);
  };

  const clearChat = () => {
    setMessages([]);
    setSessionId(null);
  };

  return (
    <div className="chatbot-container">
      <div className={`chatbot-window ${isOpen ? "open" : ""}`}>
        <div className="chatbot-header">
          <div className="chatbot-title">
            Physical AI & Humanoid Robotics Assistant
          </div>
          <div className="chatbot-controls">
            <div className="menu-container">
              <button
                className="menu-btn"
                onClick={() => setShowMenu(!showMenu)}
                title="Menu"
              >
                ⋮
              </button>
              {showMenu && (
                <div className="menu-dropdown">
                  <button
                    onClick={() => {
                      clearChat();
                      setShowMenu(false);
                    }}
                  >
                    🗑️ Clear Chat
                  </button>
                  <button
                    onClick={() => {
                      toggleChat();
                      setShowMenu(false);
                    }}
                  >
                    ✖ Close
                  </button>
                </div>
              )}
            </div>
          </div>
        </div>

        <div className="chatbot-messages">
          {messages.length === 0 ? (
            <div className="welcome-message">
              <p>Hello! I'm your Physical AI & Humanoid Robotics assistant.</p>
              <p>
                Ask me anything about the book content, or select text on the
                page to ask specific questions about it.
              </p>

              <div className="suggestion-chips">
                <button
                  className="suggestion-chip"
                  onClick={() => setInputValue("What is Physical AI?")}
                >
                  What is Physical AI?
                </button>
                <button
                  className="suggestion-chip"
                  onClick={() => setInputValue("Explain ROS2 nodes")}
                >
                  Explain ROS2 nodes
                </button>
                <button
                  className="suggestion-chip"
                  onClick={() => setInputValue("How do I install Gazebo?")}
                >
                  How do I install Gazebo?
                </button>
              </div>
            </div>
          ) : (
            messages.map((msg, index) => (
              <div key={index} className={`message ${msg.role}`}>
                <div className="message-content">
                  <div className="message-header">
                    <div
                      className={`avatar ${
                        msg.role === "user" ? "user-avatar" : "assistant-avatar"
                      }`}
                    >
                      {msg.role === "user" ? "👤" : "🤖"}
                    </div>
                    <div className="role-label">
                      {msg.role === "user" ? "You" : "Assistant"}
                    </div>
                  </div>
                  <div
                    className="content-text"
                    dangerouslySetInnerHTML={{
                      __html:
                        msg.role === "assistant"
                          ? parseMarkdown(msg.content)
                          : msg.content,
                    }}
                  />
                  {msg.sources && msg.sources.length > 0 && (
                    <div className="sources-section">
                      <strong>Sources:</strong>
                      <ul>
                        {msg.sources.map((source, idx) => (
                          <li key={idx}>
                            {typeof source === "string"
                              ? source
                              : source.file_path ||
                                source.page_content?.substring(0, 100) ||
                                `Source ${idx + 1}`}
                          </li>
                        ))}
                      </ul>
                    </div>
                  )}
                  {msg.role === "assistant" && (
                    <button
                      className="copy-btn"
                      onClick={() => navigator.clipboard.writeText(msg.content)}
                      title="Copy to clipboard"
                    >
                      Copy
                    </button>
                  )}
                </div>
              </div>
            ))
          )}
          {isLoading && (
            <div className="message assistant">
              <div className="message-content">
                <div className="message-header">
                  <div className="avatar assistant-avatar">🤖</div>
                  <div className="role-label">Assistant</div>
                </div>
                <div className="typing-indicator">
                  <div className="typing-dot"></div>
                  <div className="typing-dot"></div>
                  <div className="typing-dot"></div>
                </div>
              </div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>

        <div className="chatbot-input-area">
          {selectedText && (
            <div className="selected-text-preview">
              <div className="selected-text-header">
                <small>Using selected text as context:</small>
                <button
                  className="remove-selection-btn"
                  onClick={() => setSelectedText("")}
                  title="Remove selection"
                >
                  ×
                </button>
              </div>
              <div className="selected-text-content">
                "{selectedText.substring(0, 100)}
                {selectedText.length > 100 ? "..." : ""}"
              </div>
            </div>
          )}
          <div className="input-container">
            <textarea
              ref={inputRef}
              value={inputValue}
              onChange={handleInput}
              onKeyPress={handleKeyPress}
              placeholder="Ask a question..."
              className="chatbot-input"
              rows="1"
            />
            <button
              onClick={handleSend}
              disabled={isLoading || (!inputValue.trim() && !selectedText)}
              className="chatbot-send"
            >
              ➤
            </button>
          </div>
        </div>
      </div>
      <button className="chatbot-toggle" onClick={toggleChat}>
        <span>🤖</span>
      </button>
    </div>
  );
};

export default ChatbotWidget;

function sendMessage() {
  const input = document.getElementById('userInput');
  const model = document.getElementById('modelSelect').value;  // Get selected model
  const chatArea = document.getElementById('chatArea');
  const message = input.value.trim();

  if (message !== '') {
    fetch('/predict', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ message, model })  // Include selected model
    })
    .then(response => response.json())
    .then(data => {
      const userMsg = `<p class="user-msg">You: ${message}</p>`;
      const emotionMsg = `<p class="bot-reply">Emotion: ${data.emotion}</p>`;
      const quoteMsg = `<p class="bot-reply">PandaBud: ${data.quote}</p>`;
      
      const iframe = document.createElement("iframe");
      iframe.src = data.image_url;
      iframe.width = "180";
      iframe.height = "180";
      iframe.allow = "autoplay";
      iframe.style.border = "none";
      iframe.style.margin = "0";
      iframe.style.padding = "0";

      chatArea.innerHTML = userMsg + emotionMsg + quoteMsg;
      chatArea.appendChild(iframe);

      input.value = '';
    });
  }
}

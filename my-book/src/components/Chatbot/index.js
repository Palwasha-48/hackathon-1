import ChatbotWidget from './ChatbotWidget';

const DocusaurusChatbot = () => {
  return (
    <ChatbotWidget apiUrl={process.env.CHATBOT_API_URL || 'http://localhost:8000'} />
  );
};

export default DocusaurusChatbot;
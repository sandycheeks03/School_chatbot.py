import streamlit as st
import time

# Setup the page
st.set_page_config(
    page_title="School Assistant",
    page_icon="🏫",
    layout="wide"
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar
with st.sidebar:
    st.title("🏫 School Assistant")
    st.write("I can help with:")
    st.write("• Courses & Programs")
    st.write("• Admissions")
    st.write("• Campus Facilities")
    st.write("• Student Services")
    st.write("• Financial Information")
    
    st.divider()
    
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

# Main page
st.title("🎓 School Assistant Chatbot")
st.write("Welcome! Ask me anything about our school.")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Response function
def get_school_response(user_input):
    user_input = user_input.lower()
    
    # Greetings
    if any(word in user_input for word in ["hello", "hi", "hey"]):
        return "Hello! 👋 I'm your school assistant. How can I help you today?"
    
    # Courses
    elif any(word in user_input for word in ["course", "program", "subject", "study"]):
        return "We offer programs in: Computer Science, Business, Engineering, Arts, and Health Sciences. Which field interests you?"
    
    # Admissions
    elif any(word in user_input for word in ["admission", "apply", "enroll", "application"]):
        return "📝 **Admissions Process:**\n1. Submit online application\n2. Provide transcripts\n3. Write personal statement\n4. Letters of recommendation\n\nVisit our admissions office for details!"
    
    # Library
    elif any(word in user_input for word in ["library", "book", "study"]):
        return "📚 **Library Information:**\n• Hours: Mon-Fri 8AM-10PM, Weekends 10AM-6PM\n• Features: Computers, study rooms, online resources\n• Contact: library@school.edu"
    
    # Fees
    elif any(word in user_input for word in ["fee", "tuition", "cost", "payment"]):
        return "💰 **Financial Information:**\nTuition varies by program. Financial aid, scholarships, and payment plans available. Contact: financialaid@school.edu"
    
    # Facilities
    elif any(word in user_input for word in ["campus", "facility", "building", "lab"]):
        return "🏛️ **Campus Facilities:**\n• Modern classrooms & labs\n• Sports complex & gym\n• Student center\n• Cafeteria & food court\n• Health center"
    
    # Student services
    elif any(word in user_input for word in ["service", "support", "help", "counseling"]):
        return "👥 **Student Services:**\n• Academic advising\n• Career counseling\n• Health services\n• Disability support\n• International student services"
    
    # Housing
    elif any(word in user_input for word in ["hostel", "dorm", "housing", "accommodation"]):
        return "🏠 **Housing:**\nOn-campus housing available. Apply early through Residence Life office. Off-campus listings also available."
    
    # Contact
    elif any(word in user_input for word in ["contact", "email", "phone", "number"]):
        return "📞 **Contact Information:**\n• Main Office: (555) 123-4567\n• Email: info@school.edu\n• Address: 123 Education Lane, City, State"
    
    # Thanks
    elif any(word in user_input for word in ["thank", "thanks"]):
        return "You're welcome! 😊 Let me know if you need anything else."
    
    # Goodbye
    elif any(word in user_input for word in ["bye", "goodbye", "see you"]):
        return "Goodbye! 👋 Best of luck with your studies!"
    
    # Default
    else:
        return "I'm here to help with school information! Try asking about:\n• Courses and programs\n• Admissions process\n• Campus facilities\n• Student services\n• Financial information"

# Chat input
if prompt := st.chat_input("Ask me about our school..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.write(prompt)
    
    # Get and display bot response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            time.sleep(0.5)  # Small delay to feel natural
            response = get_school_response(prompt)
        st.write(response)
    
    # Add bot response to history
    st.session_state.messages.append({"role": "assistant", "content": response})
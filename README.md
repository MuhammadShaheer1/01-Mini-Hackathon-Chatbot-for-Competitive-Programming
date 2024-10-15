# Ai-Powered Competitive Programming Chatbot

## Team Members
<ul>
  <li>Muhammad Shaheer</li>
  <li>Kashaf Jamil</li>
  <li>Shoaib Ahmed</li>
  <li>Saher Nadeem</li>
  <li>Iram Shaheen</li>
</ul>

## Key Features

<ul>
  <li>
    <strong>Competitive Programming Solver:</strong>Handles problems from Meta Hacker Cup, Advent
of Code, and more.
  </li>
  <li>
    <strong>Memory Capability:</strong>Remembers previous questions in the chat
for seamless conversation flow.
  </li>
    <li>
    <strong>Chroma Vector Database:</strong>Efficient data retrieval using vector embeddings.
  </li>
</ul>

## Data Collection, Prepossessing and Integration

Built using OpenAI's o1-preview model, this chatbot collected and
processed data from Kaggle and various other sources. It's embedding
model plays a crucial role in addressing coding challenges by transforming
problem statements and potential solutions into a high-dimensional vector
representations. 

## UI Design and Implementation:

### Design Approach
<ul>
  <li>
    Designed UI using tools like Sigma and Bribie.
  </li>
  <li>
    Created three forms:
    <ul>
      <li>User Registration</li>
      <li>User Login</li>
      <li>Chatbot Main Interface</li>
    </ul>
  </li>
</ul>

### UI Features
<ul>
  <li>
    Consistent design for registration and login forms.
  </li>
  <li>
    Utilized Bootstrap Glass Morphism for an efficient, modern look.
  </li>
  <li>
      Customized styles with CSS to enhance user experience.
  </li>
</ul>
![alt text]([http://url/to/img.png](https://github.com/MuhammadShaheer1/01-Mini-Hackathon-Chatbot-for-Competitive-Programming/tree/main/img))
### Development Process
<ul>
  <li>
    Developed three HTML pages and linked them with base.css
  </li>
  <li>
    Implemented JavaScript for user authentication and chat functionalities.
  </li>
  <li>
      Added a button to download chat data in .docx format.
  </li>
</ul>

## Challenges
<ul>
  <li>
    <strong>No System Role Support:</strong>The new OpenAI model o1-preview does not support system roles.
  </li>
  <li>
    <strong>Data Chunking:</strong>Efficient splitting and handling of large datasets.
  </li>
    <li>
    <strong>Data Formatting:</strong>Chat data was concatenated, displaying in a single format rather than separating user inputs.
  </li>
</ul>

## Solutions Implemented
<ul>
  <li>
    <strong>Regex Patterns for Chat Separation:</strong>Implemented regex patterns (e.g., "#") to differentiate chatmessages in JavaScript.
  </li>
  <li>
    <strong>User Authentication:</strong>Created functions for user-specific chats, including:
    <ul>
      <li><strong>Login Function:</strong>Authenticates user credentials.</li>
      <li><strong>Register Function:</strong>Saves user data and redirects to the login page.</li>
    </ul>
</ul>


## Future Enhancements
<ul>
  <li>
    <strong>Dataset Expansion:</strong>Broaden the dataset to include more diverse coding challenges.
  </li>
  <li>
    <strong>Enhanced Memory & Interaction Flow:</strong>Improve chatbot memory and ensure smoother, more interactive user experiences.
  </li>
</ul>


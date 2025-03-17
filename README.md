# Spam Detector API & Streamlit UI

## Overview
This project provides a **Spam Detector** that classifies text as **Spam** or **Ham** using a trained SVM model. It consists of:
- A **Flask API** for backend processing.
- A **Streamlit UI** for user interaction.

## Features
✅ **Predicts whether a given text is Spam or Ham**  
✅ **Provides a REST API for external integrations**  
✅ **User-friendly Streamlit interface**  
✅ **Uses machine learning (SVM) for classification**  

## Installation
Make sure you have Python installed. Then, clone this repository and install dependencies:

```bash
# Clone the repository
git clone https://github.com/your-username/spam-detector.git
cd spam-detector

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

## Running the API
Start the Flask API server:
```bash
python api.py
```
By default, it runs on `http://127.0.0.1:5000`.

## Running the Streamlit UI
Run the following command:
```bash
streamlit run ui.py
```
This will launch a user interface in your browser.

## API Usage
### **Endpoint:** `/predict`  
- **Method:** `POST`
- **Content-Type:** `application/json`
- **Request Body:**
  ```json
  {
    "text": "Congratulations! You've won a free iPhone. Click here to claim now!"
  }
  ```
- **Response:**
  ```json
  {
    "prediction": "Spam"
  }
  ```

## Example Spam & Ham Texts
- **Spam:** `"Win $1000 now! Click here: http://spamlink.com"`
- **Ham:** `"Hey, are we still meeting for lunch today?"`

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Added new feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## License
This project is licensed under the MIT License.

---
**Author:** Shishir Rahman  
📧 Contact: your-email@example.com


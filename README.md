# 🛒 Shop Lifting Detection System
A Django web application that detects potential shoplifting activities in video footage using a deep learning model.
This shoplifting detection system extracts frames from a video, detects people using Haar cascades, and tracks them across frames using KCF tracking. A pre-trained model predicts suspicious activity, and a green rectangle highlights detected individuals. The visualization ensures accurate tracking and detection

## 📸 Screenshots
| Upload Page | Results Page |
|-------------|--------------|
| ![Upload Page](https://github.com/mahmouddbelo/RobberyDetection/blob/main/Shop%20Lifting%20Detection%20-%20Google%20Chrome%203_27_2025%202_14_55%20PM.png) | ![Results Page](https://github.com/mahmouddbelo/RobberyDetection/blob/main/result.png)|


## ✨ Features
- 🎥 Modern video upload interface
- 🤖 Deep learning model analysis (TensorFlow/Keras)
- 📊 Detailed visualization of detection results
- 📈 Frame-by-frame prediction breakdown
- 📱 Responsive design works on all devices
- ⏳ Real-time processing status updates

## 🛠️ Technologies Used

- **Backend**: Django 4.2, Python 3.10+
- **Machine Learning**: TensorFlow 2.13, OpenCV 4.8
- **Frontend**: Bootstrap 5, JavaScript , HTML , css
- **Database**: SQLite (Development), PostgreSQL ready

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Git
- TensorFlow 2.x
- Django

### Installation
```bash
# Clone repository
git clone https://github.com/mahmouddbelo/RobberyDetection.git
cd RobberyDetection

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up database
python manage.py migrate

# Run development server
python manage.py runserver
```
## 📂 Project Structure
```bash
RobberyDetection/
├── detection_app/          # Main app
│   ├── models.py           # DB models
│   ├── views.py            # Business logic
│   ├── utils.py            # ML processing
│   ├── urls.py            # Business logic
│   ├── tests.py            # Business logic
│   └── templates/          # HTML templates
├── shoplifting_detector/   # Project config
├── manage.py  
├── media/                  # Uploaded videos
├── requirements.txt        # Dependencies
└── README.md               # Documentation
```
## 📜 License
MIT License



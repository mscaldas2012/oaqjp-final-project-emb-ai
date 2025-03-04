import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_emotion_joy(self):
        joyResult = emotion_detector("I am glad this happened")
        self.assertEqual(joyResult['dominant_emotion'], 'joy')

    def test_emotion_anger(self):
        angerResult = emotion_detector("I am really mad about this")
        self.assertEqual(angerResult['dominant_emotion'], 'anger')

    def test_emotion_disgust(self):
        disgustResult = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(disgustResult['dominant_emotion'], 'disgust')

    def test_emotion_sadness(self):
        sadnessResult = emotion_detector("I am so sad about this")
        self.assertEqual(sadnessResult['dominant_emotion'], 'sadness')

    def test_emotion_fear(self):
        fearResult = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(fearResult['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
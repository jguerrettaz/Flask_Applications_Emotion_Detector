from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Test case 1 for joy
        r1 = emotion_detector("I am glad this happened")
        self.assertEqual(r1['dominant_emotion'], 'joy')
        # Test case 1 for anger
        r2 = emotion_detector("I am really mad about this")
        self.assertEqual(r2['dominant_emotion'], 'anger')
        # Test case 1 for disgust
        r3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(r3['dominant_emotion'], 'disgust')
        # Test case 1 for sadness
        r4 = emotion_detector("I am so sad about this")
        self.assertEqual(r4['dominant_emotion'], 'sadness')
        # Test case 1 for fear
        r5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(r5['dominant_emotion'], 'fear')

unittest.main()
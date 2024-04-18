import supervision as sv
import cv2
import numpy as np
# Define detections
image = cv2.imread("1.jpg")
detections = sv.Detections(
    xyxy=np.array([[270, 270, 370, 370]]),  # Reshaped to (1, 4)
    class_id=np.array([0]),
    confidence=np.array([0.94])
)

# Create a BoundingBoxAnnotator instance
bounding_box_annotator = sv.BoundingBoxAnnotator()

# Annotate the image with bounding boxes
annotated_frame = bounding_box_annotator.annotate(
    scene=image.copy(),
    detections=detections
)
# Plot the annotated image
sv.plot_image(annotated_frame)
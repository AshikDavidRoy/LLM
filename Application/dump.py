# # import supervision as sv
# # import cv2
# # import numpy as np

# # # Open the video file
# # video_capture = cv2.VideoCapture('2.mp4')

# # # Get the width and height of the video
# # frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
# # frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# # # Define the bounding box coordinates
# # bounding_box = np.array([[270, 270, 370, 370]])  # Reshaped to (1, 4)

# # # Create a BoundingBoxAnnotator instance
# # bounding_box_annotator = sv.BoundingBoxAnnotator()

# # while video_capture.isOpened():
# #     # Read the next frame from the video
# #     ret, frame = video_capture.read()

# #     if not ret:
# #         break

# #     # Define detections for the frame
# #     detections = sv.Detections(
# #         xyxy=bounding_box,
# #         class_id=np.array([0]),
# #         confidence=np.array([0.94])
# #     )

# #     # Annotate the frame with the bounding box
# #     annotated_frame = bounding_box_annotator.annotate(
# #         scene=frame,
# #         detections=detections
# #     )

# #     # Display the annotated frame
# #     cv2.imshow('Annotated Frame', annotated_frame)

# #     # Check if the user pressed 'q' to quit
# #     if cv2.waitKey(25) & 0xFF == ord('q'):
# #         break

# # # Release the video capture object and close all windows
# # video_capture.release()
# # cv2.destroyAllWindows()


# import supervision as sv
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# # Open the video file
# video_capture = cv2.VideoCapture('2.mp4')

# # Get the width and height of the video
# frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
# frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# # Define the bounding box coordinates
# bounding_box = np.array([[270, 270, 370, 370]])  # Reshaped to (1, 4)

# # Create a BoundingBoxAnnotator instance
# bounding_box_annotator = sv.BoundingBoxAnnotator()

# while video_capture.isOpened():
#     # Read the next frame from the video
#     ret, frame = video_capture.read()

#     if not ret:
#         break

#     # Define detections for the frame
#     detections = sv.Detections(
#         xyxy=bounding_box,
#         class_id=np.array([0]),
#         confidence=np.array([0.94])
#     )

#     # Annotate the frame with the bounding box
#     annotated_frame = bounding_box_annotator.annotate(
#         scene=frame,
#         detections=detections
#     )

#     # Display the annotated frame using matplotlib
#     plt.imshow(cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB))
#     plt.show()

#     # Check if the user pressed 'q' to quit
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         break

# # Release the video capture object and close all windows
# video_capture.release()
# cv2.destroyAllWindows()

# import cv2
# import matplotlib.pyplot as plt

# # Open the video file
# video_capture = cv2.VideoCapture('2.mp4')

# # Define the coordinates for each second (adjust these according to your data)
# coordinates = {
#     0: [(100, 100), (300, 300)],  # Example coordinates for the first second
#     1: [(150, 150), (350, 350)],  # Example coordinates for the second second
#     # Add more coordinates for each second as needed
# }

# while video_capture.isOpened():
#     # Read the next frame from the video
#     ret, frame = video_capture.read()

#     if not ret:
#         break

#     # Get the current frame index (assuming 30 frames per second)
#     frame_index = int(video_capture.get(cv2.CAP_PROP_POS_FRAMES))
    
#     # Check if the current frame index corresponds to a known coordinate
#     if frame_index in coordinates:
#         # Get the coordinates for the current frame
#         top_left, bottom_right = coordinates[frame_index]
        
#         # Draw the filled bounding box on the frame
#         color = (0, 255, 0)  # Green color
#         cv2.rectangle(frame, top_left, bottom_right, color, thickness=-1)

#     # Display the frame using matplotlib
#     plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
#     plt.show()

#     # Check if the user pressed 'q' to quit
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         break

# # Release the video capture object and close all windows
# video_capture.release()
# cv2.destroyAllWindows()



# import cv2
# import matplotlib.pyplot as plt

# # Open the video file
# video_capture = cv2.VideoCapture('2.mp4')

# # Define the coordinates for each second (adjust these according to your data)
# coordinates = {
#     0: [(100, 100), (300, 300)],    # Example coordinates for the first second
#     1: [(150, 150), (350, 350)],    # Example coordinates for the second second
#     2: [(200, 200), (300, 300)],    # Example coordinates for the first second
#     3: [(250, 250), (350, 350)],
#     4: [(300, 300), (300, 300)],    # Example coordinates for the first second
#     5: [(350, 350), (350, 350)],
#     6: [(400, 400), (300, 300)],    # Example coordinates for the first second
#     7: [(450, 450), (350, 350)],
#     # Add more coordinates for each second as needed
# }

# # Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
# output_video = cv2.VideoWriter('output_video.mp4', fourcc, 30, (640, 480))

# while video_capture.isOpened():
#     # Read the next frame from the video
#     ret, frame = video_capture.read()

#     if not ret:
#         break

#     # Get the current time in seconds
#     current_time_sec = int(video_capture.get(cv2.CAP_PROP_POS_FRAMES) / video_capture.get(cv2.CAP_PROP_FPS))

#     # Check if the current time corresponds to a known coordinate
#     if current_time_sec in coordinates:
#         # Get the bounding box coordinates for the current second
#         top_left, bottom_right = coordinates[current_time_sec]

#         # Draw the bounding box on the frame
#         cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), thickness=2)

#     # Write the frame to the output video file
#     output_video.write(frame)

#     # Display the frame
#     # cv2.imshow('Frame', frame)
#     plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
#     plt.show()


#     # Check if the user pressed 'q' to quit
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         break

# # Release the video capture and output video objects
# video_capture.release()
# output_video.release()

# # Close all windows
# cv2.destroyAllWindows()


# import cv2
# import matplotlib.pyplot as plt

# # Open the video file
# video_capture = cv2.VideoCapture('2.mp4')

# # Define the coordinates for each second (adjust these according to your data)
# coordinates = {
#     0: [(100, 100), (300, 300)],    # Example coordinates for the first second
#     1: [(150, 150), (350, 350)],    # Example coordinates for the second second
#     2: [(200, 200), (300, 300)],    # Example coordinates for the first second
#     3: [(250, 250), (350, 350)],
#     4: [(300, 300), (300, 300)],    # Example coordinates for the first second
#     5: [(350, 350), (350, 350)],
#     6: [(400, 400), (300, 300)],    # Example coordinates for the first second
#     7: [(450, 450), (350, 350)],
#     # Add more coordinates for each second as needed
# }
########################################################################################################
# import cv2
# import matplotlib.pyplot as plt
# # Function to draw bounding box on frame
# def draw_bounding_box(frame, coordinates):
#     # Draw bounding box on frame
#     cv2.rectangle(frame, coordinates[0], coordinates[1], (0, 255, 0), 2)

# # Open input video file
# input_video_path = '4.mp4'
# cap = cv2.VideoCapture(input_video_path)

# # Get video properties
# frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fps = int(cap.get(cv2.CAP_PROP_FPS))
# total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# # Initialize VideoWriter object to save output video
# output_video_path = 'output_video.mp4'
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

# # Define bounding box coordinates per second
# bounding_boxes = {
#     60: [(100, 100), (300, 300)],    # Example coordinates for the first second
#     61: [(105, 105), (350, 350)],    # Example coordinates for the second second
#     62: [(110, 110), (300, 300)],    # Example coordinates for the third second
#     63: [(115, 115), (350, 350)],    # Example coordinates for the fourth second
#     64: [(120, 120), (300, 300)],    # Example coordinates for the fifth second
#     65: [(125, 125), (350, 350)],    # Example coordinates for the sixth second
#     66: [(130, 130), (300, 300)],    # Example coordinates for the seventh second
#     67: [(135, 135), (350, 350)],
# }

# # Iterate through each frame of the input video
# for frame_index in range(total_frames):
#     # Read frame
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # Get current second
#     current_second = int(frame_index / fps)

#     # Draw bounding box if coordinates are available for the current second
#     if current_second in bounding_boxes:
#         coordinates = bounding_boxes[current_second]
#         draw_bounding_box(frame, coordinates)

#     # Write frame to output video
#     out.write(frame)

# # Release VideoWriter and input video
# out.release()
# cap.release()

# print("Output video saved successfully.")

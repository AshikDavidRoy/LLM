import vid
input_video_path = '2.mp4'
output_video_path = 'output_video_2.mp4'
timestamp_with_coordinates = [
        ["00:00:13", 100, 100, 300, 300],
        ["00:00:15", 105, 100, 300, 300],
        ["00:00:16", 110, 110, 300, 300],
        ["00:00:17", 115, 115, 300, 300],
        ["00:00:18", 120, 120, 300, 300],
        ["00:00:19", 125, 125, 300, 300],
    ]
vid.plotter(input_video_path=input_video_path,timestamp_with_coordinates=timestamp_with_coordinates,output_video_path=output_video_path)
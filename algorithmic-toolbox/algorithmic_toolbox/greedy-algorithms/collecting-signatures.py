def collecting_signatures(segments: list):
    segments.sort(key= lambda obj : obj["end"])
    points = []

    while len(segments) > 0:
        new_point = segments[0]["end"]

        def filter_segment(segment):
            if segment["start"] <= new_point and new_point <= segment["end"]:
                return False
            return True
    
        segments = list(filter(filter_segment, segments))
        points.append(str(new_point))
    
    return points


if __name__ == "__main__":
    n_of_segments = int(input())
    
    segments = []
    for i in range(n_of_segments):
        [start, end] = input().split()
        segments.append({
            "start": int(start),
            "end": int(end)
        })
    
    points = collecting_signatures(segments)
    print(len(points))
    print(" ".join(points))
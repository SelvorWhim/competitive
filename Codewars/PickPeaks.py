def pick_peaks(arr):
    pos = []
    peaks = []
    potential_peak = -1 # updated on rise, left alone during plateau (in case it's a peak plateau), used on fall
    for i in range(1,len(arr)):
        if arr[i] > arr[i-1]:
            potential_peak = i
        elif arr[i] < arr[i-1] and potential_peak > 0:
            pos.append(potential_peak)
            peaks.append(arr[potential_peak])
            potential_peak = -1
    return {"pos":pos, "peaks":peaks}

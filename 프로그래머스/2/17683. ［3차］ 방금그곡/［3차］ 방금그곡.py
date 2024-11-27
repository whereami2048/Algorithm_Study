from datetime import datetime

def solution(m, musicinfos):
    answer = []
    time_format = '%H:%M'
    m = m.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a').replace('B#', 'b')
    musicinfos = [info.split(',') for info in musicinfos]
    
    for info in musicinfos:
        start_time = datetime.strptime(info[0], time_format)
        end_time = datetime.strptime(info[1], time_format)
        music_note = info[3].replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a').replace('B#', 'b')
        
        music_len = (end_time - start_time).seconds // 60
        divide = music_len // len(music_note)
        rest = music_len % len(music_note)
        
        target_string = music_note * divide + music_note[:rest]
        
        if m in target_string:
            answer.append([music_len, info[2]])
    
    answer.sort(key=lambda x: -x[0])
    
    if len(answer):
        return answer[0][1]
    else:
        return "(None)"

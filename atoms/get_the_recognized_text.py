# this code is used to get the recognized text from our stt

def run(stt_output):
    if 'text' in stt_output:
        recognized_text = stt_output['text']
        return recognized_text
    else:
        return 'fail'

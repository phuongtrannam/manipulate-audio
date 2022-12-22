from pydub import AudioSegment

unit = 10
num_question = 8
for i in range(num_question):
    file_1 = 'U' + str(unit) + '/Q' + f"{unit:02}" + f"{i+1:02}" + '.mp3'
    file_2 = 'U' + str(unit) + '/A' + f"{unit:02}" + f"{i+1:02}" + '.mp3'
    export_file = 'U' + str(unit) + '/QA' + f"{unit:02}" + f"{i+1:02}" + '.mp3'
    sound1 = AudioSegment.from_file(file_1)
    sound2 = AudioSegment.from_file(file_2)
    combined = sound1 + sound2

    combined.export(export_file, format='mp3')
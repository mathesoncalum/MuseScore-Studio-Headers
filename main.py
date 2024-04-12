import os


def detect_line_ending(lines):
    if lines and '\r\n' in lines[0]:
        return '\r\n'
    else:
        return '\n'


def replace_in_file(filepath):
    try:
        with open(filepath, 'r', newline='') as f:
            lns = f.readlines()
            f.close()
    except Exception as e:
        print(f'Skipping {filepath}: {e}')
        return

    line_ending = detect_line_ending(lns)

    if len(lns) >= 8:
        # Depending on formatting it could be this (typically for .cpp, .h, etc.):
        lns[2] = lns[2].replace('MuseScore-CLA-applies', 'MuseScore-Studio-CLA-applies').rstrip('\r\n') + line_ending
        lns[4] = lns[4].replace('MuseScore', 'MuseScore Studio').rstrip('\r\n') + line_ending
        lns[7] = lns[7].replace('MuseScore BVBA and others', 'MuseScore Limited').rstrip('\r\n') + line_ending

        # Or this (for CMakeLists.txt etc)
        # lns[1] = lns[1].replace('MuseScore-CLA-applies', 'MuseScore-Studio-CLA-applies').rstrip('\r\n') + line_ending
        # lns[3] = lns[3].replace('MuseScore', 'MuseScore Studio').rstrip('\r\n') + line_ending
        # lns[6] = lns[6].replace('MuseScore BVBA and others', 'MuseScore Limited').rstrip('\r\n') + line_ending

    try:
        with open(filepath, 'w') as f:
            f.writelines(lns)
            f.close()
    except Exception as e:
        print(f'Skipping {filepath}: {e}')
        return


def main(directory):
    extensions = ('.cpp', '.h', '.mm', '.mm', '.js')
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extensions):
                replace_in_file(os.path.join(root, file))


if __name__ == '__main__':
    directory_path = '/Users/calum/src/MuseScore/src'
    main(directory_path)

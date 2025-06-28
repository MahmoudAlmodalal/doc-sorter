import pathlib
import shutil
import time


def get_file(dir):
    files = []
    try:
        for file in dir.iterdir():
            if file.is_file():
                files.append(file)
                print(file)
            elif file.is_dir():
                files.extend(get_file(file))
    except PermissionError:
        pass
    return files

def get_drive():
    drive_letters = [f"{d}:/" for d in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
    drives = []
    for drive_letter in drive_letters:
        drive = pathlib.Path(drive_letter)
        if drive.exists():
            drives.append(drive)
    return drives
start_time = time.time()
path = input("Enter the path to save data: ")
try:
    documents  = pathlib.Path(path)
    d = documents / "documents"
    d.mkdir(exist_ok=True)
    doc = d / "DOC"
    docx = d / "DOCX"
    txt = d / "TXT"
    rtf = d / "RTF"
    odt = d / "ODT"
    pdf = d / "PDF"
    xls = d / "XLS"
    xlsx = d / "XLSX"
    ppt = d / "PPT"
    pptx = d / "PPTX"
    info = d / "info.txt"
    info.touch()

    ext = [".doc", ".docx", ".txt", ".rtf", ".odt", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]
    dirs = [doc, docx, txt, rtf, odt, pdf, xls, xlsx, ppt, pptx ]
    for dir in dirs:
        dir.mkdir(exist_ok=True)
    all_file = []
    file_copied = []
    f = open(info, "w")
    # if windows system
    for drive in get_drive():
        all_file.extend(get_file(drive))
    
    # if Linux system
    all_file.extend(get_file(pathlib.Path("/")))

    # if mobile turmux system
    all_file.extend(get_file(pathlib.Path("/data/data/com.termux/files/home/storage/shared")))

    
    i = 1
    for file in all_file:
        if file.suffix in ext:
            try:
                shutil.copy(file.absolute(), dirs[ext.index(file.suffix)].absolute())
                file_copied.append(file)
                f.write(f"{str(i) + '- source path: ' + str(file.absolute()) :200s}{' -> ' + str(i) + '- destination path: ' + str((dirs[ext.index(file.suffix)] / file.name).absolute())}\n")
                i += 1
            except (PermissionError, shutil.SameFileError):
                pass

    f.write(f"The total number of files searched: {len(all_file)}\n")
    f.write(f"The total number of files copied: {len(file_copied)}\n")
    end_time = time.time()
    time_consumed = end_time - start_time
    f.write(f"Time consumed: {time_consumed:.4f} seconds")

    
except (FileNotFoundError, PermissionError):
    print("File not found or PermissionError")

def download(response, output):
    total_downloaded = 0
    while True:
        data = response.read(BUFF_SIZE)
        total_downloaded += len(data)
        if not data:
            break
        out_file.write(data)
        print('Downloaded {bytes}'.format(bytes=total_downloaded))

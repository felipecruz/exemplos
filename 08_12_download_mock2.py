import unittest
from unittest import mock

BUFF_SIZE = 1024

def download(response, output):
    total_downloaded = 0
    while True:
        data = response.read(BUFF_SIZE)
        total_downloaded += len(data)
        if not data:
            break
        output.write(data)
        print('Downloaded {bytes}'.format(bytes=total_downloaded))


class DownloadTest(unittest.TestCase):
    def test_download_with_no_length(self):
        response = mock.MagicMock()
        response.read = mock.MagicMock(side_effect=['data', 'more data', ''])

        output = mock.MagicMock()
        output.write = mock.MagicMock()

        download(response, output)

        calls = [mock.call(BUFF_SIZE),
                 mock.call(BUFF_SIZE),
                 mock.call(BUFF_SIZE)]

        response.read.assert_has_calls(calls)

        calls = [mock.call('data'),
                 mock.call('more data')]

        output.write.assert_has_calls(calls)

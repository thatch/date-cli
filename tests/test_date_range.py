import sys
import subprocess


def call_procress(command, stdout):
    if sys.version_info.major == 3:
        result = subprocess.run(command, stdout=stdout)
        try:
            return result.stdout.decode()
        except:
            return result
    else:
        return subprocess.check_output(command, stdout)


def test_date_range_base():
    result = call_procress(['date_range', '-s', '20200201'],
                           stdout=subprocess.PIPE)


def test_date_range_periods():
    result = call_procress(['date_range', '-s', '20200201', '-p', '20'],
                           stdout=subprocess.PIPE)
    assert len(result.split('\n')) == 21, 'paramter PERIODS not working'


def test_date_range_with_end():
    result = call_procress(['date_range', '-s', '20200201', '-e', '20200205'],
                           stdout=subprocess.PIPE)
    assert len(result.split('\n')) == 6, 'paramter END not working'


def test_date_range_with_format():
    result = call_procress(
        ['date_range', '-s', '20200201', '-p', '1', '-f', '%m%d%Y'],
        stdout=subprocess.PIPE)
    assert result == '02012020\n', 'paramter FORMAT not working'


def test_date_range_with_only():
    result = call_procress(
        ['date_range', '-s', '20200201', '-o', 's', '-p', '10'],
        stdout=subprocess.PIPE)
    assert result == '20200201\n', 'paramter ONLY  "s" value not working'
    result = call_procress(['date_range', '-s', '20200201', '-o', 'e'],
                           stdout=subprocess.PIPE)
    assert result == '20200229\n', 'paramter ONLY  "e" value not working'
    result = call_procress(
        ['date_range', '-s', '20200201', '-o', 'se', '-p', '30'],
        stdout=subprocess.PIPE)
    assert result == '20200201\n20200229\n20200301\n', 'paramter ONLY  "se" value not working'


def test_date_range_with_reverse():
    result = call_procress(
        ['date_range', '-s', '20200201', '-p', '2', '-r', 'Y'],
        stdout=subprocess.PIPE)
    assert result == '20200202\n20200201\n', 'paramter REVERSE not working'

from subprocess import Popen, PIPE

def size_of_tmp():
  proc = Popen(["python3", "size.py"], stdin=PIPE, stdout=PIPE, stderr=PIPE,
		universal_newlines=True)
  (stdout, stderr) = proc.communicate("/tmp")
  exit_code = proc.wait()
  if exit_code != 0:
    return stderr
  else:
    return stdout

if __name__ == "__main__":
  print(size_of_tmp())



from subprocess import Popen, PIPE

def command(directory):
  return ["du", "-sh", directory]


def check_size(directory):
  proc = Popen(command(directory), stdout=PIPE, stderr=PIPE, universal_newlines=True)
  result = ""
  exit_code = proc.wait()
  if exit_code != 0:
    for line in proc.stderr:
      result = result + line
  
  else:
    for line in proc.stdout:
      result = result + line
  return result

def main():
  arg = input("directory to check: ")
  result = check_size(directory=arg)
  print(result)

if __name__ == "__main__":
  main()



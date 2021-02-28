#timer function

def countdown(t):
    while t: # while t > 0 for clarity 
      mins = t // 60
      secs = t % 60
      timer = '{:02d}:{:02d}'.format(mins, secs)
      print("Signal: Green")
      print(timer) # overwrite previous line 
      time.sleep(1)
      t -= 1
    print('signal : RED')

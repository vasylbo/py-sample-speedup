##### py-sample-speedup

My try to speed up python's random.sample method. 
Original method I've got from cpythons git [mirror](https://github.com/python/cpython). 

##### Results for 100 iterations on my pc:

original_sample
```
Getting 900 elements out of 5000 - 1.723884052588857 seconds
Getting 2900 elements out of 5000 - 4.965715611200088 seconds
Getting 4900 elements out of 5000 - 8.36861182262655 seconds
```

improved_sample
```
Getting 900 elements out of 5000 - 0.27872600690874094 seconds
Getting 2900 elements out of 5000 - 0.37690155552910376 seconds
Getting 4900 elements out of 5000 - 0.47497000090513986 seconds
```

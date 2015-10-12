##### py-sample-speedup

My try to speed up python's random.sample method. 
Original method I've got from cpythons git [mirror](https://github.com/python/cpython). 

```
def improved_sample(population, k, shuffle=True):
```
```population``` and ```k``` used like in origin method. ```shuffle``` implemented due to algorithm behavior. It outputs elements in reversed order. So if you need behavior like in original sample (not only random elements, but in random order) you have leave ```shuffle``` as is(```True```). But to have maximum speed call ```improved_sample``` with ```False``` as third parameter. 

##### Results for 100 iterations on my pc:

Speed test for Original sample
```
Getting 900 elements out of 5000 - 1.7298053771223894 seconds
Getting 2900 elements out of 5000 - 4.912327008111639 seconds
Getting 4900 elements out of 5000 - 8.506528223678792 seconds
```
Speed test for Improved sample
```
Getting 900 elements out of 5000 - 1.0697965934666236 seconds
Getting 2900 elements out of 5000 - 2.8724894329827144 seconds
Getting 4900 elements out of 5000 - 4.640079082006107 seconds
```
Speed test for Improved sample with reversed saved order
```
Getting 900 elements out of 5000 - 0.26750917583522593 seconds
Getting 2900 elements out of 5000 - 0.356656296830522 seconds
Getting 4900 elements out of 5000 - 0.4441971555274584 seconds
```

##### Distribution tests:

Original sample:
![1](https://cloud.githubusercontent.com/assets/1439422/10440392/633c2ef6-7147-11e5-8dc8-eb5f70897e31.png)

Improved sample:
![2](https://cloud.githubusercontent.com/assets/1439422/10440426/b62ca514-7147-11e5-823b-fdb757e01141.png)

Improved sample with reversed saved order (doesn't make sense to show it, but still):
![3](https://cloud.githubusercontent.com/assets/1439422/10440432/bdec0b1e-7147-11e5-8f0d-28f992243e15.png)

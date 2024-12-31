## WIP WIP WIP

### boxel (even the name is WIP)
trying to improve on nk412/quickhist


### todo
- streaming percentile calcs
- support for multiple streams for comparison
- configurability
- get rid of numpy dependency
- get rid of colored dependency

### Examples

#### distribution of line lengths within source

```
╰──╴$ cat boxel.py | awk '{print length($0)}' | python boxel.py


        ┠──┨░░░░░░┃░░░░░░░┠──────────────────────────────┨
        Min:0.0
           Q1:7.0
                  Q2:23.0
                          Q3:39.0
                                                          Max:107.0
```

#### guassian

```
╰──╴$ for x in $( seq 100000); do echo $(( ($RANDOM + $RANDOM + $RANDOM) )) ; done | python boxel.py


        ┠──────────────────┨░░░░░┃░░░░░┠─────────────────┨
        Min:867.0
                           Q1:37570.0
                                 Q2:49119.0
                                       Q3:60669.0
                                                          Max:96625.0
```


#### uniform

```
╰──╴$ for x in $( seq 100000); do echo $(( $RANDOM )) ; done | python boxel.py


        ┠───────────┨░░░░░░░░░░░┃░░░░░░░░░░░░┠───────────┨
        Min:0.0
                    Q1:8175.0
                                Q2:16377.0
                                             Q3:24637.25
                                                          Max:32767.0
```


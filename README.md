# ASCII-art
A program to turn images into ASCII-art. It is created by printing characters to your terminal so as to recreate the contours of a source image.

![whysoserious](https://user-images.githubusercontent.com/30603669/42334754-c7d60e70-809b-11e8-83b6-23cc29017b1e.png)

![magnify](https://user-images.githubusercontent.com/30603669/42334790-e25775e0-809b-11e8-9635-a8b4a0c5a099.png)

# Dependencies
All of the dependencies can be installed via `pip`
 - PIL
 - colorama
 - argparse

# Usage

download [ASCIIart.py](https://github.com/sathwikmatsa/ASCII-art/blob/master/ASCIIart.py) and execute:
```
python ASCIIart.py [-h] [-c] [-i] [-m {0,1,2}] [-ws WIDTH] [-hs HEIGHT]
                   filename
```

- positional arguments:
  * filename
- optional arguments:
  * `-h, --help`            : show this help message and exit
  * `-c, --color`           : ASCII art in glorious color
  * `-i, --invert`          : invert all the brightnesses
  * `-m {0,1,2}, --map {0,1,2}` 
                          : brightness mappings: 0 for average, 1 for lightness, 2 for luminosity
  * `-ws WIDTH, --width WIDTH`
                          : width of the screen
  * `-hs HEIGHT, --height HEIGHT`
                          : height of the screen
                          
  `Use trial and error to work out the largest image that you can display on your terminal by using params -ws and -hs.`

# Features

- Set RGB mappings in 3 styles (average, lightness, luminosity)

- invert brightness

  ![inversion](https://user-images.githubusercontent.com/30603669/42338901-00de8c6c-80a9-11e8-82d1-92db465019de.png)

- 8 color pallete
  
  ![color](https://user-images.githubusercontent.com/30603669/42339301-3d2a8940-80aa-11e8-8478-67d732fd3f97.png)
  

# Acknowledgments

Gratitude to [Robert Heaton](https://robertheaton.com/) for inspiring me to do this project.
Head to his blog [post](https://robertheaton.com/2018/06/12/programming-projects-for-advanced-beginners-ascii-art/), if you want to build ASCII-art from scratch.



# License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/sathwikmatsa/ASCII-art/blob/master/LICENSE) file for details

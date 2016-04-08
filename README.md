# Word2Color

## About

Word2Color converts natural language color descriptions to 
[standard HTML4 colors](http://www.webstandards.org/learn/reference/charts/color_names/). This is especially useful in data science, where `color` attributes often do not follow any normal list -- this enables users to quickly add various colors to simplifying bins of HTML4 standard colors.

## Installation

Word2Color is only tested on Python 2.7.X, although it likely works on Python 3 as well. OpenCV 2.4.X is a dependency, but is not listed in the requirements.txt to maintain compatability with virtual environments ([See: How to install OpenCV in virtualenv](http://stackoverflow.com/a/12043136/2544124)).

## Example Usage

```python
>>> from word2color import word2color
>>> word2color.color_description_to_bin('blue cream')
'silver'
```

## Contributing

Pull requests are welcome!

## License

Word2Color is licensed under the MIT License.

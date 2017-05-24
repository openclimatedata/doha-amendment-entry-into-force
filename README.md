Ratification Status of the Doha Amendment to the Kyoto Protocol

## Data

The dataset contains dates of acceptance of the Doha Amendment to the Kyoto
Protocol and makes it available as a simple CSV file.
See the [UNFCCC page on the Ratification Status](http://unfccc.int/kyoto_protocol/doha_amendment/items/7362.php) for
further information.
Source for this dataset is the XML version in the official [UN Treaty
Collection](https://treaties.un.org/Pages/ViewDetails.aspx?src=TREATY&mtdsg_no=XXVII-7-c&chapter=27&clang=_en)


## Preparation

The `Makefile` requires Python3 and will automatically install its dependencies
into a Virtualenv when run with

```shell
make
```

Running `make` will also update the repo, then fetch and update the dataset. The
download and extraction is done in `script/process.py`.


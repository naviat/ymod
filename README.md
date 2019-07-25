# ymod
A command line interface to read and manipulate YAML files. Based on python, distributed as pip.

## Installation

```
git clone https://github.com/naviat/ymod
cd ymod
pip install .
```


## Examples

How to set a key:

```bash
> ymod -s key:subkey value
key:
  subkey: value
```

Support of different data types:

```bash
> ymod \
    -s deposit:tomochain:distribution_public_key 0x59B8515E7fF389df6926Cd52a086B0f1f46C630A \                       # number value
    -s deposit:tomochain:issuer_public_key 0x59B8515E7fF389df6926Cd52a086B0f1f46C630A \                             # boolean value
    -n deposit:tomochain:lock_unix_timestamp 0 \     # string value
    -s deposit:tomochain:signer_private_key 0x7f4c1bacba63f05827f6d8fc0e22cf68c42005775a7f73abff7d819986bae77c \    # list value
    -n deposit:tomochain:starting_balance 100  \                                                                    # null value
    -s deposit:tomochain:token_asset_code WETH

# output - YAML doesn't keep order
 deposit:
   tomochain:
     distribution_public_key: 0x59B8515E7fF389df6926Cd52a086B0f1f46C630A
     issuer_public_key: 0x59B8515E7fF389df6926Cd52a086B0f1f46C630A
     lock_unix_timestamp: 0
     signer_private_key: 0x7f4c1bacba63f05827f6d8fc0e22cf68c42005775a7f73abff7d819986bae77c
     starting_balance: 100
     token_asset_code: WETH
```
  
  
## Usage

```text
usage: ymod [-h] [-i INPUT] [-o OUTPUT] [-f FILE] [-d KEY] [-s KEY VAL]
                [-n KEY VAL] [-b KEY VAL] [-l KEY [VAL ...]] [--null KEY]
                [--version] [-v] [--debug]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        YAML file to load. Of not provided an empty YAML will
                        be the base for all operations.
  -o OUTPUT, --output OUTPUT
                        Output file. If not provided output is written to
                        STDOUT
  -f FILE, --file FILE  YAML file for inplace manipulation.
  -d KEY, --delete KEY  Delete key: mykey:subkey:subkey. Skipped silently if
                        key doesn't exist.
  -s KEY VAL, --string KEY VAL
                        Set key with string value: mykey:subkey:subkey 'my
                        value'
  -n KEY VAL, --number KEY VAL
                        Set key with number value: mykey:subkey:subkey 3.7
  -b KEY VAL, --boolean KEY VAL
                        Set key with number value: mykey:subkey:subkey true
                        (possible values: ('1', 'true', 'True', 'yes') ('',
                        '0', 'false', 'False', 'no'))
  -l KEY [VAL ...], --list KEY [VAL ...]
                        Set key with value as list of strings:
                        mykey:subkey:subkey intem1 intem2 intem3
  --null KEY            Set key with null value: mykey:subkey:subkey
  --version             show program's version number and exit
  -v, --verbose         Verbose output
  --debug               Debug output
```

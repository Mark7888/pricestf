# PricesTF Python API

This modul is a simple python api for [Nickalson's](https://github.com/Nicklason/) prices.tf website.

### Installation

This module requires [Python](https://www.python.org/) v3+ to run.

For install the module type this to your command line...

```sh
pip install pricestf
```
### Quick Example
```py
from pricestf import get_price

print(get_price("Scattergun", quality="Strange", australium=False, killstreak=0, error_message=True))
```
It will return a dictionary with the item's full name and with the buy- and sellprices.
If something went wring, it returns an error code.

Error codes:
- `0`: Unknown error
- `1`: Rate limit exceeded
- `2`: Item is not priced
- `3`: No prices for given source
- `4`: No item named <name>

[List of tf2 items](https://wiki.alliedmods.net/Team_fortress_2_item_definition_indexes)


Qualities:
- Normal
- Genuine
- Vintage
- rarity3
- Unusual
- Unique (Default)
- Community
- Valve
- Self-Made
- Customized
- Strange
- Completed
- Haunted
- Collector's
- Decorated Weapon

Australium:
- It can be `True` if australium, and `False` if not. (Default: `False`)

Killstreak:
- If ``not killstreak`` it's `0`
- If ``killstreak`` it's `1`
- If ``specialized`` it's `2`
- If ``pofessional`` it's `3`

Error message:
- If `True` it will print the error message, if `False` it wont. (Default: `True`)


License
----

MIT

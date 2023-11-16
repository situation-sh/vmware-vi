# OptionDef

Describes a user-defined option.  The name of each option is identified by the \"key\" property, inherited from the *ElementDescription* data object type. You can indicate the property's position in a hierarchy by using a dot-separated notation. The string preceding the first dot is the top of the hierarchy. The hierarchy descends to a new sublevel with each dot. For example, \"Ethernet.NetworkConnection.Bridged\". 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**option_type** | [**OptionType**](OptionType.md) |  | 

## Example

```python
from vmware_vi.models.option_def import OptionDef

# TODO update the JSON string below
json = "{}"
# create an instance of OptionDef from a JSON string
option_def_instance = OptionDef.from_json(json)
# print the JSON string representation of the object
print OptionDef.to_json()

# convert the object into a dict
option_def_dict = option_def_instance.to_dict()
# create an instance of OptionDef from a dict
option_def_form_dict = option_def.from_dict(option_def_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



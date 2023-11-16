# OptionValue

Describes the key/value pair of a configured option. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The name of the option using dot notation to reflect the option&#39;s position in a hierarchy.  For example, you might have an option called \&quot;Ethernet\&quot; and another option that is a child of that called \&quot;Connection\&quot;. In this case, the key for the latter could be defined as \&quot;Ethernet.Connection\&quot;  | 
**value** | [**Any**](Any.md) |  | [optional] 

## Example

```python
from vmware_vi.models.option_value import OptionValue

# TODO update the JSON string below
json = "{}"
# create an instance of OptionValue from a JSON string
option_value_instance = OptionValue.from_json(json)
# print the JSON string representation of the object
print OptionValue.to_json()

# convert the object into a dict
option_value_dict = option_value_instance.to_dict()
# create an instance of OptionValue from a dict
option_value_form_dict = option_value.from_dict(option_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ArrayOfInvalidIpfixConfig

A boxed array of *InvalidIpfixConfig*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[InvalidIpfixConfig]**](InvalidIpfixConfig.md) |  | 

## Example

```python
from vmware_vi.models.array_of_invalid_ipfix_config import ArrayOfInvalidIpfixConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInvalidIpfixConfig from a JSON string
array_of_invalid_ipfix_config_instance = ArrayOfInvalidIpfixConfig.from_json(json)
# print the JSON string representation of the object
print ArrayOfInvalidIpfixConfig.to_json()

# convert the object into a dict
array_of_invalid_ipfix_config_dict = array_of_invalid_ipfix_config_instance.to_dict()
# create an instance of ArrayOfInvalidIpfixConfig from a dict
array_of_invalid_ipfix_config_form_dict = array_of_invalid_ipfix_config.from_dict(array_of_invalid_ipfix_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



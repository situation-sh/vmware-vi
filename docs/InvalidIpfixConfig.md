# InvalidIpfixConfig

Illegal value specified for a property of the switch's IpfixConfig.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** | Path of the property in IpfixConfig that has an invalid value.  ***Since:*** vSphere API 5.1  | [optional] 

## Example

```python
from vmware_vi.models.invalid_ipfix_config import InvalidIpfixConfig

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidIpfixConfig from a JSON string
invalid_ipfix_config_instance = InvalidIpfixConfig.from_json(json)
# print the JSON string representation of the object
print InvalidIpfixConfig.to_json()

# convert the object into a dict
invalid_ipfix_config_dict = invalid_ipfix_config_instance.to_dict()
# create an instance of InvalidIpfixConfig from a dict
invalid_ipfix_config_form_dict = invalid_ipfix_config.from_dict(invalid_ipfix_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



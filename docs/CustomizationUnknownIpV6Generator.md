# CustomizationUnknownIpV6Generator

The ipv6 address is left unspecified.  The user must be prompted to supply an ipv6 address.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.customization_unknown_ip_v6_generator import CustomizationUnknownIpV6Generator

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationUnknownIpV6Generator from a JSON string
customization_unknown_ip_v6_generator_instance = CustomizationUnknownIpV6Generator.from_json(json)
# print the JSON string representation of the object
print CustomizationUnknownIpV6Generator.to_json()

# convert the object into a dict
customization_unknown_ip_v6_generator_dict = customization_unknown_ip_v6_generator_instance.to_dict()
# create an instance of CustomizationUnknownIpV6Generator from a dict
customization_unknown_ip_v6_generator_form_dict = customization_unknown_ip_v6_generator.from_dict(customization_unknown_ip_v6_generator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



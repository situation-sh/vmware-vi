# CustomizationCustomIpV6Generator

Use a command-line program configured with the VirtualCenter server.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**argument** | **str** | An optional argument that is passed to the utility for this ipv6 address.  The meaning of this field is user-defined, in the script.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.customization_custom_ip_v6_generator import CustomizationCustomIpV6Generator

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationCustomIpV6Generator from a JSON string
customization_custom_ip_v6_generator_instance = CustomizationCustomIpV6Generator.from_json(json)
# print the JSON string representation of the object
print CustomizationCustomIpV6Generator.to_json()

# convert the object into a dict
customization_custom_ip_v6_generator_dict = customization_custom_ip_v6_generator_instance.to_dict()
# create an instance of CustomizationCustomIpV6Generator from a dict
customization_custom_ip_v6_generator_form_dict = customization_custom_ip_v6_generator.from_dict(customization_custom_ip_v6_generator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



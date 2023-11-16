# CustomizationStatelessIpV6Generator

Use stateless autoconfiguration to configure to ipv6 address  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.customization_stateless_ip_v6_generator import CustomizationStatelessIpV6Generator

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationStatelessIpV6Generator from a JSON string
customization_stateless_ip_v6_generator_instance = CustomizationStatelessIpV6Generator.from_json(json)
# print the JSON string representation of the object
print CustomizationStatelessIpV6Generator.to_json()

# convert the object into a dict
customization_stateless_ip_v6_generator_dict = customization_stateless_ip_v6_generator_instance.to_dict()
# create an instance of CustomizationStatelessIpV6Generator from a dict
customization_stateless_ip_v6_generator_form_dict = customization_stateless_ip_v6_generator.from_dict(customization_stateless_ip_v6_generator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CustomizationCustomIpGenerator

Use a command-line program configured with the VirtualCenter server. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**argument** | **str** | An optional argument that is passed to the utility for this IP address.  The meaning of this field is user-defined, in the script.  | [optional] 

## Example

```python
from vmware_vi.models.customization_custom_ip_generator import CustomizationCustomIpGenerator

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationCustomIpGenerator from a JSON string
customization_custom_ip_generator_instance = CustomizationCustomIpGenerator.from_json(json)
# print the JSON string representation of the object
print CustomizationCustomIpGenerator.to_json()

# convert the object into a dict
customization_custom_ip_generator_dict = customization_custom_ip_generator_instance.to_dict()
# create an instance of CustomizationCustomIpGenerator from a dict
customization_custom_ip_generator_form_dict = customization_custom_ip_generator.from_dict(customization_custom_ip_generator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



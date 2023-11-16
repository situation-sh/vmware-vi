# ArrayOfCustomizationFixedIp

A boxed array of *CustomizationFixedIp*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[CustomizationFixedIp]**](CustomizationFixedIp.md) |  | 

## Example

```python
from vmware_vi.models.array_of_customization_fixed_ip import ArrayOfCustomizationFixedIp

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCustomizationFixedIp from a JSON string
array_of_customization_fixed_ip_instance = ArrayOfCustomizationFixedIp.from_json(json)
# print the JSON string representation of the object
print ArrayOfCustomizationFixedIp.to_json()

# convert the object into a dict
array_of_customization_fixed_ip_dict = array_of_customization_fixed_ip_instance.to_dict()
# create an instance of ArrayOfCustomizationFixedIp from a dict
array_of_customization_fixed_ip_form_dict = array_of_customization_fixed_ip.from_dict(array_of_customization_fixed_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



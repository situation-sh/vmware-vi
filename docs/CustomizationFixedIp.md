# CustomizationFixedIp

Use a static IP Address for the virtual network adapter. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **str** |  | 

## Example

```python
from vmware_vi.models.customization_fixed_ip import CustomizationFixedIp

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationFixedIp from a JSON string
customization_fixed_ip_instance = CustomizationFixedIp.from_json(json)
# print the JSON string representation of the object
print CustomizationFixedIp.to_json()

# convert the object into a dict
customization_fixed_ip_dict = customization_fixed_ip_instance.to_dict()
# create an instance of CustomizationFixedIp from a dict
customization_fixed_ip_form_dict = customization_fixed_ip.from_dict(customization_fixed_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



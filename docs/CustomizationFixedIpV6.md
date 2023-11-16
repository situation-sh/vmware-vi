# CustomizationFixedIpV6

Use a static ipv6 address for the virtual network adapter  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **str** |  | 
**subnet_mask** | **int** |  | 

## Example

```python
from vmware_vi.models.customization_fixed_ip_v6 import CustomizationFixedIpV6

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationFixedIpV6 from a JSON string
customization_fixed_ip_v6_instance = CustomizationFixedIpV6.from_json(json)
# print the JSON string representation of the object
print CustomizationFixedIpV6.to_json()

# convert the object into a dict
customization_fixed_ip_v6_dict = customization_fixed_ip_v6_instance.to_dict()
# create an instance of CustomizationFixedIpV6 from a dict
customization_fixed_ip_v6_form_dict = customization_fixed_ip_v6.from_dict(customization_fixed_ip_v6_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ArrayOfPhysicalNicCdpInfo

A boxed array of *PhysicalNicCdpInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PhysicalNicCdpInfo]**](PhysicalNicCdpInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_physical_nic_cdp_info import ArrayOfPhysicalNicCdpInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPhysicalNicCdpInfo from a JSON string
array_of_physical_nic_cdp_info_instance = ArrayOfPhysicalNicCdpInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfPhysicalNicCdpInfo.to_json()

# convert the object into a dict
array_of_physical_nic_cdp_info_dict = array_of_physical_nic_cdp_info_instance.to_dict()
# create an instance of ArrayOfPhysicalNicCdpInfo from a dict
array_of_physical_nic_cdp_info_form_dict = array_of_physical_nic_cdp_info.from_dict(array_of_physical_nic_cdp_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



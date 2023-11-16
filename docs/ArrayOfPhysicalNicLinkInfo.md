# ArrayOfPhysicalNicLinkInfo

A boxed array of *PhysicalNicLinkInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PhysicalNicLinkInfo]**](PhysicalNicLinkInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_physical_nic_link_info import ArrayOfPhysicalNicLinkInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPhysicalNicLinkInfo from a JSON string
array_of_physical_nic_link_info_instance = ArrayOfPhysicalNicLinkInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfPhysicalNicLinkInfo.to_json()

# convert the object into a dict
array_of_physical_nic_link_info_dict = array_of_physical_nic_link_info_instance.to_dict()
# create an instance of ArrayOfPhysicalNicLinkInfo from a dict
array_of_physical_nic_link_info_form_dict = array_of_physical_nic_link_info.from_dict(array_of_physical_nic_link_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



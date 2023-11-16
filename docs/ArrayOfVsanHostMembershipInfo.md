# ArrayOfVsanHostMembershipInfo

A boxed array of *VsanHostMembershipInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VsanHostMembershipInfo]**](VsanHostMembershipInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vsan_host_membership_info import ArrayOfVsanHostMembershipInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVsanHostMembershipInfo from a JSON string
array_of_vsan_host_membership_info_instance = ArrayOfVsanHostMembershipInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVsanHostMembershipInfo.to_json()

# convert the object into a dict
array_of_vsan_host_membership_info_dict = array_of_vsan_host_membership_info_instance.to_dict()
# create an instance of ArrayOfVsanHostMembershipInfo from a dict
array_of_vsan_host_membership_info_form_dict = array_of_vsan_host_membership_info.from_dict(array_of_vsan_host_membership_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



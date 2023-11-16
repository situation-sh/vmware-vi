# HostMultipathInfoFixedLogicalUnitPolicy

The *HostMultipathInfoFixedLogicalUnitPolicy* data object describes a multipathing policy for a logical unit which uses a preferred path whenever possible. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prefer** | **str** | Preferred path used for the **fixed** policy.  | 

## Example

```python
from vmware_vi.models.host_multipath_info_fixed_logical_unit_policy import HostMultipathInfoFixedLogicalUnitPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of HostMultipathInfoFixedLogicalUnitPolicy from a JSON string
host_multipath_info_fixed_logical_unit_policy_instance = HostMultipathInfoFixedLogicalUnitPolicy.from_json(json)
# print the JSON string representation of the object
print HostMultipathInfoFixedLogicalUnitPolicy.to_json()

# convert the object into a dict
host_multipath_info_fixed_logical_unit_policy_dict = host_multipath_info_fixed_logical_unit_policy_instance.to_dict()
# create an instance of HostMultipathInfoFixedLogicalUnitPolicy from a dict
host_multipath_info_fixed_logical_unit_policy_form_dict = host_multipath_info_fixed_logical_unit_policy.from_dict(host_multipath_info_fixed_logical_unit_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



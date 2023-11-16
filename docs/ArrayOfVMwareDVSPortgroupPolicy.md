# ArrayOfVMwareDVSPortgroupPolicy

A boxed array of *VMwareDVSPortgroupPolicy*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VMwareDVSPortgroupPolicy]**](VMwareDVSPortgroupPolicy.md) |  | 

## Example

```python
from vmware_vi.models.array_of_v_mware_dvs_portgroup_policy import ArrayOfVMwareDVSPortgroupPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVMwareDVSPortgroupPolicy from a JSON string
array_of_v_mware_dvs_portgroup_policy_instance = ArrayOfVMwareDVSPortgroupPolicy.from_json(json)
# print the JSON string representation of the object
print ArrayOfVMwareDVSPortgroupPolicy.to_json()

# convert the object into a dict
array_of_v_mware_dvs_portgroup_policy_dict = array_of_v_mware_dvs_portgroup_policy_instance.to_dict()
# create an instance of ArrayOfVMwareDVSPortgroupPolicy from a dict
array_of_v_mware_dvs_portgroup_policy_form_dict = array_of_v_mware_dvs_portgroup_policy.from_dict(array_of_v_mware_dvs_portgroup_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



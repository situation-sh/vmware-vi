# DistributedVirtualSwitchManagerHostDvsFilterSpec

Base class for filters to check host compatibility.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inclusive** | **bool** | If this flag is true, then the filter returns the hosts in the *DistributedVirtualSwitchManagerHostContainer* that satisfy the criteria specified by this filter, otherwise it returns hosts that don&#39;t meet the criteria.  ***Since:*** vSphere API 4.1  | 

## Example

```python
from vmware_vi.models.distributed_virtual_switch_manager_host_dvs_filter_spec import DistributedVirtualSwitchManagerHostDvsFilterSpec

# TODO update the JSON string below
json = "{}"
# create an instance of DistributedVirtualSwitchManagerHostDvsFilterSpec from a JSON string
distributed_virtual_switch_manager_host_dvs_filter_spec_instance = DistributedVirtualSwitchManagerHostDvsFilterSpec.from_json(json)
# print the JSON string representation of the object
print DistributedVirtualSwitchManagerHostDvsFilterSpec.to_json()

# convert the object into a dict
distributed_virtual_switch_manager_host_dvs_filter_spec_dict = distributed_virtual_switch_manager_host_dvs_filter_spec_instance.to_dict()
# create an instance of DistributedVirtualSwitchManagerHostDvsFilterSpec from a dict
distributed_virtual_switch_manager_host_dvs_filter_spec_form_dict = distributed_virtual_switch_manager_host_dvs_filter_spec.from_dict(distributed_virtual_switch_manager_host_dvs_filter_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



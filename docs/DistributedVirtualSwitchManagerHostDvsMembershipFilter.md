# DistributedVirtualSwitchManagerHostDvsMembershipFilter

Check host compatibility against all hosts in the DVS (or not in the DVS if inclusive flag in base class is false)  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distributed_virtual_switch** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.distributed_virtual_switch_manager_host_dvs_membership_filter import DistributedVirtualSwitchManagerHostDvsMembershipFilter

# TODO update the JSON string below
json = "{}"
# create an instance of DistributedVirtualSwitchManagerHostDvsMembershipFilter from a JSON string
distributed_virtual_switch_manager_host_dvs_membership_filter_instance = DistributedVirtualSwitchManagerHostDvsMembershipFilter.from_json(json)
# print the JSON string representation of the object
print DistributedVirtualSwitchManagerHostDvsMembershipFilter.to_json()

# convert the object into a dict
distributed_virtual_switch_manager_host_dvs_membership_filter_dict = distributed_virtual_switch_manager_host_dvs_membership_filter_instance.to_dict()
# create an instance of DistributedVirtualSwitchManagerHostDvsMembershipFilter from a dict
distributed_virtual_switch_manager_host_dvs_membership_filter_form_dict = distributed_virtual_switch_manager_host_dvs_membership_filter.from_dict(distributed_virtual_switch_manager_host_dvs_membership_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


